# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW5-AST manipulation/Example_DSL/grammar/ExampleDSL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,72,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,3,1,31,8,1,1,1,3,1,34,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,
        3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,
        9,4,9,60,8,9,11,9,12,9,61,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,
        1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,1,0,2,3,1,0,5,
        6,61,0,26,1,0,0,0,2,30,1,0,0,0,4,38,1,0,0,0,6,41,1,0,0,0,8,43,1,
        0,0,0,10,46,1,0,0,0,12,48,1,0,0,0,14,53,1,0,0,0,16,55,1,0,0,0,18,
        59,1,0,0,0,20,63,1,0,0,0,22,67,1,0,0,0,24,69,1,0,0,0,26,27,3,2,1,
        0,27,28,5,0,0,1,28,1,1,0,0,0,29,31,3,4,2,0,30,29,1,0,0,0,30,31,1,
        0,0,0,31,33,1,0,0,0,32,34,3,8,4,0,33,32,1,0,0,0,33,34,1,0,0,0,34,
        35,1,0,0,0,35,36,3,12,6,0,36,37,3,18,9,0,37,3,1,0,0,0,38,39,5,1,
        0,0,39,40,3,6,3,0,40,5,1,0,0,0,41,42,7,0,0,0,42,7,1,0,0,0,43,44,
        5,4,0,0,44,45,3,10,5,0,45,9,1,0,0,0,46,47,7,1,0,0,47,11,1,0,0,0,
        48,49,5,7,0,0,49,50,3,14,7,0,50,51,5,8,0,0,51,52,3,16,8,0,52,13,
        1,0,0,0,53,54,5,11,0,0,54,15,1,0,0,0,55,56,5,11,0,0,56,17,1,0,0,
        0,57,58,5,9,0,0,58,60,3,20,10,0,59,57,1,0,0,0,60,61,1,0,0,0,61,59,
        1,0,0,0,61,62,1,0,0,0,62,19,1,0,0,0,63,64,3,22,11,0,64,65,5,10,0,
        0,65,66,3,24,12,0,66,21,1,0,0,0,67,68,5,11,0,0,68,23,1,0,0,0,69,
        70,5,11,0,0,70,25,1,0,0,0,3,30,33,61
    ]

