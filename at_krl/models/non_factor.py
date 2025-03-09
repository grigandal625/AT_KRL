import json
from typing import Literal

from at_krl.core.non_factor import NonFactor
from at_krl.models.kb_entity import KBEntityModel
from at_krl.utils.context import Context


# check tag
class NonFactorModel(KBEntityModel):
    tag: Literal["with"]
    belief: float
    probability: float
    accuracy: float

    def build_target(self, data, context: Context):
        return NonFactor(**data)


if __name__ == "__main__":
    json_data = """
    {"non_factor": {
        "tag": "with",
        "belief": 0.8,
        "probability": 0.7,
        "accuracy": 0.9
    }
    }
    """

    data = json.loads(json_data)

    numeric_type_model = NonFactorModel(**data["non_factor"])

    context = Context(name="test", kb=None)

    non_factor = numeric_type_model.to_internal(context)

    print(non_factor.krl)
