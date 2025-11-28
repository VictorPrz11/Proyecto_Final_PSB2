from antlr4 import *
from ArduinoMexaLexer import ArduinoMexaLexer
from ArduinoMexaParser import ArduinoMexaParser
import sys

# error_listener.py
from antlr4.error.ErrorListener import ErrorListener

from visitor import TraductorArduinoVisitor

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"[Error de sintaxis] Línea {line}, Columna {column}: {msg}")

def print_tree(tree, rule_names, indent=0):
    """Función auxiliar para imprimir el árbol de forma jerárquica"""

    text = tree.getText().replace('\\n', ' ')
    rule_name = rule_names[tree.getRuleIndex()] if hasattr(tree, 'getRuleIndex') else ''
    print('  ' * indent + f"{rule_name}: {text}")
    for i in range(tree.getChildCount()):
        print_tree(tree.getChild(i), rule_names, indent + 1)

def run_parser(input_code):
    # Lexer
    input_stream = InputStream(input_code)
    lexer = ArduinoMexaLexer(input_stream)

    # Detectar errores léxicos (tokens inválidos)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    for token in tokens.tokens:
        if token.type == Token.INVALID_TYPE:
            print(f"[Error léxico] Token inválido: '{token.text}' en línea {token.line}, columna {token.column}")

    # Parser
    parser = ArduinoMexaParser(tokens)
    '''parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener()) '''

    # Árbol de análisis sintáctico
    tree = parser.program()
    rule_names = parser.ruleNames

    print("\\n--- Árbol de Sintaxis Abstracta (AST) ---\\n")
    print_tree(tree, rule_names)

    traductor = TraductorArduinoVisitor()
    resultado = traductor.visit(tree)
    return resultado



