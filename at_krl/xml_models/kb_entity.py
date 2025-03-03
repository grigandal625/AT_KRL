from pydantic_xml import BaseXmlModel

from at_krl.utils.context import Context


class KBEntityXMLModel(BaseXmlModel):
    def get_data(self, context: Context):
        return self.model_dump()

    def build_target(self, data, context: Context):
        raise NotImplementedError("Not implemented")

    def to_internal(self, context: Context):
        data = self.get_data(context)
        return self.build_target(data, context)
