from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel


class SimpleReferenceModel(SimpleEvaluatableModel):
    tag: Literal["ref"] = Field(default="ref")
    id: str
    ref: Optional["SimpleReferenceModel"] = Field(default=None)

    def build_target(self, data):
        if self.ref is not None:
            data["ref"] = self.ref.to_internal()
        return SimpleReference(**data)
