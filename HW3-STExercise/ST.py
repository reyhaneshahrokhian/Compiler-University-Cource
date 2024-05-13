from antlr4 import *
from gen.STGrammarListener import STGrammarListener
from gen.STGrammarParser import STGrammarParser

class SymbolTable:
    def __init__(self):
        self.symbol_table = {}
        self.next_id = 1

    def add_symbol(self, name, type, value):
        self.symbol_table[name] = {'id': self.next_id, 'type': type, 'value': value}
        self.next_id += 1

    def get_symbol(self, name):
        return self.symbol_table.get(name, None)

    def show_symbol_table(self):
        print("Symbol Table:")
        for name, symbol in self.symbol_table.items():
            print(f"ID: {symbol['id']}, Name: {name}, Type: {symbol['type']}, Value: {symbol['value']}")

class SymbolTableListener(ParseTreeListener):
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def enterAssign(self, ctx):
        id_name = ctx.ID().getText()
        expr_ctx = ctx.expr()
        expr_type = self.get_type(expr_ctx)
        expr_value = self.evaluate_expr(expr_ctx)
        self.symbol_table.add_symbol(id_name, expr_type, expr_value)

    def get_type(self, ctx):
        text = self.evaluate_expr(ctx)

        if isinstance(text, int):
            return 'integer'
        elif isinstance(text, float):
            return 'float'
        elif isinstance(text, str):
            if text.startswith('"') and text.endswith('"'):
                return 'string'

    def evaluate_expr(self, ctx):
        if ctx.term():
            return self.evaluate_term(ctx.term())
        elif ctx.expr(0):
            temp1 = self.evaluate_expr(ctx.expr(0))
            temp2 = self.evaluate_expr(ctx.expr(1))
            if ctx.ADD():
                return temp1 + temp2
            elif ctx.SUB():
                return temp1 - temp2
        else:
            return None

    def evaluate_term(self, ctx):
        if ctx.factor():
            return self.evaluate_factor(ctx.factor())
        elif ctx.term(0):
            temp1 = self.evaluate_term(ctx.term(0))
            temp2 = self.evaluate_term(ctx.term(1))
            if ctx.MUL():
                return temp1 * temp2
            elif ctx.DIV():
                return temp1 / temp2
        else:
            return None

    def evaluate_factor(self, ctx):
        text = ctx.getText()

        if text.replace('.', '', 1).isdigit():
            if '.' in text:
                return float(text)
            else:
                return int(text)
        elif ctx.ID():
            symbol = self.symbol_table.get_symbol(ctx.ID().getText())
            if symbol:
                return symbol['value']
            else:
                return None
        elif ctx.expr():
            return self.evaluate_expr(ctx.expr())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        else:
            return None
