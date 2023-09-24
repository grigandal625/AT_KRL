from at_krl.grammar.at_krlListener import at_krlListener
from at_krl.core.kb_value import KBValue, NonFactor
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_operation import KBOperation
from at_krl.core.kb_instruction import AssignInstruction
from at_krl.core.kb_rule import KBRule
from at_krl.grammar.at_krlParser import at_krlParser
from typing import Any, Union


def uni(s: str) -> Union[str, int, float]:
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            res = str(s)
            if res.startswith('"') and res.endswith('"'):
                res = res[1:-1]
            return res


class ATKRLListener(at_krlListener):
    res = None

    def exitBelief(self, ctx: at_krlParser.BeliefContext | Any):
        ctx.content = {'belief': float(ctx.children[2].getText(
        )), 'probability': float(ctx.children[4].getText())}

    def exitAccuracy(self, ctx: at_krlParser.AccuracyContext | Any):
        ctx.content = {'accuracy': float(ctx.children[1].getText())}

    def exitNon_factor(self, ctx: at_krlParser.Non_factorContext | Any):
        ctx.content = NonFactor(**{
            k: v
            for child in ctx.children if hasattr(child, 'content') and isinstance(child.content, dict)
            for k, v in child.content.items()
        })

    def exitKb_value(self, ctx: at_krlParser.Kb_valueContext | Any):
        if len(ctx.children) == 1:
            ctx.content = KBValue(uni(ctx.getText()))
        else:
            ctx.content = ctx.children[1].content
            ctx.content.non_factor = ctx.children[2].content

    def exitRef_path(self, ctx: at_krlParser.Ref_pathContext | Any):
        if len(ctx.children) == 1:
            ctx.content = KBReference(ctx.getText())
        else:
            ctx.content = KBReference(
                ctx.children[0].getText(), ctx.children[2].content)

    def exitKb_rule(self, ctx: at_krlParser.Kb_ruleContext | Any):
        id = ctx.children[1].getText()
        condition = ctx.children[2].content
        instructions = [
            child.content for child in ctx.children[3].children[1:]]
        else_instructions = None
        if not isinstance(ctx.children[4], at_krlParser.Kb_rule_commentContext):
            else_instructions = [
                child.content for child in ctx.children[4].children[1:]]
        comment = ctx.children[-1].content
        rule = KBRule(id, condition, instructions,
                             else_instructions=else_instructions, desc=comment)
        ctx.content = rule

    def exitAssign_instruction(self, ctx: at_krlParser.Assign_instructionContext | Any):
        ref = ctx.children[0].content if isinstance(
            ctx.children[0], at_krlParser.Ref_pathContext) else ctx.children[1].content
        value = ctx.children[2].content if isinstance(
            ctx.children[2], at_krlParser.EvaluatableContext) else ctx.children[0].content
        ctx.content = AssignInstruction(ref, value)
        if len(ctx.children) == 4:
            ctx.content.non_factor = ctx.children[3].content

    def exitKb_reference(self, ctx: at_krlParser.Kb_referenceContext | Any):
        if len(ctx.children) == 1:
            ctx.content = ctx.children[0].content
        elif isinstance(ctx.children[2], at_krlParser.Non_factorContext):
            ctx.content = ctx.children[1].content
            ctx.content.non_factor = ctx.children[2].content

    def exitKb_operation(self, ctx: at_krlParser.Kb_operationContext | Any):
        if len(ctx.children) == 1:
            ctx.content = ctx.children[0].content
        elif len(ctx.children) == 2:
            if isinstance(ctx.children[1], at_krlParser.Non_factorContext):
                ctx.content = ctx.children[0].content
                ctx.content.non_factor = ctx.children[1].content
            else:
                ctx.content = KBOperation(
                    ctx.children[0].getText(), ctx.children[1].content)
        elif len(ctx.children) == 3:
            if isinstance(ctx.children[2], at_krlParser.Non_factorContext):
                ctx.content = KBOperation(ctx.children[0].getText(
                ), ctx.children[1].content, non_factor=ctx.children[2].content)
            elif (ctx.children[0].getText() == '(') and (ctx.children[2].getText() == ')'):
                ctx.content = ctx.children[1].content
            else:
                ctx.content = KBOperation(ctx.children[1].getText(
                ), ctx.children[0].content, ctx.children[2].content)
        elif len(ctx.children) == 4:
            ctx.content = KBOperation(ctx.children[1].getText(
            ), ctx.children[0].content, ctx.children[2].content, ctx.children[3].content)
        else:
            raise

    def exitEvaluatable(self, ctx: at_krlParser.EvaluatableContext | Any):
        ctx.content = ctx.children[0].content

    def exitInstructions(self, ctx: at_krlParser.InstructionsContext | Any):
        ctx.content = ctx.children[0].content

    def exitKb_rule_condition(self, ctx: at_krlParser.Kb_rule_conditionContext | Any):
        ctx.content = ctx.children[1].content

    def exitKb_rule_comment(self, ctx: at_krlParser.Kb_rule_commentContext | Any):
        ctx.content = ' '.join(child.getText() for child in ctx.children[1:])
