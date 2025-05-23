from typing import Optional

from pydantic_xml import attr
from pydantic_xml import element

from at_krl.core.kb_reference import KBReference
from at_krl.utils.context import Context
from at_krl.xml_models.kb_value import KBEvaluatableLegacyXMLModel
from at_krl.xml_models.kb_value import KBEvaluatableXMLModel
from at_krl.xml_models.non_factor import NonFactorXMLModel


class KBReferenceXMLModel(KBEvaluatableXMLModel, tag="ref"):
    id: str = attr()
    ref: Optional["KBReferenceXMLModel"] = element(default=None)
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        result = super().get_data(context)
        if self.ref:
            result["ref"] = self.ref.to_internal(context.create_child("ref"))
        return result

    def build_target(self, data, context: Context):
        result = KBReference(**data)
        return result


class KBReferenceLegacyXMLModel(KBEvaluatableLegacyXMLModel, tag="ref"):
    id: str = attr()
    ref: Optional["KBReferenceXMLModel"] = element(default=None)
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        result = super().get_data(context)
        if self.ref:
            result["ref"] = self.ref.to_internal(context.create_child("ref"))
        return result

    def build_target(self, data, context: Context):
        result = KBReference(**data)
        return result
