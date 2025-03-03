from dataclasses import dataclass
from typing import Any
from typing import Literal

from at_krl.core.kb_value import KBValue
from at_krl.models.non_factor import NonFactorModel
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.simple.simple_value import SimpleValueModel
from at_krl.utils.context import Context


class EvaluatableModel(SimpleEvaluatableModel):
    non_factor: NonFactorModel

    def build_target(self, data, context: Context):
        raise NotImplementedError()


@dataclass
class KBValueModel(EvaluatableModel, SimpleValueModel):
    tag: Literal["value"]
    content: Any

    def build_target(self, data, context: Context):
        return KBValue(**data)
