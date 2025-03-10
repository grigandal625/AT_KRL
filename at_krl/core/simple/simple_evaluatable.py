from dataclasses import dataclass

from at_krl.core.kb_entity import KBEntity
from at_krl.core.simple.legacy import LegacyMixin


@dataclass(kw_only=True)
class SimpleEvaluatable(LegacyMixin, KBEntity):
    def to_simple(self) -> "SimpleEvaluatable":
        raise NotImplementedError("Not implemented")

    @staticmethod
    def from_simple(v: "SimpleEvaluatable") -> "SimpleEvaluatable":
        raise NotImplementedError("Not implemented")
