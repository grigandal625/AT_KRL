from typing import Optional

from pydantic_xml import element

from at_krl.core.kb_value import KBValue
from at_krl.utils.context import Context
from at_krl.xml_models.non_factor import NonFactorXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableLegacyXMLModel
from at_krl.xml_models.simple.simple_evaluatable import SimpleEvaluatableXMLModel


class KBEvaluatableXMLModel(SimpleEvaluatableXMLModel):
    __xml_abstract__ = True

    # non_factor: Optional[NonFactorXMLModel] = element(default=None)
    # не-факторы не включаем, потому что тогда он будет первым в порядке дочерних xml-элементов
    # и при построении обьекта из xml-данных модель не сможет найти его, поскольку в xml мы пишем его последним.

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data


class KBEvaluatableLegacyXMLModel(SimpleEvaluatableLegacyXMLModel):
    __xml_abstract__ = True

    # non_factor: Optional[NonFactorXMLModel] = element(default=None)
    # не-факторы не включаем, потому что тогда он будет первым в порядке дочерних xml-элементов
    # и при построении обьекта из xml-данных модель не сможет найти его, поскольку в xml мы пишем его последним.

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data


class KBValueXMLModel(KBEvaluatableXMLModel, tag="value"):
    content: int | float | bool | str
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def build_target(self, data, context: Context) -> KBValue:
        return KBValue(**data)


class KBValueLegacyXMLModel(KBEvaluatableLegacyXMLModel, tag="value"):
    content: int | float | bool | str
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def build_target(self, data, context: Context) -> KBValue:
        return KBValue(**data)


if __name__ == "__main__":
    xml_data = """
    <value>123.45<with belief="50" probability="70" accuracy="0"/></value>
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
