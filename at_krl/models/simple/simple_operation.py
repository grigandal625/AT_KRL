from typing import Literal
from typing import Optional

from pydantic import Field

from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel

# from at_krl.models.simple.operation_tags import TAGS_SIGNS


class SimpleOperationModel(SimpleEvaluatableModel):
    tag: Literal[
        "eq", "gt", "ge", "lt", "le", "ne", "and", "or", "not", "xor", "neg", "add", "sub", "mul", "div", "mod", "pow"
    ]
    sign: str
    left: SimpleEvaluatableModel
    right: Optional[SimpleEvaluatableModel] = Field(default=None)

    def build_target(self, data):
        data["left"] = self.left.to_internal()
        data["right"] = self.right.to_internal()

        return SimpleOperation(**data)
