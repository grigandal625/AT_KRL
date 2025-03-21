from dataclasses import dataclass
from dataclasses import field
from typing import Literal

from at_krl.core.kb_entity import KBEntity
from at_krl.utils.numbers import to_number_or_str


def num(v):
    i = int(v)
    f = float(v)

    if i == f:
        return i
    return f


@dataclass(kw_only=True)
class NonFactor(KBEntity):
    tag: Literal["with"] = field(init=False, default="with")
    belief: float = field(default=50)
    probability: float = field(default=100)
    accuracy: float = field(default=0)

    def __post_init__(self):
        self.belief = to_number_or_str(self.belief)
        if self.belief is None:
            self.belief = 50
        self.probability = to_number_or_str(self.probability)
        if self.probability is None:
            self.probability = 100
        self.accuracy = to_number_or_str(self.accuracy)
        if self.accuracy is None:
            self.accuracy = 0

    @property
    def is_default(self):
        return self.belief == 50 and self.probability == 100 and self.accuracy == 0

    @property
    def not_default_krl(self):
        if self.is_default:
            return ""
        return " " + self.krl

    @property
    def attrs(self) -> dict:
        return {"belief": str(self.belief), "probability": str(self.probability), "accuracy": str(self.accuracy)}

    def get_krl(self, *args, **kwargs) -> str:
        return f"УВЕРЕННОСТЬ [{self.belief}; {self.probability}] ТОЧНОСТЬ {self.accuracy}"

    @property
    def xml_owner_path(self):
        return self.owner.xml_owner_path + "/with"
