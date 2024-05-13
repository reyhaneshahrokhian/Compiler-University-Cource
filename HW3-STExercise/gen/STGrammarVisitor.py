# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW3-STExercise/STGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .STGrammarParser import STGrammarParser
else:
    from STGrammarParser import STGrammarParser

# This class defines a complete generic visitor for a parse tree produced by STGrammarParser.

class STGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by STGrammarParser#start.
    def visitStart(self, ctx:STGrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#assigns.
    def visitAssigns(self, ctx:STGrammarParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#assign.
    def visitAssign(self, ctx:STGrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#expr.
    def visitExpr(self, ctx:STGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#term.
    def visitTerm(self, ctx:STGrammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#factor_is_string.
    def visitFactor_is_string(self, ctx:STGrammarParser.Factor_is_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#factor_is_integer.
    def visitFactor_is_integer(self, ctx:STGrammarParser.Factor_is_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#factor_is_float.
    def visitFactor_is_float(self, ctx:STGrammarParser.Factor_is_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#factor_is_expression.
    def visitFactor_is_expression(self, ctx:STGrammarParser.Factor_is_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#factor_is_id.
    def visitFactor_is_id(self, ctx:STGrammarParser.Factor_is_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STGrammarParser#sign.
    def visitSign(self, ctx:STGrammarParser.SignContext):
        return self.visitChildren(ctx)



del STGrammarParser