class ExampleDSLParser ( Parser ):

    grammarFileName = "ExampleDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'output:'", "'html'", "'console'", "'hint:'", 
                     "'True'", "'False'", "'game:'", "'X'", "'bomb:'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTEGER", 
                      "WS", "NEWLINE" ]

    RULE_start = 0
    RULE_program = 1
    RULE_output = 2
    RULE_output_types = 3
    RULE_hints = 4
    RULE_hint_option = 5
    RULE_initiate_game = 6
    RULE_width = 7
    RULE_height = 8
    RULE_bomb_placements = 9
    RULE_bomb_location = 10
    RULE_x_location = 11
    RULE_y_location = 12

    ruleNames =  [ "start", "program", "output", "output_types", "hints", 
                   "hint_option", "initiate_game", "width", "height", "bomb_placements", 
                   "bomb_location", "x_location", "y_location" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INTEGER=11
    WS=12
    NEWLINE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program(self):
            return self.getTypedRuleContext(ExampleDSLParser.ProgramContext,0)


        def EOF(self):
            return self.getToken(ExampleDSLParser.EOF, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ExampleDSLParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.program()
            self.state = 27
            self.match(ExampleDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initiate_game(self):
            return self.getTypedRuleContext(ExampleDSLParser.Initiate_gameContext,0)


        def bomb_placements(self):
            return self.getTypedRuleContext(ExampleDSLParser.Bomb_placementsContext,0)


        def output(self):
            return self.getTypedRuleContext(ExampleDSLParser.OutputContext,0)


        def hints(self):
            return self.getTypedRuleContext(ExampleDSLParser.HintsContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExampleDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 29
                self.output()


            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 32
                self.hints()


            self.state = 35
            self.initiate_game()
            self.state = 36
            self.bomb_placements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def output_types(self):
            return self.getTypedRuleContext(ExampleDSLParser.Output_typesContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput" ):
                return visitor.visitOutput(self)
            else:
                return visitor.visitChildren(self)




    def output(self):

        localctx = ExampleDSLParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ExampleDSLParser.T__0)
            self.state = 39
            self.output_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Output_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_output_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput_types" ):
                listener.enterOutput_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput_types" ):
                listener.exitOutput_types(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutput_types" ):
                return visitor.visitOutput_types(self)
            else:
                return visitor.visitChildren(self)




    def output_types(self):

        localctx = ExampleDSLParser.Output_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_output_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HintsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hint_option(self):
            return self.getTypedRuleContext(ExampleDSLParser.Hint_optionContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_hints

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHints" ):
                listener.enterHints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHints" ):
                listener.exitHints(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHints" ):
                return visitor.visitHints(self)
            else:
                return visitor.visitChildren(self)




    def hints(self):

        localctx = ExampleDSLParser.HintsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_hints)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(ExampleDSLParser.T__3)
            self.state = 44
            self.hint_option()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hint_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_hint_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHint_option" ):
                listener.enterHint_option(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHint_option" ):
                listener.exitHint_option(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHint_option" ):
                return visitor.visitHint_option(self)
            else:
                return visitor.visitChildren(self)




    def hint_option(self):

        localctx = ExampleDSLParser.Hint_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_hint_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Initiate_gameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def width(self):
            return self.getTypedRuleContext(ExampleDSLParser.WidthContext,0)


        def height(self):
            return self.getTypedRuleContext(ExampleDSLParser.HeightContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_initiate_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitiate_game" ):
                listener.enterInitiate_game(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitiate_game" ):
                listener.exitInitiate_game(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitiate_game" ):
                return visitor.visitInitiate_game(self)
            else:
                return visitor.visitChildren(self)




    def initiate_game(self):

        localctx = ExampleDSLParser.Initiate_gameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initiate_game)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExampleDSLParser.T__6)
            self.state = 49
            self.width()
            self.state = 50
            self.match(ExampleDSLParser.T__7)
            self.state = 51
            self.height()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_width

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidth" ):
                listener.enterWidth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidth" ):
                listener.exitWidth(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWidth" ):
                return visitor.visitWidth(self)
            else:
                return visitor.visitChildren(self)




    def width(self):

        localctx = ExampleDSLParser.WidthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_width)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_height

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeight" ):
                listener.enterHeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeight" ):
                listener.exitHeight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeight" ):
                return visitor.visitHeight(self)
            else:
                return visitor.visitChildren(self)




    def height(self):

        localctx = ExampleDSLParser.HeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_height)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bomb_placementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bomb_location(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExampleDSLParser.Bomb_locationContext)
            else:
                return self.getTypedRuleContext(ExampleDSLParser.Bomb_locationContext,i)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_bomb_placements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBomb_placements" ):
                listener.enterBomb_placements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBomb_placements" ):
                listener.exitBomb_placements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBomb_placements" ):
                return visitor.visitBomb_placements(self)
            else:
                return visitor.visitChildren(self)




    def bomb_placements(self):

        localctx = ExampleDSLParser.Bomb_placementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bomb_placements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.match(ExampleDSLParser.T__8)
                self.state = 58
                self.bomb_location()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bomb_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def x_location(self):
            return self.getTypedRuleContext(ExampleDSLParser.X_locationContext,0)


        def y_location(self):
            return self.getTypedRuleContext(ExampleDSLParser.Y_locationContext,0)


        def getRuleIndex(self):
            return ExampleDSLParser.RULE_bomb_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBomb_location" ):
                listener.enterBomb_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBomb_location" ):
                listener.exitBomb_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBomb_location" ):
                return visitor.visitBomb_location(self)
            else:
                return visitor.visitChildren(self)




    def bomb_location(self):

        localctx = ExampleDSLParser.Bomb_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bomb_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.x_location()
            self.state = 64
            self.match(ExampleDSLParser.T__9)
            self.state = 65
            self.y_location()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class X_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_x_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX_location" ):
                listener.enterX_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX_location" ):
                listener.exitX_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitX_location" ):
                return visitor.visitX_location(self)
            else:
                return visitor.visitChildren(self)




    def x_location(self):

        localctx = ExampleDSLParser.X_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_x_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Y_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExampleDSLParser.INTEGER, 0)

        def getRuleIndex(self):
            return ExampleDSLParser.RULE_y_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterY_location" ):
                listener.enterY_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitY_location" ):
                listener.exitY_location(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitY_location" ):
                return visitor.visitY_location(self)
            else:
                return visitor.visitChildren(self)




    def y_location(self):

        localctx = ExampleDSLParser.Y_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_y_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ExampleDSLParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





