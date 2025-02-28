from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
from typing import Any
from typing import Literal
from typing import Optional
from xml.etree.ElementTree import Element

from at_krl.core.kb_value import Evaluatable
from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.temporal.allen_class import AllenClass
from at_krl.core.temporal.allen_evaluatable import AllenEvaluatable

logger = getLogger(__name__)


@dataclass(kw_only=True)
class AllenReference(SimpleReference, AllenEvaluatable):
    ref: Any = field(init=False, metadata={"serialize": False}, default=None)
    index: Optional["Evaluatable"] = field(default=None)
    target: "AllenClass" = field(init=False, metadata={"serialize": False})
    meta: Literal["allen_reference"] = field(init=False, default="allen_reference")

    def __post_init__(self):
        if self.index:
            self.index.owner = self

    @property
    def attrs(self) -> dict:
        result = super().attrs
        result["meta"] = self.meta
        return result

    @property
    def inner_xml(self) -> Element:
        result = super().inner_xml
        if self.index:
            index_element = Element(tag="index")
            index_element.append(self.index.xml)
            result.append(index_element)
        return result

    @property
    def xml_owner_path(self) -> str:
        if self.index:
            return f"{self.owner.xml_owner_path}/{self.id}[{self.index.krl}]"
        return f"{self.owner.xml_owner_path}/{self.id}"

    @property
    def krl(self) -> str:
        if self.index:
            return f"{self.id}[{self.index.krl}]"
        return self.id

    @staticmethod
    def from_simple(ref: "SimpleReference") -> "AllenReference":
        return AllenReference(id=ref.id)

    def to_simple(self) -> "SimpleReference":
        if self.index:
            logger.warning("Index will be lost after converting AllenReference to simple reference")
        return super().to_simple()
