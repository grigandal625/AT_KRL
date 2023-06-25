# Generated from /app/evaluatable.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .evaluatableParser import evaluatableParser
else:
    from evaluatableParser import evaluatableParser

# This class defines a complete listener for a parse tree produced by evaluatableParser.
class evaluatableListener(ParseTreeListener):

    # Enter a parse tree produced by evaluatableParser#kb_value.
    def enterKb_value(self, ctx:evaluatableParser.Kb_valueContext):
        pass

    # Exit a parse tree produced by evaluatableParser#kb_value.
    def exitKb_value(self, ctx:evaluatableParser.Kb_valueContext):
        pass


    # Enter a parse tree produced by evaluatableParser#kb_reference.
    def enterKb_reference(self, ctx:evaluatableParser.Kb_referenceContext):
        pass

    # Exit a parse tree produced by evaluatableParser#kb_reference.
    def exitKb_reference(self, ctx:evaluatableParser.Kb_referenceContext):
        pass


    # Enter a parse tree produced by evaluatableParser#kb_operation.
    def enterKb_operation(self, ctx:evaluatableParser.Kb_operationContext):
        pass

    # Exit a parse tree produced by evaluatableParser#kb_operation.
    def exitKb_operation(self, ctx:evaluatableParser.Kb_operationContext):
        pass


    # Enter a parse tree produced by evaluatableParser#evaluatable.
    def enterEvaluatable(self, ctx:evaluatableParser.EvaluatableContext):
        pass

    # Exit a parse tree produced by evaluatableParser#evaluatable.
    def exitEvaluatable(self, ctx:evaluatableParser.EvaluatableContext):
        pass



del evaluatableParser