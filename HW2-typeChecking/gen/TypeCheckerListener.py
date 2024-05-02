# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW2/TypeChecker.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete listener for a parse tree produced by TypeCheckerParser.
class TypeCheckerListener(ParseTreeListener):

    # Enter a parse tree produced by TypeCheckerParser#start.
    def enterStart(self, ctx:TypeCheckerParser.StartContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#start.
    def exitStart(self, ctx:TypeCheckerParser.StartContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#expr3.
    def enterExpr3(self, ctx:TypeCheckerParser.Expr3Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr3.
    def exitExpr3(self, ctx:TypeCheckerParser.Expr3Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#expr2.
    def enterExpr2(self, ctx:TypeCheckerParser.Expr2Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr2.
    def exitExpr2(self, ctx:TypeCheckerParser.Expr2Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#expr1.
    def enterExpr1(self, ctx:TypeCheckerParser.Expr1Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr1.
    def exitExpr1(self, ctx:TypeCheckerParser.Expr1Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#term2.
    def enterTerm2(self, ctx:TypeCheckerParser.Term2Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#term2.
    def exitTerm2(self, ctx:TypeCheckerParser.Term2Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#term3.
    def enterTerm3(self, ctx:TypeCheckerParser.Term3Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#term3.
    def exitTerm3(self, ctx:TypeCheckerParser.Term3Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#term1.
    def enterTerm1(self, ctx:TypeCheckerParser.Term1Context):
        pass

    # Exit a parse tree produced by TypeCheckerParser#term1.
    def exitTerm1(self, ctx:TypeCheckerParser.Term1Context):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factString.
    def enterFactString(self, ctx:TypeCheckerParser.FactStringContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factString.
    def exitFactString(self, ctx:TypeCheckerParser.FactStringContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factInteger.
    def enterFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factInteger.
    def exitFactInteger(self, ctx:TypeCheckerParser.FactIntegerContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factFloat.
    def enterFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factFloat.
    def exitFactFloat(self, ctx:TypeCheckerParser.FactFloatContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#factExpr.
    def enterFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#factExpr.
    def exitFactExpr(self, ctx:TypeCheckerParser.FactExprContext):
        pass



del TypeCheckerParser