from typing import Literal
from typing import Optional
from typing import Union

from pydantic_xml import attr
from pydantic_xml import element

from at_krl.core.kb_operation import KBOperation
from at_krl.core.temporal.allen_attribute_expression import AllenAttributeExpression
from at_krl.core.temporal.allen_operation import AllenOperation
from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityRootXMLModel
from at_krl.xml_models.kb_reference import KBReferenceLegacyXMLModel
from at_krl.xml_models.kb_reference import KBReferenceXMLModel
from at_krl.xml_models.kb_value import KBEvaluatableXMLModel
from at_krl.xml_models.kb_value import KBValueLegacyXMLModel
from at_krl.xml_models.kb_value import KBValueXMLModel
from at_krl.xml_models.non_factor import NonFactorXMLModel
from at_krl.xml_models.temporal.allen_evaluatable import AllenEvaluatableLegacyXMLModel
from at_krl.xml_models.temporal.allen_evaluatable import AllenEvaluatableXMLModel


class BinaryKBOperationXMLModel(KBEvaluatableXMLModel):
    left: Union[
        KBValueXMLModel,
        "AllenAttributeExpressionXMLModel",
        KBReferenceXMLModel,
        "AnyKBOperation",
        "AnyAllenOperation",
    ]
    right: Union[
        KBValueXMLModel,
        "AllenAttributeExpressionXMLModel",
        KBReferenceXMLModel,
        "AnyKBOperation",
        "AnyAllenOperation",
    ]
    non_factor: NonFactorXMLModel = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        data["sign"] = self.__xml_tag__
        return data

    def build_target(self, data, context: Context):
        return KBOperation(**data)


class UnaryKBOperationXMLModel(KBEvaluatableXMLModel):
    operand: Union[
        KBValueXMLModel,
        "AllenAttributeExpressionXMLModel",
        KBReferenceXMLModel,
        "AnyKBOperation",
        "AnyAllenOperation",
    ]
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.operand.to_internal(context.create_child("left"))
        data["sign"] = self.__xml_tag__
        data.pop("operand", None)
        return data

    def build_target(self, data, context: Context):
        return KBOperation(**data)


class KBEq(BinaryKBOperationXMLModel, tag="eq"):
    pass


class KBGt(BinaryKBOperationXMLModel, tag="gt"):
    pass


class KBGe(BinaryKBOperationXMLModel, tag="ge"):
    pass


class KBLt(BinaryKBOperationXMLModel, tag="lt"):
    pass


class KBLe(BinaryKBOperationXMLModel, tag="le"):
    pass


class KBNe(BinaryKBOperationXMLModel, tag="ne"):
    pass


class KBAnd(BinaryKBOperationXMLModel, tag="and"):
    pass


class KBOr(BinaryKBOperationXMLModel, tag="or"):
    pass


class KBNot(UnaryKBOperationXMLModel, tag="not"):
    pass


class KBXor(BinaryKBOperationXMLModel, tag="xor"):
    pass


class KBNeg(UnaryKBOperationXMLModel, tag="neg"):
    pass


class KBAdd(BinaryKBOperationXMLModel, tag="add"):
    pass


class KBSub(BinaryKBOperationXMLModel, tag="sub"):
    pass


class KBMul(BinaryKBOperationXMLModel, tag="mul"):
    pass


class KBDiv(BinaryKBOperationXMLModel, tag="div"):
    pass


class KBMod(BinaryKBOperationXMLModel, tag="mod"):
    pass


class KBPow(BinaryKBOperationXMLModel, tag="pow"):
    pass


AnyKBOperation = (
    KBEq
    | KBGt
    | KBGe
    | KBLt
    | KBLe
    | KBNe
    | KBAnd
    | KBOr
    | KBNot
    | KBXor
    | KBNeg
    | KBAdd
    | KBSub
    | KBMul
    | KBMod
    | KBPow
)

KBEvaluatableRoot = Union[
    "AllenAttributeExpressionXMLModel",
    KBReferenceXMLModel,
    KBValueXMLModel,
    AnyKBOperation,
    "AnyAllenOperation",
]


class KBEvaluatableRootXMLModel(KBEntityRootXMLModel):
    root: KBEvaluatableRoot


