from pydantic_xml import BaseXmlModel
from pydantic_xml import RootXmlModel

from at_krl.core.kb_entity import KBEntity
from at_krl.utils.context import Context


class KBEntityXMLModel(BaseXmlModel):
    def get_data(self, context: Context):
        return self.model_dump()

    def build_target(self, data, context: Context) -> KBEntity:
        raise NotImplementedError("Not implemented")

    def to_internal(self, context: Context):
        data = self.get_data(context)
        return self.build_target(data, context)


class KBEntityRootXMLModel(RootXmlModel):
    root: KBEntityXMLModel

    def to_internal(self, context: Context):
        return self.root.to_internal(context)
