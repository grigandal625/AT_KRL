from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
from typing import List
from typing import Optional
from xml.etree.ElementTree import Element

from at_krl.core.simple.operation_tags import TAGS_SIGNS
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable

logger = getLogger(__name__)

EQ_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "eq"]
LOG_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "log"]
AR_OPERATION_NAMES = [s for s, v in TAGS_SIGNS.items() if v.get("meta", None) == "math"]


def is_binary(left, right):
    return left is not None and right is not None


@dataclass(kw_only=True)
class SimpleOperation(SimpleEvaluatable):
    tag: str = field(init=False)
    sign: str = field(metadata={"serialize": False})
    left: SimpleEvaluatable
    right: Optional[SimpleEvaluatable] = field(default=None)
    operation_name: str = field(init=False, metadata={"serialize": False})

    def __post_init__(self):
        for op in TAGS_SIGNS:
            if self.sign in TAGS_SIGNS[op]["values"]:
                if TAGS_SIGNS[op]["is_binary"] == is_binary(self.left, self.right):
                    self.operation_name = op
                    self.tag = op
                    break

        if self.tag is None:
            raise ValueError(f"Unknown operation: {self.sign}")

        self.left.owner = self
        if self.right is not None:
            self.right.owner = self

        if self.operation_name in EQ_OPERATION_NAMES:
            self.legacy_tag = "EqOp"
        elif self.operation_name in LOG_OPERATION_NAMES:
            self.legacy_tag = "LogOp"
        elif self.operation_name in AR_OPERATION_NAMES:
            self.legacy_tag = "ArOp"
        else:
            logger.warning(f"Unknown operation {self.sign} for legacy operation {self.operation_name}")

    @property
    def legacy_available(self) -> bool:
        return self.legacy_tag in ["EqOp", "LogOp", "ArOp"]

    @property
    def legacy_inner_xml(self) -> List[Element]:
        result = [self.left.legacy_inner_xml]
        if self.is_binary:
            result.append(self.right.legacy_inner_xml)
        return result

    @property
    def legacy_attrs(self) -> dict:
        if self.legacy_tag == "LogOp":
            return {"Value": self.operation_name.upper()}
        return {"Value": self.operation_name}

    @property
    def is_binary(self):
        return is_binary(self.left, self.right)

    @property
    def inner_xml(self) -> List[Element]:
        result = [self.left.xml]
        if self.is_binary:
            result.append(self.right.xml)
        return result

    @property
    def krl(self) -> str:
        if self.is_binary:
            return f"({self.left.krl}) {self.sign} ({self.right.krl})"
        return f"{self.sign} ({self.left.krl})"

    def to_simple(self) -> "SimpleOperation":
        return SimpleOperation(self.sign, self.left.to_simple(), self.right.to_simple() if self.right else None)

    @staticmethod
    def from_simple(operation: "SimpleOperation") -> "SimpleOperation":
        return SimpleOperation(
            sign=operation.sign,
            left=operation.left.from_simple(operation.left),
            right=operation.right.from_simple(operation.right) if operation.right else None,
        )
