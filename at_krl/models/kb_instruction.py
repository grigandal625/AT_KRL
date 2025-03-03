from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.kb_instruction import AssignInstruction
from at_krl.core.kb_instruction import KBInstruction
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_operation import KBOperationModel
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import KBValueModel
from at_krl.models.non_factor import NonFactorModel


class KBInstructionModel(KBEntityModel):
    tag: str = Field(default="instruction")
    non_factor: Optional[NonFactorModel]

    def build_target(self, data):
        if self.non_factor is not None:
            data["non_factor"] = self.non_factor.to_internal()
        return KBInstruction(**data)


class AssignInstructionModel(KBInstructionModel):
    tag: Literal["assign"] = Field(default="assign")
    ref: KBReferenceModel
    value: KBValueModel | KBReferenceModel | KBOperationModel

    def build_target(self, data):
        data["ref"] = self.value.to_internal()
        data["value"] = self.value.to_internal()
        return AssignInstruction(**data)
