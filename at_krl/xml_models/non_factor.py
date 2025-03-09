from pydantic_xml import attr

from at_krl.core.non_factor import NonFactor
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel


class NonFactorXMLModel(KBEntityXMLModel, tag="with"):
    belief: float = attr()
    probability: float = attr()
    accuracy: float = attr()

    def build_target(self, data, context: Context):
        return NonFactor(**data)
