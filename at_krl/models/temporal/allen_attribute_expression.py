from typing import Literal

from at_krl.core.temporal.allen_attribute_expression import FutureEvaluatingObject
from at_krl.models.kb_entity import KBEntityModel


class FutureEvaluatingObjectModel(KBEntityModel):
    name: Literal[
        "DURATION", "OCCURANCE_COUNT", "OPEN_COUNT", "CLOSE_COUNT", "OPENT_TACT", "CLOSE_TACT", "OCCURANCE_TACT"
    ]

    def build_target(self, data):
        return FutureEvaluatingObject(**data)


# class AllenAttributeExpressionModel(SimpleReferenceModel, AllenEvaluatableModel):
#     ref: AllenReferenceModel
#     id: Literal["ДЛИТЕЛЬНОСТЬ", "КОЛ_ВОЗН", "КОЛ_НАЧ", "КОЛ_ОКОНЧ", "ТАКТ_НАЧ", "ТАКТ_ОКОНЧ", "ТАКТ_ВОЗН"]
#     meta: Literal["allen_attribute_expression"]
#     target: FutureEvaluatingObjectModel

#     def build_target(self, data):
#         data['ref'] = self.ref.to_internal()
#         data['target'] = self.target.to_internal()
#         return AllenAttributeExpression(**data)
