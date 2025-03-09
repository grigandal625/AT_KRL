from typing import List
from typing import Optional
from typing import Union

from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.utils.context import Context
from at_krl.xml_models.kb_class import KBClassLegacyXMLModel
from at_krl.xml_models.kb_class import KBClassXMLModel
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.kb_type import KBFuzzyTypeXMLModel
from at_krl.xml_models.kb_type import KBNumericTypeXMLModel
from at_krl.xml_models.kb_type import KBSymbolicTypeXMLModel
from at_krl.xml_models.temporal.allen_event import KBEventLegacyXMLModel
from at_krl.xml_models.temporal.allen_event import KBEventXMLModel
from at_krl.xml_models.temporal.allen_interval import KBIntervalLegacyXMLModel
from at_krl.xml_models.temporal.allen_interval import KBIntervalXMLModel


class KnowledgeBaseXMLModel(KBEntityXMLModel, tag="knowledge-base"):
    problem_info: Optional[str] = element(tag="problem-info", default=None)
    types: List[
        Union[
            KBFuzzyTypeXMLModel,
            KBSymbolicTypeXMLModel,
            KBNumericTypeXMLModel,
        ]
    ] = wrapped("types", element())
    classes: List[Union[KBClassXMLModel, KBEventXMLModel, KBIntervalXMLModel]] = wrapped("classes", element())

    def to_internal(self, context: Context = None):
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


class KnowledgeBaseLegacyXMLModel(KBEntityXMLModel, tag="knowledge-base"):
    problem_info: Optional[str] = element(tag="problem-info", default=None)
    types: List[
        Union[
            KBFuzzyTypeXMLModel,
            KBSymbolicTypeXMLModel,
            KBNumericTypeXMLModel,
        ]
    ] = wrapped("types", element())
    intervals: Optional[List[KBIntervalLegacyXMLModel]] = wrapped("IntervalsAndEvents/Intervals", element(default=None))
    events: Optional[List[KBEventLegacyXMLModel]] = wrapped("IntervalsAndEvents/Events", element(default=None))
    classes: List[KBClassLegacyXMLModel] = wrapped("classes", element())

    def to_internal(self, context: Context = None):
        if context is None:
            context = Context(name="knowledge-base")
        context.kb = KnowledgeBase()
        return super().to_internal(context)

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.types:
            data["types"] = [type.to_internal(context.create_child("type")) for type in self.types]
        if self.intervals:
            data["classes"] += [interval.to_internal(context.create_child("interval")) for interval in self.intervals]
        if self.events:
            data["classes"] += [event.to_internal(context.create_child("event")) for event in self.events]
        if self.classes:
            data["classes"] += [cls.to_internal(context.create_child("class")) for cls in self.classes]
        data.pop("intervals", None)
        data.pop("events", None)
        return data

    def build_target(self, data: dict, context: Context):
        context.kb.problem_info = data.get("problem_info", None)
        context.kb.rebuild_rules()
        return context.kb
