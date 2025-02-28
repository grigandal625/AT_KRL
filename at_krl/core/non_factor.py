from dataclasses import dataclass
from dataclasses import field
from typing import Literal

from at_krl.core.kb_entity import KBEntity


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

    @property
    def is_default(self):
        return self.belief == 50 and self.probability == 100 and self.accuracy == 0

    @property
    def attrs(self) -> dict:
        return {"belief": str(self.belief), "probability": str(self.probability), "accuracy": str(self.accuracy)}

    @property
    def krl(self) -> str:
        return f"УВЕРЕННОСТЬ [{self.belief}; {self.probability}] ТОЧНОСТЬ {self.accuracy}"

    @property
    def xml_owner_path(self):
        return self.owner.xml_owner_path + "/with"
