from typing import List
from typing import Literal
from typing import Optional

from at_krl.core.kb_type import KBFuzzyType
from at_krl.core.kb_type import KBNumericType
from at_krl.core.kb_type import KBSymbolicType
from at_krl.core.kb_type import KBType
from at_krl.models.fuzzy.membership_function import MembershipFunctionModel
from at_krl.models.kb_entity import KBEntityModel
from at_krl.models.kb_entity import KBRootModel
from at_krl.utils.context import Context


class KBTypeModel(KBEntityModel):
    id: Optional[str]
    desc: Optional[str]
    tag: Literal["type"]

    def build_target(self, data, context: Context):
        return KBType(**data)


class KBNumericTypeModel(KBTypeModel):
    from_: float
    to_: float

    def build_target(self, data, context: Context):
        result = KBNumericType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result


class KBSymbolicTypeModel(KBTypeModel):
    values: List[str]
    meta: Literal["string"]

    def build_target(self, data, context: Context):
        result = KBSymbolicType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result


class MFListModel(KBRootModel[List[MembershipFunctionModel]]):
    def build_target(self):
        return [p.to_internal() for p in self.root]


class KBFuzzyTypeModel(KBTypeModel):
    membership_functions: MFListModel

    def build_target(self, data, context: Context):
        data["membership_functions"] = self.membership_functions.to_internal()
        result = KBFuzzyType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result
