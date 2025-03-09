from typing import Literal
from typing import Union

from at_krl.core.temporal.allen_event import KBEvent
from at_krl.models.simple.simple_operation import SimpleOperationModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.models.simple.simple_value import SimpleValueModel
from at_krl.models.temporal.allen_class import AllenClassModel
from at_krl.utils.context import Context


class KBEventModel(AllenClassModel):
    tag: Literal["event"]
    occurance_condition: Union[SimpleValueModel, SimpleReferenceModel, SimpleOperationModel]

    def get_data(self, context):
        data = super().get_data(context)
        data["occurance_condition"] = self.occurance_condition.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        result = KBEvent(**data)
        if context.kb:
            context.kb.classes.events.append(result)
        return result
