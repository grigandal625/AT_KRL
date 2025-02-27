from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
from at_krl.core.temporal.allen_class import AllenClass

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBEvent(AllenClass):
    tag: Literal["event"] = field(init=False, default="event")
    occurance_condition: SimpleEvaluatable
    group: Literal["СОБЫТИЕ"] = field(init=False, default="СОБЫТИЕ")

    legacy_tag = Literal["Event"] = field(init=False, metadata={"serialize": False}, default="Event")

    def __post_init__(self):
        self.occurance_condition.owner = self
        return super().__post_init__()

    @property
    def inner_xml(self) -> Element:
        result = Element(tag="properties")
        occurance_condition = Element(tag="property", attrib={"id": "УслВозн", "type": "ЛогВыр"})
        value = Element(tag="value")
        value.append(self.occurance_condition.xml)
        occurance_condition.append(value)
        result.append(occurance_condition)
        return result

    @property
    def legacy_inner_xml(self) -> Element:
        formula = Element("Formula")
        formula.append(self.occurance_condition.legacy_xml)
        return formula

    @property
    def legacy_attrs(self) -> dict:
        return {"Name": self.id}

    @property
    def legacy_available(self) -> bool:
        raise True

    @property
    def inner_krl(self):
        return f"""АТРИБУТЫ
    АТРИБУТ УслВозн
        ТИП ЛогВыр
        ЗНАЧЕНИЕ
            {self.occurance_condition.krl}
"""

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        if not self._validated:
            self.occurance_condition.validate(kb)
            self._validated = True

    @property
    def xml_owner_path(self):
        from at_krl.core.knowledge_base import KnowledgeBase

        owner: KnowledgeBase = self.owner
        return owner.xml_owner_path + f"/IntervalsAndEvents/Events/Event[{owner.classes.events.index(self)}]"
