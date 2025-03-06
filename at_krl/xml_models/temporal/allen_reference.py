from at_krl.xml_models.temporal.allen_evaluatable import AllenEvaluatableXMLModel, AllenEvaluatableLegacyXMLModel
from pydantic_xml import attr, element
from typing import Literal, Optional, TYPE_CHECKING
from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.utils.context import Context
from at_krl.xml_models.kb_value import KBValueXMLModel
from at_krl.xml_models.kb_reference import KBReferenceXMLModel
if TYPE_CHECKING:
    from at_krl.xml_models.kb_operation import KBEvaluatableRootXMLModel

class AllenReferenceXMLModel(AllenEvaluatableXMLModel, tag="ref"):
    id: str = attr()
    meta: Literal["allen_reference"] = attr()
    index: Optional["KBEvaluatableRootXMLModel"] = element(tag="index", default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop('meta', None)
        return data

    def build_target(self, data, context: Context):
        result = AllenReference(**data)

        if context.kb:
            interval = context.kb.get_interval_by_id(result.id)
            event = context.kb.get_event_by_id(result.id)

            if interval and event:
                raise ValueError(f'Found both interval and event with id {result.id}')
            
            if not event and not interval:
                raise ValueError(f'No event or interval found with id {result.id}')

            result.target = interval or event
            result.validate_legacy_tag()

AllenReferenceXMLModel.model_rebuild()

class AllenReferenceLegacyXMLModel(AllenEvaluatableLegacyXMLModel):
    id: str = attr(name="Name")

    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        return result


class IntervalReferenceLegacyXMLModel(AllenEvaluatableLegacyXMLModel, tag="Interval"):

    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        if context.kb:
            result.target = context.kb.get_interval_by_id(result.id)
            if not result.target:
                raise ValueError(f'No interval found with id {result.id}')
            result.validate_legacy_tag()
        return result


class EventReferenceLegacyXMLModel(AllenEvaluatableLegacyXMLModel, tag="Event"):

    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        if context.kb:
            result.target = context.kb.get_event_by_id(result.id)
            if not result.target:
                raise ValueError(f'No event found with id {result.id}')
            result.validate_legacy_tag()
        return result


if __name__ == '__main__':
    xml_data = """
    <ref id="my_event" meta="allen_reference">
        <index>
            <value>5</value>
        </index>
    </ref>
    """
    model = AllenReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="my_event" meta="allen_reference" />
    """
    model = AllenReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <Interval Name="my_interval" />
    """
    model = IntervalReferenceLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <Event Name="my_event" />
    """
    model = EventReferenceLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))