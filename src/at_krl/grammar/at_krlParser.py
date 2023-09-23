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
        4,1,43,179,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,1,1,1,1,1,1,1,
        1,1,3,1,45,8,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,2,1,2,
        1,3,1,3,4,3,60,8,3,11,3,12,3,61,1,4,1,4,1,4,1,5,1,5,4,5,69,8,5,11,
        5,12,5,70,1,6,1,6,4,6,75,8,6,11,6,12,6,76,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,94,8,9,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,102,8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,3,10,114,8,10,3,10,116,8,10,1,10,1,10,1,10,1,10,1,
        10,3,10,123,8,10,1,10,1,10,1,10,1,10,1,10,3,10,130,8,10,1,10,1,10,
        1,10,1,10,1,10,3,10,137,8,10,1,10,1,10,1,10,1,10,1,10,3,10,144,8,
        10,5,10,146,8,10,10,10,12,10,149,9,10,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,3,11,159,8,11,1,12,1,12,1,12,3,12,164,8,12,1,13,1,13,
        1,13,1,13,3,13,170,8,13,1,13,1,13,1,13,3,13,175,8,13,1,14,1,14,1,
        14,1,76,1,20,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,5,1,0,
        1,3,1,0,38,39,2,0,37,37,40,40,1,0,5,6,1,0,7,10,192,0,30,1,0,0,0,
        2,46,1,0,0,0,4,48,1,0,0,0,6,57,1,0,0,0,8,63,1,0,0,0,10,66,1,0,0,
        0,12,72,1,0,0,0,14,78,1,0,0,0,16,85,1,0,0,0,18,93,1,0,0,0,20,115,
        1,0,0,0,22,158,1,0,0,0,24,160,1,0,0,0,26,174,1,0,0,0,28,176,1,0,
        0,0,30,31,3,2,1,0,31,1,1,0,0,0,32,33,3,24,12,0,33,34,7,0,0,0,34,
        37,3,28,14,0,35,38,3,18,9,0,36,38,1,0,0,0,37,35,1,0,0,0,37,36,1,
        0,0,0,38,47,1,0,0,0,39,40,3,28,14,0,40,41,5,4,0,0,41,44,3,24,12,
        0,42,45,3,18,9,0,43,45,1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,47,
        1,0,0,0,46,32,1,0,0,0,46,39,1,0,0,0,47,3,1,0,0,0,48,49,5,14,0,0,
        49,50,7,1,0,0,50,51,3,8,4,0,51,53,3,6,3,0,52,54,3,10,5,0,53,52,1,
        0,0,0,53,54,1,0,0,0,54,55,1,0,0,0,55,56,3,12,6,0,56,5,1,0,0,0,57,
        59,5,16,0,0,58,60,3,0,0,0,59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,
        0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,64,5,15,0,0,64,65,3,20,10,0,65,
        9,1,0,0,0,66,68,5,17,0,0,67,69,3,0,0,0,68,67,1,0,0,0,69,70,1,0,0,
        0,70,68,1,0,0,0,70,71,1,0,0,0,71,11,1,0,0,0,72,74,5,22,0,0,73,75,
        9,0,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,76,74,1,0,0,0,
        77,13,1,0,0,0,78,79,5,12,0,0,79,80,5,32,0,0,80,81,7,2,0,0,81,82,
        7,3,0,0,82,83,7,2,0,0,83,84,5,33,0,0,84,15,1,0,0,0,85,86,5,13,0,
        0,86,87,7,2,0,0,87,17,1,0,0,0,88,89,3,14,7,0,89,90,3,16,8,0,90,94,
        1,0,0,0,91,94,3,14,7,0,92,94,3,16,8,0,93,88,1,0,0,0,93,91,1,0,0,
        0,93,92,1,0,0,0,94,19,1,0,0,0,95,96,6,10,-1,0,96,97,3,24,12,0,97,
        98,5,1,0,0,98,101,3,28,14,0,99,102,3,18,9,0,100,102,1,0,0,0,101,
        99,1,0,0,0,101,100,1,0,0,0,102,116,1,0,0,0,103,116,3,26,13,0,104,
        116,3,22,11,0,105,106,5,30,0,0,106,107,3,20,10,0,107,108,5,31,0,
        0,108,116,1,0,0,0,109,110,7,4,0,0,110,113,3,20,10,0,111,114,3,18,
        9,0,112,114,1,0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,116,1,0,
        0,0,115,95,1,0,0,0,115,103,1,0,0,0,115,104,1,0,0,0,115,105,1,0,0,
        0,115,109,1,0,0,0,116,147,1,0,0,0,117,118,10,6,0,0,118,119,5,28,
        0,0,119,122,3,20,10,0,120,123,3,18,9,0,121,123,1,0,0,0,122,120,1,
        0,0,0,122,121,1,0,0,0,123,146,1,0,0,0,124,125,10,5,0,0,125,126,5,
        27,0,0,126,129,3,20,10,0,127,130,3,18,9,0,128,130,1,0,0,0,129,127,
        1,0,0,0,129,128,1,0,0,0,130,146,1,0,0,0,131,132,10,4,0,0,132,133,
        5,26,0,0,133,136,3,20,10,0,134,137,3,18,9,0,135,137,1,0,0,0,136,
        134,1,0,0,0,136,135,1,0,0,0,137,146,1,0,0,0,138,139,10,3,0,0,139,
        140,5,25,0,0,140,143,3,20,10,0,141,144,3,18,9,0,142,144,1,0,0,0,
        143,141,1,0,0,0,143,142,1,0,0,0,144,146,1,0,0,0,145,117,1,0,0,0,
        145,124,1,0,0,0,145,131,1,0,0,0,145,138,1,0,0,0,146,149,1,0,0,0,
        147,145,1,0,0,0,147,148,1,0,0,0,148,21,1,0,0,0,149,147,1,0,0,0,150,
        151,5,30,0,0,151,152,3,22,11,0,152,153,3,18,9,0,153,154,5,31,0,0,
        154,159,1,0,0,0,155,159,5,43,0,0,156,159,5,37,0,0,157,159,5,40,0,
        0,158,150,1,0,0,0,158,155,1,0,0,0,158,156,1,0,0,0,158,157,1,0,0,
        0,159,23,1,0,0,0,160,163,7,1,0,0,161,162,5,29,0,0,162,164,3,24,12,
        0,163,161,1,0,0,0,163,164,1,0,0,0,164,25,1,0,0,0,165,166,5,30,0,
        0,166,169,3,24,12,0,167,170,3,18,9,0,168,170,1,0,0,0,169,167,1,0,
        0,0,169,168,1,0,0,0,170,171,1,0,0,0,171,172,5,31,0,0,172,175,1,0,
        0,0,173,175,3,24,12,0,174,165,1,0,0,0,174,173,1,0,0,0,175,27,1,0,
        0,0,176,177,3,20,10,0,177,29,1,0,0,0,21,37,44,46,53,61,70,76,93,
        101,113,115,122,129,136,143,145,147,158,163,169,174
    ]

