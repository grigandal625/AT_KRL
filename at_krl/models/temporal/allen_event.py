from typing import Literal

from at_krl.core.temporal.allen_event import KBEvent
from at_krl.models.simple.simple_evaluatable import SimpleEvaluatableModel
from at_krl.models.temporal.allen_class import AllenClassModel
from at_krl.utils.context import Context


class KBEventModel(AllenClassModel):
    tag: Literal["event"]
    occurance_condition: SimpleEvaluatableModel
    group: Literal["СОБЫТИЕ"]

    def build_target(self, data, context: Context):
        data["occurance_condition"] = self.occurance_condition.to_internal(context)
        result = KBEvent(**data)
        if context.kb:
            context.kb.classes.events.append(result)
        return result
