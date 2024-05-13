# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW3-STExercise/STGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .STGrammarParser import STGrammarParser
else:
    from STGrammarParser import STGrammarParser

# This class defines a complete listener for a parse tree produced by STGrammarParser.
class STGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by STGrammarParser#start.
    def enterStart(self, ctx:STGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by STGrammarParser#start.
    def exitStart(self, ctx:STGrammarParser.StartContext):
        pass


    # Enter a parse tree produced by STGrammarParser#assigns.
    def enterAssigns(self, ctx:STGrammarParser.AssignsContext):
        pass

    # Exit a parse tree produced by STGrammarParser#assigns.
    def exitAssigns(self, ctx:STGrammarParser.AssignsContext):
        pass


    # Enter a parse tree produced by STGrammarParser#assign.
    def enterAssign(self, ctx:STGrammarParser.AssignContext):
        pass

    # Exit a parse tree produced by STGrammarParser#assign.
    def exitAssign(self, ctx:STGrammarParser.AssignContext):
        pass


    # Enter a parse tree produced by STGrammarParser#expr.
    def enterExpr(self, ctx:STGrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by STGrammarParser#expr.
    def exitExpr(self, ctx:STGrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by STGrammarParser#term.
    def enterTerm(self, ctx:STGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by STGrammarParser#term.
    def exitTerm(self, ctx:STGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by STGrammarParser#factor_is_string.
    def enterFactor_is_string(self, ctx:STGrammarParser.Factor_is_stringContext):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_string.
    def exitFactor_is_string(self, ctx:STGrammarParser.Factor_is_stringContext):
        pass


    # Enter a parse tree produced by STGrammarParser#factor_is_integer.
    def enterFactor_is_integer(self, ctx:STGrammarParser.Factor_is_integerContext):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_integer.
    def exitFactor_is_integer(self, ctx:STGrammarParser.Factor_is_integerContext):
        pass


    # Enter a parse tree produced by STGrammarParser#factor_is_float.
    def enterFactor_is_float(self, ctx:STGrammarParser.Factor_is_floatContext):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_float.
    def exitFactor_is_float(self, ctx:STGrammarParser.Factor_is_floatContext):
        pass


    # Enter a parse tree produced by STGrammarParser#factor_is_expression.
    def enterFactor_is_expression(self, ctx:STGrammarParser.Factor_is_expressionContext):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx:STGrammarParser.Factor_is_expressionContext):
        pass


    # Enter a parse tree produced by STGrammarParser#factor_is_id.
    def enterFactor_is_id(self, ctx:STGrammarParser.Factor_is_idContext):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_id.
    def exitFactor_is_id(self, ctx:STGrammarParser.Factor_is_idContext):
        pass


    # Enter a parse tree produced by STGrammarParser#sign.
    def enterSign(self, ctx:STGrammarParser.SignContext):
        pass

    # Exit a parse tree produced by STGrammarParser#sign.
    def exitSign(self, ctx:STGrammarParser.SignContext):
        pass



del STGrammarParser