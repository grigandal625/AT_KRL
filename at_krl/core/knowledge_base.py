import json
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import List
from typing import Literal
from typing import Optional
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import fromstring

from antlr4 import CommonTokenStream
from antlr4 import InputStream

from at_krl.core.kb_class import KBClass
from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_rule import KBRule
from at_krl.core.kb_type import KBType
from at_krl.core.temporal.allen_event import KBEvent
from at_krl.core.temporal.allen_interval import KBInterval
from at_krl.grammar.at_krl_lexer import at_krl_lexer
from at_krl.grammar.at_krl_parser import at_krl_parser
from at_krl.utils.error_listener import ATKRLErrorListener


@dataclass(kw_only=True)
class KBClasses(KBEntity):
    tag: Literal["classes"] = field(init=False, default="classes")
    objects: List[KBClass] = field(init=False, default_factory=list)
    events: List[KBEvent] = field(init=False, default_factory=list)
    intervals: List[KBInterval] = field(init=False, default_factory=list)
    owner: "KnowledgeBase" = field(init=False, default=None, metadata={"serialize": False})

    @property
    def all(self):
        return self.objects + self.intervals + self.events

    @property
    def temporal_objects(self):
        return self.intervals + self.events


def get_world():
    return KBClass(
        id="world", desc="Класс верхнего уровня, включающий в себя экземпляры других классов и общие правила"
    )


def find_index_by_tag(parent: Element, tag: str):
    for index, child in enumerate(parent):
        if child.tag == tag:
            return index
    return -1


