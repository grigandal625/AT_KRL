from typing import List
from typing import Optional

from pydantic_xml import attr
from pydantic_xml import element
from pydantic_xml import wrapped

from at_krl.core.kb_class import KBClass
from at_krl.core.kb_class import PropertyDefinition
from at_krl.core.kb_class import TypeOrClassReference
from at_krl.utils.context import Context
from at_krl.xml_models.kb_entity import KBEntityXMLModel
from at_krl.xml_models.kb_operation import KBEvaluatableRootXMLModel
from at_krl.xml_models.kb_rule import KBRuleLegacyXMLModel
from at_krl.xml_models.kb_rule import KBRuleXMLModel
from at_krl.xml_models.simple.simple_class import SimpleClassXMLModel


class PropertyDefinitionXMLModel(KBEntityXMLModel, tag="property"):
    id: str = attr()
    desc: Optional[str] = attr(default=None)
    type: str = attr()
    source: Optional[str] = attr(default="asked")
    value: Optional[KBEvaluatableRootXMLModel] = element(tag="value", default=None)
    question: Optional[str] = element(tag="question", default=None)
    query: Optional[str] = element(tag="query", default=None)

    def get_data(self, context: Context):
        data = super().get_data(context)
        data["type"] = TypeOrClassReference(id=self.type)
        if context.kb:
            data["type"].target = context.kb.get_type_by_id(data["type"].id)
        if self.value:
            data["value"] = self.value.to_internal(context.create_child("value"))
        return data

    def build_target(self, data, context: Context):
        return PropertyDefinition(**data)


class KBClassXMLModel(SimpleClassXMLModel, tag="class"):
    group: Optional[str] = attr(default=None)
    properties: Optional[List[PropertyDefinitionXMLModel]] = wrapped("properties", element(default=None))
    rules: Optional[List[KBRuleXMLModel]] = wrapped("rules", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.properties:
            data["properties"] = [prop.to_internal(context.create_child("property")) for prop in self.properties]
        if self.rules:
            data["rules"] = [rule.to_internal(context.create_child("rule")) for rule in self.rules]
        return data

    def build_target(self, data, context: Context):
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.objects.append(result)
            result.owner = context.kb
        return result


class KBClassLegacyXMLModel(KBEntityXMLModel, tag="class"):
    id: str = attr()
    group: Optional[str] = attr(default=None)
    desc: Optional[str] = attr(default=None)
    properties: Optional[List[PropertyDefinitionXMLModel]] = wrapped("properties", element(default=None))
    rules: Optional[List[KBRuleLegacyXMLModel]] = wrapped("rules", element(default=None))

    def get_data(self, context: Context):
        data = super().get_data(context)
        if self.properties:
            data["properties"] = [prop.to_internal(context.create_child("property")) for prop in self.properties]
        if self.rules:
            data["rules"] = [rule.to_internal(context.create_child("rule")) for rule in self.rules]
        return data

    def build_target(self, data, context: Context):
        result = KBClass(**data)
        if context.kb:
            context.kb.classes.objects.append(result)
            result.owner = context.kb
        return result


if __name__ == "__main__":
    xml_data = """
    <class id="КЛАСС_Пострадавший_1" desc="Пострадавший_1" group="Пострадавший_1">
        <properties>
            <property id="Состояние" type="Состояния" desc="Состояние" source="asked"/>
            <property id="Степень_тяжести" type="Степень_тяжести" desc="Степень_тяжести" source="asked"/>
            <property id="Тип_травмы" type="Типы_травм" desc="Тип_травмы" source="asked"/>
            <property id="Приоритет_пострадавшего" type="Степень_приоритета" desc="Приоритет_пострадавшего"
            source="asked"/>
        </properties>
    </class>
    """

    model = KBClassXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)

    model = KBClassLegacyXMLModel.from_xml(xml_data)
    print(model.to_internal(context=Context(name="test", kb=None)).krl)
