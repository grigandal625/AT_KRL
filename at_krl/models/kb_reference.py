from at_krl.core.kb_reference import KBReference
from at_krl.models.kb_value import EvaluatableModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel


class KBReferenceModel(EvaluatableModel, SimpleReferenceModel):
    def build_target(self, data, context):
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))

        return KBReference(**data)
