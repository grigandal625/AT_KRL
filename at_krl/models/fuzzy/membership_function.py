from typing import List
from typing import Literal

from at_krl.core.fuzzy.membership_function import MembershipFunction
from at_krl.core.fuzzy.membership_function import MFPoint
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel


class MFPointModel(KBEntityModel):
    tag: Literal["point"]
    x: float
    y: float

    def build_target(self, data):
        return MFPoint(**data)


class MFPointListModel(KBRootModel[List[MFPointModel]]):
    def build_target(self, data):
        return [p.to_internal() for p in self.points]


class MembershipFunctionModel(KBEntityModel):
    tag: Literal["parameter"]
    name: str
    min: float
    max: float
    points: MFPointListModel

    def build_target(self, data):
        data["points"] = self.points.to_internal()
        return MembershipFunction(**data)
