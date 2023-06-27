# Generated from /app/at_krl.g4 by ANTLR 4.13.0
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
        4,1,26,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,3,
        2,30,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,50,8,4,3,4,52,8,4,1,5,1,5,1,5,1,5,3,5,58,
        8,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,66,8,5,1,5,1,5,1,5,1,5,3,5,72,8,
        5,1,5,1,5,1,5,1,5,3,5,78,8,5,1,5,1,5,1,5,1,5,3,5,84,8,5,1,5,1,5,
        1,5,1,5,3,5,90,8,5,5,5,92,8,5,10,5,12,5,95,9,5,1,6,1,6,1,6,0,1,10,
        7,0,2,4,6,8,10,12,0,4,2,0,21,21,24,24,1,0,1,2,1,0,22,23,1,0,3,6,
        110,0,14,1,0,0,0,2,21,1,0,0,0,4,29,1,0,0,0,6,39,1,0,0,0,8,51,1,0,
        0,0,10,65,1,0,0,0,12,96,1,0,0,0,14,15,5,7,0,0,15,16,5,16,0,0,16,
        17,7,0,0,0,17,18,7,1,0,0,18,19,7,0,0,0,19,20,5,17,0,0,20,1,1,0,0,
        0,21,22,5,8,0,0,22,23,7,0,0,0,23,3,1,0,0,0,24,30,3,0,0,0,25,30,3,
        2,1,0,26,27,3,0,0,0,27,28,3,2,1,0,28,30,1,0,0,0,29,24,1,0,0,0,29,
        25,1,0,0,0,29,26,1,0,0,0,30,5,1,0,0,0,31,32,5,14,0,0,32,33,3,6,3,
        0,33,34,3,4,2,0,34,35,5,15,0,0,35,40,1,0,0,0,36,40,5,26,0,0,37,40,
        5,21,0,0,38,40,5,24,0,0,39,31,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,
        0,39,38,1,0,0,0,40,7,1,0,0,0,41,42,5,14,0,0,42,43,3,8,4,0,43,44,
        3,4,2,0,44,45,5,15,0,0,45,52,1,0,0,0,46,49,7,2,0,0,47,48,5,13,0,
        0,48,50,3,8,4,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,41,
        1,0,0,0,51,46,1,0,0,0,52,9,1,0,0,0,53,54,6,5,-1,0,54,55,7,3,0,0,
        55,57,3,10,5,0,56,58,3,4,2,0,57,56,1,0,0,0,57,58,1,0,0,0,58,66,1,
        0,0,0,59,66,3,8,4,0,60,66,3,6,3,0,61,62,5,14,0,0,62,63,3,10,5,0,
        63,64,5,15,0,0,64,66,1,0,0,0,65,53,1,0,0,0,65,59,1,0,0,0,65,60,1,
        0,0,0,65,61,1,0,0,0,66,93,1,0,0,0,67,68,10,7,0,0,68,69,5,12,0,0,
        69,71,3,10,5,0,70,72,3,4,2,0,71,70,1,0,0,0,71,72,1,0,0,0,72,92,1,
        0,0,0,73,74,10,6,0,0,74,75,5,11,0,0,75,77,3,10,5,0,76,78,3,4,2,0,
        77,76,1,0,0,0,77,78,1,0,0,0,78,92,1,0,0,0,79,80,10,5,0,0,80,81,5,
        10,0,0,81,83,3,10,5,0,82,84,3,4,2,0,83,82,1,0,0,0,83,84,1,0,0,0,
        84,92,1,0,0,0,85,86,10,4,0,0,86,87,5,9,0,0,87,89,3,10,5,0,88,90,
        3,4,2,0,89,88,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,0,91,67,1,0,0,0,
        91,73,1,0,0,0,91,79,1,0,0,0,91,85,1,0,0,0,92,95,1,0,0,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,11,1,0,0,0,95,93,1,0,0,0,96,97,3,10,5,0,97,
        13,1,0,0,0,12,29,39,49,51,57,65,71,77,83,89,91,93
    ]

