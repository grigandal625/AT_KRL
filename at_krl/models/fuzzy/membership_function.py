from typing import List
from typing import Literal

from at_krl.core.fuzzy.membership_function import MembershipFunction
from at_krl.core.fuzzy.membership_function import MFPoint
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.utils.context import Context


class MFPointModel(KBEntityModel):
    tag: Literal["point"]
    x: float
    y: float

    def build_target(self, data, context: Context):
        return MFPoint(**data)


class MFPointListModel(KBRootModel[List[MFPointModel]]):
    def to_internal(self, context: Context):
        return [p.to_internal(context) for p in self.root]


class MembershipFunctionModel(KBEntityModel):
    tag: Literal["parameter"]
    name: str
    min: float
    max: float
    points: MFPointListModel

    def get_data(self, context):
        data = super().get_data(context)
        data["points"] = self.points.to_internal(context)
        return data

    def build_target(self, data, context: Context):
        return MembershipFunction(**data)
