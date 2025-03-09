import logging
import re
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
class KBClass(LegacyMixin, SimpleClass):
    properties: Optional[List["PropertyDefinition"]] = field(default_factory=list)
    rules: Optional[List[KBRule]] = field(default_factory=list)

    def __post_init__(self):
        super().__post_init__()
        self.rules = self.rules or []
        self.properties = self.properties or []
        if self.group:
            self.group = re.sub(r"\W", "_", self.group)

    @property
    def attrs(self) -> dict:
        return {
            "id": self.id,
            "desc": self.desc or self.id,
            "group": self.group or "ГРУППА1",
        }

    @property
    def legacy_attrs(self):
        return self.attrs

    def get_inner_xml(self, *args, **kwargs) -> List[Element] | Iterable[Element]:
        properties = Element("properties")
        for p in self.properties:
            properties.append(p.get_xml(*args, **kwargs))
        if self.rules:
            rules = Element("rules")
            for r in self.rules:
                rules.append(r.get_xml(*args, **kwargs))
            return [properties, rules]
        return [properties]

    @property
    def legacy_inner_xml(self) -> List[Element]:
        return self.get_inner_xml(legacy=True)

    @property
    def inner_krl(self):
        krl = f"""    АТРИБУТЫ{self.properties_krl}"""
        if self.rules:
            krl += f"""
    ПРАВИЛА{self.rules_krl}"""
        return krl

    @property
    def properties_krl(self) -> str:
        indent = " " * 4
        properties_krl = ""
        for p in self.properties:
            property_krl_lines = p.krl.split("\n")
            property_krl = "\n".join([indent + line for line in property_krl_lines])
            properties_krl += "\n" + property_krl
        return properties_krl

    @property
    def rules_krl(self) -> str:
        indent = " " * 4
        rules_krl = "\n"
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
    meta: Literal["type_or_class"] = field(init=False, default="type_or_class")
    target: Union[KBType, KBClass] = field(default=None, init=False, metadata={"serialize": False})
    ref: None = field(init=False)

    @property
    def attrs(self) -> dict:
        result = super().attrs
        result["meta"] = self.meta
        return result


@dataclass(kw_only=True)
class PropertyDefinition(LegacyMixin, KBEntity):  # LegacyMixin для совместимости со старым АТ-РЕШАТЕЛЕМ
    tag: Literal["property"] = field(init=False, default="property")
    id: str
    type: TypeOrClassReference
    desc: Optional[str] = field(default=None)
    value: Optional[SimpleEvaluatable] = field(default=None)
    source: Optional[str] = field(default="asked")
    question: Optional[str] = field(default=None)
    query: Optional[str] = field(default=None)

    legacy_tag: Literal["property"] = field(init=False, default="property", metadata={"serialize": False})

    def __post_init__(self):
        if isinstance(self.type, str):
            self.type = TypeOrClassReference(id=self.type)

    def get_krl(self, *args, **kwargs):
        krl = f"""АТРИБУТ {self.id}
    ТИП {self.type.krl}"""
        if self.value:
            krl += f"""
    ЗНАЧЕНИЕ
        {self.value.krl}"""

        krl += f"""
    КОММЕНТАРИЙ {self.desc or self.id}"""
        return krl

    @property
    def attrs(self):
        result = {"id": self.id, "type": self.type.krl, "desc": self.desc or self.id, "source": self.source}
        if not self.value:
            result["create"] = "true"
        return result

    @property
    def legacy_attrs(self):
        return self.attrs

    def get_inner_xml(self, *args, **kwargs):
        if kwargs.get("legacy"):
            return self.legacy_inner_xml
        result = []
        if self.value:
            value = Element("value")
            value.append(self.value.xml)
            result.append(value)
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
            value = Element("value")
            value.append(self.value.xml)
            result.append(value)
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
class KBInstance(LegacyMixin, KBEntity):
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
        return {"id": self.id, "type": self.type.krl, "desc": self.desc or self.id, "create": str(self.create).lower()}

    @property
    def legacy_attrs(self) -> dict:
        return {"id": self.id, "type": self.type.krl, "desc": self.desc or self.id, "create": str(self.create).lower()}

    def get_inner_xml(self, *args, **kwargs) -> List[Element]:
        if kwargs.get("legacy"):
            return self.legacy_inner_xml
        result = []
        if self.value:
            value = Element("value")
            value.append(self.value.xml)
            result.append(value)
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
            value = Element("value")
            value.append(self.value.xml)
            result.append(value)
        if self.properties:
            properties = Element("properties")
            for prop in self.properties:
                properties.append(prop.get_xml(legacy=True))
            result.append(properties)
        return result

    def get_krl(self, *args, **kwargs) -> str:
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
    definition: PropertyDefinition = field(init=False, metadata={"serialize": False})
