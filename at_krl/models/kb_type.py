import json
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


if __name__ == "__main__":
    json_data = """
    {
    "numeric_type": {
        "tag": "type",
        "id": "numeric_type_1",
        "desc": "A numeric type example",
        "from": 0.0,
        "to": 100.0,
        "meta": "number"
    },
    "symbolic_type": {
        "tag": "type",
        "id": "symbolic_type_1",
        "desc": "A symbolic type example",
        "values": ["Low", "Medium", "High"],
        "meta": "string"
    },
    "fuzzy_type": {
        "tag": "type",
        "id": "fuzzy_type_1",
        "desc": "A fuzzy type example",
        "meta": "fuzzy",
        "membership_functions": [
            {
                "tag": "parameter",
                "name": "Low",
                "min": 0.0,
                "max": 50.0,
                "points": [
                    {
                        "tag": "point",
                        "x": 0.0,
                        "y": 1.0
                    },
                    {
                        "tag": "point",
                        "x": 50.0,
                        "y": 0.0
                    }
                ]
            },
            {
                "tag": "parameter",
                "name": "Medium",
                "min": 30.0,
                "max": 70.0,
                "points": [
                    {
                        "tag": "point",
                        "x": 30.0,
                        "y": 0.0
                    },
                    {
                        "tag": "point",
                        "x": 50.0,
                        "y": 1.0
                    },
                    {
                        "tag": "point",
                        "x": 70.0,
                        "y": 0.0
                    }
                ]
            },
            {
                "tag": "parameter",
                "name": "High",
                "min": 50.0,
                "max": 100.0,
                "points": [
                    {
                        "tag": "point",
                        "x": 50.0,
                        "y": 0.0
                    },
                    {
                        "tag": "point",
                        "x": 100.0,
                        "y": 1.0
                    }
                ]
            }
        ]
    }
    }
    """

    data = json.loads(json_data)

    numeric_type_model = KBNumericTypeModel(**data["numeric_type"])
    symbolic_type_model = KBSymbolicTypeModel(**data["symbolic_type"])
    fuzzy_type_model = KBFuzzyTypeModel(**data["fuzzy_type"])

    context = Context(name="test", kb=None)

    numeric_type = numeric_type_model.to_internal(context)
    symbolic_type = symbolic_type_model.to_internal(context)
    fuzzy_type = fuzzy_type_model.to_internal(context)

    print(numeric_type.krl)
    print(symbolic_type.krl)
    print(fuzzy_type.krl)
