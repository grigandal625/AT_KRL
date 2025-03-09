from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.kb_class import KBClass
from at_krl.core.kb_class import KBInstance
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_class import TypeOrClassReference
from at_krl.core.kb_value import Evaluatable
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.models.kb_operation import KBOperationModel
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_rule import KBRuleModel
from at_krl.models.kb_value import KBValueModel
from at_krl.models.simple.simple_class import SimpleClassModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.utils.context import Context


# if TYPE_CHECKING:
#     from at_krl.models.kb_class import KBClassModel


class TypeOrClassReferenceModel(SimpleReferenceModel):
    meta: Literal["type_or_class"]
    ref: None = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        data.pop("meta", None)
        data.pop("ref", None)
        return data

    def build_target(self, data, context: Context):
        result = TypeOrClassReference(**data)
        if context.kb:
            cls = context.kb.get_class_by_id(result.id)
            type = context.kb.get_type_by_id(result.id)
            if not type and not cls:
                raise ValueError(f"No type or class found with id {result.id}")
            if cls and type:
                raise ValueError(f"Found both class and type with id {result.id}")
            result.target = cls or type
        return result


class PropertyDefinitionModel(KBEntityModel):  # LegacyMixin для совместимости со старым АТ-РЕШАТЕЛЕМ
    tag: Literal["property"] = Field(default="property")
    id: str
    type: str | TypeOrClassReferenceModel
    desc: Optional[str] = Field(default=None)
    value: Optional[Union[KBValueModel, KBReferenceModel, KBOperationModel]] = Field(default=None)
    source: Optional[str] = Field(default="asked")
    question: Optional[str] = Field(default=None)
    query: Optional[str] = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        if isinstance(self.type, str):
            data["type"] = TypeOrClassReferenceModel(tag="ref", id=self.type, meta="type_or_class").to_internal(context)
        else:
            data["type"] = self.type.to_internal(context)
        if self.value:
            data["value"] = self.value.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return PropertyDefinition(**data)


class PropertyDefinitionListModel(KBRootModel[List[PropertyDefinitionModel]]):
    def to_internal(self, context: Context):
        return [p.to_internal(context) for p in self.root]


class KBRuleListModel(KBRootModel[List[KBRuleModel]]):
    def to_internal(self, context: Context):
        return [p.to_internal(context) for p in self.root]


class KBClassModel(SimpleClassModel):
    properties: PropertyDefinitionListModel = Field(default_factory=list)
    rules: Optional[KBRuleListModel] = Field(default_factory=list)
    group: Optional[str] = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        data["properties"] = self.properties.to_internal(context)
        if self.rules:
            data["rules"] = self.rules.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.objects.append(result)
        return result


class KBInstanceModel(KBEntityModel):
    tag: Literal["instance"]
    id: str
    type: TypeOrClassReferenceModel
    desc: Optional[str] = Field(default=None)
    value: Optional[Evaluatable] = Field(default=None)
    create: bool = Field(default=True)
    properties: Optional["KBPropertyListModel"] = Field(default_factory=list)

    def get_data(self, context):
        data = super().get_data(context)
        data["type"] = self.type.to_internal(context)
        if self.value:
            data["value"] = self.value.to_internal(context)
        if self.properties:
            data["properties"] = self.properties.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return KBInstance(**data)


class KBPropertyModel(KBInstanceModel):
    tag: Literal["property"]


class KBPropertyListModel(KBRootModel[List[KBPropertyModel]]):
    def to_internal(self, context):
        return [p.to_internal(context) for p in self.root]
