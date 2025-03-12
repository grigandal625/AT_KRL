from typing import Literal
from typing import Optional
from typing import Union

from pydantic import Field

from at_krl.core.kb_operation import KBOperation
from at_krl.core.temporal.allen_attribute_expression import AllenAttributeExpression
from at_krl.core.temporal.allen_operation import AllenOperation
from at_krl.core.temporal.allen_reference import AllenReference
from at_krl.models.kb_reference import KBReferenceModel
from at_krl.models.kb_value import EvaluatableModel
from at_krl.models.kb_value import KBValueModel
from at_krl.models.simple.simple_operation import SimpleOperationModel
from at_krl.models.simple.simple_reference import SimpleReferenceModel
from at_krl.models.temporal.allen_evaluatable import AllenEvaluatableModel
from at_krl.utils.context import Context


class KBOperationModel(EvaluatableModel, SimpleOperationModel):
    tag: Literal[
        "eq", "gt", "ge", "lt", "le", "ne", "and", "or", "not", "xor", "neg", "add", "sub", "mul", "div", "mod", "pow"
    ]
    left: Union[
        KBValueModel, "AllenAttributeExpressionModel", KBReferenceModel, "KBOperationModel", "AllenOperationModel"
    ]
    right: Optional[
        Union[
            KBValueModel, "AllenAttributeExpressionModel", KBReferenceModel, "KBOperationModel", "AllenOperationModel"
        ]
    ] = Field(default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.non_factor:
            data["non_factor"] = self.non_factor.to_internal(context.create_child("non_factor"))
        return data

    def build_target(self, data, context):
        return KBOperation(**data)


class AllenReferenceModel(SimpleReferenceModel, AllenEvaluatableModel):
    index: Optional[
        Union[KBValueModel, "AllenAttributeExpressionModel", KBReferenceModel, KBOperationModel, "AllenOperationModel"]
    ] = Field(default=None)
    meta: Literal["allen_reference"]
    ref: None = Field(default=None)

    def get_data(self, context):
        data = super().get_data(context)
        data.pop("meta", None)
        if self.index:
            data["index"] = self.index.to_internal(context.create_child("index"))
        data.pop("ref", None)
        return data

    def build_target(self, data, context):
        result = AllenReference(**data)
        if context.kb:
            interval = context.kb.get_interval_by_id(result.id)
            event = context.kb.get_event_by_id(result.id)
            if interval and event:
                raise ValueError(f"Found both interval and event with id {result.id}")
            if not event and not interval:
                raise ValueError(f"No event or interval found with id {result.id}")
            result.target = interval or event
            result.validate_legacy_tag()
        return result


class AllenAttributeExpressionModel(SimpleReferenceModel, AllenEvaluatableModel):
    ref: AllenReferenceModel
    id: Literal["ДЛИТЕЛЬНОСТЬ", "КОЛ_ВОЗН", "КОЛ_НАЧ", "КОЛ_ОКОНЧ", "ТАКТ_НАЧ", "ТАКТ_ОКОНЧ", "ТАКТ_ВОЗН"]
    meta: Literal["allen_attribute_expression"]

    def get_data(self, context):
        data = super().get_data(context)
        data["ref"] = self.ref.to_internal(context)
        data.pop("meta", None)
        return data

    def build_target(self, data, context: Context):
        return AllenAttributeExpression(**data)


class AllenOperationModel(SimpleOperationModel, AllenEvaluatableModel):
    tag: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]
    left: AllenReferenceModel
    right: AllenReferenceModel
    # sign: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]

    def build_target(self, data, context: Context):
        return AllenOperation(**data)


KBOperationModel.model_rebuild()
AllenReferenceModel.model_rebuild()
AllenAttributeExpressionModel.model_rebuild()
AllenOperationModel.model_rebuild()
