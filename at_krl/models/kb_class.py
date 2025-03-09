from typing import List
from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.kb_class import KBClass
from at_krl.core.kb_class import KBInstance
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_value import Evaluatable
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
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


class KBRuleListModel(KBRootModel[List[KBRuleModel]]):
    def build_target(self, data, context: Context):
        return [p.to_internal() for p in self.points]


class KBClassModel(SimpleClassModel):
    properties: Optional["PropertyDefinitionListModel"] = Field(default_factory=list)
    rules: Optional[KBRuleListModel] = Field(default_factory=list)

    def build_target(self, data, context: Context):
        data["properties"] = self.properties.to_internal
        data["rules"] = self.rules.to_internal()
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.append(result)
        return result


class TypeOrClassReferenceModel(SimpleReferenceModel):
    pass


class PropertyDefinitionModel(KBEntityModel):  # LegacyMixin для совместимости со старым АТ-РЕШАТЕЛЕМ
    tag: Literal["property"] = Field(default="property")
    id: str
    type: TypeOrClassReferenceModel
    desc: Optional[str] = Field(default=None)
    value: Optional[SimpleEvaluatable] = Field(default=None)
    value: KBValueModel | KBReferenceModel | KBOperationModel
    source: Optional[str] = Field(default="asked")
    question: Optional[str] = Field(default=None)
    query: Optional[str] = Field(default=None)

    def build_target(self, data, context: Context):
        return PropertyDefinition(**data)


class PropertyDefinitionListModel(KBRootModel[List[PropertyDefinitionModel]]):
    def build_target(self, data, context: Context):
        return [p.to_internal() for p in self.root]


class KBInstanceModel(KBEntityModel):
    tag: Literal["instance"] = Field(default="instance")
    id: str
    type: TypeOrClassReferenceModel
    desc: Optional[str] = Field(default=None)
    value: Optional[Evaluatable] = Field(default=None)
    create: bool = Field(default=True)
    properties: Optional["KBPropertyListModel"] = Field(default_factory=list)

    def build_target(self, data, context: Context):
        # if self.properties:
        data["properties"] = self.properties.to_internal()

        return KBInstance(**data)


class KBPropertyModel(KBInstanceModel):
    tag: Literal["property"] = Field(default="property")  # ?


class KBPropertyListModel(KBRootModel[List[KBPropertyModel]]):
    def build_target(self, data, context: Context):
        return [p.to_internal() for p in self.root]
