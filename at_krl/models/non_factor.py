from typing import Literal

from at_krl.core.non_factor import NonFactor
from at_krl.models.kb_entity import KBEntityModel


# check tag
class NonFactorModel(KBEntityModel):
    tag: Literal["with"]
    belief: float
    probability: float
    accuracy: float

    def build_target(self, data):
        return NonFactor(**data)
