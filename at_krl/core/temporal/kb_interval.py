from xml.etree.ElementTree import Element
from at_krl.core.kb_class import KBClass

from at_krl.core.temporal.utils import SimpleEvaluatable
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class KBInterval(KBClass):
    open: SimpleEvaluatable = None
    close: SimpleEvaluatable = None

    def __init__(self, id: str, open: SimpleEvaluatable, close: SimpleEvaluatable, desc: str = None) -> None:
        super().__init__(id, [], [], group='ИНТЕРВАЛ', desc=desc)
        self.open = open
        self.open.owner = self
        self.close = close
        self.close.owner = self
        self.tag = 'Interval'

    @property
    def attrs(self) -> dict:
        return {'Name': self.id}

    @property
    def inner_xml(self) -> List[Element]:
        open = Element('Open')
        open.append(self.open.xml)
        close = Element('Close')
        close.append(self.close.xml)
        return [open, close]

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('properties', None)
        res.pop('rules', None)
        res.pop('id', None)
        res['Open'] = self.open.__dict__()
        res['Close'] = self.close.__dict__()
        return res

    @property
    def inner_krl(self):
        return f"""АТРИБУТЫ
АТРИБУТ УслНач
ТИП ЛогВыр
ЗНАЧЕНИЕ 
{self.open.krl}
АТРИБУТ УслОконч
ТИП ЛогВыр
ЗНАЧЕНИЕ 
{self.close.krl}
"""

    @staticmethod
    def from_xml(xml: Element) -> 'KBInterval':
        return KBInterval(
            id=xml.attrib.get('Name'),
            open=SimpleEvaluatable.from_xml(
                xml.find('Open')[0]),
            close=SimpleEvaluatable.from_xml(
                xml.find('Close')[0]),
            desc=xml.attrib.get('desc', None),
        )

    @staticmethod
    def from_dict(d: dict) -> 'KBInterval':
        return KBInterval(
            id=d.get('Name'),
            open=SimpleEvaluatable.from_dict(d.get('Open')),
            close=SimpleEvaluatable.from_dict(d.get('Close')),
            desc=d.get('desc', None),
        )

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.open.validate(kb, *args, **kwargs)
            self.close.validate(kb, *args, **kwargs)
            self._validated = True

    @property
    def xml_owner_path(self):
        from at_krl.core.knowledge_base import KnowledgeBase
        owner: KnowledgeBase = self.owner
        return owner.xml_owner_path + f'/IntervalsAndEvents/Intervals/Interval[{owner.classes.intervals.index(self)}]'