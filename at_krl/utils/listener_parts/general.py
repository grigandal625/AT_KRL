from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForGeneralMixin:
    def exitCommentary(self, ctx: at_krl_parser.CommentaryContext):
        ctx.content = ctx.children[1].getText()[1:]
