# Generated from ArduinoMexa.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ArduinoMexaParser import ArduinoMexaParser
else:
    from ArduinoMexaParser import ArduinoMexaParser

# This class defines a complete generic visitor for a parse tree produced by ArduinoMexaParser.

class ArduinoMexaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArduinoMexaParser#program.
    def visitProgram(self, ctx:ArduinoMexaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#bloqueEstatico.
    def visitBloqueEstatico(self, ctx:ArduinoMexaParser.BloqueEstaticoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#bloqueLoop.
    def visitBloqueLoop(self, ctx:ArduinoMexaParser.BloqueLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#sentencia.
    def visitSentencia(self, ctx:ArduinoMexaParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtPrenderled.
    def visitStmtPrenderled(self, ctx:ArduinoMexaParser.StmtPrenderledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtApagarled.
    def visitStmtApagarled(self, ctx:ArduinoMexaParser.StmtApagarledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtLeersensor.
    def visitStmtLeersensor(self, ctx:ArduinoMexaParser.StmtLeersensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtMoverServo.
    def visitStmtMoverServo(self, ctx:ArduinoMexaParser.StmtMoverServoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtEsperar.
    def visitStmtEsperar(self, ctx:ArduinoMexaParser.StmtEsperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtAsignacion.
    def visitStmtAsignacion(self, ctx:ArduinoMexaParser.StmtAsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtCondicion.
    def visitStmtCondicion(self, ctx:ArduinoMexaParser.StmtCondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtBuzzer.
    def visitStmtBuzzer(self, ctx:ArduinoMexaParser.StmtBuzzerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtEscribirLCD.
    def visitStmtEscribirLCD(self, ctx:ArduinoMexaParser.StmtEscribirLCDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtMotorOn.
    def visitStmtMotorOn(self, ctx:ArduinoMexaParser.StmtMotorOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtMotorOff.
    def visitStmtMotorOff(self, ctx:ArduinoMexaParser.StmtMotorOffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtReleOn.
    def visitStmtReleOn(self, ctx:ArduinoMexaParser.StmtReleOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtReleOff.
    def visitStmtReleOff(self, ctx:ArduinoMexaParser.StmtReleOffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtRgbOn.
    def visitStmtRgbOn(self, ctx:ArduinoMexaParser.StmtRgbOnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#stmtRgbOff.
    def visitStmtRgbOff(self, ctx:ArduinoMexaParser.StmtRgbOffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#prenderled.
    def visitPrenderled(self, ctx:ArduinoMexaParser.PrenderledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#apagarled.
    def visitApagarled(self, ctx:ArduinoMexaParser.ApagarledContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#leersensor.
    def visitLeersensor(self, ctx:ArduinoMexaParser.LeersensorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#moverservo.
    def visitMoverservo(self, ctx:ArduinoMexaParser.MoverservoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#esperar.
    def visitEsperar(self, ctx:ArduinoMexaParser.EsperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#asignacion.
    def visitAsignacion(self, ctx:ArduinoMexaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#condicion.
    def visitCondicion(self, ctx:ArduinoMexaParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#tocarbuzzer.
    def visitTocarbuzzer(self, ctx:ArduinoMexaParser.TocarbuzzerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#escribirlcd.
    def visitEscribirlcd(self, ctx:ArduinoMexaParser.EscribirlcdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#encendermotor.
    def visitEncendermotor(self, ctx:ArduinoMexaParser.EncendermotorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#apagarmotor.
    def visitApagarmotor(self, ctx:ArduinoMexaParser.ApagarmotorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#activarrele.
    def visitActivarrele(self, ctx:ArduinoMexaParser.ActivarreleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#desactivarrele.
    def visitDesactivarrele(self, ctx:ArduinoMexaParser.DesactivarreleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#prenderrgb.
    def visitPrenderrgb(self, ctx:ArduinoMexaParser.PrenderrgbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#apagarrgb.
    def visitApagarrgb(self, ctx:ArduinoMexaParser.ApagarrgbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#expr.
    def visitExpr(self, ctx:ArduinoMexaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#termino.
    def visitTermino(self, ctx:ArduinoMexaParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#factor.
    def visitFactor(self, ctx:ArduinoMexaParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArduinoMexaParser#comparador.
    def visitComparador(self, ctx:ArduinoMexaParser.ComparadorContext):
        return self.visitChildren(ctx)



del ArduinoMexaParser