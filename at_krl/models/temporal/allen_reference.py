from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.models.kb_reference import KBReferenceModel  # ?
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.models.temporal.allen_evaluatable import AllenEvaluatableModel


class AllenReferenceModel(SimpleReferenceModel, AllenEvaluatableModel):
    index: Optional[KBReferenceModel]  # ?
    meta: Literal["allen_reference"] = Field(default="allen_reference")

    def build_target(self, data):
        data["index"] = self.index.to_internal()
        return AllenReference(**data)
