from at_krl.core.kb_class import KBClass
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_class import TypeOrClassReference
from at_krl.core.temporal.allen_event import KBEvent
from at_krl.core.temporal.allen_interval import KBInterval
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForKBClassMixin:
    def exitTemporal_attribute_condition(self, ctx: at_krl_parser.Temporal_attribute_conditionContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Simple_evaluatableContext).content

    def exitOpen(self, ctx: at_krl_parser.OpenContext):
        ctx.content = self.search_context_by_type(
            ctx.children, at_krl_parser.Temporal_attribute_conditionContext
        ).content

    def exitClose(self, ctx: at_krl_parser.CloseContext):
        ctx.content = self.search_context_by_type(
            ctx.children, at_krl_parser.Temporal_attribute_conditionContext
        ).content

    def exitOccurance_condition(self, ctx: at_krl_parser.Occurance_conditionContext):
        ctx.content = self.search_context_by_type(
            ctx.children, at_krl_parser.Temporal_attribute_conditionContext
        ).content

    def exitInterval_body(self, ctx: at_krl_parser.Interval_bodyContext):
        ctx.content = {
            "meta": "interval",
            "open": self.search_context_by_type(ctx.children, at_krl_parser.OpenContext).content,
            "close": self.search_context_by_type(ctx.children, at_krl_parser.CloseContext).content,
        }

    def exitEvent_body(self, ctx: at_krl_parser.Event_bodyContext):
        ctx.content = {
            "meta": "event",
            "occurance_condition": self.search_context_by_type(
                ctx.children, at_krl_parser.Occurance_conditionContext
            ).content,
        }

    def exitLong_attribute(self, ctx: at_krl_parser.Long_attributeContext):
        type_reference = TypeOrClassReference(id=ctx.children[2].getText())
        type_reference.target = self.KB.get_type_by_id(type_reference.krl)

        if not type_reference.target:
            raise ValueError(f"Type '{type_reference.krl}' not found in the knowledge base.")

        value_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_operationContext)
        value = value_child.content if value_child else None

        commentary_child = self.search_context_by_type(ctx.children, at_krl_parser.CommentaryContext)
        desc = commentary_child.content if commentary_child else None

        ctx.content = {
            "type": type_reference,
            "value": value,
            "desc": desc,
        }

    def exitShort_attribute(self, ctx: at_krl_parser.Short_attributeContext):
        type_id = self.search_terminal_by_token_name(ctx.children, "NAME").getText()
        type_reference = TypeOrClassReference(id=type_id)
        type_reference.target = self.KB.get_type_by_id(type_reference.krl)

        if not type_reference.target:
            raise ValueError(f"Type '{type_reference.krl}' not found in the knowledge base.")

        value_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_operationContext)
        value = value_child.content if value_child else None

        ctx.content = {
            "type": type_reference,
            "value": value,
        }

    def exitAttr_declaration(self, ctx: at_krl_parser.Attr_declarationContext):
        ctx.content = self.search_terminal_by_token_name(ctx.children, "NAME").getText()

    def exitAttribute(self, ctx: at_krl_parser.AttributeContext):
        name = ctx.children[0].content
        body = ctx.children[1].content

        attr = PropertyDefinition(id=name, **body)
        ctx.content = attr

    def exitAttributes(self, ctx: at_krl_parser.AttributesContext):
        ctx.content = [child.content for child in self.filter_by_types(ctx.children, at_krl_parser.AttributeContext)]

    def exitObject_body(self, ctx):
        group_child = self.search_terminal_by_token_name(ctx.children, "NAME")
        group = group_child.getText() if group_child else None

        properties = self.search_context_by_type(ctx.children, at_krl_parser.AttributesContext).content

        ctx.content = {
            "meta": "object",
            "group": group,
            "properties": properties,
        }

    def exitKb_class_body(self, ctx):
        object_body_child = self.search_context_by_type(ctx.children, at_krl_parser.Object_bodyContext)
        event_body_child = self.search_context_by_type(ctx.children, at_krl_parser.Event_bodyContext)
        interval_body_child = self.search_context_by_type(ctx.children, at_krl_parser.Interval_bodyContext)

        if object_body_child:
            ctx.content = object_body_child.content
        elif event_body_child:
            ctx.content = event_body_child.content
        elif interval_body_child:
            ctx.content = interval_body_child.content
        else:
            raise ValueError(f"Unsupported KB class body type {ctx.getText()}")

    def exitKb_class(self, ctx):
        name = ctx.children[1].getText()
        body = self.search_context_by_type(ctx.children, at_krl_parser.Kb_class_bodyContext).content
        commentary_child = self.search_context_by_type(ctx.children, at_krl_parser.CommentaryContext)
        desc = commentary_child.content if commentary_child else None

        meta = body.pop("meta")
        desc = body.pop("desc", None)

        classes = {
            "object": KBClass,
            "event": KBEvent,
            "interval": KBInterval,
        }
        cls = classes[meta]
        if meta == "object":
            class_id = self.KB.get_free_class_id(name)
            cls_definition = cls(id=class_id, **body, desc=f"Класс для {name}")
            cls_definition.owner = self.KB
            ctx.content = cls_definition

            prop_type = TypeOrClassReference(id=class_id)
            prop_type.target = cls_definition

            object_world_prop = PropertyDefinition(id=name, type=prop_type, desc=desc)
            object_world_prop.owner = self.KB.world
            self.KB.world.properties.append(object_world_prop)
            self.KB.classes.objects.append(ctx.content)
        elif meta == "event":
            class_id = name
            cls_definition = cls(id=class_id, **body, desc=desc)
            cls_definition.owner = self.KB
            self.KB.classes.events.append(cls_definition)
            ctx.content = cls_definition
        elif meta == "interval":
            class_id = name
            cls_definition = cls(id=class_id, **body, desc=desc)
            cls_definition.owner = self.KB
            self.KB.classes.intervals.append(cls_definition)
            ctx.content = cls_definition
