from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.kb_instruction import AssignInstruction
from at_krl.core.kb_instruction import KBInstruction
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_operation import AllenAttributeExpressionModel
from at_krl.models.kb_operation import AllenOperationModel
from at_krl.models.kb_operation import KBOperationModel
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import KBValueModel
from at_krl.models.non_factor import NonFactorModel
from at_krl.utils.context import Context

# test done


class KBInstructionModel(KBEntityModel):
    tag: str = Field(default="instruction")
    non_factor: Optional[NonFactorModel] = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        if self.non_factor is not None:
            data["non_factor"] = self.non_factor.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return KBInstruction(**data)


class AssignInstructionModel(KBInstructionModel):
    tag: Literal["assign"] = Field(default="assign")
    ref: KBReferenceModel
    value: Union[KBValueModel, AllenAttributeExpressionModel, KBReferenceModel, KBOperationModel, AllenOperationModel]

    def get_data(self, context):
        data = super().get_data(context)
        data["ref"] = self.ref.to_internal(context)
        data["value"] = self.value.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return AssignInstruction(**data)


AssignInstructionModel.model_rebuild()
