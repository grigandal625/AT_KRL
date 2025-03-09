import json
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
from at_krl.utils.context import Context

# test done


class KBInstructionModel(KBEntityModel):
    tag: str = Field(default="instruction")
    non_factor: Optional[NonFactorModel]

    def build_target(self, data, context: Context):
        if self.non_factor is not None:
            data["non_factor"] = self.non_factor.to_internal(context)
        return KBInstruction(**data)


class AssignInstructionModel(KBInstructionModel):
    tag: Literal["assign"] = Field(default="assign")
    ref: KBReferenceModel
    value: KBValueModel | KBReferenceModel | KBOperationModel

    def build_target(self, data, context: Context):
        data["non_factor"] = self.value.to_internal(context)
        data["ref"] = self.value.to_internal(context)
        data["value"] = self.value.to_internal(context)
        return AssignInstruction(**data)


ASSIGN_INSTRUCTION_JSON = """
{
    "tag": "assign",
    "ref": {
        "tag": "ref",
        "id": "target_var",
        "non_factor": {
            "tag": "with",
            "belief": 0.9,
            "probability": 0.8,
            "accuracy": 0.95
        }
    },
    "value": {
        "tag": "value",
        "content": 42,
        "non_factor": {
            "tag": "with",
            "belief": 0.85,
            "probability": 0.75,
            "accuracy": 0.9
        }
    },
    "non_factor": {
        "tag": "with",
        "belief": 0.8,
        "probability": 0.7,
        "accuracy": 0.85
    }
}
"""

if __name__ == "__main__":
    # Загрузка данных
    data = json.loads(ASSIGN_INSTRUCTION_JSON)

    # Создание контекста
    context = Context(name="test_assign", kb=None)

    # Создание вложенных моделей
    ref_model = KBReferenceModel(**data["ref"])
    value_model = KBValueModel(**data["value"])
    non_factor1 = NonFactorModel(**data["non_factor"])

    filtered_data = {k: v for k, v in data.items() if k not in ["ref", "value", "non_factor"]}
    # Создание модели инструкции
    filtered_data2 = AssignInstructionModel(**filtered_data, ref=ref_model, value=value_model, non_factor=non_factor1)
    print(filtered_data2.to_internal(context).krl)
