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


if __name__ == "__main__":
    xml_data = """
    <rule id="1" meta="simple" desc="Лихорадка">
        <condition>
            <and>
                <eq>
                    <ref id="ОБЪЕКТ2">
                        <ref id="АТРИБУТ5"/>
                    </ref>
                    <value>Субфебрильная</value>
                    <with belief="50" probability="100" accuracy="0"/>
                </eq>
                <and>
                    <eq>
                        <ref id="ОБЪЕКТ3">
                            <ref id="АТРИБУТ1"/>
                        </ref>
                        <value>да</value>
                        <with belief="50" probability="100" accuracy="0"/>
                    </eq>
                    <eq>
                        <ref id="ОБЪЕКТ4">
                            <ref id="АТРИБУТ1"/>
                        </ref>
                        <value>да</value>
                        <with belief="50" probability="100" accuracy="0"/>
                    </eq>
                </and>
            </and>
        </condition>
    <action>
        <assign>
            <ref id="ОБЪЕКТ4">
                <ref id="АТРИБУТ11"/>
            </ref>
            <value>да</value>
            <with belief="50" probability="100" accuracy="0"/>
        </assign>
    </action>
    </rule>
    """
    model = KBRuleXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)

    xml_data = """
    <rule id="Зануление_скорости_по_прибытии_М1" meta="simple"
    desc="Правило для зануления скорости машины по прибытии на назначенное место">
        <condition>
            <EvIntRel Value="b">
                <Event Name="Машина_1_приехала_на_место_назначения"/>
                <Interval Name="Распределение_пострадавших"/>
            </EvIntRel>
        </condition>
        <action>
            <assign>
                <ref id="Машина_1">
                    <ref id="Координата_X_Вектора_Скорости">
                        <with belief="50" probability="100" accuracy="0"/>
                    </ref>
                </ref>
                <value>0</value>
                <with belief="50" probability="100" accuracy="0"/>
            </assign>
            <assign>
                <ref id="Машина_1">
                    <ref id="Координата_Y_Вектора_Скорости">
                        <with belief="50" probability="100" accuracy="0"/>
                    </ref>
                </ref>
                <value>0</value>
                <with belief="50" probability="100" accuracy="0"/>
            </assign>
        </action>
    </rule>
    """

    model = KBRuleLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)
