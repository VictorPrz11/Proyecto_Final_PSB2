import unittest
import sys
import os

# --- TRUCO: Agregamos la carpeta 'src' al camino para poder importar tus módulos ---
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, '..', 'src')
sys.path.append(src_path)
# -----------------------------------------------------------------------------------

from antlr4 import InputStream, CommonTokenStream
from ArduinoMexaLexer import ArduinoMexaLexer
from ArduinoMexaParser import ArduinoMexaParser
from visitor import TraductorArduinoVisitor

class TestArduinoMexa(unittest.TestCase):

    def compilar_texto(self, codigo):
        """Función auxiliar que simula lo que hace tu main.py"""
        input_stream = InputStream(codigo)
        lexer = ArduinoMexaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ArduinoMexaParser(stream)
        tree = parser.program()

        # Si hay errores de sintaxis, retornamos None
        if parser.getNumberOfSyntaxErrors() > 0:
            return None

        visitor = TraductorArduinoVisitor()
        return visitor.visit(tree)

    def test_codigo_basico(self):
        """Prueba 1: Verifica que un código simple de LED genere digitalWrite"""
        codigo_fuente = """
        ESTATICO
        x = 1;

        LOOP
        PRENDERLED(13, 1);
        """
        resultado = self.compilar_texto(codigo_fuente)

        # Verificamos (Assert) que el resultado contenga las traducciones esperadas
        self.assertIsNotNone(resultado)
        self.assertIn("void setup()", resultado)
        self.assertIn("void loop()", resultado)
        self.assertIn("digitalWrite(13, 1);", resultado)
        print("Prueba Básica: SUPERADA")

    def test_matematicas(self):
        """Prueba 2: Verifica que las operaciones matemáticas se procesen"""
        codigo_fuente = """
        LOOP
        a = 5 + 5;
        """
        resultado = self.compilar_texto(codigo_fuente)
        self.assertIn("a = 5 + 5;", resultado)
        print("Prueba Matemáticas: SUPERADA")

    def test_error_sintaxis(self):
        """Prueba 3: Verifica que el compilador detecte errores (ej. minúsculas)"""
        codigo_malo = """
        estatico
        """
        # Aquí hacemos el proceso manual para contar errores
        input_stream = InputStream(codigo_malo)
        lexer = ArduinoMexaLexer(input_stream)
        parser = ArduinoMexaParser(CommonTokenStream(lexer))
        parser.program()

        # Esperamos que el número de errores sea mayor a 0
        self.assertGreater(parser.getNumberOfSyntaxErrors(), 0)
        print("Prueba de Error Sintáctico: SUPERADA")


if __name__ == '__main__':
    unittest.main()