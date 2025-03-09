from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.utils.context import Context


class SimpleReferenceModel(SimpleEvaluatableModel):
    tag: Literal["ref"] = Field(default="ref")
    id: str
    ref: Optional["SimpleReferenceModel"] = Field(default=None)

    def build_target(self, data, context: Context):
        if self.ref is not None:
            data["ref"] = self.ref.to_internal(context)
        return SimpleReference(**data)


SimpleReferenceModel.model_rebuild()
