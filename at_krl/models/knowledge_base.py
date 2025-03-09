from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.models.kb_class import KBClassModel
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_type import KBFuzzyTypeModel
from at_krl.models.kb_type import KBNumericTypeModel
from at_krl.models.kb_type import KBSymbolicTypeModel
from at_krl.models.temporal.allen_event import KBEventModel
from at_krl.models.temporal.allen_interval import KBIntervalModel
from at_krl.utils.context import Context


class KnowledgeBaseModel(KBEntityModel):
    tag: Literal["knowledge-base"]
    problem_info: Optional[str] = Field(default=None)
    types: List[Union[KBFuzzyTypeModel, KBSymbolicTypeModel, KBNumericTypeModel]]
    classes: List[Union[KBClassModel, KBIntervalModel, KBEventModel]]

    def to_internal(self, context: Context = None) -> KnowledgeBase:
        if context is None:
            context = Context(name="knowledge-base")
        context.kb = KnowledgeBase()
        return super().to_internal(context)

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.types:
            data["types"] = [type.to_internal(context.create_child("type")) for type in self.types]
        if self.classes:
            data["classes"] = [cls.to_internal(context.create_child("class")) for cls in self.classes]
        return data

    def build_target(self, data: dict, context: Context):
        context.kb.problem_info = data.get("problem_info", None)
        context.kb.rebuild_rules()
        return context.kb


KnowledgeBaseModel.model_rebuild()
