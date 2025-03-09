from typing import List
from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.kb_rule import KBRule
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.models.kb_instruction import AssignInstructionModel
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
    condition: KBValueModel | KBReferenceModel | KBOperationModel
    instructions: KBInstructionListModel
    meta: Literal["simple", "periodic"] = Field(default="simple")
    else_instructions: Optional[KBInstructionListModel] = Field(default_factory=list)
    period: Optional[int] = Field(default=None)
    desc: Optional[str] = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        data.pop("meta")
        return data

    def build_target(self, data, context: Context):
        data["condition"] = self.condition.to_internal(context)
        data["instructions"] = self.instructions.to_internal(context)
        if self.else_instructions:
            data["else_instructions"] = self.else_instructions.to_internal(context)

        result = KBRule(**data)
        if context.kb:
            context.kb.rules.append(result)
        return result


# Пример данных для тестирования
# json_data = """
#     {
#         "rule": {
#             "tag": "rule",
#             "id": "temp_control_rule",
#             "condition": {
#                 "tag": gt,
#                 "sign": ">",
#                 "left": {
#                     "tag": "ref",
#                     "id": "current_temp"
#                 },
#                 "right": {
#                     "tag": "value",
#                     "content": 30
#                 }
#             },
#             "instructions": {
#                 "root": [
#                     {
#                         "tag": "assign",
#                         "ref": {
#                             "tag": "ref",
#                             "id": "target_var"
#                         },
#                         "value": {
#                             "tag": "value",
#                             "content": 42
#                         }
#                     }
#                 ]
#             },
#             "else_instructions": {
#                 "root": [
#                     {
#                         "tag": "assign",
#                         "ref": {
#                             "tag": "ref",
#                             "id": "fallback_var"
#                         },
#                         "value": {
#                             "tag": "value",
#                             "content": 0
#                         }
#                     }
#                 ]
#             },
#             "period": 5,
#             "desc": "Temperature control rule"
#         }
#     }
#     """
# def test_kbrule_model():
#     data = json.loads(json_data)
#     rule_data = data["rule"]
#     context = Context(name="test", kb=None)

#     # Создаем вложенные модели
#     condition_model = KBOperationModel(**rule_data["condition"])
#     instructions_model = KBInstructionListModel(**rule_data["instructions"])
#     else_instructions_model = KBInstructionListModel(**rule_data["else_instructions"])


#     filtered_data = {
#         k: v for k, v in rule_data.items()
#         if k not in ["condition", "instructions", "else_instructions"]
#     }

#     # Собираем модель правила
#     rule_model = KBRuleModel(
#         **filtered_data,
#         condition=condition_model,
#         instructions=instructions_model,
#         else_instructions=else_instructions_model
#     )

#     # Проверки
#     assert rule_model.id == "temp_control"
#     assert rule_model.period == 5
#     assert isinstance(rule_model.condition.left, KBReferenceModel)
#     assert rule_model.instructions.root[0].non_factor.belief == 0.95

#     # Конвертация
#     rule = rule_model.to_internal(context)

#     # assert len(context.kb.rules) == 1
#     # assert isinstance(rule.condition, SimpleOperation)
#     # assert rule.instructions[0].non_factor.accuracy == 1.0
#     print(rule.krl)

# if __name__ == "__main__":
#     test_kbrule_model()
