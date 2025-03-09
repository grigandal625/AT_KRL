from typing import List
from typing import Literal
from typing import Optional

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.kb_rule import KBRule
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.kb_instruction import AssignInstructionLegacyXMLModel
from at_krl.xml_models.kb_instruction import AssignInstructionXMLModel
from at_krl.xml_models.kb_operation import KBEvaluatableLegacyRootXMLModel
from at_krl.xml_models.kb_operation import KBEvaluatableRootXMLModel


class KBRuleXMLModel(KBEntityXMLModel, tag="rule"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    meta: Optional[Literal["simple", "periodic"]] = attr(default="simple")
    period: Optional[int] = attr(default=None)
    condition: KBEvaluatableRootXMLModel = element(tag="condition")
    instructions: List[AssignInstructionXMLModel] = wrapped("action", element())
    else_instructions: Optional[List[AssignInstructionXMLModel]] = wrapped("else-action", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("meta", None)
        data["condition"] = self.condition.to_internal(context.create_child("condition"))
        data["instructions"] = [
            instruction.to_internal(context.create_child("action")) for instruction in self.instructions
        ]
        if self.else_instructions:
            data["else_instructions"] = [
                instruction.to_internal(context.create_child("else-action")) for instruction in self.else_instructions
            ]
        return data

    def build_target(self, data, context: Context):
        return KBRule(**data)


class KBRuleLegacyXMLModel(KBEntityXMLModel, tag="rule"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    meta: Optional[Literal["simple", "periodic"]] = attr(default="simple")
    period: Optional[int] = attr(default=None)
    condition: KBEvaluatableLegacyRootXMLModel = element(tag="condition")
    instructions: List[AssignInstructionLegacyXMLModel] = wrapped("action", element())
    else_instructions: Optional[List[AssignInstructionLegacyXMLModel]] = wrapped("else-action", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("meta", None)
        data["condition"] = self.condition.to_internal(context.create_child("condition"))
        data["instructions"] = [
            instruction.to_internal(context.create_child("action")) for instruction in self.instructions
        ]
        if self.else_instructions:
            data["else_instructions"] = [
                instruction.to_internal(context.create_child("else-action")) for instruction in self.else_instructions
            ]
        return data

    def build_target(self, data, context: Context):
        return KBRule(**data)
