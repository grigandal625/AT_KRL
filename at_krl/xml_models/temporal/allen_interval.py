from typing import Literal

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.temporal.allen_interval import KBInterval
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableLegacyRootXMLModel
from at_krl.xml_models.simple.simple_operation import SimpleEvaluatableRootXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassLegacyXMLModel
from at_krl.xml_models.temporal.allen_class import AllenClassXMLModel


class OpenXMLModel(KBEntityXMLModel, tag="property"):
    id: Literal["УслНач"] = attr()
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


class CloseXMLModel(KBEntityXMLModel, tag="property"):
    id: Literal["УслОконч"] = attr()
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


class KBIntervalXMLModel(AllenClassXMLModel, tag="interval"):
    open: OpenXMLModel = wrapped("properties")
    close: CloseXMLModel = wrapped("properties")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["open"] = self.open.to_internal(context.create_child("open"))
        data["close"] = self.close.to_internal(context.create_child("close"))
        return data

    def build_target(self, data, context: Context):
        result = KBInterval(**data)
        if context.kb:
            context.kb.classes.intervals.append(result)
            result.owner = context.kb.classes
        return result


class KBIntervalLegacyXMLModel(AllenClassLegacyXMLModel, tag="Interval"):
    id: str = attr(name="Name")
    open: SimpleEvaluatableLegacyRootXMLModel = element(tag="Open")
    close: SimpleEvaluatableLegacyRootXMLModel = element(tag="Close")

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["open"] = self.open.to_internal(context.create_child("open"))
        data["close"] = self.close.to_internal(context.create_child("close"))
        return data

    def build_target(self, data, context: Context):
        result = KBInterval(**data)
        if context.kb:
            context.kb.classes.intervals.append(result)
            result.owner = context.kb.classes
        return result


if __name__ == "__main__":
    xml_data = """
    <interval id="INTERVAL1">
        <properties>
            <property id="УслНач" type="ЛогВыр">
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
            <property id="УслОконч" type="ЛогВыр">
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
    </interval>
    """

    model = KBIntervalXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)

    xml_data = """
    <Interval Name="Машина_2_подъезжает">
        <Open>
            <EqOp Value="ge">
                <ArOp Value="+">
                    <ArOp Value="*">
                        <ArOp Value="-">
                            <Attribute Value="Машина_2.Координата_Y_Цели"/>
                            <Attribute Value="Машина_2.Координата_Y"/>
                        </ArOp>
                        <ArOp Value="-">
                            <Attribute Value="Машина_2.Координата_Y_Цели"/>
                            <Attribute Value="Машина_2.Координата_Y"/>
                        </ArOp>
                    </ArOp>
                    <ArOp Value="*">
                        <ArOp Value="-">
                            <Attribute Value="Машина_2.Координата_X_Цели"/>
                            <Attribute Value="Машина_2.Координата_X"/>
                        </ArOp>
                        <ArOp Value="-">
                            <Attribute Value="Машина_2.Координата_X_Цели"/>
                            <Attribute Value="Машина_2.Координата_X"/>
                        </ArOp>
                    </ArOp>
                </ArOp>
                <Number Value="10"/>
            </EqOp>
        </Open>
        <Close>
            <LogOp Value="AND">
                <EqOp Value="eq">
                    <Attribute Value="Машина_2.Координата_Y_Цели"/>
                    <Attribute Value="Машина_2.Координата_Y"/>
                </EqOp>
                <EqOp Value="eq">
                    <Attribute Value="Машина_2.Координата_X_Цели"/>
                    <Attribute Value="Машина_2.Координата_X"/>
                </EqOp>
            </LogOp>
        </Close>
    </Interval>
    """
    model = KBIntervalLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)
