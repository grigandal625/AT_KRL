from typing import Optional
from typing import Union

from pydantic_xml import element

from at_krl.core.kb_instruction import AssignInstruction
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.kb_operation import AllenAttributeExpressionXMLModel
from at_krl.xml_models.kb_operation import AnyAllenOperation
from at_krl.xml_models.kb_operation import AnyKBOperation
from at_krl.xml_models.kb_operation import AnyKBOperationLegacy
from at_krl.xml_models.kb_operation import EvIntRelLegacyXMLModel
from at_krl.xml_models.kb_operation import EvRelLegacyXMLModel
from at_krl.xml_models.kb_operation import IntRelLegacyXMLModel
from at_krl.xml_models.kb_reference import KBReferenceLegacyXMLModel
from at_krl.xml_models.kb_reference import KBReferenceXMLModel
from at_krl.xml_models.kb_value import KBValueLegacyXMLModel
from at_krl.xml_models.kb_value import KBValueXMLModel
from at_krl.xml_models.non_factor import NonFactorXMLModel
from at_krl.xml_models.simple.simple_reference import SimpleReferenceXMLModel


class KBInstructionXMLModel(KBEntityXMLModel):
    pass


class KBInstructionLegacyXMLModel(KBEntityXMLModel):
    pass


class AssignInstructionXMLModel(KBInstructionXMLModel, tag="assign"):
    ref: SimpleReferenceXMLModel
    value: Union[
        AllenAttributeExpressionXMLModel, AnyAllenOperation, AnyKBOperation, KBValueXMLModel, KBReferenceXMLModel
    ]
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["ref"] = self.ref.to_internal(context.create_child("ref"))
        data["value"] = self.value.to_internal(context.create_child("value"))
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data

    def build_target(self, data, context: Context):
        return AssignInstruction(**data)


class AssignInstructionLegacyXMLModel(KBInstructionLegacyXMLModel, tag="assign"):
    ref: SimpleReferenceXMLModel
    value: Union[
        AnyKBOperationLegacy,
        KBValueLegacyXMLModel,
        KBReferenceLegacyXMLModel,
        EvIntRelLegacyXMLModel,
        EvRelLegacyXMLModel,
        IntRelLegacyXMLModel,
    ]
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["ref"] = self.ref.to_internal(context.create_child("ref"))
        data["value"] = self.value.to_internal(context.create_child("value"))
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data

    def build_target(self, data, context: Context):
        return AssignInstruction(**data)


if __name__ == "__main__":
    xml_data = """
    <assign>
        <ref id="ОБЪЕКТ6">
            <ref id="АТРИБУТ2"/>
        </ref>
        <value>Некротическая форма аспергиллеза</value>
        <with belief="50" probability="70" accuracy="0"/>
    </assign>
    """
    model = AssignInstructionXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))
