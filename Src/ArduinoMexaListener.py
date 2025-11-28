# Generated from ArduinoMexa.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArduinoMexaParser import ArduinoMexaParser
else:
    from ArduinoMexaParser import ArduinoMexaParser

# This class defines a complete listener for a parse tree produced by ArduinoMexaParser.
class ArduinoMexaListener(ParseTreeListener):

    # Enter a parse tree produced by ArduinoMexaParser#program.
    def enterProgram(self, ctx:ArduinoMexaParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#program.
    def exitProgram(self, ctx:ArduinoMexaParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#bloqueEstatico.
    def enterBloqueEstatico(self, ctx:ArduinoMexaParser.BloqueEstaticoContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#bloqueEstatico.
    def exitBloqueEstatico(self, ctx:ArduinoMexaParser.BloqueEstaticoContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#bloqueLoop.
    def enterBloqueLoop(self, ctx:ArduinoMexaParser.BloqueLoopContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#bloqueLoop.
    def exitBloqueLoop(self, ctx:ArduinoMexaParser.BloqueLoopContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#sentencia.
    def enterSentencia(self, ctx:ArduinoMexaParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#sentencia.
    def exitSentencia(self, ctx:ArduinoMexaParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtPrenderled.
    def enterStmtPrenderled(self, ctx:ArduinoMexaParser.StmtPrenderledContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtPrenderled.
    def exitStmtPrenderled(self, ctx:ArduinoMexaParser.StmtPrenderledContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtApagarled.
    def enterStmtApagarled(self, ctx:ArduinoMexaParser.StmtApagarledContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtApagarled.
    def exitStmtApagarled(self, ctx:ArduinoMexaParser.StmtApagarledContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtLeersensor.
    def enterStmtLeersensor(self, ctx:ArduinoMexaParser.StmtLeersensorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtLeersensor.
    def exitStmtLeersensor(self, ctx:ArduinoMexaParser.StmtLeersensorContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtMoverServo.
    def enterStmtMoverServo(self, ctx:ArduinoMexaParser.StmtMoverServoContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtMoverServo.
    def exitStmtMoverServo(self, ctx:ArduinoMexaParser.StmtMoverServoContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtEsperar.
    def enterStmtEsperar(self, ctx:ArduinoMexaParser.StmtEsperarContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtEsperar.
    def exitStmtEsperar(self, ctx:ArduinoMexaParser.StmtEsperarContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtAsignacion.
    def enterStmtAsignacion(self, ctx:ArduinoMexaParser.StmtAsignacionContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtAsignacion.
    def exitStmtAsignacion(self, ctx:ArduinoMexaParser.StmtAsignacionContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtCondicion.
    def enterStmtCondicion(self, ctx:ArduinoMexaParser.StmtCondicionContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtCondicion.
    def exitStmtCondicion(self, ctx:ArduinoMexaParser.StmtCondicionContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtBuzzer.
    def enterStmtBuzzer(self, ctx:ArduinoMexaParser.StmtBuzzerContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtBuzzer.
    def exitStmtBuzzer(self, ctx:ArduinoMexaParser.StmtBuzzerContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtEscribirLCD.
    def enterStmtEscribirLCD(self, ctx:ArduinoMexaParser.StmtEscribirLCDContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtEscribirLCD.
    def exitStmtEscribirLCD(self, ctx:ArduinoMexaParser.StmtEscribirLCDContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtMotorOn.
    def enterStmtMotorOn(self, ctx:ArduinoMexaParser.StmtMotorOnContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtMotorOn.
    def exitStmtMotorOn(self, ctx:ArduinoMexaParser.StmtMotorOnContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtMotorOff.
    def enterStmtMotorOff(self, ctx:ArduinoMexaParser.StmtMotorOffContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtMotorOff.
    def exitStmtMotorOff(self, ctx:ArduinoMexaParser.StmtMotorOffContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtReleOn.
    def enterStmtReleOn(self, ctx:ArduinoMexaParser.StmtReleOnContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtReleOn.
    def exitStmtReleOn(self, ctx:ArduinoMexaParser.StmtReleOnContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtReleOff.
    def enterStmtReleOff(self, ctx:ArduinoMexaParser.StmtReleOffContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtReleOff.
    def exitStmtReleOff(self, ctx:ArduinoMexaParser.StmtReleOffContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtRgbOn.
    def enterStmtRgbOn(self, ctx:ArduinoMexaParser.StmtRgbOnContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtRgbOn.
    def exitStmtRgbOn(self, ctx:ArduinoMexaParser.StmtRgbOnContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#stmtRgbOff.
    def enterStmtRgbOff(self, ctx:ArduinoMexaParser.StmtRgbOffContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#stmtRgbOff.
    def exitStmtRgbOff(self, ctx:ArduinoMexaParser.StmtRgbOffContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#prenderled.
    def enterPrenderled(self, ctx:ArduinoMexaParser.PrenderledContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#prenderled.
    def exitPrenderled(self, ctx:ArduinoMexaParser.PrenderledContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#apagarled.
    def enterApagarled(self, ctx:ArduinoMexaParser.ApagarledContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#apagarled.
    def exitApagarled(self, ctx:ArduinoMexaParser.ApagarledContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#leersensor.
    def enterLeersensor(self, ctx:ArduinoMexaParser.LeersensorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#leersensor.
    def exitLeersensor(self, ctx:ArduinoMexaParser.LeersensorContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#moverservo.
    def enterMoverservo(self, ctx:ArduinoMexaParser.MoverservoContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#moverservo.
    def exitMoverservo(self, ctx:ArduinoMexaParser.MoverservoContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#esperar.
    def enterEsperar(self, ctx:ArduinoMexaParser.EsperarContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#esperar.
    def exitEsperar(self, ctx:ArduinoMexaParser.EsperarContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#asignacion.
    def enterAsignacion(self, ctx:ArduinoMexaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#asignacion.
    def exitAsignacion(self, ctx:ArduinoMexaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#condicion.
    def enterCondicion(self, ctx:ArduinoMexaParser.CondicionContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#condicion.
    def exitCondicion(self, ctx:ArduinoMexaParser.CondicionContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#tocarbuzzer.
    def enterTocarbuzzer(self, ctx:ArduinoMexaParser.TocarbuzzerContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#tocarbuzzer.
    def exitTocarbuzzer(self, ctx:ArduinoMexaParser.TocarbuzzerContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#escribirlcd.
    def enterEscribirlcd(self, ctx:ArduinoMexaParser.EscribirlcdContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#escribirlcd.
    def exitEscribirlcd(self, ctx:ArduinoMexaParser.EscribirlcdContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#encendermotor.
    def enterEncendermotor(self, ctx:ArduinoMexaParser.EncendermotorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#encendermotor.
    def exitEncendermotor(self, ctx:ArduinoMexaParser.EncendermotorContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#apagarmotor.
    def enterApagarmotor(self, ctx:ArduinoMexaParser.ApagarmotorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#apagarmotor.
    def exitApagarmotor(self, ctx:ArduinoMexaParser.ApagarmotorContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#activarrele.
    def enterActivarrele(self, ctx:ArduinoMexaParser.ActivarreleContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#activarrele.
    def exitActivarrele(self, ctx:ArduinoMexaParser.ActivarreleContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#desactivarrele.
    def enterDesactivarrele(self, ctx:ArduinoMexaParser.DesactivarreleContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#desactivarrele.
    def exitDesactivarrele(self, ctx:ArduinoMexaParser.DesactivarreleContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#prenderrgb.
    def enterPrenderrgb(self, ctx:ArduinoMexaParser.PrenderrgbContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#prenderrgb.
    def exitPrenderrgb(self, ctx:ArduinoMexaParser.PrenderrgbContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#apagarrgb.
    def enterApagarrgb(self, ctx:ArduinoMexaParser.ApagarrgbContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#apagarrgb.
    def exitApagarrgb(self, ctx:ArduinoMexaParser.ApagarrgbContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#expr.
    def enterExpr(self, ctx:ArduinoMexaParser.ExprContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#expr.
    def exitExpr(self, ctx:ArduinoMexaParser.ExprContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#termino.
    def enterTermino(self, ctx:ArduinoMexaParser.TerminoContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#termino.
    def exitTermino(self, ctx:ArduinoMexaParser.TerminoContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#factor.
    def enterFactor(self, ctx:ArduinoMexaParser.FactorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#factor.
    def exitFactor(self, ctx:ArduinoMexaParser.FactorContext):
        pass


    # Enter a parse tree produced by ArduinoMexaParser#comparador.
    def enterComparador(self, ctx:ArduinoMexaParser.ComparadorContext):
        pass

    # Exit a parse tree produced by ArduinoMexaParser#comparador.
    def exitComparador(self, ctx:ArduinoMexaParser.ComparadorContext):
        pass



del ArduinoMexaParser