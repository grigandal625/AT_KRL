from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Literal
from xml.etree.ElementTree import Element

from at_krl.core.kb_entity import KBEntity


@dataclass(kw_only=True)
class MFPoint(KBEntity):
    tag: Literal["point"] = field(init=False, default_factory="point")
    x: float | int = field(default=None)
    y: float | int = field(default=None)

    @property
    def attrs(self) -> dict:
        return dict(x=str(self.x), y=str(self.y), **super().attrs)

    @property
    def krl(self) -> str:
        return f"{self.x}|{self.y}"


@dataclass(kw_only=True)
class MembershipFunction(KBEntity):
    tag: Literal["parameter"] = field(init=False, default="parameter")
    points: List[MFPoint] = field(default_factory=list)
    name: str
    min: float
    max: float

    def __post_init__(self):
        for point in self.points:
            point.owner = self

    @property
    def attrs(self) -> dict:
        res = super().attrs
        res["min-value"] = str(self.min)
        res["max-value"] = str(self.max)
        return res

    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        value = Element("value")
        value.text = self.name
        mf = Element("mf")
        for point in self.points:
            mf.append(point.xml)
        return [value, mf]

    @property
    def krl(self) -> str:
        points_krl = "={" + "; ".join([p.krl for p in self.points]) + "}"
        return f'"{self.name}" {self.min} {self.max} {len(self.points)} {points_krl}'
