from typing import Literal

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.temporal.allen_event import KBEvent
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableLegacyRootXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableRootXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassLegacyXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassXMLModel


class OccuranceConditionXMLModel(KBEntityXMLModel, tag="property"):
    id: Literal["УслВозн"] = attr()
    type: Literal["ЛогВыр"] = attr()
    value: SimpleEvaluatableRootXMLModel = element(tag="value")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("id", None)
        data.pop("type", None)
        data["value"] = self.value.to_internal(context.create_child("value"))
        return data

    def build_target(self, data, context: Context):
        return data["value"]


class KBEventXMLModel(AllenClassXMLModel, tag="event"):
    occurance_condition: OccuranceConditionXMLModel = wrapped("properties")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["occurance_condition"] = self.occurance_condition.to_internal(context.create_child("occurance_condition"))
        return data

    def build_target(self, data, context: Context):
        return KBEvent(**data)


class KBEventLegacyXMLModel(AllenClassLegacyXMLModel, tag="Event"):
    id: str = attr(name="Name")
    occurance_condition: SimpleEvaluatableLegacyRootXMLModel = element(tag="Formula")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["occurance_condition"] = self.occurance_condition.to_internal(context.create_child("occurance_condition"))
        return data

    def build_target(self, data, context: Context):
        return KBEvent(**data)


if __name__ == "__main__":
    xml_data = """
    <event id="EVENT1">
        <properties>
            <property id="УслВозн" type="ЛогВыр">
                <value>
                    <and>
                        <eq>
                            <ref id="OBJECT1">
                                <ref id="ATTRIBUTE1" />
                            </ref>
                            <value>test</value>
                        </eq>
                        <gt>
                            <ref id="OBJECT1">
                                <ref id="ATTRIBUTE2" />
                            </ref>
                            <value>15</value>
                        </gt>
                    </and>
                </value>
            </property>
        </properties>
    </event>
    """

    model = KBEventXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)

    xml_data = """
    <Event Name="Машина_2_приехала_на_ЛПУ1">
        <Formula>
            <LogOp Value="AND">
                <LogOp Value="AND">
                    <EqOp Value="eq">
                        <Attribute Value="Машина_2.Координата_X_Цели"/>
                        <Attribute Value="ЛПУ_1.Координата_X"/>
                    </EqOp>
                    <EqOp Value="eq">
                        <Attribute Value="Машина_2.Координата_Y_Цели"/>
                        <Attribute Value="ЛПУ_1.Координата_Y"/>
                    </EqOp>
                </LogOp>
                <LogOp Value="AND">
                    <EqOp Value="eq">
                        <Attribute Value="Машина_2.Координата_X"/>
                        <Attribute Value="Машина_2.Координата_X_Цели"/>
                    </EqOp>
                    <EqOp Value="eq">
                        <Attribute Value="Машина_2.Координата_Y"/>
                        <Attribute Value="Машина_2.Координата_Y_Цели"/>
                    </EqOp>
                </LogOp>
            </LogOp>
        </Formula>
    </Event>
    """
    model = KBEventLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)
