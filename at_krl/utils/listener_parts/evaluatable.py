from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_value import KBValue
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForEvaluatableMixin:
    def exitKb_value(self, ctx: at_krl_parser.Kb_valueContext):
        simple_value_child = self.search_context_by_type(ctx.children, at_krl_parser.Simple_valueContext)
        non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)
        kb_value = KBValue.from_simple(simple_value_child.content)

        if non_factor_child:
            kb_value.non_factor = non_factor_child.content

        ctx.content = kb_value

    def exitKb_reference(self, ctx):
        ref_path_child = self.search_context_by_type(ctx.children, at_krl_parser.Ref_pathContext)
        non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)

        kb_reference = KBReference.from_simple(ref_path_child.content)

        if non_factor_child:
            kb_reference.non_factor = non_factor_child.content

        ctx.content = kb_reference
