# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW5-AST manipulation/Example_DSL/grammar/ExampleDSL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExampleDSLParser import ExampleDSLParser
else:
    from ExampleDSLParser import ExampleDSLParser

# This class defines a complete listener for a parse tree produced by ExampleDSLParser.
class ExampleDSLListener(ParseTreeListener):

    # Enter a parse tree produced by ExampleDSLParser#start.
    def enterStart(self, ctx:ExampleDSLParser.StartContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#start.
    def exitStart(self, ctx:ExampleDSLParser.StartContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#program.
    def enterProgram(self, ctx:ExampleDSLParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#program.
    def exitProgram(self, ctx:ExampleDSLParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#output.
    def enterOutput(self, ctx:ExampleDSLParser.OutputContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#output.
    def exitOutput(self, ctx:ExampleDSLParser.OutputContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#output_types.
    def enterOutput_types(self, ctx:ExampleDSLParser.Output_typesContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#output_types.
    def exitOutput_types(self, ctx:ExampleDSLParser.Output_typesContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#hints.
    def enterHints(self, ctx:ExampleDSLParser.HintsContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#hints.
    def exitHints(self, ctx:ExampleDSLParser.HintsContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#hint_option.
    def enterHint_option(self, ctx:ExampleDSLParser.Hint_optionContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#hint_option.
    def exitHint_option(self, ctx:ExampleDSLParser.Hint_optionContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#initiate_game.
    def enterInitiate_game(self, ctx:ExampleDSLParser.Initiate_gameContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#initiate_game.
    def exitInitiate_game(self, ctx:ExampleDSLParser.Initiate_gameContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#width.
    def enterWidth(self, ctx:ExampleDSLParser.WidthContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#width.
    def exitWidth(self, ctx:ExampleDSLParser.WidthContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#height.
    def enterHeight(self, ctx:ExampleDSLParser.HeightContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#height.
    def exitHeight(self, ctx:ExampleDSLParser.HeightContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#bomb_placements.
    def enterBomb_placements(self, ctx:ExampleDSLParser.Bomb_placementsContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#bomb_placements.
    def exitBomb_placements(self, ctx:ExampleDSLParser.Bomb_placementsContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#bomb_location.
    def enterBomb_location(self, ctx:ExampleDSLParser.Bomb_locationContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#bomb_location.
    def exitBomb_location(self, ctx:ExampleDSLParser.Bomb_locationContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#x_location.
    def enterX_location(self, ctx:ExampleDSLParser.X_locationContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#x_location.
    def exitX_location(self, ctx:ExampleDSLParser.X_locationContext):
        pass


    # Enter a parse tree produced by ExampleDSLParser#y_location.
    def enterY_location(self, ctx:ExampleDSLParser.Y_locationContext):
        pass

    # Exit a parse tree produced by ExampleDSLParser#y_location.
    def exitY_location(self, ctx:ExampleDSLParser.Y_locationContext):
        pass



del ExampleDSLParser