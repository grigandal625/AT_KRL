from typing import Any
from typing import Optional

from pydantic import Field

from at_krl.core.kb_value import KBValue
from at_krl.models.non_factor import NonFactorModel
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.simple.simple_value import SimpleValueModel
from at_krl.utils.context import Context


class EvaluatableModel(SimpleEvaluatableModel):
    non_factor: Optional[NonFactorModel] = Field(default=None)

    def build_target(self, data, context: Context):
        raise NotImplementedError("Not implemented")


class KBValueModel(EvaluatableModel, SimpleValueModel):
    content: Any

    def get_data(self, context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return KBValue(**data)
