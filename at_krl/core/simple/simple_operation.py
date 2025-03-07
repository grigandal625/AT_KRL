from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
from typing import List
from typing import Literal
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

    legacy_tag: Literal["EqOp", "LogOp", "ArOp"] = field(init=False, repr=False, metadata={"serialize": False})

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
            self.legacy_tag = None

    @property
    def legacy_available(self) -> bool:
        return self.legacy_tag in ["EqOp", "LogOp", "ArOp"]

    @property
    def legacy_inner_xml(self) -> List[Element]:
        result = [self.left.get_xml(legacy=True)]
        if self.is_binary:
            result.append(self.right.get_xml(legacy=True))
        return result

    @property
    def legacy_attrs(self) -> dict:
        if self.legacy_tag == "LogOp":
            return {"Value": self.operation_name.upper()}
        return {"Value": self.operation_name}

    @property
    def is_binary(self):
        return is_binary(self.left, self.right)

    def get_inner_xml(self, *args, **kwargs) -> List[Element]:
        if kwargs.get("legacy"):
            return self.legacy_inner_xml
        result = [self.left.xml]
        if self.is_binary:
            result.append(self.right.xml)
        return result

    @property
    def original_sign(self):
        return TAGS_SIGNS[self.operation_name]["values"][0]

    def get_krl(self, *args, **kwargs) -> str:
        if self.is_binary:
            return (
                f"({self.left.get_krl(*args, **kwargs)}) {self.original_sign} ({self.right.get_krl(*args, **kwargs)})"
            )
        return f"{self.sign} ({self.left.get_krl(*args, **kwargs)})"

    def to_simple(self) -> "SimpleOperation":
        return SimpleOperation(
            sign=self.sign, left=self.left.to_simple(), right=self.right.to_simple() if self.right else None
        )

    @staticmethod
    def from_simple(operation: "SimpleOperation") -> "SimpleOperation":
        return SimpleOperation(
            sign=operation.sign,
            left=operation.left.from_simple(operation.left),
            right=operation.right.from_simple(operation.right) if operation.right else None,
        )
