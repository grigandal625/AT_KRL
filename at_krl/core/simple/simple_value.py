import json
from dataclasses import dataclass
from dataclasses import field
from logging import getLogger
from typing import Any
from typing import Literal

from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable

logger = getLogger(__name__)


@dataclass(kw_only=True)
class SimpleValue(SimpleEvaluatable):
    tag: Literal["value"] = field(default="value", init=False)
    content: Any

    legacy_tag: Literal["TruthVal", "Number", "String"] = field(
        init=False, default=None
    )  # для совместимости со старым темпоральным решателем

    def __post_init__(self):
        if isinstance(self.content, bool):
            self.legacy_tag = "TruthVal"
        elif isinstance(self.content, float) or isinstance(self.content, int):
            self.legacy_tag = "Number"
        elif isinstance(self.content, str):
            self.legacy_tag = "String"
        else:
            logger.warning(f'Unsupported content type "{type(self.content)}" of {self.content} for legacy value')

    @property
    def legacy_available(self) -> bool:
        return self.legacy_tag in ["TruthVal", "Number", "String"]

    @property
    def legacy_inner_xml(self) -> str:
        return None

    @property
    def legacy_attrs(self) -> dict:
        return {"Value": str(self.content)}

    def get_krl(self, *args, **kwargs) -> str:
        return json.dumps(self.content, ensure_ascii=False)

    @property
    def inner_xml(self) -> str:
        if isinstance(self.content, bool):
            return str(self.content).lower()
        return str(self.content)

    def to_simple(self) -> "SimpleValue":
        return SimpleValue(content=self.content)

    @staticmethod
    def from_simple(v: "SimpleValue") -> "SimpleValue":
        return SimpleValue(content=v.content)
