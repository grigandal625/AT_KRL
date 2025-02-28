from typing import Type
from typing import Union

from at_krl.core.kb_operation import KBOperation
from at_krl.core.kb_operation import NonFactor
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
        simple_ref_child = self.search_context_by_type(ctx.children, at_krl_parser.Simple_refContext)
        non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)

        kb_reference = KBReference.from_simple(simple_ref_child.content)

        if non_factor_child:
            kb_reference.non_factor = non_factor_child.content

        ctx.content = kb_reference

    @staticmethod
    def get_operation_or_evaluatable_exiters(
        target_ctx_type: Union[Type[at_krl_parser.Kb_operationContext], Type[at_krl_parser.Kb_evaluatableContext]]
    ):
        def exiter(self, ctx):
            if len(ctx.children) == 1:  # покрывает и случай с AllenOperation
                ctx.content = ctx.children[0].content
                return
            non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)

            operation_children = self.filter_by_types(ctx.children, target_ctx_type)

            is_unary_operation = (
                (len(ctx.children) == 2) and not non_factor_child or (len(ctx.children) == 3) and non_factor_child
            ) and (len(operation_children) == 1)

            is_binary_operation = (
                (len(ctx.children) == 3) and not non_factor_child or (len(ctx.children) == 4) and non_factor_child
            ) and (len(operation_children) == 2)

            if is_unary_operation:
                left = operation_children[0].content
                sign = ctx.children[0].getText()
                ctx.content = KBOperation(
                    sign=sign, left=left, non_factor=non_factor_child.content if non_factor_child else NonFactor()
                )
            elif is_binary_operation:
                left = operation_children[0].content
                sign = ctx.children[1].content
                right = operation_children[1].content
                ctx.content = KBOperation(
                    sign=sign,
                    left=left,
                    right=right,
                    non_factor=non_factor_child.content if non_factor_child else NonFactor(),
                )
            elif len(operation_children) == 1:
                ctx.content = operation_children[0].content
                if non_factor_child:
                    ctx.content.non_factor = non_factor_child.content
            else:
                raise ValueError(f"Bad operation {ctx.getText()}")
            return ctx

        return exiter

    def exitKb_operation(self, ctx: at_krl_parser.Kb_operationContext):
        return self.get_operation_or_evaluatable_exiters(at_krl_parser.Kb_operationContext)(self, ctx)

    def exitKb_evaluatable(self, ctx: at_krl_parser.Kb_evaluatableContext):
        return self.get_operation_or_evaluatable_exiters(at_krl_parser.Kb_evaluatableContext)(self, ctx)

    def exitEvaluatable(self, ctx: at_krl_parser.EvaluatableContext):
        ctx.content = ctx.children[0].content
