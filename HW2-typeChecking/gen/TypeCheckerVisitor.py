# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW2/TypeChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete generic visitor for a parse tree produced by TypeCheckerParser.

class TypeCheckerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypeCheckerParser#start.
    def visitStart(self, ctx:TypeCheckerParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#expr3.
    def visitExpr3(self, ctx:TypeCheckerParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#expr2.
    def visitExpr2(self, ctx:TypeCheckerParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#expr1.
    def visitExpr1(self, ctx:TypeCheckerParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#term2.
    def visitTerm2(self, ctx:TypeCheckerParser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#term3.
    def visitTerm3(self, ctx:TypeCheckerParser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#term1.
    def visitTerm1(self, ctx:TypeCheckerParser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factString.
    def visitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factInteger.
    def visitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factFloat.
    def visitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#factExpr.
    def visitFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        return self.visitChildren(ctx)



del TypeCheckerParser