class BinaryKBOperationLegacyXMLModel(KBEvaluatableXMLModel):
    left: Union[
        KBValueLegacyXMLModel,
        KBReferenceLegacyXMLModel,
        "AnyKBOperationLegacy",
        "EvIntRelLegacyXMLModel",
        "IntRelLegacyXMLModel",
        "EvRelLegacyXMLModel",
    ]
    right: Union[
        KBValueLegacyXMLModel,
        KBReferenceLegacyXMLModel,
        "AnyKBOperationLegacy",
        "EvIntRelLegacyXMLModel",
        "IntRelLegacyXMLModel",
        "EvRelLegacyXMLModel",
    ]
    non_factor: NonFactorXMLModel = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        data["sign"] = self.__xml_tag__
        return data

    def build_target(self, data, context: Context):
        return KBOperation(**data)


class UnaryKBOperationLegacyXMLModel(KBEvaluatableXMLModel):
    operand: Union[
        KBValueLegacyXMLModel,
        KBReferenceLegacyXMLModel,
        "AnyKBOperationLegacy",
        "EvIntRelLegacyXMLModel",
        "IntRelLegacyXMLModel",
        "EvRelLegacyXMLModel",
    ]
    non_factor: Optional[NonFactorXMLModel] = element(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.operand.to_internal(context.create_child("left"))
        data["sign"] = self.__xml_tag__
        data.pop("operand", None)
        return data

    def build_target(self, data, context: Context):
        return KBOperation(**data)


class KBEqLegacy(BinaryKBOperationLegacyXMLModel, tag="eq"):
    pass


class KBGtLegacy(BinaryKBOperationLegacyXMLModel, tag="gt"):
    pass


class KBGeLegacy(BinaryKBOperationLegacyXMLModel, tag="ge"):
    pass


class KBLtLegacy(BinaryKBOperationLegacyXMLModel, tag="lt"):
    pass


class KBLeLegacy(BinaryKBOperationLegacyXMLModel, tag="le"):
    pass


class KBNeLegacy(BinaryKBOperationLegacyXMLModel, tag="ne"):
    pass


class KBAndLegacy(BinaryKBOperationLegacyXMLModel, tag="and"):
    pass


class KBOrLegacy(BinaryKBOperationLegacyXMLModel, tag="or"):
    pass


class KBNotLegacy(UnaryKBOperationLegacyXMLModel, tag="not"):
    pass


class KBXorLegacy(BinaryKBOperationLegacyXMLModel, tag="xor"):
    pass


class KBNegLegacy(UnaryKBOperationLegacyXMLModel, tag="neg"):
    pass


class KBAddLegacy(BinaryKBOperationLegacyXMLModel, tag="add"):
    pass


class KBSubLegacy(BinaryKBOperationLegacyXMLModel, tag="sub"):
    pass


class KBMulLegacy(BinaryKBOperationLegacyXMLModel, tag="mul"):
    pass


class KBDivLegacy(BinaryKBOperationLegacyXMLModel, tag="div"):
    pass


class KBModLegacy(BinaryKBOperationLegacyXMLModel, tag="mod"):
    pass


class KBPowLegacy(BinaryKBOperationLegacyXMLModel, tag="pow"):
    pass


AnyKBOperationLegacy = (
    KBEqLegacy
    | KBGtLegacy
    | KBGeLegacy
    | KBLtLegacy
    | KBLeLegacy
    | KBNeLegacy
    | KBAndLegacy
    | KBOrLegacy
    | KBNotLegacy
    | KBXorLegacy
    | KBNegLegacy
    | KBAddLegacy
    | KBSubLegacy
    | KBMulLegacy
    | KBModLegacy
    | KBPowLegacy
)

KBEvaluatableLegacyRoot = Union[
    KBReferenceLegacyXMLModel,
    KBValueLegacyXMLModel,
    AnyKBOperationLegacy,
    "EvIntRelLegacyXMLModel",
    "IntRelLegacyXMLModel",
    "EvRelLegacyXMLModel",
]


class KBEvaluatableLegacyRootXMLModel(KBEntityRootXMLModel):
    root: KBEvaluatableLegacyRoot


class AllenReferenceXMLModel(AllenEvaluatableXMLModel, tag="ref"):
    id: str = attr()
    meta: Literal["allen_reference"] = attr()
    index: Optional[KBEvaluatableRootXMLModel] = element(tag="index", default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("meta", None)
        if self.index:
            data["index"] = self.index.to_internal(context.create_child("index"))
        return data

    def build_target(self, data, context: Context):
        result = AllenReference(**data)

        if context.kb:
            interval = context.kb.get_interval_by_id(result.id)
            event = context.kb.get_event_by_id(result.id)

            if interval and event:
                raise ValueError(f"Found both interval and event with id {result.id}")

            if not event and not interval:
                raise ValueError(f"No event or interval found with id {result.id}")

            result.target = interval or event
            result.validate_legacy_tag()
        return result


class AllenReferenceLegacyXMLModel(AllenEvaluatableLegacyXMLModel):
    id: str = attr(name="Name")

    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        return result


class IntervalReferenceLegacyXMLModel(AllenReferenceLegacyXMLModel, tag="Interval"):
    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        if context.kb:
            result.target = context.kb.get_interval_by_id(result.id)
            if not result.target:
                raise ValueError(f"No interval found with id {result.id}")
            result.validate_legacy_tag()
        return result


class EventReferenceLegacyXMLModel(AllenReferenceLegacyXMLModel, tag="Event"):
    def build_target(self, data, context: Context):
        result = AllenReference(**data)
        if context.kb:
            result.target = context.kb.get_event_by_id(result.id)
            if not result.target:
                raise ValueError(f"No event found with id {result.id}")
            result.validate_legacy_tag()
        return result


class AllenAttributeExpressionXMLModel(AllenEvaluatableXMLModel, tag="ref"):
    ref: AllenReferenceXMLModel
    id: Literal["ДЛИТЕЛЬНОСТЬ", "КОЛ_ВОЗН", "КОЛ_НАЧ", "КОЛ_ОКОНЧ", "ТАКТ_НАЧ", "ТАКТ_ОКОНЧ", "ТАКТ_ВОЗН"] = attr()
    meta: Literal["allen_attribute_expression"] = attr()

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("meta", None)
        data["ref"] = self.ref.to_internal(context.create_child("ref"))
        return data

    def build_target(self, data, context: Context):
        return AllenAttributeExpression(**data)


class AllenOperationXMLModel(AllenEvaluatableXMLModel):
    left: AllenReferenceXMLModel
    right: AllenReferenceXMLModel

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        data["sign"] = self.__xml_tag__
        return data

    def build_target(self, data, context: Context):
        return AllenOperation(**data)


class AllenBOperationXMLModel(AllenOperationXMLModel, tag="b"):
    pass


class AllenBIOperationXMLModel(AllenOperationXMLModel, tag="bi"):
    pass


class AllenMOperationXMLModel(AllenOperationXMLModel, tag="m"):
    pass


class AllenMIOperationXMLModel(AllenOperationXMLModel, tag="mi"):
    pass


class AllenSOperationXMLModel(AllenOperationXMLModel, tag="s"):
    pass


class AllenSIOperationXMLModel(AllenOperationXMLModel, tag="si"):
    pass


class AllenFOperationXMLModel(AllenOperationXMLModel, tag="f"):
    pass


class AllenFIOperationXMLModel(AllenOperationXMLModel, tag="fi"):
    pass


class AllenDOperationXMLModel(AllenOperationXMLModel, tag="d"):
    pass


class AllenDIOperationXMLModel(AllenOperationXMLModel, tag="di"):
    pass


class AllenOOperationXMLModel(AllenOperationXMLModel, tag="o"):
    pass


class AllenOIOperationXMLModel(AllenOperationXMLModel, tag="oi"):
    pass


class AllenEOperationXMLModel(AllenOperationXMLModel, tag="e"):
    pass


class AllenAOperationXMLModel(AllenOperationXMLModel, tag="a"):
    pass


AnyAllenOperation = Union[
    AllenBOperationXMLModel,
    AllenBIOperationXMLModel,
    AllenMOperationXMLModel,
    AllenMIOperationXMLModel,
    AllenSOperationXMLModel,
    AllenSIOperationXMLModel,
    AllenFOperationXMLModel,
    AllenFIOperationXMLModel,
    AllenDOperationXMLModel,
    AllenDIOperationXMLModel,
    AllenOOperationXMLModel,
    AllenOIOperationXMLModel,
    AllenEOperationXMLModel,
    AllenAOperationXMLModel,
]


class AllenOperationRootXMLModel(KBEntityRootXMLModel):
    root: AnyAllenOperation


class AllenOperationLegacyXMLModel(AllenEvaluatableLegacyXMLModel):
    sign: Literal[
        "b",
        "bi",
        "m",
        "mi",
        "s",
        "si",
        "f",
        "fi",
        "d",
        "di",
        "o",
        "oi",
        "e",
        "a",
    ] = attr(name="Value")

    left: Union[IntervalReferenceLegacyXMLModel, EventReferenceLegacyXMLModel]
    right: Union[IntervalReferenceLegacyXMLModel, EventReferenceLegacyXMLModel]

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["left"] = self.left.to_internal(context.create_child("left"))
        data["right"] = self.right.to_internal(context.create_child("right"))
        return data

    def build_target(self, data, context: Context):
        return AllenOperation(**data)


class EvIntRelLegacyXMLModel(AllenOperationLegacyXMLModel, tag="EvIntRel"):
    left: EventReferenceLegacyXMLModel
    right: IntervalReferenceLegacyXMLModel


class IntRelLegacyXMLModel(AllenOperationLegacyXMLModel, tag="IntRel"):
    left: IntervalReferenceLegacyXMLModel
    right: IntervalReferenceLegacyXMLModel


class EvRelLegacyXMLModel(AllenOperationLegacyXMLModel, tag="EvRel"):
    left: EventReferenceLegacyXMLModel
    right: EventReferenceLegacyXMLModel


class AllenOperationLegacyRootXMLModel(KBEntityRootXMLModel):
    root: Union[EvIntRelLegacyXMLModel, IntRelLegacyXMLModel, EvRelLegacyXMLModel]


AllenAttributeExpressionXMLModel.model_rebuild()
AllenReferenceXMLModel.model_rebuild()
AllenBOperationXMLModel.model_rebuild()
AllenBIOperationXMLModel.model_rebuild()
AllenMOperationXMLModel.model_rebuild()
AllenMIOperationXMLModel.model_rebuild()
AllenSOperationXMLModel.model_rebuild()
AllenSIOperationXMLModel.model_rebuild()
AllenFOperationXMLModel.model_rebuild()
AllenFIOperationXMLModel.model_rebuild()
AllenDOperationXMLModel.model_rebuild()
AllenDIOperationXMLModel.model_rebuild()
AllenOOperationXMLModel.model_rebuild()
AllenOIOperationXMLModel.model_rebuild()
AllenEOperationXMLModel.model_rebuild()
AllenAOperationXMLModel.model_rebuild()
AllenOperationRootXMLModel.model_rebuild()
EvIntRelLegacyXMLModel.model_rebuild()
IntRelLegacyXMLModel.model_rebuild()
EvRelLegacyXMLModel.model_rebuild()
AllenOperationLegacyRootXMLModel.model_rebuild()

BinaryKBOperationXMLModel.model_rebuild()
UnaryKBOperationXMLModel.model_rebuild()

KBEq.model_rebuild()
KBGt.model_rebuild()
KBGe.model_rebuild()
KBLt.model_rebuild()
KBLe.model_rebuild()
KBNe.model_rebuild()
KBAnd.model_rebuild()
KBOr.model_rebuild()
KBNot.model_rebuild()
KBXor.model_rebuild()
KBNeg.model_rebuild()
KBAdd.model_rebuild()
KBSub.model_rebuild()
KBMul.model_rebuild()
KBDiv.model_rebuild()
KBMod.model_rebuild()
KBPow.model_rebuild()
KBEvaluatableRootXMLModel.model_rebuild()

BinaryKBOperationLegacyXMLModel.model_rebuild()
UnaryKBOperationLegacyXMLModel.model_rebuild()

KBEqLegacy.model_rebuild()
KBGtLegacy.model_rebuild()
KBGeLegacy.model_rebuild()
KBLtLegacy.model_rebuild()
KBLeLegacy.model_rebuild()
KBNeLegacy.model_rebuild()
KBAndLegacy.model_rebuild()
KBOrLegacy.model_rebuild()
KBNotLegacy.model_rebuild()
KBXorLegacy.model_rebuild()
KBNegLegacy.model_rebuild()
KBAddLegacy.model_rebuild()
KBSubLegacy.model_rebuild()
KBMulLegacy.model_rebuild()
KBDivLegacy.model_rebuild()
KBModLegacy.model_rebuild()
KBPowLegacy.model_rebuild()

KBEvaluatableLegacyRootXMLModel.model_rebuild()


if __name__ == "__main__":
    xml_data = """
    <AllenOperationRootXMLModel>
        <d>
            <ref id="INTERVAL1" meta="allen_reference" />
            <ref id="INTERVAL2" meta="allen_reference" />
        </d>
    </AllenOperationRootXMLModel>
    """

    model = AllenOperationRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <AllenOperationLegacyRootXMLModel>
        <EvIntRel Value="b">
            <Event Name="EVENT1" />
            <Interval Name="INTERVAL1"/>
        </EvIntRel>
    </AllenOperationLegacyRootXMLModel>
    """

    model = AllenOperationLegacyRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="ДЛИТЕЛЬНОСТЬ" meta="allen_attribute_expression">
        <ref id="МОЙ_ИНТЕРВАЛ" meta="allen_reference" />
    </ref>
    """

    model = AllenAttributeExpressionXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="my_event" meta="allen_reference">
        <index>
            <value>5</value>
        </index>
    </ref>
    """
    model = AllenReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <ref id="my_event" meta="allen_reference" />
    """
    model = AllenReferenceXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <Interval Name="my_interval" />
    """
    model = IntervalReferenceLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <Event Name="my_event" />
    """
    model = EventReferenceLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <KBEvaluatableRootXMLModel>
        <and>
            <eq>
                <ref id="ДЛИТЕЛЬНОСТЬ" meta="allen_attribute_expression">
                    <ref id="INTERVAL" meta="allen_reference"/>
                </ref>
                <value>10</value>
                <with belief="90" probability="100" accuracy="0" />
            </eq>
            <d>
                <ref id="INTERVAL1" meta="allen_reference" />
                <ref id="INTERVAL2" meta="allen_reference" />
            </d>
        </and>
    </KBEvaluatableRootXMLModel>
    """
    model = KBEvaluatableRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <KBEvaluatableLegacyRootXMLModel>
        <and>
            <eq>
                <ref id="obj">
                    <ref id="attr" />
                </ref>
                <value>10</value>
                <with belief="70" probability="80" accuracy="0" />
            </eq>
            <EvIntRel Value="d">
                <Event Name="EVENT1" />
                <Interval Name="INTERVAL1" />
            </EvIntRel>
        </and>
    </KBEvaluatableLegacyRootXMLModel>
    """
    model = KBEvaluatableLegacyRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <KBEvaluatableLegacyRootXMLModel>
        <ne>
            <ref id="Пострадавший_2">
                <ref id="Степень_тяжести">
                    <with belief="50" probability="100" accuracy="0"/>
                </ref>
                <with belief="50" probability="100" accuracy="0"/>
            </ref>
            <value>Тяжелая</value>
            <with belief="50" probability="100" accuracy="0"/>
        </ne>
    </KBEvaluatableLegacyRootXMLModel>
    """

    model = KBEvaluatableLegacyRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))

    xml_data = """
    <KBEvaluatableLegacyRootXMLModel>
        <and>
            <ne>
                <ref id="Пострадавший_2">
                    <ref id="Степень_тяжести">
                        <with belief="50" probability="100" accuracy="0"/>
                    </ref>
                    <with belief="50" probability="100" accuracy="0"/>
                </ref>
                <value>Очень_тяжелая</value>
                <with belief="50" probability="100" accuracy="0"/>
            </ne>
            <and>
                <ne>
                    <ref id="Пострадавший_2">
                        <ref id="Степень_тяжести">
                            <with belief="50" probability="100" accuracy="0"/>
                        </ref>
                        <with belief="50" probability="100" accuracy="0"/>
                    </ref>
                    <value>Тяжелая</value>
                    <with belief="50" probability="100" accuracy="0"/>
                </ne>
                <ne>
                    <ref id="Пострадавший_2">
                        <ref id="Степень_тяжести">
                            <with belief="50" probability="100" accuracy="0"/>
                        </ref>
                        <with belief="50" probability="100" accuracy="0"/>
                    </ref>
                    <value>Средняя</value>
                    <with belief="50" probability="100" accuracy="0"/>
                </ne>
            </and>
        </and>
    </KBEvaluatableLegacyRootXMLModel>
    """

    model = KBEvaluatableLegacyRootXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))
