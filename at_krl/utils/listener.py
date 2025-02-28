from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.grammar.at_krl_parserListener import at_krl_parserListener
from at_krl.utils.listener_parts import evaluatable
from at_krl.utils.listener_parts import general
from at_krl.utils.listener_parts import kb_rule
from at_krl.utils.listener_parts import kb_type
from at_krl.utils.listener_parts import non_factor
from at_krl.utils.listener_parts import simple
from at_krl.utils.listener_parts import temporal
from at_krl.grammar.at_krl_parser import at_krl_parser
from at_krl.core.kb_class import PropertyDefinition, TypeOrClassReference
from antlr4.tree.Tree import TerminalNodeImpl


def get_number(v: str):
    if "." in v:
        v = float(v)
    else:
        v = int(v)
    return v


class ATKRLListener(
    non_factor.ListenerForNonFactorMixin,
    simple.ListenerForSimpleMixin,
    evaluatable.ListenerForEvaluatableMixin,
    temporal.ListenerForTemporalMixin,
    general.ListenerForGeneralMixin,
    kb_rule.ListenerForKBRuleMixin,
    kb_type.ListenerForKBTypeMixin,
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
    def filter_by_types(children, *ctx_types):
        return [child for child in children if any([isinstance(child, ctx_type) for ctx_type in ctx_types])]

    @staticmethod
    def search_terminal_by_token_name(children, token_name):
        for child in children:
            if isinstance(child, TerminalNodeImpl) and at_krl_parser.symbolicNames[child.symbol.type] == token_name:
                return child

    @staticmethod
    def filter_by_token_names(children, *token_names):
        return [
            child for child in children 
            if any(
                [isinstance(child, TerminalNodeImpl) and at_krl_parser.symbolicNames[child.symbol.type] == token_name 
                for token_name in token_names]
            )
        ]

    def exitTemporal_attribute_condition(self, ctx: at_krl_parser.Temporal_attribute_conditionContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Simple_evaluatableContext).content

    def exitOpen(self, ctx: at_krl_parser.OpenContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Temporal_attribute_conditionContext).content

    def exitClose(self, ctx: at_krl_parser.CloseContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Temporal_attribute_conditionContext).content

    def exitOccurance_condition(self, ctx: at_krl_parser.Occurance_conditionContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Temporal_attribute_conditionContext).content

    def exitInterval_body(self, ctx: at_krl_parser.Interval_bodyContext):
        ctx.content = {
            'open': self.search_context_by_type(ctx.children, at_krl_parser.OpenContext).content,
            'close': self.search_context_by_type(ctx.children, at_krl_parser.CloseContext).content,
        }

    def exitEvent_body(self, ctx: at_krl_parser.Event_bodyContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Occurance_conditionContext).content
    
    def exitLong_attribute(self, ctx: at_krl_parser.Long_attributeContext):
        type_reference = TypeOrClassReference(id=ctx.children[2].getText())
        
        value_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_operationContext)
        value = value_child.content if value_child else None

        commentary_child = self.search_context_by_type(ctx.children, at_krl_parser.CommentaryContext)
        desc = commentary_child.content if commentary_child else None

        ctx.content = {
            'type': type_reference,
            'value': value,
            'desc': desc,
        }

    def exitShort_attribute(self, ctx: at_krl_parser.Short_attributeContext):
        type_id = self.search_terminal_by_token_name(ctx.children, 'NAME').getText()
        type_reference = TypeOrClassReference(id=type_id)

        value_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_operationContext)
        value = value_child.content if value_child else None

        ctx.content = {
            'type': type_reference,
            'value': value,
        }

    def exitAttr_declaration(self, ctx: at_krl_parser.Attr_declarationContext):
        ctx.content = self.search_terminal_by_token_name(ctx.children, 'NAME').getText()

    def exitAttribute(self, ctx: at_krl_parser.AttributeContext):
        name = ctx.children[0].content
        body = ctx.children[1].content

        attr = PropertyDefinition(
            id=name,
            **body
        )
        ctx.content = attr

    def exitAttributes(self, ctx: at_krl_parser.AttributesContext):
        ctx.content = [child.content for child in self.filter_by_types(ctx.children, at_krl_parser.AttributeContext)]



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
