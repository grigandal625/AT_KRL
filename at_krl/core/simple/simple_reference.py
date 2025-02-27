from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from typing import Optional
from xml.etree.ElementTree import Element

from at_krl.core.kb_entity import KBEntity
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable


@dataclass(kw_only=True)
class SimpleReference(SimpleEvaluatable):
    tag: Literal["ref"] = field(default="ref", init=False)
    id: str
    ref: "SimpleReference" = field(default=None)

    target: KBEntity = field(default=None, init=False, metadata={"serialize": False})

    legacy_tag: Literal["Attribute"] = field(
        init=False, default="Attribute"
    )  # для совместимости со старым темпоральным решателем

    def __post_init__(self):
        if self.ref:
            self.ref.owner = self

    @property
    def krl(self) -> str:
        if self.ref:
            return f"{self.id}.{self.ref.krl}"
        return self.id

    @property
    def legacy_attrs(self) -> dict:
        return {"Value": self.krl}

    @property
    def legacy_inner_xml(self):
        return None

    @property
    def legacy_available(self) -> bool:
        return True

    @property
    def attrs(self) -> dict:
        return {"id": self.id}

    @property
    def inner_xml(self) -> Optional[Element]:
        if self.ref:
            return self.ref.xml

    @property
    def fullfiled(self) -> bool:
        return self.target is not None

    def to_simple(self) -> "SimpleReference":
        return SimpleReference(id=self.id, ref=self.ref.to_simple() if self.ref else None)

    @staticmethod
    def from_simple(ref: "SimpleReference") -> "SimpleReference":
        return SimpleReference(
            id=ref.id,
            ref=SimpleReference.from_simple(ref.ref) if ref.ref else None,
        )

    @staticmethod
    def parse(ref_str: str) -> "SimpleReference":
        if ref_str == "":
            return None
        elif "." in ref_str:
            return SimpleReference(
                ref_str[: ref_str.index(".")], SimpleReference.parse(ref_str[ref_str.index(".") + 1 :])
            )
        else:
            return SimpleReference(ref_str)
