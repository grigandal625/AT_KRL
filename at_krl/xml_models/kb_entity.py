from at_krl.utils.context import Context
from at_krl.xml_models.utils import MultiTagXmlModel


class KBEntityXMLModel(MultiTagXmlModel, abstract=True):
    def get_data(self, context: Context):
        return self.model_dump()

    def build_target(self, data, context: Context):
        raise NotImplementedError("Not implemented")

    def to_internal(self, context: Context):
        data = self.get_data(context)
        return self.build_target(data, context)
