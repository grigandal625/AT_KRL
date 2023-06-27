# Generated from /app/at_krl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .at_krlParser import at_krlParser
else:
    from at_krlParser import at_krlParser

# This class defines a complete listener for a parse tree produced by at_krlParser.
class at_krlListener(ParseTreeListener):

    # Enter a parse tree produced by at_krlParser#belief.
    def enterBelief(self, ctx:at_krlParser.BeliefContext):
        pass

    # Exit a parse tree produced by at_krlParser#belief.
    def exitBelief(self, ctx:at_krlParser.BeliefContext):
        pass


    # Enter a parse tree produced by at_krlParser#accuracy.
    def enterAccuracy(self, ctx:at_krlParser.AccuracyContext):
        pass

    # Exit a parse tree produced by at_krlParser#accuracy.
    def exitAccuracy(self, ctx:at_krlParser.AccuracyContext):
        pass


    # Enter a parse tree produced by at_krlParser#non_factor.
    def enterNon_factor(self, ctx:at_krlParser.Non_factorContext):
        pass

    # Exit a parse tree produced by at_krlParser#non_factor.
    def exitNon_factor(self, ctx:at_krlParser.Non_factorContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_value.
    def enterKb_value(self, ctx:at_krlParser.Kb_valueContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_value.
    def exitKb_value(self, ctx:at_krlParser.Kb_valueContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_reference.
    def enterKb_reference(self, ctx:at_krlParser.Kb_referenceContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_reference.
    def exitKb_reference(self, ctx:at_krlParser.Kb_referenceContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_operation.
    def enterKb_operation(self, ctx:at_krlParser.Kb_operationContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_operation.
    def exitKb_operation(self, ctx:at_krlParser.Kb_operationContext):
        pass


    # Enter a parse tree produced by at_krlParser#evaluatable.
    def enterEvaluatable(self, ctx:at_krlParser.EvaluatableContext):
        pass

    # Exit a parse tree produced by at_krlParser#evaluatable.
    def exitEvaluatable(self, ctx:at_krlParser.EvaluatableContext):
        pass



del at_krlParser