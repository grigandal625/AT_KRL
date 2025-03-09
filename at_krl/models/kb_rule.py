from typing import List
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.kb_rule import KBRule
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.models.kb_instruction import AssignInstructionModel
from at_krl.models.kb_operation import AllenAttributeExpressionModel
from at_krl.models.kb_operation import AllenOperationModel
from at_krl.models.kb_operation import KBOperationModel
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import KBValueModel
from at_krl.utils.context import Context


class KBInstructionListModel(KBRootModel[List[AssignInstructionModel]]):
    def to_internal(self, context: Context):
        return [p.to_internal(context) for p in self.root]


class KBRuleModel(KBEntityModel):
    tag: Literal["rule"] = Field(default="rule")

    id: str
    condition: Union[
        KBValueModel, AllenAttributeExpressionModel, KBReferenceModel, KBOperationModel, AllenOperationModel
    ]
    instructions: KBInstructionListModel
    meta: Literal["simple", "periodic"] = Field(default="simple")
    else_instructions: Optional[KBInstructionListModel] = Field(default_factory=list)
    period: Optional[int] = Field(default=None)
    desc: Optional[str] = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        data.pop("meta")
        data["condition"] = self.condition.to_internal(context)
        data["instructions"] = self.instructions.to_internal(context)
        if self.else_instructions:
            data["else_instructions"] = self.else_instructions.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        result = KBRule(**data)
        if context.kb:
            context.kb.rules.append(result)
        return result


KBRuleModel.model_rebuild()
