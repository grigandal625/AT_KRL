from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.models.simple.simple_value import SimpleValueModel
from at_krl.utils.context import Context

# from at_krl.models.simple.operation_tags import TAGS_SIGNS


class SimpleOperationModel(SimpleEvaluatableModel):
    tag: Literal[
        "eq", "gt", "ge", "lt", "le", "ne", "and", "or", "not", "xor", "neg", "add", "sub", "mul", "div", "mod", "pow"
    ]
    sign: str
    left: Union[SimpleValueModel, SimpleReferenceModel, "SimpleOperationModel"]
    right: Optional[Union[SimpleValueModel, SimpleReferenceModel, "SimpleOperationModel"]] = Field(default=None)

    def build_target(self, data, context: Context):
        data["left"] = self.left.to_internal(context)
        data["right"] = self.right.to_internal(context)

        return SimpleOperation(**data)
