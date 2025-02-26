from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from typing import Optional

from at_krl.core.kb_entity import KBEntity


@dataclass(kw_only=True)
class SimpleClass(KBEntity):
    tag: Literal["class"] = field(init=False, default="class")
    id: str
    group: Optional[str] = field(default=None)
    desc: Optional[str] = field(default=None)

    def __post_init__(self):
        self.desc = self.desc or self.id

    @property
    def attrs(self) -> dict:
        return {'id': self.id, 'desc': self.desc, 'group': self.group}
