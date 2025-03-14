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

    @property
    def xml_owner_path(self) -> str:
        from at_krl.core.simple.simple_operation import SimpleOperation

        if isinstance(self.owner, SimpleOperation):
            subpath = "/left/" if self.owner.left is self else "/right/"
            return self.owner.xml_owner_path + subpath + self.tag
        return self.owner.xml_owner_path + "/" + self.tag
