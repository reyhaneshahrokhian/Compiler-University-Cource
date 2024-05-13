# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW3-STExercise/STGrammar.g4 by ANTLR 4.13.1
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
        4,1,13,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,41,9,3,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,5,
        1,5,3,5,59,8,5,1,5,1,5,3,5,63,8,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,71,
        8,5,1,6,1,6,1,6,0,2,6,8,7,0,2,4,6,8,10,12,0,1,1,0,2,3,78,0,14,1,
        0,0,0,2,22,1,0,0,0,4,24,1,0,0,0,6,28,1,0,0,0,8,42,1,0,0,0,10,70,
        1,0,0,0,12,72,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,3,4,2,0,18,19,5,12,0,0,19,20,3,2,1,0,20,23,1,0,0,0,21,23,3,4,
        2,0,22,17,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,13,0,0,25,26,
        5,1,0,0,26,27,3,6,3,0,27,5,1,0,0,0,28,29,6,3,-1,0,29,30,3,8,4,0,
        30,39,1,0,0,0,31,32,10,3,0,0,32,33,5,2,0,0,33,38,3,6,3,4,34,35,10,
        2,0,0,35,36,5,3,0,0,36,38,3,6,3,3,37,31,1,0,0,0,37,34,1,0,0,0,38,
        41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,7,1,0,0,0,41,39,1,0,0,
        0,42,43,6,4,-1,0,43,44,3,10,5,0,44,53,1,0,0,0,45,46,10,3,0,0,46,
        47,5,4,0,0,47,52,3,8,4,4,48,49,10,2,0,0,49,50,5,5,0,0,50,52,3,8,
        4,3,51,45,1,0,0,0,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,
        1,0,0,0,54,9,1,0,0,0,55,53,1,0,0,0,56,71,5,8,0,0,57,59,3,12,6,0,
        58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,71,5,10,0,0,61,63,3,
        12,6,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,71,5,9,0,0,65,
        66,5,6,0,0,66,67,3,6,3,0,67,68,5,7,0,0,68,71,1,0,0,0,69,71,5,13,
        0,0,70,56,1,0,0,0,70,58,1,0,0,0,70,62,1,0,0,0,70,65,1,0,0,0,70,69,
        1,0,0,0,71,11,1,0,0,0,72,73,7,0,0,0,73,13,1,0,0,0,8,22,37,39,51,
        53,58,62,70
    ]

class STGrammarParser ( Parser ):

    grammarFileName = "STGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ADD", "SUB", "MUL", "DIV", 
                      "LPAREN", "RPAREN", "STRING", "FLOAT", "INTEGER", 
                      "WS", "NEWLINE", "ID" ]

    RULE_start = 0
    RULE_assigns = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_sign = 6

    ruleNames =  [ "start", "assigns", "assign", "expr", "term", "factor", 
                   "sign" ]

    EOF = Token.EOF
    T__0=1
    ADD=2
    SUB=3
    MUL=4
    DIV=5
    LPAREN=6
    RPAREN=7
    STRING=8
    FLOAT=9
    INTEGER=10
    WS=11
    NEWLINE=12
    ID=13

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

        def assigns(self):
            return self.getTypedRuleContext(STGrammarParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(STGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return STGrammarParser.RULE_start

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

        localctx = STGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.assigns()
            self.state = 15
            self.match(STGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(STGrammarParser.AssignContext,0)


        def NEWLINE(self):
            return self.getToken(STGrammarParser.NEWLINE, 0)

        def assigns(self):
            return self.getTypedRuleContext(STGrammarParser.AssignsContext,0)


        def getRuleIndex(self):
            return STGrammarParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = STGrammarParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assign()
                self.state = 18
                self.match(STGrammarParser.NEWLINE)
                self.state = 19
                self.assigns()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(STGrammarParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(STGrammarParser.ExprContext,0)


        def getRuleIndex(self):
            return STGrammarParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = STGrammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(STGrammarParser.ID)
            self.state = 25
            self.match(STGrammarParser.T__0)
            self.state = 26
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = str()

        def term(self):
            return self.getTypedRuleContext(STGrammarParser.TermContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STGrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(STGrammarParser.ExprContext,i)


        def ADD(self):
            return self.getToken(STGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(STGrammarParser.SUB, 0)

        def getRuleIndex(self):
            return STGrammarParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = STGrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = STGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(STGrammarParser.ADD)
                        self.state = 33
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = STGrammarParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(STGrammarParser.SUB)
                        self.state = 36
                        self.expr(3)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = str()

        def factor(self):
            return self.getTypedRuleContext(STGrammarParser.FactorContext,0)


        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STGrammarParser.TermContext)
            else:
                return self.getTypedRuleContext(STGrammarParser.TermContext,i)


        def MUL(self):
            return self.getToken(STGrammarParser.MUL, 0)

        def DIV(self):
            return self.getToken(STGrammarParser.DIV, 0)

        def getRuleIndex(self):
            return STGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = STGrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = STGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(STGrammarParser.MUL)
                        self.state = 47
                        self.term(4)
                        pass

                    elif la_ == 2:
                        localctx = STGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 48
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 49
                        self.match(STGrammarParser.DIV)
                        self.state = 50
                        self.term(3)
                        pass

             
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.rule_type = str()


        def getRuleIndex(self):
            return STGrammarParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.rule_type = ctx.rule_type



    class Factor_is_integerContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(STGrammarParser.INTEGER, 0)
        def sign(self):
            return self.getTypedRuleContext(STGrammarParser.SignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_integer" ):
                listener.enterFactor_is_integer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_integer" ):
                listener.exitFactor_is_integer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_integer" ):
                return visitor.visitFactor_is_integer(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_floatContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(STGrammarParser.FLOAT, 0)
        def sign(self):
            return self.getTypedRuleContext(STGrammarParser.SignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_float" ):
                listener.enterFactor_is_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_float" ):
                listener.exitFactor_is_float(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_float" ):
                return visitor.visitFactor_is_float(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_stringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(STGrammarParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_string" ):
                listener.enterFactor_is_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_string" ):
                listener.exitFactor_is_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_string" ):
                return visitor.visitFactor_is_string(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_expressionContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(STGrammarParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(STGrammarParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(STGrammarParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_expression" ):
                listener.enterFactor_is_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_expression" ):
                listener.exitFactor_is_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_expression" ):
                return visitor.visitFactor_is_expression(self)
            else:
                return visitor.visitChildren(self)


    class Factor_is_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STGrammarParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(STGrammarParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_is_id" ):
                listener.enterFactor_is_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_is_id" ):
                listener.exitFactor_is_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_is_id" ):
                return visitor.visitFactor_is_id(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = STGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = STGrammarParser.Factor_is_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(STGrammarParser.STRING)
                pass

            elif la_ == 2:
                localctx = STGrammarParser.Factor_is_integerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==3:
                    self.state = 57
                    self.sign()


                self.state = 60
                self.match(STGrammarParser.INTEGER)
                pass

            elif la_ == 3:
                localctx = STGrammarParser.Factor_is_floatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==2 or _la==3:
                    self.state = 61
                    self.sign()


                self.state = 64
                self.match(STGrammarParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = STGrammarParser.Factor_is_expressionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.match(STGrammarParser.LPAREN)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(STGrammarParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = STGrammarParser.Factor_is_idContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.match(STGrammarParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(STGrammarParser.ADD, 0)

        def SUB(self):
            return self.getToken(STGrammarParser.SUB, 0)

        def getRuleIndex(self):
            return STGrammarParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = STGrammarParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




