from typing import List
from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.kb_rule import KBRule
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.models.kb_instruction import KBInstructionModel
from at_krl.models.kb_operation import KBOperationModel
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import KBValueModel


class KBInstructionListModel(KBRootModel[List[KBInstructionModel]]):
    def build_target(self, data):
        return [p.to_internal() for p in self.points]


class KBRuleModel(KBEntityModel):
    tag: Literal["rule"] = Field(default="rule")

    id: str
    condition: KBValueModel | KBReferenceModel | KBOperationModel
    instructions: KBInstructionListModel
    else_instructions: Optional[KBInstructionListModel] = Field(default_factory=list)
    period: Optional[int] = Field(default=None)
    desc: Optional[str] = Field(default=None)

    def build_target(self, data):
        data["condition"] = self.condition.to_internal()
        data["instructions"] = self.instructions.to_internal()
        if self.else_instructions:
            data["else_instructions"] = self.else_instructions.to_internal()
        return KBRule(**data)
