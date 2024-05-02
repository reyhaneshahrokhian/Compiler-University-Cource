# Generated from /home/reyhan/Desktop/study/uni/4022/Compiler/HW/HW2/TypeChecker.g4 by ANTLR 4.13.1
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
        4,1,12,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,35,8,2,10,2,12,2,38,9,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,3,0,2,2,4,4,0,2,4,6,0,0,51,0,8,1,
        0,0,0,2,11,1,0,0,0,4,25,1,0,0,0,6,46,1,0,0,0,8,9,3,2,1,0,9,10,5,
        0,0,1,10,1,1,0,0,0,11,12,6,1,-1,0,12,13,3,4,2,0,13,22,1,0,0,0,14,
        15,10,3,0,0,15,16,5,3,0,0,16,21,3,4,2,0,17,18,10,2,0,0,18,19,5,4,
        0,0,19,21,3,4,2,0,20,14,1,0,0,0,20,17,1,0,0,0,21,24,1,0,0,0,22,20,
        1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,22,1,0,0,0,25,26,6,2,-1,0,
        26,27,3,6,3,0,27,36,1,0,0,0,28,29,10,3,0,0,29,30,5,5,0,0,30,35,3,
        6,3,0,31,32,10,2,0,0,32,33,5,6,0,0,33,35,3,6,3,0,34,28,1,0,0,0,34,
        31,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,
        0,38,36,1,0,0,0,39,47,5,8,0,0,40,47,5,9,0,0,41,47,5,10,0,0,42,43,
        5,1,0,0,43,44,3,2,1,0,44,45,5,2,0,0,45,47,1,0,0,0,46,39,1,0,0,0,
        46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,47,7,1,0,0,0,5,20,22,34,
        36,46
    ]

class TypeCheckerParser ( Parser ):

    grammarFileName = "TypeChecker.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "Plus", "MINUS", 
                      "MUL", "DIVIDE", "ASSIGN", "STRING", "INTEGER", "FLOAT", 
                      "Whitespace", "Newline" ]

    RULE_start = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_fact = 3

    ruleNames =  [ "start", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    Plus=3
    MINUS=4
    MUL=5
    DIVIDE=6
    ASSIGN=7
    STRING=8
    INTEGER=9
    FLOAT=10
    Whitespace=11
    Newline=12

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

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)


        def EOF(self):
            return self.getToken(TypeCheckerParser.EOF, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_start

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

        localctx = TypeCheckerParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(TypeCheckerParser.EOF)
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
            self.type_ = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Expr3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3" ):
                listener.enterExpr3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3" ):
                listener.exitExpr3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)


    class Expr2Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(TypeCheckerParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)


    class Expr1Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)

        def Plus(self):
            return self.getToken(TypeCheckerParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypeCheckerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TypeCheckerParser.Expr3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 12
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 20
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = TypeCheckerParser.Expr1Context(self, TypeCheckerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.match(TypeCheckerParser.Plus)
                        self.state = 16
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = TypeCheckerParser.Expr2Context(self, TypeCheckerParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 18
                        self.match(TypeCheckerParser.MINUS)
                        self.state = 19
                        self.term(0)
                        pass

             
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            self.type_ = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_


    class Term2Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)

        def DIVIDE(self):
            return self.getToken(TypeCheckerParser.DIVIDE, 0)
        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm2" ):
                listener.enterTerm2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm2" ):
                listener.exitTerm2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm2" ):
                return visitor.visitTerm2(self)
            else:
                return visitor.visitChildren(self)


    class Term3Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm3" ):
                listener.enterTerm3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm3" ):
                listener.exitTerm3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm3" ):
                return visitor.visitTerm3(self)
            else:
                return visitor.visitChildren(self)


    class Term1Context(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(TypeCheckerParser.TermContext,0)

        def MUL(self):
            return self.getToken(TypeCheckerParser.MUL, 0)
        def fact(self):
            return self.getTypedRuleContext(TypeCheckerParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm1" ):
                listener.enterTerm1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm1" ):
                listener.exitTerm1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm1" ):
                return visitor.visitTerm1(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TypeCheckerParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = TypeCheckerParser.Term3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 26
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = TypeCheckerParser.Term1Context(self, TypeCheckerParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        self.match(TypeCheckerParser.MUL)
                        self.state = 30
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = TypeCheckerParser.Term2Context(self, TypeCheckerParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(TypeCheckerParser.DIVIDE)
                        self.state = 33
                        self.fact()
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = str()


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.type_ = ctx.type_



    class FactIntegerContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(TypeCheckerParser.INTEGER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactInteger" ):
                listener.enterFactInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactInteger" ):
                listener.exitFactInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactInteger" ):
                return visitor.visitFactInteger(self)
            else:
                return visitor.visitChildren(self)


    class FactExprContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactExpr" ):
                listener.enterFactExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactExpr" ):
                listener.exitFactExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactExpr" ):
                return visitor.visitFactExpr(self)
            else:
                return visitor.visitChildren(self)


    class FactFloatContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(TypeCheckerParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactFloat" ):
                listener.enterFactFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactFloat" ):
                listener.exitFactFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactFloat" ):
                return visitor.visitFactFloat(self)
            else:
                return visitor.visitChildren(self)


    class FactStringContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TypeCheckerParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(TypeCheckerParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactString" ):
                listener.enterFactString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactString" ):
                listener.exitFactString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactString" ):
                return visitor.visitFactString(self)
            else:
                return visitor.visitChildren(self)



    def fact(self):

        localctx = TypeCheckerParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fact)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = TypeCheckerParser.FactStringContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(TypeCheckerParser.STRING)
                pass
            elif token in [9]:
                localctx = TypeCheckerParser.FactIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(TypeCheckerParser.INTEGER)
                pass
            elif token in [10]:
                localctx = TypeCheckerParser.FactFloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(TypeCheckerParser.FLOAT)
                pass
            elif token in [1]:
                localctx = TypeCheckerParser.FactExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.match(TypeCheckerParser.T__0)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(TypeCheckerParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

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
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
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
         




