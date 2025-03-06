from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
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
    ref: None = field(init=False, metadata={"serialize": False}, default=None)
    index: Optional["Evaluatable"] = field(default=None)
    target: "AllenClass" = field(init=False, metadata={"serialize": False}, default=None)
    meta: Literal["allen_reference"] = field(init=False, default="allen_reference")

    legacy_tag: Literal["Event", "Interval"] = field(init=False, metadata={"serialize": False})

    def __post_init__(self):
        if self.index:
            self.index.owner = self

    @property
    def attrs(self) -> dict:
        result = super().attrs
        result["meta"] = self.meta
        return result

    def get_inner_xml(self, *args, **kwargs) -> Element:
        if kwargs.get('legacy'):
            return self.legacy_inner_xml
        result = super().get_inner_xml(*args, **kwargs)
        if self.index:
            index_element = Element("index")
            index_element.append(self.index.xml)
            result.append(index_element)
        return result

    @property
    def legacy_attrs(self) -> dict:
        return {"Name": self.id}

    @property
    def legacy_inner_xml(self) -> None:
        return None

    @property
    def legacy_available(self) -> bool:
        return hasattr(self, "legacy_tag") and self.legacy_tag in ['Event', 'Interval']

    def validate_legacy_tag(self):
        if self.target:
            self.legacy_tag = self.target.legacy_tag

    @property
    def xml_owner_path(self) -> str:
        if self.index:
            return f"{self.owner.xml_owner_path}/{self.id}[{self.index.krl}]"
        return f"{self.owner.xml_owner_path}/{self.id}"

    def get_krl(self, *args, **kwargs) -> str:
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
