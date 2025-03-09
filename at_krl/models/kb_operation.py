from typing import Optional
from typing import TYPE_CHECKING
from typing import Union

from pydantic import Field

from at_krl.core.kb_operation import KBOperation
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import EvaluatableModel
from at_krl.models.kb_value import KBValueModel
from at_krl.models.simple.simple_operation import SimpleOperationModel

if TYPE_CHECKING:
    pass


class KBOperationModel(EvaluatableModel, SimpleOperationModel):
    left: Union[KBValueModel, KBReferenceModel, "KBOperationModel"]
    right: Optional[Union[KBValueModel, KBReferenceModel, "KBOperationModel"]] = Field(default=None)

    def build_target(self, data, context):
        data["left"] = self.left.to_internal(context.create_child("left"))
        if self.right:
            data["right"] = self.right.to_internal(context.create_child("right"))
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))

        return KBOperation(**data)
