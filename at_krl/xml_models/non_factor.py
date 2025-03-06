from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.core.non_factor import NonFactor
from pydantic_xml import attr
from at_krl.utils.context import Context


class NonFactorXMLModel(KBEntityXMLModel, tag="with"):
    belief: float = attr()
    probability: float = attr()
    accuracy: float = attr()

    def build_target(self, data, context: Context):
        return NonFactor(**data)


if __name__ == "__main__":
    xml_data = """
    <with belief="80" probability="90" accuracy="0.95"/>
    """
    model = NonFactorXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))