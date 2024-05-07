from xml.etree.ElementTree import Element
from at_krl.core.kb_class import KBClass
from at_krl.core.temporal.utils import SimpleEvaluatable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class KBEvent(KBClass):
    occurance_condition: SimpleEvaluatable = None

    def __init__(self, id: str, occurance_condition: SimpleEvaluatable, desc: str = None) -> None:
        super().__init__(id, [], [], group='СОБЫТИЕ', desc=desc)
        self.occurance_condition = occurance_condition
        self.occurance_condition.owner = self
        self.tag = 'Event'

    @property
    def attrs(self) -> dict:
        return {'Name': self.id}

    @property
    def inner_xml(self) -> Element:
        formula = Element('Formula')
        formula.append(self.occurance_condition.xml)
        return formula

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('properties', None)
        res.pop('rules', None)
        res.pop('id', None)
        res['Formula'] = self.occurance_condition.__dict__()
        return res

    @property
    def inner_krl(self):
        return f"""АТРИБУТЫ
АТРИБУТ УслВозн
ТИП ЛогВыр
ЗНАЧЕНИЕ 
{self.occurance_condition.krl}
"""

    @staticmethod
    def from_xml(xml: Element) -> 'KBEvent':
        return KBEvent(
            id=xml.attrib.get('Name'),
            occurance_condition=SimpleEvaluatable.from_xml(
                xml.find('Formula')[0]),
            desc=xml.attrib.get('desc', None),
        )

    @staticmethod
    def from_dict(d: dict):
        return KBEvent(
            id=d.get('Name'),
            occurance_condition=SimpleEvaluatable.from_dict(d.get('Formula')),
            desc=d.get('desc', None),
        )

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.occurance_condition.validate(kb)
            self._validated = True

    @property
    def xml_owner_path(self):
        from at_krl.core.knowledge_base import KnowledgeBase
        owner: KnowledgeBase = self.owner
        return owner.xml_owner_path + f'/IntervalsAndEvents/Events/Event[{owner.classes.events.index(self)}]'