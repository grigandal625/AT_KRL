from typing import List
from typing import Literal
from typing import Optional

from pydantic import Field

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

    def get_data(self, context: Context):
        data = super().get_data(context)
        data.pop("meta")
        return data

    def build_target(self, data, context: Context):
        return KBType(**data)


class KBNumericTypeModel(KBTypeModel):
    from_: float = Field(alias="from")
    to_: float = Field(alias="to")
    meta: Literal["number"] = Field(default="number")

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
    def to_internal(self, context: Context):
        return [p.to_internal(context) for p in self.root]


class KBFuzzyTypeModel(KBTypeModel):
    membership_functions: MFListModel
    meta: Literal["fuzzy"] = Field(default="fuzzy")

    def build_target(self, data, context: Context):
        data["membership_functions"] = self.membership_functions.to_internal(context)
        result = KBFuzzyType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result
