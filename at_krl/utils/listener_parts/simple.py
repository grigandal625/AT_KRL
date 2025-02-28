import json

from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.simple.simple_value import SimpleValue
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForSimpleMixin:
    def exitSimple_value(self, ctx: at_krl_parser.Simple_valueContext):
        ctx.content = SimpleValue(content=json.loads(ctx.getText()))

    def exitRef_path(self, ctx: at_krl_parser.Ref_pathContext):
        if len(ctx.children) == 1:
            ctx.content = SimpleReference(id=ctx.getText())
        else:
            ref_path_child = self.search_context_by_type(ctx.children, at_krl_parser.Ref_pathContext)
            ctx.content = SimpleReference(id=ctx.children[0].getText(), ref=ref_path_child.content)

    def exitSimple_ref(self, ctx: at_krl_parser.Simple_refContext):
        ctx.content = ctx.children[0].content

    def exitSimple_operation(self, ctx: at_krl_parser.Simple_operationContext):
        if len(ctx.children) == 1:
            ctx.content = ctx.children[0].content
        elif len(ctx.children) == 2:
            ctx.content = SimpleOperation(sign=ctx.children[0].getText(), left=ctx.children[1].content)
        elif len(ctx.children) == 3:
            filtered = self.filter_by_types(ctx.children, at_krl_parser.Simple_operationContext)
            if len(filtered) == 2:
                ctx.content = SimpleOperation(
                    sign=ctx.children[1].getText(), left=ctx.children[0].content, right=ctx.children[2].content
                )
            elif len(filtered) == 1:
                ctx.content = filtered[0].content
            else:
                raise ValueError(f"Invalid simple operation {ctx.getText()}")
        elif len(ctx.children) > 3:
            filtered = self.filter_by_types(ctx.children, at_krl_parser.Simple_operationContext)
            if len(filtered) == 1:
                ctx.content = filtered[0].content
            else:
                raise ValueError(f"Invalid simple operation {ctx.getText()}")

    def exitSimple_evaluatable(self, ctx: at_krl_parser.Simple_evaluatableContext):
        ctx.content = ctx.children[0].content
