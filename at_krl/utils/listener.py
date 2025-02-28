from typing import Union

from at_krl.core.kb_operation import KBOperation
from at_krl.core.kb_operation import NonFactor
from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.grammar.at_krl_parser import at_krl_parser
from at_krl.grammar.at_krl_parserListener import at_krl_parserListener
from at_krl.utils.listener_parts import evaluatable
from at_krl.utils.listener_parts import non_factor
from at_krl.utils.listener_parts import simple


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


class ATKRLListener(
    non_factor.ListenerForNonFactorMixin,
    simple.ListenerForSimpleMixin,
    evaluatable.ListenerForEvaluatableMixin,
    at_krl_parserListener,
):
    KB = None

    def __init__(self, *args, **kwargs):
        at_krl_parserListener.__init__(self, *args, **kwargs)
        self.KB = KnowledgeBase()

    @staticmethod
    def search_context_by_type(children, ctx_type):
        for child in children:
            if isinstance(child, ctx_type):
                return child

    @staticmethod
    def filter_by_type(children, ctx_type):
        return [child for child in children if isinstance(child, ctx_type)]

    def exitKb_operation(self, ctx):
        if len(ctx.children) == 1:
            ctx.content = ctx.children[0].content
            return
        non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)

        operation_children = self.filter_by_type(ctx.children, at_krl_parser.Kb_operationContext)

        is_unary_operation = (
            (len(ctx.children) == 2) and not non_factor_child or (len(ctx.children) == 3) and non_factor_child
        ) and (len(operation_children) == 1)

        is_binary_operation = (
            (len(ctx.children) == 3) and not non_factor_child or (len(ctx.children) == 4) and non_factor_child
        ) and (len(operation_children) == 2)

        if is_unary_operation:
            left = operation_children[0].content
            sign = ctx.children[0].content
            ctx.content = KBOperation(
                sign=sign, left=left, non_factor=non_factor_child.content if non_factor_child else NonFactor()
            )
        elif is_binary_operation:
            left = operation_children[0].content
            sign = ctx.children[1].getText()
            right = operation_children[1].content
            ctx.content = KBOperation(
                sign=sign,
                left=left,
                right=right,
                non_factor=non_factor_child.content if non_factor_child else NonFactor(),
            )
        elif len(operation_children) == 1:
            ctx.content = operation_children[0].content
        else:
            raise ValueError(f"Bad operation {ctx.getText()}")

    def exitKb_evaluatable(self, ctx):
        return super().exitKb_evaluatable(ctx)

    # def exitKb_rule(self, ctx: at_krl_parser.Kb_ruleContext | Any):
    #     if ctx.children:
    #         id = ctx.children[1].getText()
    #         condition = ctx.children[2].content
    #         instructions = [child.content for child in ctx.children[3].children[1:]]
    #         else_instructions = None
    #         comment = None
    #         if len(ctx.children) > 4:
    #             if not isinstance(ctx.children[4], at_krl_parser.CommentaryContext):
    #                 else_instructions = [child.content for child in ctx.children[4].children[1:]]
    #             if isinstance(ctx.children[-1], at_krl_parser.CommentaryContext):
    #                 comment = ctx.children[-1].content
    #         rule = KBRule(id, condition, instructions, else_instructions=else_instructions, desc=comment)
    #         ctx.content = rule
    #         self.KB.add_rule(rule)

    # def exitAssign_instruction(self, ctx: at_krl_parser.Assign_instructionContext | Any):
    #     ref = (
    #         ctx.children[0].content
    #         if isinstance(ctx.children[0], at_krl_parser.Ref_pathContext)
    #         else ctx.children[1].content
    #     )
    #     value = (
    #         ctx.children[2].content
    #         if isinstance(ctx.children[2], at_krl_parser.EvaluatableContext)
    #         else ctx.children[0].content
    #     )
    #     ctx.content = AssignInstruction(ref, value)
    #     if len(ctx.children) == 4:
    #         ctx.content.non_factor = ctx.children[3].content

    # def exitKb_reference(self, ctx: at_krl_parser.Kb_referenceContext | Any):
    #     if len(ctx.children) == 1:
    #         s = ctx.children[0].content
    #         ctx.content = KBReference(s.id, s.ref)
    #     else:
    #         s = ctx.children[1].content
    #         n = None
    #         if isinstance(ctx.children[2], at_krl_parser.Non_factorContext):
    #             n = ctx.children[2].content
    #         ctx.content = KBReference(s.id, s.ref, non_factor=n)

    # def exitKb_operation(self, ctx: at_krl_parser.Kb_operationContext | Any):
    #     if len(ctx.children) == 1:
    #         ctx.content = ctx.children[0].content
    #     elif (ctx.children[0].getText() == "(") and (ctx.children[2].getText() == ")"):
    #         ctx.content = ctx.children[1].content
    #     elif len(ctx.children) == 2:
    #         if isinstance(ctx.children[1], at_krl_parser.Non_factorContext):
    #             ctx.content = ctx.children[0].content
    #             ctx.content.non_factor = ctx.children[1].content
    #         else:
    #             ctx.content = KBOperation(ctx.children[0].getText(), ctx.children[1].content)
    #     elif len(ctx.children) == 3:
    #         if isinstance(ctx.children[2], at_krl_parser.Non_factorContext):
    #             ctx.content = KBOperation(
    #                 ctx.children[0].getText(), ctx.children[1].content, non_factor=ctx.children[2].content
    #             )
    #         elif (ctx.children[0].getText() == "(") and (ctx.children[2].getText() == ")"):
    #             ctx.content = ctx.children[1].content
    #         else:
    #             ctx.content = KBOperation(ctx.children[1].getText(), ctx.children[0].content, ctx.children[2].content)
    #     elif len(ctx.children) == 4:
    #         ctx.content = KBOperation(
    #             ctx.children[1].getText(), ctx.children[0].content, ctx.children[2].content, ctx.children[3].content
    #         )
    #     else:
    #         raise

    # def exitEvaluatable(self, ctx: at_krl_parser.EvaluatableContext | Any):
    #     ctx.content = ctx.children[0].content

    # def exitInstructions(self, ctx: at_krl_parser.InstructionsContext | Any):
    #     ctx.content = ctx.children[0].content

    # def exitKb_rule_condition(self, ctx: at_krl_parser.Kb_rule_conditionContext | Any):
    #     ctx.content = ctx.children[1].content

    # def exitCommentary(self, ctx: at_krl_parser.CommentaryContext | Any):
    #     ctx.content = " ".join(child.getText() for child in ctx.children[1:])

    # def exitMf_point(self, ctx: at_krl_parser.Mf_pointContext | Any):
    #     x = ctx.children[0].getText()
    #     if "." in x:
    #         x = float(x)
    #     else:
    #         x = int(x)

    #     y = ctx.children[2].getText()
    #     if "." in y:
    #         y = float(y)
    #     else:
    #         y = int(y)
    #     ctx.content = MFPoint(x, y)

    # def exitKb_type(self, ctx: at_krl_parser.Kb_typeContext | Any):
    #     body_context = ctx.children[2]
    #     fuzzy_contexts = [c for c in body_context.children if isinstance(c, at_krl_parser.Fuzzy_type_bodyContext)]
    #     numeric_contexts = [c for c in body_context.children if isinstance(c, at_krl_parser.Numeric_type_bodyContext)]
    #     symbolic_contexts = [
    #       c for c in body_context.children if isinstance(c, at_krl_parser.Symbolic_type_bodyContext)]

    #     type_name = ctx.children[1].getText()
    #     desc = None
    #     if isinstance(ctx.children[-1], at_krl_parser.CommentaryContext):
    #         desc = ctx.children[-1].content
    #     if len(fuzzy_contexts):
    #         ctx.content = KBFuzzyType(type_name, fuzzy_contexts[0].content, desc=desc)
    #     elif len(numeric_contexts):
    #         ctx.content = KBNumericType(type_name, *numeric_contexts[0].content, desc=desc)
    #     elif len(symbolic_contexts):
    #         ctx.content = KBSymbolicType(type_name, symbolic_contexts[0].content, desc=desc)
    #     ctx.content.owner = self.KB
    #     self.KB.types.append(ctx.content)
    #     return super().exitKb_type(ctx)

    # def exitSymbolic_type_body(self, ctx: at_krl_parser.Symbolic_type_bodyContext | Any):
    #     ctx.content = [uni(child.getText()) for child in ctx.children[1:]]
    #     return super().exitSymbolic_type_body(ctx)

    # def exitNumeric_type_body(self, ctx: at_krl_parser.Numeric_type_bodyContext | Any):
    #     texts = [c.getText() for c in ctx.children]
    #     exit_minuses = [t for t in texts]
    #     for i, t in enumerate(texts):
    #         if t == "-":
    #             exit_minuses[i + 1] = "-" + exit_minuses[i + 1]
    #     exit_minuses = [e for e in exit_minuses if e != "-"]

    #     from_ = exit_minuses[2]
    #     to_ = exit_minuses[4]

    #     if "." in from_:
    #         from_ = float(from_)
    #     else:
    #         from_ = int(from_)

    #     if "." in to_:
    #         to_ = float(to_)
    #     else:
    #         to_ = int(to_)
    #     ctx.content = [from_, to_]
    #     return super().exitNumeric_type_body(ctx)

    # def exitFuzzy_type_body(self, ctx: at_krl_parser.Fuzzy_type_bodyContext | Any):
    #     ctx.content = [c.content for c in ctx.children if isinstance(c, at_krl_parser.Membersip_functionContext)]
    #     return super().exitFuzzy_type_body(ctx)

    # def exitMembersip_function(self, ctx: at_krl_parser.Membersip_functionContext | Any):
    #     mf_name = uni(ctx.children[0].children[0].getText())
    #     min = ctx.children[0].children[1].getText()
    #     max = ctx.children[0].children[2].getText()
    #     if "." in min:
    #         min = float(min)
    #     else:
    #         min = int(min)

    #     if "." in max:
    #         max = float(max)
    #     else:
    #         max = int(max)

    #     mf_points = [c.content for c in ctx.children[1].children if isinstance(c, at_krl_parser.Mf_pointContext)]

    #     ctx.content = MembershipFunction(mf_name, min, max, mf_points)
    #     return super().exitMembersip_function(ctx)

    # def exitKb_class(self, ctx: at_krl_parser.Kb_classContext | Any):
    #     object_id = ctx.children[1].getText()
    #     body_context = ctx.children[2].children[0]
    #     desc = None
    #     if isinstance(ctx.children[-1], at_krl_parser.CommentaryContext):
    #         desc = ctx.children[-1].content

    #     if isinstance(body_context, at_krl_parser.Object_bodyContext):
    #         class_id = self.KB.get_free_class_id(object_id)
    #         group = None
    #         if len(body_context.children) > 1:
    #             if isinstance(body_context.children[1], Tree.TerminalNodeImpl):
    #                 group = body_context.children[1].getText()
    #         attrs_context = [c for c in body_context.children if isinstance(c, at_krl_parser.AttributesContext)][0]

    #         attrs = attrs_context.content
    #         cls = KBClass(class_id, attrs, group=group, desc=desc)
    #         cls.owner = self.KB
    #         ctx.content = cls
    #         object_world_prop = KBProperty(object_id, class_id, desc=desc)
    #         object_world_prop.owner_class = self.KB.world
    #         object_world_prop._type_or_class = cls
    #         self.KB.world.properties.append(object_world_prop)
    #         self.KB.classes.objects.append(ctx.content)

    #     elif isinstance(body_context, at_krl_parser.Interval_bodyContext):
    #         class_id = object_id
    #         open, close = [
    #             c.content for c in body_context.children if isinstance(c, at_krl_parser.Simple_evaluatableContext)
    #         ]
    #         interval = KBInterval(class_id, open, close, desc=desc)
    #         interval.owner = self.KB
    #         ctx.content = interval
    #         self.KB.classes.intervals.append(ctx.content)
    #     elif isinstance(body_context, at_krl_parser.Event_bodyContext):
    #         class_id = object_id
    #         occurance_conditions = [
    #             c.content for c in body_context.children if isinstance(c, at_krl_parser.Simple_evaluatableContext)
    #         ]
    #         if len(occurance_conditions):
    #             occurance_condition = occurance_conditions[0]
    #             event = KBEvent(class_id, occurance_condition, desc=desc)
    #             event.owner = self.KB
    #             ctx.content = event
    #             self.KB.classes.events.append(ctx.content)
    #     return super().exitKb_class(ctx)

    # def exitAttribute(self, ctx: at_krl_parser.AttributeContext | Any):
    #     attr_id = ctx.children[1].getText()
    #     attr_type = ctx.children[3].getText()

    #     desc = None
    #     if isinstance(ctx.children[-1], at_krl_parser.CommentaryContext):
    #         desc = ctx.children[-1].content

    #     value = None
    #     value_contexts = [c for c in ctx.children if isinstance(c, at_krl_parser.EvaluatableContext)]
    #     if len(value_contexts):
    #         value = value_contexts[0].content

    #     ctx.content = KBProperty(attr_id, attr_type, desc=desc, value=value)
    #     return super().exitAttribute(ctx)

    # def exitAttributes(self, ctx: at_krl_parser.AttributesContext | Any):
    #     ctx.content = [c.content for c in ctx.children if isinstance(c, at_krl_parser.AttributeContext)]
    #     return super().exitAttributes(ctx)

    # def exitSimple_value(self, ctx: at_krl_parser.Simple_valueContext | Any):
    #     ctx.content = SimpleValue(uni(ctx.getText()))
    #     return super().exitSimple_value(ctx)

    # def exitSimple_ref(self, ctx: at_krl_parser.Simple_refContext | Any):
    #     ctx.content = SimpleReference(id=ctx.children[0].content.id, ref=ctx.children[0].content.ref)
    #     return super().exitSimple_ref(ctx)

    # def exitSimple_operation(self, ctx: at_krl_parser.Simple_operationContext | Any):
    #     if len(ctx.children) == 1:
    #         ctx.content = ctx.children[0].content
    #     elif len(ctx.children) == 2:
    #         left_context = ctx.children[1]
    #         sign = ctx.children[1].getText()

    #         if isinstance(left_context, at_krl_parser.Ref_pathContext):
    #             left = SimpleReference(id=left_context.content.id, ref=left_context.content.ref)
    #         else:
    #             left = left_context.content

    #         ctx.content = SimpleOperation.from_dict(
    #             {
    #                 "sign": sign,
    #                 "left": left.__dict__(),
    #             }
    #         )

    #     elif isinstance(
    #         ctx.children[0], Tree.TerminalNodeImpl) and isinstance(ctx.children[2], Tree.TerminalNodeImpl):
    #         ctx.content = ctx.children[1].content
    #     else:
    #         left_context = ctx.children[0]
    #         sign = ctx.children[1].getText()
    #         right_context = ctx.children[2]

    #         if isinstance(left_context, at_krl_parser.Ref_pathContext):
    #             left = SimpleReference(id=left_context.content.id, ref=left_context.content.ref)
    #         else:
    #             left = left_context.content

    #         if isinstance(right_context, at_krl_parser.Ref_pathContext):
    #             right = SimpleReference(id=right_context.content.id, ref=right_context.content.ref)
    #         else:
    #             right = right_context.content

    #         ctx.content = SimpleOperation.from_dict(
    #             {"sign": sign, "left": left.__dict__(), "right": right.__dict__()})
    #     return super().exitSimple_operation(ctx)

    # def exitSimple_evaluatable(self, ctx: at_krl_parser.Simple_evaluatableContext | Any):
    #     ctx.content = ctx.children[0].content
    #     return super().exitSimple_evaluatable(ctx)

    # def exitallen_operation(self, ctx: at_krl_parser.allen_operationContext | Any):
    #     sign = ctx.children[1].getText()
    #     left_id = ctx.children[0].getText()
    #     right_id = ctx.children[2].getText()

    #     left = self._search_interval_or_event(left_id)
    #     right = self._search_interval_or_event(right_id)

    #     ctx.content = AllenOperation(sign, left, right)
    #     return super().exitallen_operation(ctx)

    # def _search_interval_or_event(self, class_id):
    #     res = self.KB.get_interval_by_id(class_id)
    #     if res is None:
    #         res = self.KB.get_event_by_id(class_id)
    #         if res is None:
    #             res = class_id
    #     return res
