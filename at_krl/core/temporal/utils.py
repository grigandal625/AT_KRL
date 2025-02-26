from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from xml.etree.ElementTree import Element

from at_krl.core.kb_class import KBInstance
from at_krl.core.kb_operation import TAGS_SIGNS
from at_krl.core.kb_reference import KBReference
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.simple.simple_value import SimpleValue

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase
    from at_krl.core.kb_class import KBClass


# для обратной совместимости со старым темпоральным решателем


@dataclass(kw_only=True)
class AllenInnerEvaluatable(SimpleEvaluatable):
    pass


@dataclass(kw_only=True)
class AllenInnerValue(SimpleValue, AllenInnerEvaluatable):
    tag: Literal["TruthVal", "Number", "String"] = field(init=False)

    def __post_init__(self):
        if isinstance(self.content, bool):
            self.tag = "TruthVal"
        elif isinstance(self.content, float) or isinstance(self.content, int):
            self.tag = "Number"
        elif isinstance(self.content, str):
            self.tag = "String"
        else:
            raise ValueError(f'Unsupported content type "{type(self.content)}" of {self.content} for Allen inner value')

    @property
    def inner_xml(self) -> str:
        return None

    @property
    def attrs(self) -> dict:
        if self.tag == "TruthVal":
            return "TRUE" if self.content else "FALSE"
        return {"Value": str(self.content)}


@dataclass(kw_only=True)
class AllenInnerReference(SimpleReference, AllenInnerEvaluatable):
    tag: Literal["Attribute"] = field(init=False, default="Attribute")
    target: "KBClass" = field(default=None, init=False, repr=False)

    @property
    def attrs(self) -> dict:
        return {"Value": self.krl}

    @property
    def inner_xml(self) -> None:
        return None

    @staticmethod
    def parse(ref_str: str) -> "SimpleReference":
        return AllenInnerReference.from_simple(SimpleReference.parse(ref_str))

    @staticmethod
    def from_xml(xml: Element) -> "SimpleReference":
        ref_path = xml.attrib.get("Value")
        return AllenInnerReference.parse(ref_str=ref_path)

    def validate(self, kb: "KnowledgeBase", *args, inst: KBInstance = None, **kwargs):
        return KBReference.validate(self, kb, *args, inst=inst, **kwargs)


EQ_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "eq"]
LOG_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "log"]
AR_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "math"]

AllenInnerEvaluatable = Union[AllenInnerValue, AllenInnerReference, "AllenInnerOperation"]


@dataclass(kw_only=True)
class AllenInnerOperation(SimpleOperation, AllenInnerEvaluatable):
    tag: Literal["EqOp", "LogOp", "ArOp"] = field(init=False)
    left: AllenInnerEvaluatable
    right: Optional[AllenInnerEvaluatable] = field(default=None)

    def __post_init__(self):
        super().__post_init__()
        if self.operation_name in EQ_OPERATION_NAMES:
            self.tag = "EqOp"
        elif self.operation_name in LOG_OPERATION_NAMES:
            self.tag = "LogOp"
        elif self.operation_name in AR_OPERATION_NAMES:
            self.tag = "ArOp"
        else:
            raise ValueError(f'Unsupported sign "{self.sign}" for AllenInnerOperation')

    @property
    def attrs(self) -> dict:
        if self.tag == "LogOp":
            return {"Value": self.operation_name.upper()}
        return {"Value": self.operation_name}
