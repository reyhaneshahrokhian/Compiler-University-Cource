# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW5-AST manipulation/Example_DSL/grammar/ExampleDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExampleDSLParser import ExampleDSLParser
else:
    from ExampleDSLParser import ExampleDSLParser

# This class defines a complete generic visitor for a parse tree produced by ExampleDSLParser.

class ExampleDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExampleDSLParser#start.
    def visitStart(self, ctx:ExampleDSLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#program.
    def visitProgram(self, ctx:ExampleDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#output.
    def visitOutput(self, ctx:ExampleDSLParser.OutputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#output_types.
    def visitOutput_types(self, ctx:ExampleDSLParser.Output_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#hints.
    def visitHints(self, ctx:ExampleDSLParser.HintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#hint_option.
    def visitHint_option(self, ctx:ExampleDSLParser.Hint_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#initiate_game.
    def visitInitiate_game(self, ctx:ExampleDSLParser.Initiate_gameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#width.
    def visitWidth(self, ctx:ExampleDSLParser.WidthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#height.
    def visitHeight(self, ctx:ExampleDSLParser.HeightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#bomb_placements.
    def visitBomb_placements(self, ctx:ExampleDSLParser.Bomb_placementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#bomb_location.
    def visitBomb_location(self, ctx:ExampleDSLParser.Bomb_locationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#x_location.
    def visitX_location(self, ctx:ExampleDSLParser.X_locationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExampleDSLParser#y_location.
    def visitY_location(self, ctx:ExampleDSLParser.Y_locationContext):
        return self.visitChildren(ctx)



del ExampleDSLParser