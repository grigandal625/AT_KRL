from typing import Literal
from typing import Optional, List

from pydantic_xml import attr
from pydantic_xml import element

from at_krl.core.kb_type import KBNumericType, KBSymbolicType, KBFuzzyType
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.fuzzy.membership_function import MembershipFunctionXMLModel


class KBTypeXMLModel(KBEntityXMLModel, tag="type"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    meta: str = attr()

    def get_data(self, context: Context):
        result = super().get_data(context)
        result.pop("meta", None)
        return result


class KBNumericTypeXMLModel(KBTypeXMLModel):
    from_: float = element(tag="from")
    to_: float = element(tag="to")
    meta: Literal["numeric", "number"] = attr()

    def build_target(self, data, context: Context):
        result = KBNumericType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result


class KBSymbolicTypeXMLModel(KBTypeXMLModel):
    meta: Literal["string", "symbolic"] = attr()
    values: List[str] = element(tag="value")

    def build_target(self, data, context: Context):
        result = KBSymbolicType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result


class KBFuzzyTypeXMLModel(KBTypeXMLModel):
    meta: Literal["fuzzy"] = attr()
    membership_functions: List[MembershipFunctionXMLModel] = element()

    def build_target(self, data, context: Context):
        data['membership_functions'] = [
            f.to_internal(context=context.create_child('membership_functions').create_child(i)) 
            for i, f in enumerate(self.membership_functions)
        ]
        return KBFuzzyType(**data)
