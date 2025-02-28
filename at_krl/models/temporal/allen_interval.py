from typing import Literal

from at_krl.core.temporal.allen_interval import KBInterval
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.temporal.allen_class import AllenClassModel


class KBIntervalModel(AllenClassModel):
    tag: Literal["interval"]
    open: SimpleEvaluatableModel
    close: SimpleEvaluatableModel
    group: Literal["ИНТЕРВАЛ"]

    def build_target(self, data):
        data["open"] = self.open.to_internal()
        data["close"] = self.close.to_internal()
        return KBInterval(**data)
