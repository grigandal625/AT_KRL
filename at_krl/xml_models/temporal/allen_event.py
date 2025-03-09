from typing import Literal

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.temporal.allen_event import KBEvent
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableLegacyRootXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableRootXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassLegacyXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassXMLModel


class OccuranceConditionXMLModel(KBEntityXMLModel, tag="property"):
    id: Literal["УслВозн"] = attr()
    type: Literal["ЛогВыр"] = attr()
    value: SimpleEvaluatableRootXMLModel = element(tag="value")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("id", None)
        data.pop("type", None)
        data["value"] = self.value.to_internal(context.create_child("value"))
        return data

    def build_target(self, data, context: Context):
        return data["value"]


class KBEventXMLModel(AllenClassXMLModel, tag="event"):
    occurance_condition: OccuranceConditionXMLModel = wrapped("properties")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["occurance_condition"] = self.occurance_condition.to_internal(context.create_child("occurance_condition"))
        return data

    def build_target(self, data, context: Context):
        result = KBEvent(**data)
        if context.kb:
            context.kb.classes.events.append(result)
            result.owner = context.kb.classes
        return result


class KBEventLegacyXMLModel(AllenClassLegacyXMLModel, tag="Event"):
    id: str = attr(name="Name")
    occurance_condition: SimpleEvaluatableLegacyRootXMLModel = element(tag="Formula")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["occurance_condition"] = self.occurance_condition.to_internal(context.create_child("occurance_condition"))
        return data

    def build_target(self, data, context: Context):
        result = KBEvent(**data)
        if context.kb:
            context.kb.classes.events.append(result)
            result.owner = context.kb.classes
        return result
