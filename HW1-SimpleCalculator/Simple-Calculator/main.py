from antlr4 import *

from CalculatorListener import CalculatorListener
from gen.ArithmeticExpressionLexer import ArithmeticExpressionLexer
from gen.ArithmeticExpressionParser import ArithmeticExpressionParser

input_expression = input("Enter an arithmetic expression: ")
lexer = ArithmeticExpressionLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = ArithmeticExpressionParser(token_stream)
parse_tree = parser.start()
listener = CalculatorListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)
result = listener.result
print("Result :", result)
