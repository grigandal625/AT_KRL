from xml.etree.ElementTree import Element
from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_rule import KBRule
from at_krl.core.kb_value import Evaluatable, KBValue
from at_krl.core.kb_type import KBType
from typing import Iterable, List, Union, TYPE_CHECKING

from at_krl.exceptions.kb_exception import KBValidationError

import logging

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase

logger = logging.getLogger(__name__)


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
        for prop in self.properties:
            prop.owner_class = self
        self.rules = rules or []
        for rule in self.rules:
            rule.owner = self
        self.tag = 'class'
        self.group = group or 'ГРУППА1'

    @property
    def attrs(self) -> dict:
        return {
            'id': self.id,
            'desc': self.desc,
            'group': self.group or 'ГРУППА1',
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
        group = xml.attrib.get('desc', id)
        properties = []
        ps = xml.find('properties')
        if ps:
            properties = [KBProperty.from_xml(p) for p in ps]
        rules = []
        rs = xml.find('rules')
        if rs:
            rules = [KBRule.from_xml(r) for r in rs]
        return KBClass(id, properties, rules=rules, desc=desc, group=group)

    @staticmethod
    def from_dict(d: dict):
        id = d.get('id')
        desc = d.get('desc', id)
        group = d.get('group', 'ГРУППА1')
        properties = [KBProperty.from_dict(p) for p in d.get('properties', [])]
        rules = [KBRule.from_dict(r) for r in d.get('rules', [])]
        return KBClass(id, properties, rules, desc=desc, group=group)

    def validate_properties(self, kb: 'KnowledgeBase'):
        for prop in self.properties:
            prop.validate(kb, self)

    def validate_rules(self, kb: 'KnowledgeBase'):
        if self.rules:
            inst = self.create_instance(
                kb, self.id + '_instance', self.desc, ignore_validation=True)
            for rule in self.rules:
                rule.validate(kb, inst=inst)

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.validate_properties(kb)
            self.validate_rules(kb)
            self._validated = True

    def create_instance(self, kb: 'KnowledgeBase', _id: str, desc: str = None, source: str = None, as_property: bool = False, ignore_validation: bool = False) -> Union['KBInstance', 'KBProperty']:
        if (not self._validated) and (not ignore_validation):
            self.validate(kb)

        if as_property:
            inst = KBProperty(_id, self.id, desc, source)
        else:
            inst = KBInstance(_id, self.id, desc=desc)
        inst.value = KBValue(id(inst))
        inst._type_or_class = self
        inst._validated = True
        for prop in self.properties:
            if prop.is_type_instance:
                prop_inst = KBProperty(
                    prop.id, prop.type_or_class_id, prop.desc, prop.source, prop.value)
            elif prop.is_class_instance:
                prop_inst = prop._type_or_class.create_instance(
                    kb, prop.id, prop.desc, prop.source, as_property=True, ignore_validation=ignore_validation)
            prop_inst._type_or_class = prop.type_or_class
            prop_inst.owner_class = self
            prop_inst.owner = inst
            prop_inst._validated = True

            inst.properties_instances.append(prop_inst)
        return inst

    @property
    def xml_owner_path(self):
        from at_krl.core.knowledge_base import KnowledgeBase
        owner: KnowledgeBase = self.owner
        if (owner.world == self) and not owner.with_world:
            return owner.xml_owner_path + f'/classes/class[{len(owner.classes.objects)}]'
        return owner.xml_owner_path + f'/classes/class[{owner.classes.objects.index(self)}]'

class KBInstance(KBEntity):
    id: str = None
    type_or_class_id: str = None
    _type_or_class: Union['KBType', KBClass] = None
    desc: str = None
    value: Evaluatable = None
    properties_instances: List['KBProperty'] = None

    def __init__(self, id: str, type_or_class_id: str, desc: str = None, value: Evaluatable = None) -> None:
        self.id = id
        self.type_or_class_id = type_or_class_id
        self.desc = desc or id
        self.tag = 'instance'
        self.value = value
        self.properties_instances = []  # наполнятся при валидации

    @property
    def attrs(self) -> dict:
        return {
            'id': self.id,
            'type': self.type_or_class_id,
            'desc': self.desc
        }

    @property
    def type_or_class(self) -> Union['KBType', KBClass, None]:
        return self._type_or_class

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
    def inner_xml(self) -> List[Element] | None:
        if self.value is None:
            return None
        
        prop_inst_xml = Element("properties_instances")
        for prop in self.properties_instances:
            prop_inst_xml.append(prop.xml)
        return [self.value.xml, prop_inst_xml]

    def __dict__(self) -> dict:
        res = dict(**(self.attrs), **(super().__dict__()))
        if self.value is not None:
            res['value'] = self.value.__dict__()
        res['properties_instances'] = []
        for prop in self.properties_instances:
            res['properties_instances'].append(prop.__dict__())
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'KBInstance':
        value = None
        if xml.find('value'):
            value = Evaluatable.from_xml(xml.find('value'))
        res = KBInstance(
            id=xml.attrib.get("id"),
            type_or_class_id=xml.attrib.get("type"),
            desc=xml.attrib.get("desc", None),
            value=value,
        )
        if xml.find('properties_instances'):
            for prop_inst_xml in xml.find('properties_instances'):
                prop_inst = KBProperty.from_xml(prop_inst_xml)
                res.properties_instances.append(prop_inst)
        return res

    @staticmethod
    def from_dict(d: dict) -> 'KBInstance':
        value = None
        if d.get('value', None) is not None:
            value = Evaluatable.from_dict(d.get('value'))
        res = KBInstance(
            id=d.get("id"),
            type_or_class_id=d.get("type"),
            desc=d.get("desc", None),
            value=value
        )
        for prop_inst_dict in d.get("properties_instances", []):
            prop_inst = KBProperty.from_dict(prop_inst_dict)
            res.properties_instances.append(prop_inst)
        return res

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            for t in kb.types:
                if t.id == self.type_or_class_id:
                    self._type_or_class = t
                    if (self.value is not None) and (not self._type_or_class.validate_value(self.value)):
                        self._validated = False
                    else:
                        self._validated = True
                    if not self._validated:
                        msg = f'"{self.id}" Failed on {self.tag} validation'
                        logger.warning(msg)
                        if kb._raise_on_validation:
                            raise KBValidationError(msg, kb_entity=self)
                    return

            if self.type_or_class_id == 'world':
                self._validate_by_obj(kb.world, kb)
            else:
                for obj in kb.classes.objects:
                    self._validate_by_obj(obj, kb)

            if not self._validated:
                msg = f'Failed validation on {self.tag} "{self.id}"'
                logger.warning(msg)
                if kb._raise_on_validation:
                    raise KBValidationError(msg, kb_entity=self)

    def _validate_by_obj(self, obj: 'KBClass', kb: 'KnowledgeBase'):
        if obj.id == self.type_or_class_id:
            self._type_or_class = obj
            if not obj._validated:
                obj.validate_properties(kb)
            for prop in obj.properties:
                having_prop_instances = [p for p in self.properties_instances if p.id == prop.id]
                if len(having_prop_instances) == 1:
                    having_prop = having_prop_instances[0]
                    having_prop.owner_class = self._type_or_class
                    having_prop.owner = self
                    having_prop.validate(kb)
                elif len(having_prop_instances) > 1:
                    msg = f"Found more than one property instance \"{prop.id}\""
                    logger.warning(msg)
                    if kb._raise_on_validation:
                        raise KBValidationError(msg, kb_entity=self)
                else:
                    if prop.is_type_instance:
                        prop_inst = KBProperty(
                            prop.id, prop.type_or_class_id, prop.desc, prop.source, prop.value)
                    elif prop.is_class_instance:
                        prop_inst = prop._type_or_class.create_instance(
                            kb, prop.id, prop.desc, prop.source, as_property=True)
                    prop_inst.owner_class = self._type_or_class
                    prop_inst.owner = self
                    prop_inst._validated = True
                    self.properties_instances.append(prop_inst)
            self._validated = True

    @property
    def is_type_instance(self):
        return isinstance(self._type_or_class, KBType)

    @property
    def is_class_instance(self):
        return isinstance(self._type_or_class, KBClass)


class KBProperty(KBInstance):
    source: str = None
    # устанавливается при валидации или в конструкторе родительского класса
    owner_class: KBClass = None
    # устанавливается при вызове create_instance родительского класса
    owner: KBInstance = None

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
        res = KBProperty(
            id=xml.attrib.get("id"),
            type_or_class_id=xml.attrib.get("type"),
            desc=xml.attrib.get("desc"),
            source=xml.attrib.get("source"),
            value=value,
        )
        if xml.find('properties_instances'):
            for prop_inst_xml in xml.find('properties_instances'):
                prop_inst = KBProperty.from_xml(prop_inst_xml)
                res.properties_instances.append(prop_inst)
        return res

    @staticmethod
    def from_dict(d: dict) -> 'KBProperty':
        value = None
        if d.get('value', None) is not None:
            value = Evaluatable.from_dict(d.get('value'))
        res = KBProperty(
            id=d.get("id"),
            type_or_class_id=d.get("type"),
            desc=d.get("desc"),
            source=d.get("source"),
            value=value
        )
        for prop_inst_dict in d.get("properties_instances", []):
            prop_inst = KBProperty.from_dict(prop_inst_dict)
            res.properties_instances.append(prop_inst)
        return res
    
    @property
    def xml_owner_path(self):
        idx = self.owner_class.properties.index(self)
        return self.owner_class.xml_owner_path + f'/properties/property[{idx}]'
