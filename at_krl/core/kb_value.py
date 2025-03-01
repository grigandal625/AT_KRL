from copy import deepcopy
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Literal
from xml.etree.ElementTree import Element

from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
from at_krl.core.simple.simple_value import SimpleValue


@dataclass(kw_only=True)
class Evaluatable(SimpleEvaluatable):
    non_factor: NonFactor = field(default_factory=NonFactor)

    def __post_init__(self):
        if self.non_factor:
            self.non_factor.owner = self

    @property
    def xml(self) -> Element:
        result = super().xml
        if self.non_factor:
            result.append(self.non_factor.xml)
        return result

    def get_krl(self, *args, **kwargs):
        if self.non_factor:
            if kwargs.get("convert_default_non_factor", True):
                kwargs["convert_default_non_factor"] = False
                return f"{super().get_krl(*args, **kwargs)} {self.non_factor.krl}"
            return f"{super().get_krl(*args, **kwargs)}{self.non_factor.not_default_krl}"
        return super().get_krl(*args, **kwargs)

    @property
    def xml_owner_path(self) -> str:
        from at_krl.core.kb_rule import KBRule

        if isinstance(self.owner, KBRule):
            if self.owner.condition != self:
                raise ValueError(self._unknown_ownership)
            return self.owner.xml_owner_path + "/condition/" + self.tag

        from at_krl.core.kb_operation import KBOperation

        if isinstance(self.owner, KBOperation):
            if (self.owner.left != self) and (self.owner.right != self):
                raise ValueError(self._unknown_ownership)
            if self.owner.is_binary:
                if self.owner.left.__class__ == self.owner.right.__class__:
                    index = "0" if self.owner.left == self else "1"
                    return self.owner.xml_owner_path + "/" + self.tag + f"[{index}]"

        from at_krl.core.kb_instruction import AssignInstruction

        if isinstance(self.owner, AssignInstruction):
            if (self.owner.value != self) and (self.owner.ref != self):
                raise ValueError(self._unknown_ownership)
            if self.owner.ref.__class__ == self.owner.value.__class__:
                index = "0" if self.owner.ref == self else "1"
                return self.owner.xml_owner_path + "/" + self.tag + f"[{index}]"

        return self.owner.xml_owner_path + "/" + self.tag


@dataclass(kw_only=True)
class KBValue(Evaluatable, SimpleValue):
    tag: Literal["value"] = field(init=False, default="value")
    content: Any

    def copy(self):
        if self.non_factor is not None:
            return KBValue(
                content=deepcopy(self.content),
                non_factor=NonFactor(self.non_factor.belief, self.non_factor.probability, self.non_factor.accuracy),
            )
        return KBValue(content=deepcopy(self.content))

    @staticmethod
    def from_simple(simple_value: SimpleValue) -> "KBValue":
        return KBValue(content=simple_value.content, non_factor=NonFactor())
