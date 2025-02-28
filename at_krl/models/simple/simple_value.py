from typing import Any
from typing import Literal

from pydantic import Field

from at_krl.core.simple.simple_value import SimpleValue
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel


class SimpleValueModel(SimpleEvaluatableModel):
    tag: Literal["value"] = Field(default="value")
    content: Any

    def build_target(self, data):
        return SimpleValue(**data)
