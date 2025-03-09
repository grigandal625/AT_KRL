from typing import Optional

from pydantic_xml import attr
from pydantic_xml import element

from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.utils.context import Context
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel


class SimpleReferenceXMLModel(SimpleEvaluatableXMLModel, tag="ref"):
    id: str = attr()
    ref: Optional["SimpleReferenceXMLModel"] = element(default=None)

    def get_data(self, context: Context):
        result = super().get_data(context)
        if self.ref:
            result["ref"] = self.ref.to_internal(context.create_child("ref"))
        return result

    def build_target(self, data, context: Context):
        result = SimpleReference(**data)
        return result


class SimpleReferenceLegacyXMLModel(SimpleEvaluatableLegacyXMLModel, tag="Attribute"):
    value: str = attr(name="Value")

    def build_target(self, data, context: Context):
        result = SimpleReference.parse(data.get("value"))
        return result
