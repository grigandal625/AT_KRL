from at_krl.core.temporal.allen_attribute_expression import AllenAttributeExpression
from at_krl.core.temporal.allen_operation import AllenOperation
from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForTemporalMixin:
    def exitAllen_reference(self, ctx: at_krl_parser.Allen_referenceContext):
        ctx.content = AllenReference.from_simple(ctx.children[0].content)

    def exitAllen_indexed_reference(self, ctx: at_krl_parser.Allen_indexed_referenceContext):
        ctx.content = ctx.children[0].content
        if len(ctx.children) == 2:
            index = ctx.children[1].content
            ctx.content.index = index

    def exitIndex(self, ctx: at_krl_parser.IndexContext):
        ctx.content = ctx.children[1].content

    def exitAllen_attribute_expression(self, ctx: at_krl_parser.Allen_attribute_expressionContext):
        ctx.content = AllenAttributeExpression(id=ctx.children[2].getText(), ref=ctx.children[0].content)

    def exitAllen_operation(self, ctx: at_krl_parser.Allen_operationContext):
        operation = AllenOperation(
            sign=ctx.children[1].content, left=ctx.children[0].content, right=ctx.children[2].content
        )
        left_event = self.KB.get_event_by_id(operation.left.id)
        right_event = self.KB.get_event_by_id(operation.right.id)
        left_interval = self.KB.get_interval_by_id(operation.left.id)
        right_interval = self.KB.get_interval_by_id(operation.right.id)

        if left_event and left_interval:
            raise ValueError(f'Found event and interval with same names "{operation.left.id}"')
        elif right_event and right_interval:
            raise ValueError(f'Found event and interval with same names "{operation.left.id}"')

        left = left_event or left_interval
        right = right_event or right_interval

        operation.left.target = left
        operation.right.target = right

        operation.fullfill_legacy_tag()

        ctx.content = operation

    def exitAllen_evaluatable(self, ctx: at_krl_parser.Allen_evaluatableContext):
        ctx.content = ctx.children[0].content

    def exitAllen(self, ctx: at_krl_parser.AllenContext):
        ctx.content = ctx.children[0].getText()