class at_krlParser ( Parser ):

    grammarFileName = "at_krl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':='", "'<-'", "'->'", "';'", 
                     "','", "'-'", "'~'", "'!'", "'not'", "'\\r\\n'", "'\\u0423\\u0412\\u0415\\u0420\\u0415\\u041D\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u0422\\u041E\\u0427\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u041F\\u0420\\u0410\\u0412\\u0418\\u041B\\u041E'", 
                     "'\\u0415\\u0421\\u041B\\u0418'", "'\\u0422\\u041E'", 
                     "'\\u0418\\u041D\\u0410\\u0427\\u0415'", "'\\u0422\\u0418\\u041F'", 
                     "'\\u041E\\u0411\\u042A\\u0415\\u041A\\u0422'", "'\\u0413\\u0420\\u0423\\u041F\\u041F\\u0410'", 
                     "'\\u0410\\u0422\\u0420\\u0418\\u0411\\u0423\\u0422'", 
                     "'\\u041A\\u041E\\u041C\\u041C\\u0415\\u041D\\u0422\\u0410\\u0420\\u0418\\u0419'", 
                     "'\\u0418\\u041D\\u0422\\u0415\\u0420\\u0412\\u0410\\u041B'", 
                     "'\\u0421\\u041E\\u0411\\u042B\\u0422\\u0418\\u0415'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NEW_LINE", 
                      "BELIEF", "ACCURACY", "RULE", "IF", "THEN", "ELSE", 
                      "TYPE", "OBJECT", "GROUP", "ATTR", "COMMENT", "INTERVAL", 
                      "EVENT", "LOG_SIGN", "COMP_SIGN", "LOWP_MATH_SIGN", 
                      "HIGHP_MATH_SIGN", "DOT", "L_BR", "R_BR", "LS_BR", 
                      "RS_BR", "LF_BR", "RF_BR", "LETTER", "NUMERIC", "ALPHANUMERIC", 
                      "ALPHANUMERIC_U", "FRAC", "WS", "COMM_CHAR", "STRING" ]

    RULE_instructions = 0
    RULE_assign_instruction = 1
    RULE_kb_rule = 2
    RULE_kb_rule_instructions = 3
    RULE_kb_rule_condition = 4
    RULE_kb_rule_else_instructions = 5
    RULE_kb_rule_comment = 6
    RULE_belief = 7
    RULE_accuracy = 8
    RULE_non_factor = 9
    RULE_kb_operation = 10
    RULE_kb_value = 11
    RULE_ref_path = 12
    RULE_kb_reference = 13
    RULE_evaluatable = 14

    ruleNames =  [ "instructions", "assign_instruction", "kb_rule", "kb_rule_instructions", 
                   "kb_rule_condition", "kb_rule_else_instructions", "kb_rule_comment", 
                   "belief", "accuracy", "non_factor", "kb_operation", "kb_value", 
                   "ref_path", "kb_reference", "evaluatable" ]

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
    NEW_LINE=11
    BELIEF=12
    ACCURACY=13
    RULE=14
    IF=15
    THEN=16
    ELSE=17
    TYPE=18
    OBJECT=19
    GROUP=20
    ATTR=21
    COMMENT=22
    INTERVAL=23
    EVENT=24
    LOG_SIGN=25
    COMP_SIGN=26
    LOWP_MATH_SIGN=27
    HIGHP_MATH_SIGN=28
    DOT=29
    L_BR=30
    R_BR=31
    LS_BR=32
    RS_BR=33
    LF_BR=34
    RF_BR=35
    LETTER=36
    NUMERIC=37
    ALPHANUMERIC=38
    ALPHANUMERIC_U=39
    FRAC=40
    WS=41
    COMM_CHAR=42
    STRING=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InstructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_instruction(self):
            return self.getTypedRuleContext(at_krlParser.Assign_instructionContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructions" ):
                listener.enterInstructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructions" ):
                listener.exitInstructions(self)




    def instructions(self):

        localctx = at_krlParser.InstructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_instructions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.assign_instruction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_instructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ref_path(self):
            return self.getTypedRuleContext(at_krlParser.Ref_pathContext,0)


        def evaluatable(self):
            return self.getTypedRuleContext(at_krlParser.EvaluatableContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_assign_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_instruction" ):
                listener.enterAssign_instruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_instruction" ):
                listener.exitAssign_instruction(self)




    def assign_instruction(self):

        localctx = at_krlParser.Assign_instructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assign_instruction)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.ref_path()
                self.state = 33
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 34
                self.evaluatable()
                self.state = 37
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 35
                    self.non_factor()
                    pass
                elif token in [7, 8, 9, 10, 17, 22, 30, 37, 38, 39, 40, 43]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.evaluatable()
                self.state = 40
                self.match(at_krlParser.T__3)
                self.state = 41
                self.ref_path()
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 42
                    self.non_factor()
                    pass
                elif token in [7, 8, 9, 10, 17, 22, 30, 37, 38, 39, 40, 43]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(at_krlParser.RULE, 0)

        def kb_rule_condition(self):
            return self.getTypedRuleContext(at_krlParser.Kb_rule_conditionContext,0)


        def kb_rule_instructions(self):
            return self.getTypedRuleContext(at_krlParser.Kb_rule_instructionsContext,0)


        def kb_rule_comment(self):
            return self.getTypedRuleContext(at_krlParser.Kb_rule_commentContext,0)


        def ALPHANUMERIC(self):
            return self.getToken(at_krlParser.ALPHANUMERIC, 0)

        def ALPHANUMERIC_U(self):
            return self.getToken(at_krlParser.ALPHANUMERIC_U, 0)

        def kb_rule_else_instructions(self):
            return self.getTypedRuleContext(at_krlParser.Kb_rule_else_instructionsContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule" ):
                listener.enterKb_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule" ):
                listener.exitKb_rule(self)




    def kb_rule(self):

        localctx = at_krlParser.Kb_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_kb_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(at_krlParser.RULE)
            self.state = 49
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 50
            self.kb_rule_condition()
            self.state = 51
            self.kb_rule_instructions()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 52
                self.kb_rule_else_instructions()


            self.state = 55
            self.kb_rule_comment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_instructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THEN(self):
            return self.getToken(at_krlParser.THEN, 0)

        def instructions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krlParser.InstructionsContext)
            else:
                return self.getTypedRuleContext(at_krlParser.InstructionsContext,i)


        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rule_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_instructions" ):
                listener.enterKb_rule_instructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_instructions" ):
                listener.exitKb_rule_instructions(self)




    def kb_rule_instructions(self):

        localctx = at_krlParser.Kb_rule_instructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_kb_rule_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(at_krlParser.THEN)
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.instructions()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10858751068032) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(at_krlParser.IF, 0)

        def kb_operation(self):
            return self.getTypedRuleContext(at_krlParser.Kb_operationContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rule_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_condition" ):
                listener.enterKb_rule_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_condition" ):
                listener.exitKb_rule_condition(self)




    def kb_rule_condition(self):

        localctx = at_krlParser.Kb_rule_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_kb_rule_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(at_krlParser.IF)
            self.state = 64
            self.kb_operation(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_else_instructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(at_krlParser.ELSE, 0)

        def instructions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krlParser.InstructionsContext)
            else:
                return self.getTypedRuleContext(at_krlParser.InstructionsContext,i)


        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rule_else_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_else_instructions" ):
                listener.enterKb_rule_else_instructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_else_instructions" ):
                listener.exitKb_rule_else_instructions(self)




    def kb_rule_else_instructions(self):

        localctx = at_krlParser.Kb_rule_else_instructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_kb_rule_else_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(at_krlParser.ELSE)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.instructions()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10858751068032) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(at_krlParser.COMMENT, 0)

        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rule_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_comment" ):
                listener.enterKb_rule_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_comment" ):
                listener.exitKb_rule_comment(self)




    def kb_rule_comment(self):

        localctx = at_krlParser.Kb_rule_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_kb_rule_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(at_krlParser.COMMENT)
            self.state = 74 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 73
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 76 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 14, self.RULE_belief)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(at_krlParser.BELIEF)
            self.state = 79
            self.match(at_krlParser.LS_BR)
            self.state = 80
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 82
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
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
        self.enterRule(localctx, 16, self.RULE_accuracy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(at_krlParser.ACCURACY)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
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
        self.enterRule(localctx, 18, self.RULE_non_factor)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.belief()
                self.state = 89
                self.accuracy()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.belief()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.accuracy()
                pass


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

        def ref_path(self):
            return self.getTypedRuleContext(at_krlParser.Ref_pathContext,0)


        def evaluatable(self):
            return self.getTypedRuleContext(at_krlParser.EvaluatableContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


        def kb_reference(self):
            return self.getTypedRuleContext(at_krlParser.Kb_referenceContext,0)


        def kb_value(self):
            return self.getTypedRuleContext(at_krlParser.Kb_valueContext,0)


        def L_BR(self):
            return self.getToken(at_krlParser.L_BR, 0)

        def kb_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krlParser.Kb_operationContext)
            else:
                return self.getTypedRuleContext(at_krlParser.Kb_operationContext,i)


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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_kb_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 96
                self.ref_path()
                self.state = 97
                self.match(at_krlParser.T__0)
                self.state = 98
                self.evaluatable()
                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 99
                    self.non_factor()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 103
                self.kb_reference()
                pass

            elif la_ == 3:
                self.state = 104
                self.kb_value()
                pass

            elif la_ == 4:
                self.state = 105
                self.match(at_krlParser.L_BR)
                self.state = 106
                self.kb_operation(0)
                self.state = 107
                self.match(at_krlParser.R_BR)
                pass

            elif la_ == 5:
                self.state = 109
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.kb_operation(0)
                self.state = 113
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 111
                    self.non_factor()
                    pass

                elif la_ == 2:
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 117
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 118
                        self.match(at_krlParser.HIGHP_MATH_SIGN)
                        self.state = 119
                        self.kb_operation(0)
                        self.state = 122
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                        if la_ == 1:
                            self.state = 120
                            self.non_factor()
                            pass

                        elif la_ == 2:
                            pass


                        pass

                    elif la_ == 2:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 124
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 125
                        self.match(at_krlParser.LOWP_MATH_SIGN)
                        self.state = 126
                        self.kb_operation(0)
                        self.state = 129
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                        if la_ == 1:
                            self.state = 127
                            self.non_factor()
                            pass

                        elif la_ == 2:
                            pass


                        pass

                    elif la_ == 3:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 131
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 132
                        self.match(at_krlParser.COMP_SIGN)
                        self.state = 133
                        self.kb_operation(0)
                        self.state = 136
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                        if la_ == 1:
                            self.state = 134
                            self.non_factor()
                            pass

                        elif la_ == 2:
                            pass


                        pass

                    elif la_ == 4:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 138
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 139
                        self.match(at_krlParser.LOG_SIGN)
                        self.state = 140
                        self.kb_operation(0)
                        self.state = 143
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                        if la_ == 1:
                            self.state = 141
                            self.non_factor()
                            pass

                        elif la_ == 2:
                            pass


                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 22, self.RULE_kb_value)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(at_krlParser.L_BR)
                self.state = 151
                self.kb_value()
                self.state = 152
                self.non_factor()
                self.state = 153
                self.match(at_krlParser.R_BR)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.match(at_krlParser.STRING)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(at_krlParser.NUMERIC)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
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


    class Ref_pathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHANUMERIC(self):
            return self.getToken(at_krlParser.ALPHANUMERIC, 0)

        def ALPHANUMERIC_U(self):
            return self.getToken(at_krlParser.ALPHANUMERIC_U, 0)

        def DOT(self):
            return self.getToken(at_krlParser.DOT, 0)

        def ref_path(self):
            return self.getTypedRuleContext(at_krlParser.Ref_pathContext,0)


        def getRuleIndex(self):
            return at_krlParser.RULE_ref_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef_path" ):
                listener.enterRef_path(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef_path" ):
                listener.exitRef_path(self)




    def ref_path(self):

        localctx = at_krlParser.Ref_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ref_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 161
                self.match(at_krlParser.DOT)
                self.state = 162
                self.ref_path()


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

        def ref_path(self):
            return self.getTypedRuleContext(at_krlParser.Ref_pathContext,0)


        def R_BR(self):
            return self.getToken(at_krlParser.R_BR, 0)

        def non_factor(self):
            return self.getTypedRuleContext(at_krlParser.Non_factorContext,0)


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
        self.enterRule(localctx, 26, self.RULE_kb_reference)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(at_krlParser.L_BR)
                self.state = 166
                self.ref_path()
                self.state = 169
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 167
                    self.non_factor()
                    pass
                elif token in [31]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 171
                self.match(at_krlParser.R_BR)
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.ref_path()
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
        self.enterRule(localctx, 28, self.RULE_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self._predicates[10] = self.kb_operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def kb_operation_sempred(self, localctx:Kb_operationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




