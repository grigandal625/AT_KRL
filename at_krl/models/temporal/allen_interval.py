from typing import Literal
from typing import Union

from at_krl.core.temporal.allen_interval import KBInterval
from at_krl.models.simple.simple_operation import SimpleOperationModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.models.simple.simple_value import SimpleValueModel
from at_krl.models.temporal.allen_class import AllenClassModel
from at_krl.utils.context import Context


class KBIntervalModel(AllenClassModel):
    tag: Literal["interval"]
    open: Union[SimpleValueModel, SimpleReferenceModel, SimpleOperationModel]
    close: Union[SimpleValueModel, SimpleReferenceModel, SimpleOperationModel]

    def get_data(self, context):
        data = super().get_data(context)
        data["open"] = self.open.to_internal(context)
        data["close"] = self.close.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        result = KBInterval(**data)
        if context.kb:
            context.kb.classes.intervals.append(result)
        return result
