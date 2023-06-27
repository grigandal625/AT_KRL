from at_krl.grammar.at_krlListener import at_krlListener
from at_krl.core.kb_value import KBValue, NonFactor
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_operation import KBOperation
from at_krl.grammar.at_krlParser import at_krlParser
from typing import Any, Union
from antlr4.tree.Tree import TerminalNode


def uni(s: str) -> Union[str, int, float]:
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return str(s)


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

    def exitKb_reference(self, ctx: at_krlParser.Kb_referenceContext | Any):
        if len(ctx.children) == 1:
            ctx.content = KBReference(ctx.getText())
        elif len(ctx.children) == 3:
            ctx.content = KBReference(
                ctx.children[0].getText(), ctx.children[2].content)
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
                    ctx.children[1].getText(), ctx.children[0].content)
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

    def exitEvaluatable(self, ctx: at_krlParser.EvaluatableContext | Any):
        ctx.content = ctx.children[0].content
