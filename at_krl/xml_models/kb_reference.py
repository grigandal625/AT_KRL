from at_krl.xml_models.kb_value import KBEvaluatableXMLModel, KBEvaluatableLegacyXMLModel

from at_krl.utils.context import Context
from at_krl.core.kb_reference import KBReference
from pydantic_xml import attr, element
from typing import Optional


class KBReferenceXMLModel(KBEvaluatableXMLModel, tag="ref"):
    id: str = attr()
    ref: Optional["KBReferenceXMLModel"] = element(default=None)

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

    def get_data(self, context: Context):
        result = super().get_data(context)
        if self.ref:
            result["ref"] = self.ref.to_internal(context.create_child("ref"))
        return result

    def build_target(self, data, context: Context):
        result = KBReference(**data)
        return result



if __name__ == "__main__":
    xml_data = """
    <ref id="ref1"/>
    """
    model = KBReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="ref2">
        <with belief="50" probability="100" accuracy="0"/>
    </ref>
    """
    model = KBReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="ref3">
        <ref id="ref4"/>
        <with belief="50" probability="100" accuracy="0"/>
    </ref>
    """
    model = KBReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

