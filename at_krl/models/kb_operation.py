from typing import TYPE_CHECKING

from at_krl.models.kb_value import EvaluatableModel
from at_krl.models.simple.simple_operation import SimpleOperationModel

if TYPE_CHECKING:
    pass


class KBOperationModel(EvaluatableModel, SimpleOperationModel):
    pass
