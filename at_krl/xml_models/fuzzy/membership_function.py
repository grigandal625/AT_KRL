from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.utils.context import Context

from typing import Literal
from typing import Optional, List

from pydantic_xml import attr
from pydantic_xml import element, wrapped
from at_krl.core.fuzzy.membership_function import MFPoint, MembershipFunction


class MFPointXMLModel(KBEntityXMLModel, tag="point"):
    x: float = attr()
    y: float = attr()

    def build_target(self, data, context: Context):
        return MFPoint(**data)


class MembershipFunctionXMLModel(KBEntityXMLModel, tag="parameter"):
    name: str = element(tag="value")
    min: float = attr(name="min-value")
    max: float = attr(name="max-value")
    points: List[MFPointXMLModel] = wrapped('mf', element())

    def build_target(self, data, context: Context):
        data["points"] = [
            p.to_internal(context=context.create_child("point").create_child(i)) 
            for i, p in enumerate(self.points)
        ]
        return MembershipFunction(**data)