@dataclass(kw_only=True)
class KnowledgeBase(KBEntity):
    tag: Literal["knowledge-base"] = field(init=False, default="knowledge-base")
    problem_info: Optional[str] = field(default=None)
    types: List[KBType] = field(init=False, default_factory=list)
    classes: KBClasses = field(init=False, default_factory=KBClasses)
    rules: List[KBRule] = field(init=False, default_factory=list, metadata={"serialize": False})
    with_world: bool = field(default=False, metadata={"serialize": False})
    _world: KBClass = field(init=False, default_factory=get_world, metadata={"serialize": False})

    _raise_on_validation: bool = field(default=False, metadata={"serialize": False})

    def __post_init__(self) -> None:
        self.classes.owner = self
        self.rebuild_rules()

    def rebuild_rules(self):
        self.rules = []
        world = self.get_object_by_id("world")
        self.with_world = world is not None
        if self.with_world:
            self.rules = world.rules
            self._world = world
        self._world.rules = self.rules
        self._world.owner = self.classes

    @property
    def world(self) -> KBClass:
        world = self._world
        if self.with_world:
            world = self.get_object_by_id("world")
        world.owner = self
        return world

    def to_representation(self):
        result = {
            "tag": self.tag,
            "problem_info": self.problem_info,
            "types": [tp.to_representation() for tp in self.types],
            "classes": [],
        }
        for cls in self.classes.objects:
            if cls.id != "world":
                result["classes"].append(cls.to_representation())
        for intetval in self.classes.intervals:
            result["classes"].append(intetval.to_representation())
        for event in self.classes.events:
            result["classes"].append(event.to_representation())
        result["classes"].append(self.world.to_representation())
        return result

    def get_free_class_id(self, initial: str = None, from_object_id: bool = True) -> str:
        initial = (f"КЛАСС_{initial}" if from_object_id else initial) if initial else "КЛАСС_0"
        if initial not in [cls.id for cls in self.classes.all]:
            return initial
        if initial == "КЛАСС_0":
            initial = "КЛАСС"
        c = 1
        while f"{initial}_{c}" in [cls.id for cls in self.classes.all]:
            c += 1
        return f"{initial}_{c}"

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
        if class_id == "world":
            return self.world
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
        self.world.rules.append(rule)
        rule.owner = self.world
        self.rules = self.world.rules

    def get_krl(self, *args, **kwargs):
        res = "\n".join([t.krl for t in self.types])
        for property in self.world.properties:
            object_id = property.id
            class_id = property.type.krl

            cls = self.get_object_by_id(class_id)
            class_desc = cls.desc

            cls.id = object_id
            cls.desc = property.desc

            res += "\n" + cls.krl
            cls.id = class_id
            cls.desc = class_desc

        res += "\n" + "\n".join([obj.krl for obj in self.classes.temporal_objects])
        res += "\n" + "\n".join([rule.krl for rule in self.rules])
        return res

    @property
    def xml(self):
        return self.get_xml()

    def get_xml(self, *args, **kwargs):
        if not kwargs.get("with_allen", True):
            kwargs["legacy"] = True

        knowledge_base = Element("knowledge-base")
        knowledge_base.attrib["creation-date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        problem_info = Element("problem-info")
        if self.problem_info:
            problem_info.text = self.problem_info
        knowledge_base.append(problem_info)
        types = Element("types")

        for t in self.types:
            types.append(t.get_xml(*args, **kwargs))

        knowledge_base.append(types)

        if kwargs.get("legacy") and kwargs.get("with_allen", True):
            knowledge_base.append(self.get_allen_xml(*args, **kwargs))

        classes = Element("classes")
        for c in self.classes.objects:
            if self.with_world and c.id == "world":
                continue
            classes.append(c.get_xml(*args, **kwargs))
        if not kwargs.get("legacy"):
            for c in self.classes.temporal_objects:
                classes.append(c.get_xml(*args, **kwargs))

        classes.append(self.world.get_xml(*args, **kwargs))  # rules are here
        knowledge_base.append(classes)

        return knowledge_base

    def get_allen_xml(self, *args, **kwargs) -> Element:
        intervals = Element("Intervals")
        for interval in self.classes.intervals:
            intervals.append(interval.get_xml(*args, **kwargs))

        events = Element("Events")
        for event in self.classes.events:
            events.append(event.get_xml(*args, **kwargs))

        intervals_and_events = Element("IntervalsAndEvents")
        intervals_and_events.append(intervals)
        intervals_and_events.append(events)

        return intervals_and_events

    def validate(self):
        if not self._validated:
            for t in self.types:
                t.validate(self)

            for cls in self.classes.objects:
                if cls.id != "world":
                    cls.validate(self)

            for interval in self.classes.intervals:
                interval.validate(self)

            for event in self.classes.events:
                event.validate(self)

            self.world.validate(self)
            self._validated = True

    @staticmethod
    def from_xml(xml: Element | str, allen_xml: Element | str = None, legacy: bool = False) -> "KnowledgeBase":
        from at_krl.xml_models.knowledge_base import KnowledgeBaseXMLModel, KnowledgeBaseLegacyXMLModel

        if isinstance(xml, str):
            xml = fromstring(xml)
        if allen_xml:
            legacy = True
            if isinstance(allen_xml, str):
                allen_xml = fromstring(allen_xml)
            after_types_index = find_index_by_tag(xml, "types") + 1
            xml.insert(after_types_index, allen_xml)
        model_class = KnowledgeBaseXMLModel if not legacy else KnowledgeBaseLegacyXMLModel
        kb_model = model_class.from_xml_tree(xml)
        return kb_model.to_internal()

    @staticmethod
    def from_json(d: dict | str) -> "KnowledgeBase":
        from at_krl.models.knowledge_base import KnowledgeBaseModel

        if isinstance(d, str):
            d = json.loads(d)

        kb_model = KnowledgeBaseModel(**d)
        return kb_model.to_internal()

    @staticmethod
    def from_krl(krl_text: str):
        from at_krl.utils.listener import ATKRLListener

        # Создаем поток ввода для текста ЯПЗ
        input_stream = InputStream(krl_text)

        # Создаем лексер
        lexer = at_krl_lexer(input_stream)

        # Создаем кастомный поток токенов, который пропускает скрытые токены
        stream = CommonTokenStream(lexer)
        stream.fill()  # Заполняем поток токенов

        # Создаем парсер
        parser = at_krl_parser(stream)

        listener = ATKRLListener()
        parser.addParseListener(listener)

        # Настраиваем обработчик ошибок
        error_listener = ATKRLErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Парсим входной текст
        parser.knowledge_base()
        return listener.KB

    @property
    def xml_owner_path(self):
        return self.tag
