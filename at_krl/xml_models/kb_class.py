from typing import List
from typing import Optional
from typing import Union

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.kb_class import KBClass
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_class import TypeOrClassReference
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.kb_operation import AllenAttributeExpressionXMLModel
from at_krl.xml_models.kb_operation import AnyAllenOperation
from at_krl.xml_models.kb_operation import AnyKBOperation
from at_krl.xml_models.kb_operation import AnyKBOperationLegacy
from at_krl.xml_models.kb_operation import EvIntRelLegacyXMLModel
from at_krl.xml_models.kb_operation import EvRelLegacyXMLModel
from at_krl.xml_models.kb_operation import IntRelLegacyXMLModel
from at_krl.xml_models.kb_operation import KBEvaluatableLegacyRootXMLModel
from at_krl.xml_models.kb_operation import KBEvaluatableRootXMLModel
from at_krl.xml_models.kb_reference import KBReferenceLegacyXMLModel
from at_krl.xml_models.kb_reference import KBReferenceXMLModel
from at_krl.xml_models.kb_rule import KBRuleLegacyXMLModel
from at_krl.xml_models.kb_rule import KBRuleXMLModel
from at_krl.xml_models.kb_value import KBValueLegacyXMLModel
from at_krl.xml_models.kb_value import KBValueXMLModel
from at_krl.xml_models.simple.simple_class import SimpleClassXMLModel

KBEvaluatableRoot = Union[
    AllenAttributeExpressionXMLModel,
    KBReferenceXMLModel,
    KBValueXMLModel,
    AnyKBOperation,
    AnyAllenOperation,
]

KBEvaluatableLegacyRoot = Union[
    KBReferenceLegacyXMLModel,
    KBValueLegacyXMLModel,
    AnyKBOperationLegacy,
    EvIntRelLegacyXMLModel,
    IntRelLegacyXMLModel,
    EvRelLegacyXMLModel,
]


class PropertyDefValueXMLModel(KBEvaluatableRootXMLModel, tag="value"):
    pass


class PropertyDefinitionXMLModel(KBEntityXMLModel, tag="property"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    type: str = attr()
    source: Optional[str] = attr(default="asked")
    value: Optional[PropertyDefValueXMLModel] = element(default=None)
    question: Optional[str] = element(tag="question", default=None)
    query: Optional[str] = element(tag="query", default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["type"] = TypeOrClassReference(id=self.type)
        if context.kb:
            cls = context.kb.get_class_by_id(data["type"].id)
            type = context.kb.get_type_by_id(data["type"].id)
            if not type and not cls:
                raise ValueError(f"No type or class found with id {self.type}")
            if cls and type:
                raise ValueError(f"Found both class and type with id {self.type}")
            data["type"].target = cls or type
        if self.value:
            data["value"] = self.value.to_internal(context.create_child("value"))
        return data

    def build_target(self, data, context: Context):
        return PropertyDefinition(**data)


class KBClassXMLModel(SimpleClassXMLModel, tag="class"):
    group: Optional[str] = attr(default=None)
    properties: List[PropertyDefinitionXMLModel] = wrapped("properties", element())
    rules: Optional[List[KBRuleXMLModel]] = wrapped("rules", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.properties:
            data["properties"] = [prop.to_internal(context.create_child("property")) for prop in self.properties]
        if self.rules:
            data["rules"] = [rule.to_internal(context.create_child("rule")) for rule in self.rules]
        return data

    def build_target(self, data, context: Context):
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.objects.append(result)
            result.owner = context.kb.classes
        return result


class PropertyDefValueLegacyXMLModel(KBEvaluatableLegacyRootXMLModel, tag="value"):
    pass


class PropertyDefinitionLegacyXMLModel(KBEntityXMLModel, tag="property", extra="ignore"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    type: str = attr()
    source: Optional[str] = attr(default="asked")
    value: Optional[
        Union[KBEvaluatableLegacyRoot, KBEvaluatableRoot, PropertyDefValueXMLModel, PropertyDefValueLegacyXMLModel]
    ] = element(default=None)
    question: Optional[str] = element(tag="question", default=None)
    query: Optional[str] = element(tag="query", default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["type"] = TypeOrClassReference(id=self.type)
        if context.kb:
            cls = context.kb.get_class_by_id(data["type"].id)
            type = context.kb.get_type_by_id(data["type"].id)
            if not type and not cls:
                raise ValueError(f"No type or class found with id {self.type}")
            if cls and type:
                raise ValueError(f"Found both class and type with id {self.type}")
            data["type"].target = cls or type
        if self.value:
            data["value"] = self.value.to_internal(context.create_child("value"))
        return data

    def build_target(self, data, context: Context):
        return PropertyDefinition(**data)


class KBClassLegacyXMLModel(KBEntityXMLModel, tag="class"):
    id: str = attr()
    group: Optional[str] = attr(default=None)
    desc: Optional[str] = attr(default=None)
    properties: List[Union[PropertyDefinitionLegacyXMLModel, PropertyDefinitionXMLModel]] = wrapped(
        "properties", element()
    )
    rules: Optional[List[KBRuleLegacyXMLModel]] = wrapped("rules", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.properties:
            data["properties"] = [prop.to_internal(context.create_child("property")) for prop in self.properties]
        if self.rules:
            data["rules"] = [rule.to_internal(context.create_child("rule")) for rule in self.rules]
        return data

    def build_target(self, data, context: Context):
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.objects.append(result)
            result.owner = context.kb.classes
        return result
