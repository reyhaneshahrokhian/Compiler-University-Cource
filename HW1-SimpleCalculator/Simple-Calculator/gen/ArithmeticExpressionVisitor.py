# Generated from C:/Subjects/Compiler_4022/First_excercise/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticExpressionParser import ArithmeticExpressionParser
else:
    from ArithmeticExpressionParser import ArithmeticExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticExpressionParser.

class ArithmeticExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticExpressionParser#start.
    def visitStart(self, ctx:ArithmeticExpressionParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assigns.
    def visitAssigns(self, ctx:ArithmeticExpressionParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#assign.
    def visitAssign(self, ctx:ArithmeticExpressionParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#expr.
    def visitExpr(self, ctx:ArithmeticExpressionParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#term.
    def visitTerm(self, ctx:ArithmeticExpressionParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticExpressionParser#factor.
    def visitFactor(self, ctx:ArithmeticExpressionParser.FactorContext):
        return self.visitChildren(ctx)



del ArithmeticExpressionParser