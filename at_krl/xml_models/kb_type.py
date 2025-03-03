from typing import Literal
from typing import Optional

from pydantic_xml import attr
from pydantic_xml import element

from at_krl.core.kb_type import KBNumericType
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel


class KBTypeXMLModel(KBEntityXMLModel, tag="type"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)


class KBNumericTypeXMLModel(KBTypeXMLModel):
    from_: float = element(tag="from")
    to_: float = element(tag="to")
    meta: Literal["numeric", "number"] = attr()

    def get_data(self, context: Context):
        result = super().get_data(context)
        result.pop("meta")
        return result

    def build_target(self, data, context: Context):
        result = KBNumericType(**data)
        if context.kb:
            context.kb.types.append(result)
        return result


if __name__ == "__main__":
    xml_data = """
    <type id="age" meta="number">
        <from>18</from>
        <to>65</to>
    </type>
    """
    model = KBNumericTypeXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)))
