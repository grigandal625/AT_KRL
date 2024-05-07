# Generated from /app/at_krl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .at_krlParser import at_krlParser
else:
    from at_krlParser import at_krlParser

# This class defines a complete listener for a parse tree produced by at_krlParser.
class at_krlListener(ParseTreeListener):

    # Enter a parse tree produced by at_krlParser#log_sign.
    def enterLog_sign(self, ctx:at_krlParser.Log_signContext):
        pass

    # Exit a parse tree produced by at_krlParser#log_sign.
    def exitLog_sign(self, ctx:at_krlParser.Log_signContext):
        pass


    # Enter a parse tree produced by at_krlParser#comp_sign.
    def enterComp_sign(self, ctx:at_krlParser.Comp_signContext):
        pass

    # Exit a parse tree produced by at_krlParser#comp_sign.
    def exitComp_sign(self, ctx:at_krlParser.Comp_signContext):
        pass


    # Enter a parse tree produced by at_krlParser#lowp_math_sign.
    def enterLowp_math_sign(self, ctx:at_krlParser.Lowp_math_signContext):
        pass

    # Exit a parse tree produced by at_krlParser#lowp_math_sign.
    def exitLowp_math_sign(self, ctx:at_krlParser.Lowp_math_signContext):
        pass


    # Enter a parse tree produced by at_krlParser#highp_math_sign.
    def enterHighp_math_sign(self, ctx:at_krlParser.Highp_math_signContext):
        pass

    # Exit a parse tree produced by at_krlParser#highp_math_sign.
    def exitHighp_math_sign(self, ctx:at_krlParser.Highp_math_signContext):
        pass


    # Enter a parse tree produced by at_krlParser#knowledge_base.
    def enterKnowledge_base(self, ctx:at_krlParser.Knowledge_baseContext):
        pass

    # Exit a parse tree produced by at_krlParser#knowledge_base.
    def exitKnowledge_base(self, ctx:at_krlParser.Knowledge_baseContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_types.
    def enterKb_types(self, ctx:at_krlParser.Kb_typesContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_types.
    def exitKb_types(self, ctx:at_krlParser.Kb_typesContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_classes.
    def enterKb_classes(self, ctx:at_krlParser.Kb_classesContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_classes.
    def exitKb_classes(self, ctx:at_krlParser.Kb_classesContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_rules.
    def enterKb_rules(self, ctx:at_krlParser.Kb_rulesContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_rules.
    def exitKb_rules(self, ctx:at_krlParser.Kb_rulesContext):
        pass


    # Enter a parse tree produced by at_krlParser#commentary.
    def enterCommentary(self, ctx:at_krlParser.CommentaryContext):
        pass

    # Exit a parse tree produced by at_krlParser#commentary.
    def exitCommentary(self, ctx:at_krlParser.CommentaryContext):
        pass


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


    # Enter a parse tree produced by at_krlParser#kb_allen_operation.
    def enterKb_allen_operation(self, ctx:at_krlParser.Kb_allen_operationContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_allen_operation.
    def exitKb_allen_operation(self, ctx:at_krlParser.Kb_allen_operationContext):
        pass


    # Enter a parse tree produced by at_krlParser#simple_operation.
    def enterSimple_operation(self, ctx:at_krlParser.Simple_operationContext):
        pass

    # Exit a parse tree produced by at_krlParser#simple_operation.
    def exitSimple_operation(self, ctx:at_krlParser.Simple_operationContext):
        pass


    # Enter a parse tree produced by at_krlParser#simple_evaluatable.
    def enterSimple_evaluatable(self, ctx:at_krlParser.Simple_evaluatableContext):
        pass

    # Exit a parse tree produced by at_krlParser#simple_evaluatable.
    def exitSimple_evaluatable(self, ctx:at_krlParser.Simple_evaluatableContext):
        pass


    # Enter a parse tree produced by at_krlParser#simple_value.
    def enterSimple_value(self, ctx:at_krlParser.Simple_valueContext):
        pass

    # Exit a parse tree produced by at_krlParser#simple_value.
    def exitSimple_value(self, ctx:at_krlParser.Simple_valueContext):
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


    # Enter a parse tree produced by at_krlParser#simple_ref.
    def enterSimple_ref(self, ctx:at_krlParser.Simple_refContext):
        pass

    # Exit a parse tree produced by at_krlParser#simple_ref.
    def exitSimple_ref(self, ctx:at_krlParser.Simple_refContext):
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


    # Enter a parse tree produced by at_krlParser#kb_type.
    def enterKb_type(self, ctx:at_krlParser.Kb_typeContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_type.
    def exitKb_type(self, ctx:at_krlParser.Kb_typeContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_type_body.
    def enterKb_type_body(self, ctx:at_krlParser.Kb_type_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_type_body.
    def exitKb_type_body(self, ctx:at_krlParser.Kb_type_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#symbolic_type_body.
    def enterSymbolic_type_body(self, ctx:at_krlParser.Symbolic_type_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#symbolic_type_body.
    def exitSymbolic_type_body(self, ctx:at_krlParser.Symbolic_type_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#numeric_type_body.
    def enterNumeric_type_body(self, ctx:at_krlParser.Numeric_type_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#numeric_type_body.
    def exitNumeric_type_body(self, ctx:at_krlParser.Numeric_type_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#fuzzy_type_body.
    def enterFuzzy_type_body(self, ctx:at_krlParser.Fuzzy_type_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#fuzzy_type_body.
    def exitFuzzy_type_body(self, ctx:at_krlParser.Fuzzy_type_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#membersip_function.
    def enterMembersip_function(self, ctx:at_krlParser.Membersip_functionContext):
        pass

    # Exit a parse tree produced by at_krlParser#membersip_function.
    def exitMembersip_function(self, ctx:at_krlParser.Membersip_functionContext):
        pass


    # Enter a parse tree produced by at_krlParser#mf_def.
    def enterMf_def(self, ctx:at_krlParser.Mf_defContext):
        pass

    # Exit a parse tree produced by at_krlParser#mf_def.
    def exitMf_def(self, ctx:at_krlParser.Mf_defContext):
        pass


    # Enter a parse tree produced by at_krlParser#mf_point.
    def enterMf_point(self, ctx:at_krlParser.Mf_pointContext):
        pass

    # Exit a parse tree produced by at_krlParser#mf_point.
    def exitMf_point(self, ctx:at_krlParser.Mf_pointContext):
        pass


    # Enter a parse tree produced by at_krlParser#mf_body.
    def enterMf_body(self, ctx:at_krlParser.Mf_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#mf_body.
    def exitMf_body(self, ctx:at_krlParser.Mf_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_class.
    def enterKb_class(self, ctx:at_krlParser.Kb_classContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_class.
    def exitKb_class(self, ctx:at_krlParser.Kb_classContext):
        pass


    # Enter a parse tree produced by at_krlParser#kb_class_body.
    def enterKb_class_body(self, ctx:at_krlParser.Kb_class_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#kb_class_body.
    def exitKb_class_body(self, ctx:at_krlParser.Kb_class_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#event_body.
    def enterEvent_body(self, ctx:at_krlParser.Event_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#event_body.
    def exitEvent_body(self, ctx:at_krlParser.Event_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#interval_body.
    def enterInterval_body(self, ctx:at_krlParser.Interval_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#interval_body.
    def exitInterval_body(self, ctx:at_krlParser.Interval_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#object_body.
    def enterObject_body(self, ctx:at_krlParser.Object_bodyContext):
        pass

    # Exit a parse tree produced by at_krlParser#object_body.
    def exitObject_body(self, ctx:at_krlParser.Object_bodyContext):
        pass


    # Enter a parse tree produced by at_krlParser#attributes.
    def enterAttributes(self, ctx:at_krlParser.AttributesContext):
        pass

    # Exit a parse tree produced by at_krlParser#attributes.
    def exitAttributes(self, ctx:at_krlParser.AttributesContext):
        pass


    # Enter a parse tree produced by at_krlParser#attribute.
    def enterAttribute(self, ctx:at_krlParser.AttributeContext):
        pass

    # Exit a parse tree produced by at_krlParser#attribute.
    def exitAttribute(self, ctx:at_krlParser.AttributeContext):
        pass



del at_krlParser