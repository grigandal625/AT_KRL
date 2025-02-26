from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from xml.etree.ElementTree import Element

from at_krl.core.kb_entity import KBEntity
from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.temporal.allen_evaluatable import AllenEvaluatable
from at_krl.core.temporal.allen_reference import AllenReference


@dataclass(kw_only=True)
class FutureEvaluatingObject(KBEntity):
    name: Literal[
        "DURATION", "OCCURANCE_COUNT", "OPEN_COUNT", "CLOSE_COUNT", "OPENT_TACT", "CLOSE_TACT", "OCCURANCE_TACT"
    ]


NAME_TO_ID = {
    "ДЛИТЕЛЬНОСТЬ": "DURATION",
    "КОЛ_ВОЗН": "OCCURANCE_COUNT",
    "КОЛ_НАЧ": "OPEN_COUNT",
    "КОЛ_ОКОНЧ": "CLOSE_COUNT",
    "ТАКТ_НАЧ": "OPEN_TACT",
    "ТАКТ_ОКОНЧ": "CLOSE_TACT",
    "ТАКТ_ВОЗН": "OCCURANCE_TACT",
}


@dataclass(kw_only=True)
class AllenAttributeExpression(SimpleReference, AllenEvaluatable):
    ref: AllenReference = field(repr=False)
    id: Literal["ДЛИТЕЛЬНОСТЬ", "КОЛ_ВОЗН", "КОЛ_НАЧ", "КОЛ_ОКОНЧ", "ТАКТ_НАЧ", "ТАКТ_ОКОНЧ", "ТАКТ_ВОЗН"]
    meta: Literal["allen_attribute_expression"] = field(init=False, default="allen_attribute_expression")

    def __post_init__(self):
        self.ref.owner = self
        self.target = FutureEvaluatingObject(NAME_TO_ID[self.id])

    @property
    def krl(self) -> str:
        return f"{self.ref.krl}.{self.id}"

    @property
    def attrs(self) -> dict:
        result = super().attrs
        result["meta"] = self.meta
        return result

    @property
    def inner_xml(self) -> Element:
        result = super().inner_xml
        result.append(self.ref.xml)
        return result

    def to_simple(self) -> SimpleReference:
        return SimpleReference(
            id=self.ref.to_simple().id,
            ref=SimpleReference(id=self.id),
        )

    @staticmethod
    def from_simple(ref: SimpleReference) -> "AllenAttributeExpression":
        return AllenAttributeExpression(id=ref.id, ref=AllenReference(id=ref.id))
