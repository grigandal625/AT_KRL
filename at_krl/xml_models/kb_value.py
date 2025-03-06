from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel, SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.non_factor import NonFactorXMLModel
from typing import Optional
from at_krl.utils.context import Context
from at_krl.core.kb_value import KBValue
from pydantic_xml import element

class KBEvaluatableXMLModel(SimpleEvaluatableXMLModel):
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data


class KBEvaluatableLegacyXMLModel(SimpleEvaluatableLegacyXMLModel):
    non_factor: Optional[NonFactorXMLModel]

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data


class KBValueXMLModel(KBEvaluatableXMLModel, tag="value"):
    content: int | float | bool | str

    def build_target(self, data, context: Context) -> KBValue:
        return KBValue(**data)


class KBValueLegacyXMLModel(KBEvaluatableLegacyXMLModel, tag="value"):
    content: int | float | bool | str

    def build_target(self, data, context: Context) -> KBValue:
        return KBValue(**data)

    

if __name__ == "__main__":
    xml_data = """
    <value>123.45<with belief="50" probability="100" accuracy="0"/></value>
    """
    model = KBValueXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <value>True</value>
    """
    model = KBValueXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <value>False</value>
    """
    model = KBValueXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))