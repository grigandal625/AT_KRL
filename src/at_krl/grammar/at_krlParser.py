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
        4,1,43,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,40,8,1,1,1,1,
        1,1,1,1,1,1,1,3,1,47,8,1,3,1,49,8,1,1,2,4,2,52,8,2,11,2,12,2,53,
        1,3,1,3,1,3,1,3,1,3,3,3,61,8,3,1,3,1,3,1,4,1,4,4,4,67,8,4,11,4,12,
        4,68,1,5,1,5,1,5,1,6,1,6,4,6,76,8,6,11,6,12,6,77,1,7,1,7,4,7,82,
        8,7,11,7,12,7,83,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,3,10,101,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,109,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,121,8,11,3,11,123,8,11,1,11,1,11,1,11,1,11,1,11,3,11,130,8,11,
        1,11,1,11,1,11,1,11,1,11,3,11,137,8,11,1,11,1,11,1,11,1,11,1,11,
        3,11,144,8,11,1,11,1,11,1,11,1,11,1,11,3,11,151,8,11,5,11,153,8,
        11,10,11,12,11,156,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,166,8,12,1,13,1,13,1,13,3,13,171,8,13,1,14,1,14,1,14,1,14,3,
        14,177,8,14,1,14,1,14,1,14,3,14,182,8,14,1,15,1,15,1,15,1,83,1,22,
        16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,5,1,0,1,3,1,0,38,
        39,2,0,37,37,40,40,1,0,5,6,1,0,7,10,199,0,32,1,0,0,0,2,48,1,0,0,
        0,4,51,1,0,0,0,6,55,1,0,0,0,8,64,1,0,0,0,10,70,1,0,0,0,12,73,1,0,
        0,0,14,79,1,0,0,0,16,85,1,0,0,0,18,92,1,0,0,0,20,100,1,0,0,0,22,
        122,1,0,0,0,24,165,1,0,0,0,26,167,1,0,0,0,28,181,1,0,0,0,30,183,
        1,0,0,0,32,33,3,2,1,0,33,1,1,0,0,0,34,35,3,26,13,0,35,36,7,0,0,0,
        36,39,3,30,15,0,37,40,3,20,10,0,38,40,1,0,0,0,39,37,1,0,0,0,39,38,
        1,0,0,0,40,49,1,0,0,0,41,42,3,30,15,0,42,43,5,4,0,0,43,46,3,26,13,
        0,44,47,3,20,10,0,45,47,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,49,
        1,0,0,0,48,34,1,0,0,0,48,41,1,0,0,0,49,3,1,0,0,0,50,52,3,6,3,0,51,
        50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,5,1,0,0,
        0,55,56,5,14,0,0,56,57,7,1,0,0,57,58,3,10,5,0,58,60,3,8,4,0,59,61,
        3,12,6,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,3,14,7,
        0,63,7,1,0,0,0,64,66,5,16,0,0,65,67,3,0,0,0,66,65,1,0,0,0,67,68,
        1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,9,1,0,0,0,70,71,5,15,0,0,
        71,72,3,22,11,0,72,11,1,0,0,0,73,75,5,17,0,0,74,76,3,0,0,0,75,74,
        1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,13,1,0,0,0,
        79,81,5,22,0,0,80,82,9,0,0,0,81,80,1,0,0,0,82,83,1,0,0,0,83,84,1,
        0,0,0,83,81,1,0,0,0,84,15,1,0,0,0,85,86,5,12,0,0,86,87,5,32,0,0,
        87,88,7,2,0,0,88,89,7,3,0,0,89,90,7,2,0,0,90,91,5,33,0,0,91,17,1,
        0,0,0,92,93,5,13,0,0,93,94,7,2,0,0,94,19,1,0,0,0,95,96,3,16,8,0,
        96,97,3,18,9,0,97,101,1,0,0,0,98,101,3,16,8,0,99,101,3,18,9,0,100,
        95,1,0,0,0,100,98,1,0,0,0,100,99,1,0,0,0,101,21,1,0,0,0,102,103,
        6,11,-1,0,103,104,3,26,13,0,104,105,5,1,0,0,105,108,3,30,15,0,106,
        109,3,20,10,0,107,109,1,0,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,
        123,1,0,0,0,110,123,3,28,14,0,111,123,3,24,12,0,112,113,5,30,0,0,
        113,114,3,22,11,0,114,115,5,31,0,0,115,123,1,0,0,0,116,117,7,4,0,
        0,117,120,3,22,11,0,118,121,3,20,10,0,119,121,1,0,0,0,120,118,1,
        0,0,0,120,119,1,0,0,0,121,123,1,0,0,0,122,102,1,0,0,0,122,110,1,
        0,0,0,122,111,1,0,0,0,122,112,1,0,0,0,122,116,1,0,0,0,123,154,1,
        0,0,0,124,125,10,6,0,0,125,126,5,28,0,0,126,129,3,22,11,0,127,130,
        3,20,10,0,128,130,1,0,0,0,129,127,1,0,0,0,129,128,1,0,0,0,130,153,
        1,0,0,0,131,132,10,5,0,0,132,133,5,27,0,0,133,136,3,22,11,0,134,
        137,3,20,10,0,135,137,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,
        153,1,0,0,0,138,139,10,4,0,0,139,140,5,26,0,0,140,143,3,22,11,0,
        141,144,3,20,10,0,142,144,1,0,0,0,143,141,1,0,0,0,143,142,1,0,0,
        0,144,153,1,0,0,0,145,146,10,3,0,0,146,147,5,25,0,0,147,150,3,22,
        11,0,148,151,3,20,10,0,149,151,1,0,0,0,150,148,1,0,0,0,150,149,1,
        0,0,0,151,153,1,0,0,0,152,124,1,0,0,0,152,131,1,0,0,0,152,138,1,
        0,0,0,152,145,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,0,154,155,1,
        0,0,0,155,23,1,0,0,0,156,154,1,0,0,0,157,158,5,30,0,0,158,159,3,
        24,12,0,159,160,3,20,10,0,160,161,5,31,0,0,161,166,1,0,0,0,162,166,
        5,43,0,0,163,166,5,37,0,0,164,166,5,40,0,0,165,157,1,0,0,0,165,162,
        1,0,0,0,165,163,1,0,0,0,165,164,1,0,0,0,166,25,1,0,0,0,167,170,7,
        1,0,0,168,169,5,29,0,0,169,171,3,26,13,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,27,1,0,0,0,172,173,5,30,0,0,173,176,3,26,13,0,174,177,
        3,20,10,0,175,177,1,0,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,178,
        1,0,0,0,178,179,5,31,0,0,179,182,1,0,0,0,180,182,3,26,13,0,181,172,
        1,0,0,0,181,180,1,0,0,0,182,29,1,0,0,0,183,184,3,22,11,0,184,31,
        1,0,0,0,22,39,46,48,53,60,68,77,83,100,108,120,122,129,136,143,150,
        152,154,165,170,176,181
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
    RULE_kb_rules = 2
    RULE_kb_rule = 3
    RULE_kb_rule_instructions = 4
    RULE_kb_rule_condition = 5
    RULE_kb_rule_else_instructions = 6
    RULE_kb_rule_comment = 7
    RULE_belief = 8
    RULE_accuracy = 9
    RULE_non_factor = 10
    RULE_kb_operation = 11
    RULE_kb_value = 12
    RULE_ref_path = 13
    RULE_kb_reference = 14
    RULE_evaluatable = 15

    ruleNames =  [ "instructions", "assign_instruction", "kb_rules", "kb_rule", 
                   "kb_rule_instructions", "kb_rule_condition", "kb_rule_else_instructions", 
                   "kb_rule_comment", "belief", "accuracy", "non_factor", 
                   "kb_operation", "kb_value", "ref_path", "kb_reference", 
                   "evaluatable" ]

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
            self.state = 32
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
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.ref_path()
                self.state = 35
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.evaluatable()
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 37
                    self.non_factor()
                    pass
                elif token in [7, 8, 9, 10, 17, 22, 30, 37, 38, 39, 40, 43]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.evaluatable()
                self.state = 42
                self.match(at_krlParser.T__3)
                self.state = 43
                self.ref_path()
                self.state = 46
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 44
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


    class Kb_rulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krlParser.Kb_ruleContext)
            else:
                return self.getTypedRuleContext(at_krlParser.Kb_ruleContext,i)


        def getRuleIndex(self):
            return at_krlParser.RULE_kb_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rules" ):
                listener.enterKb_rules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rules" ):
                listener.exitKb_rules(self)




    def kb_rules(self):

        localctx = at_krlParser.Kb_rulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_kb_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.kb_rule()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14):
                    break

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
        self.enterRule(localctx, 6, self.RULE_kb_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(at_krlParser.RULE)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 57
            self.kb_rule_condition()
            self.state = 58
            self.kb_rule_instructions()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 59
                self.kb_rule_else_instructions()


            self.state = 62
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
        self.enterRule(localctx, 8, self.RULE_kb_rule_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(at_krlParser.THEN)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.instructions()
                self.state = 68 
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
        self.enterRule(localctx, 10, self.RULE_kb_rule_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(at_krlParser.IF)
            self.state = 71
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
        self.enterRule(localctx, 12, self.RULE_kb_rule_else_instructions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(at_krlParser.ELSE)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.instructions()
                self.state = 77 
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
        self.enterRule(localctx, 14, self.RULE_kb_rule_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(at_krlParser.COMMENT)
            self.state = 81 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 80
                    self.matchWildcard()

                else:
                    raise NoViableAltException(self)
                self.state = 83 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_belief)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(at_krlParser.BELIEF)
            self.state = 86
            self.match(at_krlParser.LS_BR)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==37 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 90
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
        self.enterRule(localctx, 18, self.RULE_accuracy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(at_krlParser.ACCURACY)
            self.state = 93
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
        self.enterRule(localctx, 20, self.RULE_non_factor)
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.belief()
                self.state = 96
                self.accuracy()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.belief()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 99
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_kb_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 103
                self.ref_path()
                self.state = 104
                self.match(at_krlParser.T__0)
                self.state = 105
                self.evaluatable()
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.non_factor()
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.state = 110
                self.kb_reference()
                pass

            elif la_ == 3:
                self.state = 111
                self.kb_value()
                pass

            elif la_ == 4:
                self.state = 112
                self.match(at_krlParser.L_BR)
                self.state = 113
                self.kb_operation(0)
                self.state = 114
                self.match(at_krlParser.R_BR)
                pass

            elif la_ == 5:
                self.state = 116
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.kb_operation(0)
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self.non_factor()
                    pass

                elif la_ == 2:
                    pass


                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 152
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 124
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 125
                        self.match(at_krlParser.HIGHP_MATH_SIGN)
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

                    elif la_ == 2:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 131
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 132
                        self.match(at_krlParser.LOWP_MATH_SIGN)
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

                    elif la_ == 3:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 138
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 139
                        self.match(at_krlParser.COMP_SIGN)
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

                    elif la_ == 4:
                        localctx = at_krlParser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 145
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 146
                        self.match(at_krlParser.LOG_SIGN)
                        self.state = 147
                        self.kb_operation(0)
                        self.state = 150
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                        if la_ == 1:
                            self.state = 148
                            self.non_factor()
                            pass

                        elif la_ == 2:
                            pass


                        pass

             
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_kb_value)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(at_krlParser.L_BR)
                self.state = 158
                self.kb_value()
                self.state = 159
                self.non_factor()
                self.state = 160
                self.match(at_krlParser.R_BR)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(at_krlParser.STRING)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 3)
                self.state = 163
                self.match(at_krlParser.NUMERIC)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
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
        self.enterRule(localctx, 26, self.RULE_ref_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 168
                self.match(at_krlParser.DOT)
                self.state = 169
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
        self.enterRule(localctx, 28, self.RULE_kb_reference)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(at_krlParser.L_BR)
                self.state = 173
                self.ref_path()
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13]:
                    self.state = 174
                    self.non_factor()
                    pass
                elif token in [31]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 178
                self.match(at_krlParser.R_BR)
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
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
        self.enterRule(localctx, 30, self.RULE_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
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
        self._predicates[11] = self.kb_operation_sempred
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
         




