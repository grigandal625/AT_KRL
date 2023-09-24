# Generated from /app/at_krl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .at_krlParser import at_krlParser
else:
    from at_krlParser import at_krlParser

# This class defines a complete listener for a parse tree produced by at_krlParser.
class at_krlListener(ParseTreeListener):

    # Enter a parse tree produced by at_krlParser#instructions.
    def enterInstructions(self, ctx:at_krlParser.InstructionsContext):
        pass

    # Exit a parse tree produced by at_krlParser#instructions.
    def exitInstructions(self, ctx:at_krlParser.InstructionsContext):
        pass


    # Enter a parse tree produced by at_krlParser#assign_instruction.
    def enterAssign_instruction(self, ctx:at_krlParser.Assign_instructionContext):
        pass

    # Exit a parse tree produced by at_krlParser#assign_instruction.
    def exitAssign_instruction(self, ctx:at_krlParser.Assign_instructionContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rules.
    def enterKb_rules(self, ctx:at_krlParser.Kb_rulesContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rules.
    def exitKb_rules(self, ctx:at_krlParser.Kb_rulesContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rule.
    def enterKb_rule(self, ctx:at_krlParser.Kb_ruleContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rule.
    def exitKb_rule(self, ctx:at_krlParser.Kb_ruleContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rule_instructions.
    def enterKb_rule_instructions(self, ctx:at_krlParser.Kb_rule_instructionsContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rule_instructions.
    def exitKb_rule_instructions(self, ctx:at_krlParser.Kb_rule_instructionsContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rule_condition.
    def enterKb_rule_condition(self, ctx:at_krlParser.Kb_rule_conditionContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rule_condition.
    def exitKb_rule_condition(self, ctx:at_krlParser.Kb_rule_conditionContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rule_else_instructions.
    def enterKb_rule_else_instructions(self, ctx:at_krlParser.Kb_rule_else_instructionsContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rule_else_instructions.
    def exitKb_rule_else_instructions(self, ctx:at_krlParser.Kb_rule_else_instructionsContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rule_comment.
    def enterKb_rule_comment(self, ctx:at_krlParser.Kb_rule_commentContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rule_comment.
    def exitKb_rule_comment(self, ctx:at_krlParser.Kb_rule_commentContext):
        pass


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


    # Enter a parse tree produced by at_krlParser#kb_operation.
    def enterKb_operation(self, ctx:at_krlParser.Kb_operationContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_operation.
    def exitKb_operation(self, ctx:at_krlParser.Kb_operationContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_value.
    def enterKb_value(self, ctx:at_krlParser.Kb_valueContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_value.
    def exitKb_value(self, ctx:at_krlParser.Kb_valueContext):
        pass


    # Enter a parse tree produced by at_krlParser#ref_path.
    def enterRef_path(self, ctx:at_krlParser.Ref_pathContext):
        pass

    # Exit a parse tree produced by at_krlParser#ref_path.
    def exitRef_path(self, ctx:at_krlParser.Ref_pathContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_reference.
    def enterKb_reference(self, ctx:at_krlParser.Kb_referenceContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_reference.
    def exitKb_reference(self, ctx:at_krlParser.Kb_referenceContext):
        pass


    # Enter a parse tree produced by at_krlParser#evaluatable.
    def enterEvaluatable(self, ctx:at_krlParser.EvaluatableContext):
        pass

    # Exit a parse tree produced by at_krlParser#evaluatable.
    def exitEvaluatable(self, ctx:at_krlParser.EvaluatableContext):
        pass



del at_krlParser