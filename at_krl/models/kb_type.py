from typing import List
from typing import Literal
from typing import Optional

from at_krl.core.kb_type import KBFuzzyType
from at_krl.core.kb_type import KBNumericType
from at_krl.core.kb_type import KBType
from at_krl.models.fuzzy.membership_function import MembershipFunctionModel
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel


# ready
class KBTypeModel(KBEntityModel):
    id: Optional[str]
    desc: Optional[str]
    tag: Literal["type"]

    def build_target(self, data):
        return KBType(**data)


class KBNumericTypeModel(KBTypeModel):
    from_: float
    to_: float

    def build_target(self, data):
        return KBNumericType(**data)


class MFListModel(KBRootModel[List[MembershipFunctionModel]]):
    def build_target(self):
        return [p.to_internal() for p in self.root]


class KBFuzzyTypeModel(KBTypeModel):
    membership_functions: MFListModel

    def build_target(self, data):
        data["membership_functions"] = self.membership_functions.to_internal()
        return KBFuzzyType(**data)
