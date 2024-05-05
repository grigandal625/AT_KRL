from at_krl.core.kb_type import KBType
from at_krl.core.kb_class import KBClass, KBInstance
from at_krl.core.kb_rule import KBRule
from at_krl.core.kb_value import KBEntity, KBValue

from at_krl.core.temporal.kb_interval import KBInterval
from at_krl.core.temporal.kb_event import KBEvent

from typing import List, Union
from datetime import datetime

from xml.etree.ElementTree import Element


class KBClasses:
    tag = 'classes'
    objects: List[KBClass]
    events: List[KBEvent]
    intervals: List[KBInterval]
    owner: 'KnowledgeBase' = None

    def __init__(self):
        self.objects = []
        self.events = []
        self.intervals = []

    @property
    def all(self):
        return self.objects + self.intervals + self.events

    @property
    def temporal_objects(self):
        return self.intervals + self.events


class KnowledgeBase(KBEntity):
    types: List[KBType]
    classes: KBClasses
    rules: List[KBRule]
    with_world: bool
    _world: KBClass

    _raise_on_validation: bool = False
    _validated: bool = False

    def __init__(self, with_world: bool = False) -> None:
        self.tag = 'knowledge-base'
        self.types = []
        self.classes = KBClasses()
        self.classes.owner = self
        self.rules = []
        self.with_world = with_world
        self._world = KBClass(
            'world', 
            [], 
            self.rules, 
            desc='Класс верхнего уровня, включающий в себя экземпляры других классов и общие правила')
        self._world.owner = self.classes

    @property
    def world(self) -> KBClass:
        world = self._world
        if self.with_world:
            world = self.get_object_by_id('world')
        world.owner = self
        return world

    def get_free_class_id(self, initial: str = None, from_object_id: bool = True) -> str:
        initial = (
            f'КЛАСС_{initial}' if from_object_id else initial) if initial else 'КЛАСС_0'
        if not initial in [cls.id for cls in self.classes.all]:
            return initial
        if initial == 'КЛАСС_0':
            initial = 'КЛАСС'
        c = 1
        while f'{initial}_{c}' in [cls.id for cls in self.classes.all]:
            c += 1
        return f'{initial}_{c}'

    def get_object_by_id(self, object_id: str) -> KBClass | None:
        for obj in self.classes.objects:
            if obj.id == object_id:
                return obj

    def get_event_by_id(self, event_id: str) -> KBEvent | None:
        for event in self.classes.events:
            if event.id == event_id:
                return event

    def get_interval_by_id(self, interval_id: str) -> KBInterval | None:
        for interval in self.classes.intervals:
            if interval.id == interval_id:
                return interval

    def get_class_by_id(self, class_id: str) -> KBClass | None:
        for cls in self.classes.all:
            if cls.id == class_id:
                return cls

    def get_type_by_id(self, type_id: str) -> KBType | None:
        for tp in self.types:
            if tp.id == type_id:
                return tp

    def get_rule_by_id(self, rule_id: str) -> KBRule | None:
        for rule in self.rules:
            if rule.id == rule_id:
                return rule

    def add_rule(self, rule: KBRule):
        self.rules.append(rule)
        if not self.with_world:
            if rule not in self.world.rules:
                self.world.rules.append(rule)
                rule.owner = self.world

    @property
    def krl(self):
        res = '\n'.join([t.krl for t in self.types])
        for property in self.world.properties:
            object_id = property.id
            class_id = property.type_or_class_id

            cls = self.get_object_by_id(class_id)
            cls.id = object_id

            res += '\n' + cls.krl
            cls.id = class_id

        res += '\n' + \
            '\n'.join([obj.krl for obj in self.classes.temporal_objects])
        res += '\n' + '\n'.join([rule.krl for rule in self.rules])
        return res

    @property
    def xml(self):
        return self.get_xml()

    def get_xml(self, with_allen=True) -> Element:

        knowledge_base = Element('knowledge-base')
        knowledge_base.attrib['creation-date'] = datetime.now().strftime(
            '%d.%m.%Y %H:%M:%S')

        knowledge_base.append(Element('problem-info'))
        types = Element('types')

        for t in self.types:
            types.append(t.xml)

        knowledge_base.append(types)

        if with_allen:
            knowledge_base.append(self.allen_xml)

        classes = Element('classes')
        for c in self.classes.objects:
            classes.append(c.xml)

        if not self.with_world:
            classes.append(self.world.xml)  # rules are here
        knowledge_base.append(classes)

        return knowledge_base

    @property
    def allen_xml(self) -> Element:

        intervals = Element('Intervals')
        for interval in self.classes.intervals:
            intervals.append(interval.xml)

        events = Element('Events')
        for event in self.classes.events:
            events.append(event.xml)

        intervals_and_events = Element('IntervalsAndEvents')
        intervals_and_events.append(intervals)
        intervals_and_events.append(events)

        return intervals_and_events

    def __dict__(self) -> dict:
        knowledge_base = {}
        knowledge_base['types'] = [t.__dict__() for t in self.types]
        knowledge_base['intervals'] = [i.__dict__()
                                       for i in self.classes.intervals]
        knowledge_base['events'] = [e.__dict__() for e in self.classes.events]
        knowledge_base['classes'] = [c.__dict__()
                                     for c in self.classes.objects]
        if not self.with_world:
            knowledge_base['classes'].append(self.world.__dict__())
        return knowledge_base

    def validate(self):
        if not self._validated:
            for t in self.types:
                t.validate(self)
            for cls in self.classes.objects:
                cls.validate(self)
            if not self.with_world:
                self.world.validate(self)
            for interval in self.classes.intervals:
                interval.validate(self)
            for event in self.classes.events:
                event.validate(self)

            self._validated = True

    @staticmethod
    def from_xml(xml: Element, allen_xml: Element = None) -> 'KnowledgeBase':
        KB = KnowledgeBase()
        types = xml.find('types')
        for type_xml in types:
            t = KBType.from_xml(type_xml)
            t.owner = KB
            KB.types.append(t)

        allen_xml = allen_xml or xml.find('IntervalsAndEvents')
        if allen_xml:
            intervals = allen_xml.find('Intervals')
            for interval_xml in intervals:
                i = KBInterval.from_xml(interval_xml)
                i.owner = KB
                KB.classes.intervals.append(i)

            events = allen_xml.find('Events')
            for event_xml in events:
                e = KBEvent.from_xml(event_xml)
                KB.classes.events.append(e)

        classes = xml.find('classes')
        for class_xml in classes:
            if class_xml.attrib.get('id', None) == 'world':
                KB.with_world = True
            cls = KBClass.from_xml(class_xml)
            cls.owner = KB
            KB.classes.objects.append(cls)

        if KB.world:
            KB.rules = KB.world.rules

        return KB

    @staticmethod
    def from_dict(d: dict) -> 'KnowledgeBase':
        KB = KnowledgeBase()

        types = d.get('types', [])
        for t_dict in types:
            t = KBType.from_dict(t_dict)
            t.owner = KB
            KB.types.append(t)

        intervals = d.get('intervals', [])
        for i_dict in intervals:
            i = KBInterval.from_dict(i_dict)
            i.owner = KB
            KB.classes.intervals.append(i)

        events = d.get('events', [])
        for e_dict in events:
            e = KBEvent.from_dict(e_dict)
            KB.classes.events.append(e)

        classes = d.get('classes', [])
        for c_dict in classes:
            c = KBClass.from_dict(c_dict)
            c.owner = KB
            KB.classes.objects.append(c)

        if KB.get_object_by_id('world') is not None:
            KB.with_world = True
        
        KB.rules = KB.world.rules
        return KB

    @property
    def xml_owner_path(self):
        return self.tag