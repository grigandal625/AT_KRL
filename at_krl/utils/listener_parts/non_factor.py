from at_krl.core.kb_value import NonFactor
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForNonFactorMixin:
    def exitBelief(self, ctx: at_krl_parser.BeliefContext):
        ctx.content = {"belief": float(ctx.children[2].getText()), "probability": float(ctx.children[4].getText())}

    def exitAccuracy(self, ctx: at_krl_parser.AccuracyContext):
        ctx.content = {"accuracy": float(ctx.children[1].getText())}

    def exitNon_factor(self, ctx: at_krl_parser.Non_factorContext):
        ctx.content = NonFactor(
            **{
                k: v
                for child in ctx.children
                if hasattr(child, "content") and isinstance(child.content, dict)
                for k, v in child.content.items()
            }
        )
