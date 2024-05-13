from antlr4 import *
from gen.STGrammarLexer import STGrammarLexer
from gen.STGrammarParser import STGrammarParser
from ST import SymbolTableListener, SymbolTable
    
    
input_expression = open('input.txt', 'r').read()
lexer = STGrammarLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = STGrammarParser(token_stream)
parse_tree = parser.start()

symbol_table = SymbolTable()
listener = SymbolTableListener(symbol_table)
walker = ParseTreeWalker()
try:
    walker.walk(listener, parse_tree)
except Exception as e:
    print(e)

symbol_table.show_symbol_table()