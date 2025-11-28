from ArduinoMexaVisitor import ArduinoMexaVisitor
from ArduinoMexaParser import ArduinoMexaParser
from antlr4.tree.Tree import TerminalNode


class TraductorArduinoVisitor(ArduinoMexaVisitor):
    def __init__(self):
        super().__init__()
        # Flags para inclusión de librerías
        self.usa_servo = False
        self.usa_lcd = False

        # Estructuras para gestión de código
        # Almacena pines que necesitan pinMode (para evitar repetirlo)
        self.pines_configurados = set()
        # Almacena variables que necesitan declaración global (simplificamos a 'int' por ahora)
        self.variables_declaradas = set()
        # Almacena código que debe ir en el preámbulo (declaraciones globales)
        self.codigo_preambulo = []

    # --- Programa principal ---
    def visitProgram(self, ctx: ArduinoMexaParser.ProgramContext):
        # Ya no necesitamos el print("iniciando traduccion"), lo quitamos.

        # 1. VISITAR LOOP PRIMERO (CRUCIAL): Llenamos self.pines_configurados
        # y self.variables_declaradas con lo que se use en el loop.
        loop_code_wrapped = self.visit(ctx.bloqueLoop())

        # -----------------------------------------------------------
        # 2. Manejo del bloque ESTATICO (Ahora opcional)
        # -----------------------------------------------------------
        setup_ctx = ctx.bloqueEstatico()
        setup_code_wrapped = ""

        if setup_ctx:
            # A) El bloque ESTATICO existe: Lo visitamos.
            #    Asumimos que visitBloqueEstatico añade Serial.begin() y pinMode().
            setup_code_wrapped = self.visit(setup_ctx)
        else:
            # B) El bloque ESTATICO NO existe: Generamos la estructura mínima de setup().

            # I. Código para pinMode (basado en lo que se encontró en el loop).
            pin_modes = ""
            for pin in self.pines_configurados:
                pin_modes += f"\tpinMode({pin}, OUTPUT);\n"

            # II. Código de preámbulo (ej. servo.attach()) que DEBE ir en setup.
            setup_preambulo = "\n".join(self.codigo_preambulo)
            if setup_preambulo:
                setup_preambulo += "\n"  # Salto de línea si hay contenido

            # III. Estructura mínima, incluyendo Serial.begin(9600) como primer elemento.
            setup_code_body = (
                f"\tSerial.begin(9600);\n"
                f"{pin_modes}"
                f"{setup_preambulo}"
            )
            # Envolvemos el cuerpo en la función void setup()
            setup_code_wrapped = f"void setup() {{\n{setup_code_body}}}"

        # -----------------------------------------------------------
        # 3. Generar el preámbulo (Librerías + Declaraciones)
        # -----------------------------------------------------------
        preambulo = ""

        if self.usa_servo:
            preambulo += "#include <Servo.h>\nServo servo;\n"
        if self.usa_lcd:
            preambulo += "#include <LiquidCrystal.h>\nLiquidCrystal lcd(12, 11, 5, 4, 3, 2);\n"

        # Declaración de variables globales
        for var in self.variables_declaradas:
            preambulo += f"int {var};\n"

        # 4. Ensamblar el código final
        setup_code = setup_code_wrapped.strip() or ""
        loop_code = loop_code_wrapped.strip() or ""

        return f"{preambulo}\n{setup_code}\n\n{loop_code}"
    # --- Bloques Estructurales ---

    def visitBloqueEstatico(self, ctx: ArduinoMexaParser.BloqueEstaticoContext):
        cuerpo = self.visit(ctx.sentencia()) or ""

        # Código para pinMode debe ir aquí ANTES del cuerpo principal
        pin_modes = ""
        for pin in self.pines_configurados:
            # Asegúrate de que esto también incluya el preámbulo de setup
            pin_modes += f"\tpinMode({pin}, OUTPUT);\n"

        # Agregamos Serial.begin(9600) como la primera línea OBLIGATORIA
        serial_begin = "\tSerial.begin(9600);\n"

        # Agregamos el preámbulo de setup (ej: servo.attach())
        setup_preambulo = "\n".join(self.codigo_preambulo)
        if setup_preambulo:
            setup_preambulo = "\n" + setup_preambulo + "\n"

        setup_body = serial_begin + pin_modes + setup_preambulo + cuerpo

        return f"void setup() {{\n{setup_body}}}"

    def visitBloqueLoop(self, ctx: ArduinoMexaParser.BloqueLoopContext):
        cuerpo = self.visit(ctx.sentencia()) or ""
        return f"void loop() {{\n{cuerpo}}}"

    # --- Gestión de sentencias y flujo ---

    def visitSentencia(self, ctx: ArduinoMexaParser.SentenciaContext):
        codigo = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result:
                # Asegura un salto de línea y sangría simple para las sentencias
                codigo.append(f"\t{result.strip()}")
        return "\n".join(codigo) + "\n"

    def visitStatement(self, ctx: ArduinoMexaParser.StatementContext):
        # Delega la visita al nodo hijo real (ej. PrenderledContext)
        res = self.visitChildren(ctx)
        return res or ""

    # --- Instrucciones originales ---

    def _configurar_pin_output(self, pin_expr_context):
        """Marca un pin para que se declare en pinMode(pin, OUTPUT) en el setup."""
        pin_valor = self.visit(pin_expr_context)
        # Solo añadimos el pin a configurar si es un valor simple (ID o INT)
        if pin_valor and ('+' not in pin_valor and '-' not in pin_valor):
            self.pines_configurados.add(pin_valor)
        return pin_valor

    def visitPrenderled(self, ctx: ArduinoMexaParser.PrenderledContext):
        pin = self._configurar_pin_output(ctx.expr(0))  # Usa el nuevo helper
        valor = self.visit(ctx.expr(1))  # **CORREGIDO**
        return f"digitalWrite({pin}, {valor});"

    def visitApagarled(self, ctx: ArduinoMexaParser.ApagarledContext):
        pin = self._configurar_pin_output(ctx.expr())  # **CORREGIDO**
        return f"digitalWrite({pin}, LOW);"

    def visitLeersensor(self, ctx: ArduinoMexaParser.LeersensorContext):
        var = ctx.ID().getText()
        pin = self.visit(ctx.expr())  # **CORREGIDO**
        self.variables_declaradas.add(var)  # Añadimos la variable para declaración global

        # Asumimos analogRead por defecto para un sensor genérico
        # Si quisieras digitalRead, la gramática debería diferenciar el comando
        return f"{var} = analogRead({pin});"

    def visitMoverservo(self, ctx: ArduinoMexaParser.MoverservoContext):
        self.usa_servo = True
        pin = self.visit(ctx.expr(0))  # **CORREGIDO**
        angulo = self.visit(ctx.expr(1))  # **CORREGIDO**

        # La lógica de attach debería ir en setup
        if f"servo.attach({pin})" not in self.codigo_preambulo:
            self.codigo_preambulo.append(f"servo.attach({pin});")

        return f"servo.write({angulo});"

    def visitEsperar(self, ctx: ArduinoMexaParser.EsperarContext):
        tiempo = self.visit(ctx.expr())  # **CORREGIDO**
        return f"delay({tiempo});"

    def visitAsignacion(self, ctx: ArduinoMexaParser.AsignacionContext):
        var = ctx.ID().getText()
        valor = self.visit(ctx.expr())  # **CORREGIDO**
        self.variables_declaradas.add(var)  # Añadimos la variable para declaración global
        return f"{var} = {valor};"

    def visitCondicion(self, ctx: ArduinoMexaParser.CondicionContext):
        izquierda = self.visit(ctx.expr(0))  # **CORREGIDO**
        operador = self.visit(ctx.comparador())
        derecha = self.visit(ctx.expr(1))  # **CORREGIDO**

        # El cuerpo de la sentencia debe tener un nivel extra de sangría
        bloque = self.visit(ctx.sentencia()) or ""
        cuerpo = "\n".join(f"\t{line}" for line in bloque.strip().splitlines())

        return f"if ({izquierda} {operador} {derecha}) {{\n{cuerpo}\n\t}}"

    # --- Expresiones y Operadores ---

    # ⚠️ Nota: Esta implementación de expresiones asume que ANTLR está generando
    # métodos separados para las reglas 'expr', 'termino' y 'factor'.

        # ==========================================
        #   PEGA ESTO EN TU visitor.py (Reemplaza lo anterior)
        # ==========================================

    def visitExpr(self, ctx: ArduinoMexaParser.ExprContext):
        # Regla gramatical: termino ((ADD | SUB) termino)*

        # 1. Obtenemos el primer término (la izquierda)
        # IMPORTANTE: Usamos 'termino', NO 'expr'
        resultado = self.visit(ctx.termino(0))

        # 2. Si hay más términos (es una suma o resta, ej: 5 + 3)
        if ctx.getChildCount() > 1:
            # Iteramos sobre los términos restantes
            for i in range(1, len(ctx.termino())):
                # El operador (+ o -) está justo antes del término actual
                # Estructura de hijos: [termino0, OPERADOR, termino1...]
                operador = ctx.getChild((i * 2) - 1).getText()

                siguiente_termino = self.visit(ctx.termino(i))

                # Concatenamos la operación
                resultado = f"{resultado} {operador} {siguiente_termino}"

        return resultado

    def visitTermino(self, ctx: ArduinoMexaParser.TerminoContext):
        # Regla gramatical: factor ((MUL | DIV) factor)*

        # 1. Obtenemos el primer factor
        resultado = self.visit(ctx.factor(0))

        # 2. Si hay multiplicaciones o divisiones
        if ctx.getChildCount() > 1:
            for i in range(1, len(ctx.factor())):
                operador = ctx.getChild((i * 2) - 1).getText()
                siguiente_factor = self.visit(ctx.factor(i))
                resultado = f"{resultado} {operador} {siguiente_factor}"

        return resultado

    def visitFactor(self, ctx: ArduinoMexaParser.FactorContext):
        if ctx.INT():
            return ctx.INT().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.LPAREN():  # Si es ( expr )
            return f"({self.visit(ctx.expr())})"
        # En caso de que haya una sola alternativa (ID, INT, STRING, o (expr)), ANTLR a veces no delega
        return self.visitChildren(ctx)

    def visitComparador(self, ctx: ArduinoMexaParser.ComparadorContext):
        return ctx.getText()

    # --- Instrucciones nuevas (actuadores) - Correcciones Aplicadas ---

    def visitTocarbuzzer(self, ctx: ArduinoMexaParser.TocarbuzzerContext):
        pin = self._configurar_pin_output(ctx.expr(0))  # **CORREGIDO**
        tono = self.visit(ctx.expr(1))  # **CORREGIDO**
        return f"tone({pin}, {tono});"

    def visitEscribirlcd(self, ctx: ArduinoMexaParser.EscribirlcdContext):
        self.usa_lcd = True
        fila = self.visit(ctx.expr(0))  # **CORREGIDO**
        columna = self.visit(ctx.expr(1))  # **CORREGIDO**
        # No usamos visit aquí porque STRING es un Token, no una Regla, y getText() es apropiado
        texto = ctx.STRING().getText()
        return f"lcd.setCursor({columna}, {fila});\nlcd.print({texto});"

    def visitEncendermotor(self, ctx: ArduinoMexaParser.EncendermotorContext):
        pin = self._configurar_pin_output(ctx.expr(0))  # **CORREGIDO**
        velocidad = self.visit(ctx.expr(1))  # **CORREGIDO**
        # Usamos analogWrite para control de velocidad (PWM)
        return f"analogWrite({pin}, {velocidad});"

    def visitApagarmotor(self, ctx: ArduinoMexaParser.ApagarmotorContext):
        pin = self.visit(ctx.expr())  # **CORREGIDO**
        return f"analogWrite({pin}, 0);"

    def visitActivarrele(self, ctx: ArduinoMexaParser.ActivarreleContext):
        pin = self._configurar_pin_output(ctx.expr())  # **CORREGIDO**
        return f"digitalWrite({pin}, HIGH);"

    def visitDesactivarrele(self, ctx: ArduinoMexaParser.DesactivarreleContext):
        pin = self._configurar_pin_output(ctx.expr())  # **CORREGIDO**
        return f"digitalWrite({pin}, LOW);"

    def visitPrenderrgb(self, ctx: ArduinoMexaParser.PrenderrgbContext):
        r = self._configurar_pin_output(ctx.expr(0))  # **CORREGIDO**
        g = self._configurar_pin_output(ctx.expr(1))  # **CORREGIDO**
        b = self._configurar_pin_output(ctx.expr(2))  # **CORREGIDO**
        intensidad = self.visit(ctx.expr(3))  # **CORREGIDO**

        return (
            f"analogWrite({r}, {intensidad});\n"
            f"analogWrite({g}, {intensidad});\n"
            f"analogWrite({b}, {intensidad});"
        )

    def visitApagarrgb(self, ctx: ArduinoMexaParser.ApagarrgbContext):
        r = self.visit(ctx.expr(0))  # **CORREGIDO**
        g = self.visit(ctx.expr(1))  # **CORREGIDO**
        b = self.visit(ctx.expr(2))  # **CORREGIDO**

        return (
            f"analogWrite({r}, 0);\n"
            f"analogWrite({g}, 0);\n"
            f"analogWrite({b}, 0);"
        )