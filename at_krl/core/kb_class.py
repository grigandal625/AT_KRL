import logging
from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING
from typing import Union
from xml.etree.ElementTree import Element

from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_rule import KBRule
from at_krl.core.kb_type import KBType
from at_krl.core.kb_value import Evaluatable
from at_krl.core.simple.legacy import LegacyMixin
from at_krl.core.simple.simple_class import SimpleClass
from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
from at_krl.core.simple.simple_reference import SimpleReference

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class KBClass(SimpleClass):
    properties: Optional[List["PropertyDefinition"]] = field(default_factory=list)
    rules: Optional[List[KBRule]] = field(default_factory=list)

    @property
    def attrs(self) -> dict:
        return {
            "id": self.id,
            "desc": self.desc,
            "group": self.group or "ГРУППА1",
        }

    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        properties = Element("properties")
        for p in self.properties:
            properties.append(p.xml)
        if len(self.rules):
            rules = Element("rules")
            for r in self.rules:
                rules.append(r.xml)
            return [properties, rules]
        return [properties]

    @property
    def inner_krl(self):
        krl = f"""    АТРИБУТЫ
{self.properties_krl}"""
        if self.rules:
            krl += f"""
    ПРАВИЛА
{self.rules_krl}"""
        krl += f"""
    КОММЕНТАРИЙ {self.desc or self.id}"""
        return krl

    @property
    def properties_krl(self) -> str:
        indent = " " * 4
        properties_krl = ""
        for p in self.properties:
            property_krl_lines = p.krl.split("\n")
            property_krl = "\n".join([indent + line for line in property_krl_lines])
            properties_krl += property_krl + "\n"
        return properties_krl

    @property
    def rules_krl(self) -> str:
        indent = " " * 4
        rules_krl = ""
        for r in self.rules:
            rule_krl_lines = r.krl.split("\n")
            rule_krl = "\n".join([indent + line for line in rule_krl_lines])
            rules_krl += "\n" + rule_krl + "\n"
        return rules_krl

    @property
    def xml_owner_path(self):
        owner: "KnowledgeBase" = self.owner
        if (owner.world == self) and not owner.with_world:
            return owner.xml_owner_path + f"/classes/class[{len(owner.classes.objects)}]"
        return owner.xml_owner_path + f"/classes/class[{owner.classes.objects.index(self)}]"


@dataclass(kw_only=True)
class TypeOrClassReference(SimpleReference):
    target: Union[KBType, KBClass] = field(default=None, init=False, metadata={"serialize": False})


@dataclass(kw_only=True)
class PropertyDefinition(KBEntity, LegacyMixin):  # LegacyMixin для совместимости со старым АТ-РЕШАТЕЛЕМ
    tag: Literal["property"] = field(init=False, default="property")
    id: str
    type: TypeOrClassReference
    desc: Optional[str] = field(default=None)
    value: Optional[SimpleEvaluatable] = field(default=None)
    source: Optional[str] = field(default="asked")
    question: Optional[str] = field(default=None)
    query: Optional[str] = field(default=None)

    legacy_tag: Literal["property"] = field(init=False, default="property")

    @property
    def krl(self):
        krl = f"""    АТРИБУТ {self.id}
        ТИП {self.type.target.id}"""
        if self.value:
            krl += f"""
        ЗНАЧЕНИЕ
            {self.value.krl}"""

        krl += f"""
        КОММЕНТАРИЙ {self.desc or self.id}"""
        return krl

    @property
    def attrs(self):
        return {"id": self.id, "desc": self.desc, "source": self.source}

    @property
    def legacy_attrs(self):
        return {"id": self.id, "type": self.type.krl, "desc": self.desc, "source": self.source}

    @property
    def inner_xml(self):
        type_element = Element("type")
        type_element.append(self.type.xml)
        result = [type_element]
        if self.value:
            result.append(self.value.xml)
        if self.question:
            question = Element("question")
            question.text = self.question
            result.append(question)
        if self.query:
            query = Element("query")
            query.text = self.query
            result.append(query)
        return result

    @property
    def legacy_inner_xml(self):
        result = []
        if self.value:
            result.append(self.value.xml)
        if self.question:
            question = Element("question")
            question.text = self.question
            result.append(question)
        if self.query:
            query = Element("query")
            query.text = self.query
            result.append(query)
        return result

    @property
    def legacy_available(self):
        return True


@dataclass(kw_only=True)
class KBInstance(KBEntity, LegacyMixin):
    tag: Literal["instance"] = field(init=False, default="instance")
    id: str
    type: TypeOrClassReference
    desc: Optional[str] = field(default=None)
    value: Optional[Evaluatable] = field(default=None)
    create: bool = field(default=True)
    properties: Optional[List["KBProperty"]] = field(default_factory=list)

    legacy_tag: Literal["instance"] = field(init=False, default="instance", metadata={"serialize": False})

    @property
    def attrs(self) -> dict:
        return {"id": self.id, "desc": self.desc, "create": self.create}

    @property
    def legacy_attrs(self) -> dict:
        return {"id": self.id, "type": self.type.krl, "desc": self.desc, "create": self.create}

    @property
    def inner_xml(self) -> List[Element]:
        type_element = Element("type")
        type_element.append(self.type.xml)
        result = [type_element]
        if self.value:
            result.append(self.value.xml)
        if self.properties:
            properties = Element("properties")
            for prop in self.properties:
                properties.append(prop.xml)
            result.append(properties)
        return result

    @property
    def legacy_inner_xml(self) -> List[Element]:
        result = []
        if self.value:
            result.append(self.value.xml)
        if self.properties:
            properties = Element("properties")
            for prop in self.properties:
                properties.append(prop.xml)
            result.append(properties)
        return result

    @property
    def krl(self) -> str:
        krl = f"""ЭКЗЕМПЛЯР {self.id}
ТИП {self.type.id}"""
        if self.value:
            krl += f"""
ЗНАЧЕНИЕ
    {self.value.krl}"""

        if self.properties:
            krl += f"""
АТРИБУТЫ
{self.properties_krl}"""

        krl += f"""
КОММЕНТАРИЙ {self.desc or self.id}"""
        return krl

    @property
    def properties_krl(self) -> str:
        indent = " " * 4
        properties_krl = ""
        for prop in self.properties:
            property_krl_lines = prop.krl.split("\n")
            property_krl = "\n".join([indent + line for line in property_krl_lines])
            properties_krl += property_krl + "\n"
        return properties_krl


@dataclass(kw_only=True)
class KBProperty(KBInstance):
    tag: Literal["property"] = field(init=False, default="property")
    legacy_tag: Literal["property"] = field(init=False, default="property", metadata={"serialize": False})
    definition: PropertyDefinition = property(init=False, metadata={"serialize": False})
