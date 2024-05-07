from xml.etree.ElementTree import Element
from at_krl.core.temporal.kb_event import KBEvent, KBClass
from at_krl.core.temporal.kb_interval import KBInterval
from at_krl.core.kb_operation import KBOperation
from at_krl.core.non_factor import NonFactor
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


TEMPORAL_TAGS_SIGNS = {
    # default: interval_interval: True, event_event: False, event_interval: False
    "b": {'event_event': True, 'event_interval': True},
    "bi": {},
    "m": {},
    "mi": {},
    "s": {'event_interval': True},
    "si": {},
    "f": {},
    "fi": {},
    "d": {'event_interval': True},
    "di": {},
    "o": {},
    "oi": {},
    "e": {'event_event': True},
    "a": {'interval_interval': False, 'event_interval': True},
}


class KBAllenOperation(KBOperation):
    _left: str = None
    _right: str = None
    _left_kb: KBEvent | KBInterval = None
    _right_kb: KBEvent | KBInterval = None

    def __init__(self, sign: str, left: str | KBEvent | KBInterval, right: str | KBEvent | KBInterval, events: List[KBEvent] | None = None, intervals: List[KBInterval] | None = None, rel_type: str = None):
        if sign not in TEMPORAL_TAGS_SIGNS:
            raise ValueError(f'Invalid temporal operation sign "{sign}"')

        self.op = sign
        self.convert_non_factor = False

        self.non_factor = NonFactor()
        self.non_factor.initialized = False

        if isinstance(left, str) or isinstance(right, str):
            if isinstance(left, KBClass):
                self._left = left.id
            else:
                self._left = left

            if isinstance(right, KBClass):
                self._right = right.id
            else:
                self._right = right

            self._right = right
            self.tag = rel_type

            if self.tag in ['EvRel', 'IntRel', 'EvIntRel']:
                self.validate_tag(events, intervals)

            # Если неизвестная операция
            else:
                # попытаемся определить по знаку
                for_what_matrix = list(self.for_what.values())
                if for_what_matrix.count(True) == 1:
                    if self.for_what.get('interval_interval'):
                        self.tag = 'IntRel'
                    elif self.for_what.get('event_event'):
                        self.tag = 'EvRel'
                    elif self.for_what.get('event_interval'):
                        self.tag = 'EvIntRel'
                    if events is not None and intervals is not None:
                        self.validate_tag(events, intervals)
                # если не вышло, пытаемся достать события и интервалы по ИД и определить тип операции
                elif events is not None and intervals is not None:
                    self.get_tag_by_events_and_intervals(
                        sign=sign, events=events, intervals=intervals)
                # если и теперь не вышло, то тип операции определим во время валидации БЗ

        elif isinstance(left, KBInterval) and isinstance(right, KBInterval):
            if self.for_what.get('interval_interval'):
                self.tag = 'IntRel'
                self._build_validated(left, right)
            else:
                raise ValueError(
                    f'Can not apply operation "{self.op}" to interval-interval in {left.id} {self.op} {right.id}')

        elif isinstance(left, KBEvent) and isinstance(right, KBEvent):
            if self.for_what.get('event_event'):
                self.tag = 'EvRel'
                self._build_validated(left, right)
            else:
                raise ValueError(
                    f'Can not apply operation "{self.op}" to event-event in {left.id} {self.op} {right.id}')

        elif isinstance(left, KBEvent) and isinstance(right, KBInterval):
            if self.for_what.get('event_interval'):
                self.tag = 'EvIntRel'
                self._build_validated(left, right)
            else:
                raise ValueError(
                    f'Can not apply operation "{self.op}" to event-interval in {left.id} {self.op} {right.id}')
        else:
            raise ReferenceError('Expected types (str, str) or (KBEvent, KBEvent) or (KBInterval, KBInterval)' +
                                 f' or (KBEvent, KBInterval) for (left, right) but recieved ({type(left)}, {type(right)})')

    def _build_validated(self, left: KBEvent | KBInterval, right: KBEvent | KBInterval):
        self._left_kb = left
        self._right_kb = right
        self._left = left.id
        self._right = right.id
        self._validated = True

    def get_tag_by_events_and_intervals(self, sign: str = None, events: List[KBEvent] | None = None, intervals: List[KBInterval] | None = None):
        sign = sign or self.op
        if events is not None and intervals is not None:
            event_ids = [e.id for e in events]
            interval_ids = [i.id for i in intervals]

            if self._left in event_ids and self._right in event_ids:
                if self.for_what.get('event_event'):
                    self.tag = 'EvRel'
                    self._left_kb = [
                        e for e in events if e.id == self._left][0]
                    self._right_kb = [
                        e for e in events if e.id == self._right][0]
                else:
                    raise ValueError(
                        f'Can not apply operation {self._left} {sign} {self._right} (event-event)')
            elif self._left in event_ids and self._right in interval_ids:
                if self.for_what.get('event_interval'):
                    self.tag = 'EvIntRel'
                    self._left_kb = [
                        e for e in events if e.id == self._left][0]
                    self._right_kb = [
                        i for i in intervals if i.id == self._right][0]
                else:
                    raise ValueError(
                        f'Can not apply operation {self._left} {sign} {self._right} (event-interval)')
            elif self._left in interval_ids and self._right in interval_ids:
                if self.for_what.get('interval_interval'):
                    self.tag = 'IntRel'
                    self._left_kb = [
                        i for i in intervals if i.id == self._left][0]
                    self._right_kb = [
                        i for i in intervals if i.id == self._right][0]
                else:
                    raise ValueError(
                        f'Can not apply operation {self._left} {sign} {self._right} (interval-interval)')
            else:
                raise ReferenceError(
                    f'Expected (event, event) or (interval, interval) or (event, interval) for ({self._left}, {self._right}) in operation {self._left} {sign} {self._right}')

            self._validated = True

    def validate_tag(self, events: List[KBEvent] | None = None, intervals: List[KBInterval] | None = None):
        if events is None or intervals is None:
            return
        event_ids = [e.id for e in events]
        interval_ids = [i.id for i in intervals]
        if (self.tag == 'IntRel'):
            if (self._left not in interval_ids) or (self._right not in interval_ids):
                raise ReferenceError(
                    f'Expected (interval, interval) for ({self._left}, {self._right}) in operation {self._left} {self.op} {self._right}')
            self._left_kb = [i for i in intervals if i.id == self._left][0]
            self._right_kb = [i for i in intervals if i.id == self._right][0]
        elif (self.tag == 'EvRel'):
            if ((self._left not in event_ids) or (self._right not in event_ids)):
                raise ReferenceError(
                    f'Expected (event, event) for ({self._left}, {self._right}) in operation {self._left} {self.op} {self._right}')
            self._left_kb = [e for e in events if e.id == self._left][0]
            self._right_kb = [e for e in events if e.id == self._right][0]
        elif (self.tag == 'EvIntRel'):
            if ((self._left not in event_ids) or (self._right not in interval_ids)):
                raise ReferenceError(
                    f'Expected (event, interval) for ({self._left}, {self._right}) in operation {self._left} {self.op} {self._right}')
            self._left_kb = [e for e in events if e.id == self._left][0]
            self._right_kb = [i for i in intervals if i.id == self._right][0]

        self._validated = True

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.validate_tag(kb.classes.events, kb.classes.intervals)

    @property
    def for_what(self) -> dict:
        _for_what = TEMPORAL_TAGS_SIGNS.get(self.op)
        for_what = {}
        for_what['interval_interval'] = _for_what.get('interval_interval', True)
        for_what['event_event'] = _for_what.get('event_event', False)
        for_what['event_interval'] = _for_what.get('event_interval', False)
        return for_what

    @property
    def sign(self):
        return self.op

    @property
    def inner_krl(self):
        return f"{self._left} {self.sign} {self._right}"

    @property
    def attrs(self) -> dict:
        return {'Value': self.op}

    @property
    def left_tag(self) -> str:
        if self.left:
            return self.left.tag
        if (self.tag == 'EvRel') or (self.tag == 'EvIntRel'):
            return 'Event'
        elif self.tag == 'IntRel':
            return 'Interval'

    @property
    def right_tag(self):
        if self.right:
            return self.right.tag
        if (self.tag == 'IntRel') or (self.tag == 'EvIntRel'):
            return 'Interval'
        elif self.tag == 'EvRel':
            return 'Event'

    @property
    def inner_xml(self) -> List[Element]:
        left = Element(self.left_tag)
        left.attrib['Name'] = self._left

        right = Element(self.right_tag)
        right.attrib['Name'] = self._right

        return [left, right]

    def __dict__(self) -> dict:
        res = {'tag': self.tag}
        res['Value'] = self.sign
        res['left'] = {'tag': self.left_tag, 'Name': self._left}
        res['right'] = {'tag': self.right_tag, 'Name': self._right}
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'KBAllenOperation':
        rel_type = xml.tag
        left = xml[0].attrib.get('Name')
        right = xml[1].attrib.get('Name')
        sign = xml.attrib.get('Value')
        return KBAllenOperation(sign, left, right, rel_type=rel_type)

    @staticmethod
    def from_dict(d: dict) -> 'KBAllenOperation':
        rel_type = d.get('tag')
        left = d.get('left').get('Name')
        right = d.get('right').get('Name')
        sign = d.get('Value')

        return KBAllenOperation(sign, left, right, rel_type=rel_type)

    @property
    def left(self) -> KBEvent | KBInterval | None:
        return self._left_kb

    @property
    def right(self) -> KBEvent | KBInterval | None:
        return self._right_kb

    @property
    def validated(self) -> bool:
        return self._validated

    @property
    def is_binary(self) -> bool:
        return True