class at_krlParser ( Parser ):

    grammarFileName = "at_krl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'-'", "'~'", "'!'", "'not'", 
                     "'\\u0423\\u0412\\u0415\\u0420\\u0415\\u041D\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u0422\\u041E\\u0427\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BELIEF", "ACCURACY", 
                      "LOG_SIGN", "COMP_SIGN", "LOWP_MATH_SIGN", "HIGHP_MATH_SIGN", 
                      "DOT", "L_BR", "R_BR", "LS_BR", "RS_BR", "LF_BR", 
                      "RF_BR", "LETTER", "NUMERIC", "ALPHANUMERIC", "ALPHANUMERIC_U", 
                      "FRAC", "WS", "STRING" ]

    RULE_belief = 0
    RULE_accuracy = 1
    RULE_non_factor = 2
    RULE_kb_value = 3
    RULE_kb_reference = 4
    RULE_kb_operation = 5
    RULE_evaluatable = 6

    ruleNames =  [ "belief", "accuracy", "non_factor", "kb_value", "kb_reference", 
                   "kb_operation", "evaluatable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    BELIEF=7
    ACCURACY=8
    LOG_SIGN=9
    COMP_SIGN=10
    LOWP_MATH_SIGN=11
    HIGHP_MATH_SIGN=12
    DOT=13
    L_BR=14
    R_BR=15
    LS_BR=16
    RS_BR=17
    LF_BR=18
    RF_BR=19
    LETTER=20
    NUMERIC=21
    ALPHANUMERIC=22
    ALPHANUMERIC_U=23
    FRAC=24
    WS=25
    STRING=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class BeliefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BELIEF(self):
            return self.getToken(at_krlParser.BELIEF, 0)

        def LS_BR(self):
            return self.getToken(at_krlParser.LS_BR, 0)

        def RS_BR(self):
            return self.getToken(at_krlParser.RS_BR, 0)

        def NUMERIC(self, i:int=None):
            if i is None:
                return self.getTokens(at_krlParser.NUMERIC)
            else:
                return self.getToken(at_krlParser.NUMERIC, i)

        def FRAC(self, i:int=None):
            if i is None:
                return self.getTokens(at_krlParser.FRAC)
            else:
                return self.getToken(at_krlParser.FRAC, i)

        def getRuleIndex(self):
            return at_krlParser.RULE_belief

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBelief" ):
                listener.enterBelief(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBelief" ):
                listener.exitBelief(self)




    def belief(self):

        localctx = at_krlParser.BeliefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_belief)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(at_krlParser.BELIEF)
            self.state = 15
            self.match(at_krlParser.LS_BR)
            self.state = 16
            _la = self._input.LA(1)
            if not(_la==21 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 17
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 18
            _la = self._input.LA(1)
            if not(_la==21 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 19
            self.match(at_krlParser.RS_BR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccuracyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCURACY(self):
            return self.getToken(at_krlParser.ACCURACY, 0)

        def NUMERIC(self):
            return self.getToken(at_krlParser.NUMERIC, 0)

        def FRAC(self):
            return self.getToken(at_krlParser.FRAC, 0)

        def getRuleIndex(self):
            return at_krlParser.RULE_accuracy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccuracy" ):
                listener.enterAccuracy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccuracy" ):
                listener.exitAccuracy(self)




    def accuracy(self):

        localctx = at_krlParser.AccuracyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_accuracy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(at_krlParser.ACCURACY)
            self.state = 22
            _la = self._input.LA(1)
            if not(_la==21 or _la==24):
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


    class Non_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def belief(self):
            return self.getTypedRuleContext(at_krlParser.BeliefContext,0)


        def accuracy(self):
            return self.getTypedRuleContext(at_krlParser.AccuracyContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_non_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_factor" ):
                listener.enterNon_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_factor" ):
                listener.exitNon_factor(self)




    def non_factor(self):

        localctx = at_krlParser.Non_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_non_factor)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.belief()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.accuracy()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.belief()
                self.state = 27
                self.accuracy()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BR(self):
            return self.getToken(at_krlParser.L_BR, 0)

        def kb_value(self):
            return self.getTypedRuleContext(at_krlParser.Kb_valueContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


        def R_BR(self):
            return self.getToken(at_krlParser.R_BR, 0)

        def STRING(self):
            return self.getToken(at_krlParser.STRING, 0)

        def NUMERIC(self):
            return self.getToken(at_krlParser.NUMERIC, 0)

        def FRAC(self):
            return self.getToken(at_krlParser.FRAC, 0)

        def getRuleIndex(self):
            return at_krlParser.RULE_kb_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_value" ):
                listener.enterKb_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_value" ):
                listener.exitKb_value(self)




    def kb_value(self):

        localctx = at_krlParser.Kb_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_kb_value)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(at_krlParser.L_BR)
                self.state = 32
                self.kb_value()
                self.state = 33
                self.non_factor()
                self.state = 34
                self.match(at_krlParser.R_BR)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(at_krlParser.STRING)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(at_krlParser.NUMERIC)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.match(at_krlParser.FRAC)
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


    class Kb_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BR(self):
            return self.getToken(at_krlParser.L_BR, 0)

        def kb_reference(self):
            return self.getTypedRuleContext(at_krlParser.Kb_referenceContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


        def R_BR(self):
            return self.getToken(at_krlParser.R_BR, 0)

        def ALPHANUMERIC(self):
            return self.getToken(at_krlParser.ALPHANUMERIC, 0)

        def ALPHANUMERIC_U(self):
            return self.getToken(at_krlParser.ALPHANUMERIC_U, 0)

        def DOT(self):
            return self.getToken(at_krlParser.DOT, 0)

        def getRuleIndex(self):
            return at_krlParser.RULE_kb_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_reference" ):
                listener.enterKb_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_reference" ):
                listener.exitKb_reference(self)




    def kb_reference(self):

        localctx = at_krlParser.Kb_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_kb_reference)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(at_krlParser.L_BR)
                self.state = 42
                self.kb_reference()
                self.state = 43
                self.non_factor()
                self.state = 44
                self.match(at_krlParser.R_BR)
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 47
                    self.match(at_krlParser.DOT)
                    self.state = 48
                    self.kb_reference()


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


    class Kb_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krlParser.Kb_operationContext)
            else:
                return self.getTypedRuleContext(at_krlParser.Kb_operationContext,i)


        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


        def kb_reference(self):
            return self.getTypedRuleContext(at_krlParser.Kb_referenceContext,0)


        def kb_value(self):
            return self.getTypedRuleContext(at_krlParser.Kb_valueContext,0)


        def L_BR(self):
            return self.getToken(at_krlParser.L_BR, 0)

        def R_BR(self):
            return self.getToken(at_krlParser.R_BR, 0)

        def HIGHP_MATH_SIGN(self):
            return self.getToken(at_krlParser.HIGHP_MATH_SIGN, 0)

        def LOWP_MATH_SIGN(self):
            return self.getToken(at_krlParser.LOWP_MATH_SIGN, 0)

        def COMP_SIGN(self):
            return self.getToken(at_krlParser.COMP_SIGN, 0)

        def LOG_SIGN(self):
            return self.getToken(at_krlParser.LOG_SIGN, 0)

        def getRuleIndex(self):
            return at_krlParser.RULE_kb_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_operation" ):
                listener.enterKb_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_operation" ):
                listener.exitKb_operation(self)



    def kb_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = at_krlParser.Kb_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_kb_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 54
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                self.kb_operation(0)
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.non_factor()


                pass

            elif la_ == 2:
                self.state = 59
                self.kb_reference()
                pass

            elif la_ == 3:
                self.state = 60
                self.kb_value()
                pass

            elif la_ == 4:
                self.state = 61
                self.match(at_krlParser.L_BR)
                self.state = 62
                self.kb_operation(0)
                self.state = 63
                self.match(at_krlParser.R_BR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 67
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 68
                        self.match(at_krlParser.HIGHP_MATH_SIGN)
                        self.state = 69
                        self.kb_operation(0)
                        self.state = 71
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                        if la_ == 1:
                            self.state = 70
                            self.non_factor()


                        pass

                    elif la_ == 2:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 73
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 74
                        self.match(at_krlParser.LOWP_MATH_SIGN)
                        self.state = 75
                        self.kb_operation(0)
                        self.state = 77
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                        if la_ == 1:
                            self.state = 76
                            self.non_factor()


                        pass

                    elif la_ == 3:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        self.match(at_krlParser.COMP_SIGN)
                        self.state = 81
                        self.kb_operation(0)
                        self.state = 83
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                        if la_ == 1:
                            self.state = 82
                            self.non_factor()


                        pass

                    elif la_ == 4:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        self.match(at_krlParser.LOG_SIGN)
                        self.state = 87
                        self.kb_operation(0)
                        self.state = 89
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                        if la_ == 1:
                            self.state = 88
                            self.non_factor()


                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EvaluatableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_operation(self):
            return self.getTypedRuleContext(at_krlParser.Kb_operationContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluatable" ):
                listener.enterEvaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluatable" ):
                listener.exitEvaluatable(self)




    def evaluatable(self):

        localctx = at_krlParser.EvaluatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.kb_operation(0)
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
        self._predicates[5] = self.kb_operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def kb_operation_sempred(self, localctx:Kb_operationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




