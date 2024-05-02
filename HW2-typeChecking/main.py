from antlr4 import *
from gen.TypeCheckerLexer import TypeCheckerLexer
from gen.TypeCheckerParser import TypeCheckerParser
from io import StringIO
from typeChecker import TypeCheckListener


input_expression = input("Enter an expression: ")
lexer = TypeCheckerLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = TypeCheckerParser(token_stream)
parse_tree = parser.start()
listener = TypeCheckListener()
walker = ParseTreeWalker()
try:
    walker.walk(listener, parse_tree)
except Exception as e:
    print(e)
