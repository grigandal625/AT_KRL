from xml.etree.ElementTree import Element
from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_rule import KBRule
from at_krl.core.kb_value import Evaluatable
from typing import Iterable, List, Union


class KBClass(KBEntity):
    id: str = None
    desc: str = None
    properties: List['KBProperty'] = None
    rules: List[KBRule] = None
    group: str = None

    def __init__(self, id: str, properties: List['KBProperty'], rules: List[KBRule] = None, group: str = None, desc: str = None):
        self.id = id
        self.desc = desc or id
        self.properties = properties
        self.rules = rules or []
        self.tag = 'class'
        self.group = group or 'ГРУППА1'

    @property
    def attrs(self) -> dict:
        return {
            'id': self.id,
            'desc': self.desc,
        }

    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        properties = Element('properties')
        for p in self.properties:
            properties.append(p.xml)
        if len(self.rules):
            rules = Element('rules')
            for r in self.rules:
                rules.append(r.xml)
            return [properties, rules]
        return [properties]

    def __dict__(self) -> dict:
        return dict(
            **(super().__dict__()),
            **(self.attrs),
            properties=[p.__dict__() for p in self.properties],
            rules=[r.__dict__() for r in self.rules],
        )

    @property
    def krl(self) -> str:
        group = self.group or 'ГРУППА1'

        return f"""ОБЪЕКТ {self.id}
ГРУППА {group}
{self.inner_krl}КОММЕНТАРИЙ {self.desc}
"""

    @property
    def inner_krl(self):
        properties_krl = "АТРИБУТЫ\n" + \
            '\n'.join([p.krl for p in self.properties])
        rules_krl = (
            "ПРАВИЛА\n" + '\n'.join([r.krl for r in self.rules]) + '\n') if len(self.rules) else ''
        return properties_krl + '\n' + rules_krl

    @staticmethod
    def from_xml(xml: Element) -> 'KBClass':
        id = xml.attrib.get('id')
        desc = xml.attrib.get('desc', id)
        properties = []
        ps = xml.find('properties')
        if ps:
            properties = [KBProperty.from_xml(p) for p in ps]
        rules = []
        rs = xml.find('rules')
        if rs:
            rules = [KBRule.from_xml(r) for r in rs]
        return KBClass(id, properties, rules=rules, desc=desc)

    @staticmethod
    def from_dict(d: dict):
        id = d.get('id')
        desc = d.get('desc', id)
        properties = [KBProperty.from_dict(p) for p in d.get('properties', [])]
        rules = [KBRule.from_dict(r) for r in d.get('rules', [])]
        return KBClass(id, properties, rules, desc=desc)


class KBInstance(KBEntity):
    id: str = None
    type_or_class_id: str = None
    desc: str = None
    value: Evaluatable = None

    def __init__(self, id: str, type_or_class_id: str, desc: str = None, value: Evaluatable = None) -> None:
        self.id = id
        self.type_or_class_id = type_or_class_id
        self.desc = desc or id
        self.tag = 'instance'
        self.value = value

    @property
    def attrs(self) -> dict:
        return {
            'id': self.id,
            'type': self.type_or_class_id,
            'desc': self.desc
        }

    @property
    def krl(self) -> str:
        value_krl = ''
        if self.value:
            value_krl = f'\nЗНАЧЕНИЕ\n{self.value.krl}'
        return f"""{self.krl_type} {self.id}
ТИП {self.type_or_class_id}{value_krl}
КОММЕНТАРИЙ {self.desc}"""

    @property
    def krl_type(self):
        return "ЭКЗЕМПЛЯР"

    @property
    def inner_xml(self) -> Element | None:
        if self.value is None:
            return None
        return self.value.xml

    def __dict__(self) -> dict:
        res = dict(**(self.attrs), **(super().__dict__()))
        if self.value is not None:
            res['value'] = self.value.__dict__()
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'KBInstance':
        value = None
        if xml.find('value'):
            value = Evaluatable.from_xml(xml.find('value'))
        return KBInstance(
            id=xml.attrib.get("id"),
            type_or_class_id=xml.attrib.get("type"),
            desc=xml.attrib.get("desc", None),
            value=value,
        )

    @staticmethod
    def from_dict(d: dict) -> 'KBInstance':
        value = None
        if d.get('value', None) is not None:
            value = Evaluatable.from_dict(d.get('value'))
        return KBInstance(
            id=d.get("id"),
            type_or_class_id=d.get("type"),
            desc=d.get("desc", None),
            value=value
        )


class KBProperty(KBInstance):
    source: str = None

    def __init__(self, id: str, type_or_class_id: str, desc: str = None, source: str = None, value: Evaluatable = None) -> None:
        super().__init__(id, type_or_class_id, desc=desc, value=value)
        self.tag = 'property'
        self.source = source

    @property
    def attrs(self) -> dict:
        return dict(**(super().attrs), source=self.source or 'asked')

    @property
    def krl_type(self):
        return "АТРИБУТ"

    @staticmethod
    def from_xml(xml: Element) -> 'KBProperty':
        value = None
        if xml.find('value') is not None:
            value = Evaluatable.from_xml(xml.find('value'))
        return KBProperty(
            id=xml.attrib.get("id"),
            type_or_class_id=xml.attrib.get("type"),
            desc=xml.attrib.get("desc"),
            source=xml.attrib.get("source"),
            value=value,
        )

    @staticmethod
    def from_dict(d: dict) -> 'KBProperty':
        value = None
        if d.get('value', None) is not None:
            value = Evaluatable.from_dict(d.get('value'))
        return KBProperty(
            id=d.get("id"),
            type_or_class_id=d.get("type"),
            desc=d.get("desc"),
            source=d.get("source"),
            value=value
        )
