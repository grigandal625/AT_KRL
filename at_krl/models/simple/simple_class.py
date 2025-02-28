from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.models.kb_entity import KBEntityModel


class SimpleClassModel(KBEntityModel):
    tag: Literal["class"] = Field(default="class")
    id: str
    group: Optional[str] = Field(default=None)
    desc: Optional[str] = Field(default=None)

    def build_target(self):
        raise NotImplementedError()
