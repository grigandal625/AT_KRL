from pydantic_xml import attr

from at_krl.core.simple.simple_value import SimpleValue
from at_krl.utils.context import Context
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel


class SimpleValueXMLModel(SimpleEvaluatableXMLModel, tag="value"):
    value: float | bool | str

    def build_target(self, data, context: Context):
        result = SimpleValue(content=data["value"])
        return result


class SimpleValueLegacyXMLModel(SimpleEvaluatableLegacyXMLModel):
    def build_target(self, data, context: Context):
        result = SimpleValue(content=data["value"])
        return result


class SimpleStringValueLegacyXMLModel(SimpleValueLegacyXMLModel, tag="String"):
    value: str = attr()


class SimpleNumberValueLegacyXMLModel(SimpleValueLegacyXMLModel, tag="Number"):
    value: float = attr()


class SimpleBooleanValueLegacyXMLModel(SimpleValueLegacyXMLModel, tag="TruthVal"):
    value: bool = attr()


if __name__ == "__main__":
    xml_data = "<value>FALSE</value>"
    model = SimpleValueXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = '<String value="test" />'
    model = SimpleStringValueLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = '<Number value="123.45" />'
    model = SimpleNumberValueLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = '<TruthVal value="FALSE" />'
    model = SimpleBooleanValueLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))
