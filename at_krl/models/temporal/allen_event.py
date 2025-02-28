from typing import Literal

from at_krl.core.temporal.allen_event import KBEvent
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.temporal.allen_class import AllenClassModel


class KBEventModel(AllenClassModel):
    tag: Literal["event"]
    occurance_condition: SimpleEvaluatableModel
    group: Literal["СОБЫТИЕ"]

    def build_target(self, data):
        data["occurance_condition"] = self.occurance_condition.to_internal()
        return KBEvent(**data)
