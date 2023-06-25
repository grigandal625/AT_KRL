# Generated from /app/evaluatable.g4 by ANTLR 4.13.0
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
        4,1,15,51,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,4,0,11,8,0,11,
        0,12,0,12,1,0,3,0,16,8,0,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,30,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,44,8,2,10,2,12,2,47,9,2,1,3,1,3,1,3,0,1,4,4,0,2,4,6,0,
        1,1,0,10,11,56,0,15,1,0,0,0,2,17,1,0,0,0,4,29,1,0,0,0,6,48,1,0,0,
        0,8,16,5,15,0,0,9,11,5,9,0,0,10,9,1,0,0,0,11,12,1,0,0,0,12,10,1,
        0,0,0,12,13,1,0,0,0,13,16,1,0,0,0,14,16,5,13,0,0,15,8,1,0,0,0,15,
        10,1,0,0,0,15,14,1,0,0,0,16,1,1,0,0,0,17,20,7,0,0,0,18,19,5,5,0,
        0,19,21,3,2,1,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,23,6,
        2,-1,0,23,30,3,2,1,0,24,30,3,0,0,0,25,26,5,6,0,0,26,27,3,4,2,0,27,
        28,5,7,0,0,28,30,1,0,0,0,29,22,1,0,0,0,29,24,1,0,0,0,29,25,1,0,0,
        0,30,45,1,0,0,0,31,32,10,7,0,0,32,33,5,4,0,0,33,44,3,4,2,8,34,35,
        10,6,0,0,35,36,5,3,0,0,36,44,3,4,2,7,37,38,10,5,0,0,38,39,5,2,0,
        0,39,44,3,4,2,6,40,41,10,4,0,0,41,42,5,1,0,0,42,44,3,4,2,5,43,31,
        1,0,0,0,43,34,1,0,0,0,43,37,1,0,0,0,43,40,1,0,0,0,44,47,1,0,0,0,
        45,43,1,0,0,0,45,46,1,0,0,0,46,5,1,0,0,0,47,45,1,0,0,0,48,49,3,4,
        2,0,49,7,1,0,0,0,6,12,15,20,29,43,45
    ]

class evaluatableParser ( Parser ):

    grammarFileName = "evaluatable.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "LOG_SIGN", "COMP_SIGN", "LOWP_MATH_SIGN", 
                      "HIGHP_MATH_SIGN", "DOT", "L_BRACKET", "R_BRACKET", 
                      "LETTER", "DIGIT", "ALPHANUMERIC", "ALPHANUMERIC_U", 
                      "NUMERIC", "FRAC", "WS", "STRING" ]

    RULE_kb_value = 0
    RULE_kb_reference = 1
    RULE_kb_operation = 2
    RULE_evaluatable = 3

    ruleNames =  [ "kb_value", "kb_reference", "kb_operation", "evaluatable" ]

    EOF = Token.EOF
    LOG_SIGN=1
    COMP_SIGN=2
    LOWP_MATH_SIGN=3
    HIGHP_MATH_SIGN=4
    DOT=5
    L_BRACKET=6
    R_BRACKET=7
    LETTER=8
    DIGIT=9
    ALPHANUMERIC=10
    ALPHANUMERIC_U=11
    NUMERIC=12
    FRAC=13
    WS=14
    STRING=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Kb_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(evaluatableParser.STRING, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(evaluatableParser.DIGIT)
            else:
                return self.getToken(evaluatableParser.DIGIT, i)

        def FRAC(self):
            return self.getToken(evaluatableParser.FRAC, 0)

        def getRuleIndex(self):
            return evaluatableParser.RULE_kb_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_value" ):
                listener.enterKb_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_value" ):
                listener.exitKb_value(self)




    def kb_value(self):

        localctx = evaluatableParser.Kb_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_kb_value)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(evaluatableParser.STRING)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 10 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 9
                        self.match(evaluatableParser.DIGIT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 12 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(evaluatableParser.FRAC)
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

        def ALPHANUMERIC(self):
            return self.getToken(evaluatableParser.ALPHANUMERIC, 0)

        def ALPHANUMERIC_U(self):
            return self.getToken(evaluatableParser.ALPHANUMERIC_U, 0)

        def DOT(self):
            return self.getToken(evaluatableParser.DOT, 0)

        def kb_reference(self):
            return self.getTypedRuleContext(evaluatableParser.Kb_referenceContext,0)


        def getRuleIndex(self):
            return evaluatableParser.RULE_kb_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_reference" ):
                listener.enterKb_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_reference" ):
                listener.exitKb_reference(self)




    def kb_reference(self):

        localctx = evaluatableParser.Kb_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_kb_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 18
                self.match(evaluatableParser.DOT)
                self.state = 19
                self.kb_reference()


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

        def kb_reference(self):
            return self.getTypedRuleContext(evaluatableParser.Kb_referenceContext,0)


        def kb_value(self):
            return self.getTypedRuleContext(evaluatableParser.Kb_valueContext,0)


        def L_BRACKET(self):
            return self.getToken(evaluatableParser.L_BRACKET, 0)

        def kb_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(evaluatableParser.Kb_operationContext)
            else:
                return self.getTypedRuleContext(evaluatableParser.Kb_operationContext,i)


        def R_BRACKET(self):
            return self.getToken(evaluatableParser.R_BRACKET, 0)

        def HIGHP_MATH_SIGN(self):
            return self.getToken(evaluatableParser.HIGHP_MATH_SIGN, 0)

        def LOWP_MATH_SIGN(self):
            return self.getToken(evaluatableParser.LOWP_MATH_SIGN, 0)

        def COMP_SIGN(self):
            return self.getToken(evaluatableParser.COMP_SIGN, 0)

        def LOG_SIGN(self):
            return self.getToken(evaluatableParser.LOG_SIGN, 0)

        def getRuleIndex(self):
            return evaluatableParser.RULE_kb_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_operation" ):
                listener.enterKb_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_operation" ):
                listener.exitKb_operation(self)



    def kb_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = evaluatableParser.Kb_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_kb_operation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11]:
                self.state = 23
                self.kb_reference()
                pass
            elif token in [9, 13, 15]:
                self.state = 24
                self.kb_value()
                pass
            elif token in [6]:
                self.state = 25
                self.match(evaluatableParser.L_BRACKET)
                self.state = 26
                self.kb_operation(0)
                self.state = 27
                self.match(evaluatableParser.R_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = evaluatableParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        self.match(evaluatableParser.HIGHP_MATH_SIGN)
                        self.state = 33
                        self.kb_operation(8)
                        pass

                    elif la_ == 2:
                        localctx = evaluatableParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 35
                        self.match(evaluatableParser.LOWP_MATH_SIGN)
                        self.state = 36
                        self.kb_operation(7)
                        pass

                    elif la_ == 3:
                        localctx = evaluatableParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 37
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 38
                        self.match(evaluatableParser.COMP_SIGN)
                        self.state = 39
                        self.kb_operation(6)
                        pass

                    elif la_ == 4:
                        localctx = evaluatableParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(evaluatableParser.LOG_SIGN)
                        self.state = 42
                        self.kb_operation(5)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
            return self.getTypedRuleContext(evaluatableParser.Kb_operationContext,0)


        def getRuleIndex(self):
            return evaluatableParser.RULE_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluatable" ):
                listener.enterEvaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluatable" ):
                listener.exitEvaluatable(self)




    def evaluatable(self):

        localctx = evaluatableParser.EvaluatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
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
        self._predicates[2] = self.kb_operation_sempred
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
         




