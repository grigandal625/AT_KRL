from typing import Literal

from at_krl.core.temporal.allen_operation import AllenOperation
from at_krl.models.simple.simple_operation import SimpleOperationModel
from at_krl.models.temporal.allen_reference import AllenReferenceModel
from at_krl.utils.context import Context


class AllenOperationModel(SimpleOperationModel):
    tag: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]
    left: AllenReferenceModel
    right: AllenReferenceModel
    sign: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]

    def build_target(self, data, context: Context):
        data["left"] = self.left.to_internal(context)
        data["right"] = self.right.to_internal(context)
        return AllenOperation(**data)
