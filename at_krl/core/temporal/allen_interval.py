from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Literal
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable
from at_krl.core.temporal.allen_class import AllenClass

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBInterval(AllenClass):
    tag: Literal["interval"] = field(init=False, default="interval")
    open: SimpleEvaluatable
    close: SimpleEvaluatable
    group: Literal["ИНТЕРВАЛ"] = field(init=False, default="ИНТЕРВАЛ")

    legacy_tag: Literal["Interval"] = field(init=False, metadata={"serialize": False}, default="Interval")

    def __post_init__(self):
        self.open.owner = self
        return super().__post_init__()

    def get_inner_xml(self, *args, **kwargs) -> Element:
        if kwargs.get("legacy"):
            return self.legacy_inner_xml
        result = Element("properties")

        open = Element("property", attrib={"id": "УслНач", "type": "ЛогВыр"})
        open_value = Element("value")
        open_value.append(self.open.xml)
        open.append(open_value)
        result.append(open)

        close = Element("property", attrib={"id": "УслОконч", "type": "ЛогВыр"})
        close_value = Element("value")
        close_value.append(self.close.xml)
        close.append(close_value)
        result.append(close)

        return result

    @property
    def legacy_attrs(self) -> dict:
        return {"Name": self.id}

    @property
    def legacy_inner_xml(self) -> List[Element]:
        open = Element("Open")
        open.append(self.open.get_xml(legacy=True))
        close = Element("Close")
        close.append(self.close.get_xml(legacy=True))
        return [open, close]

    @property
    def legacy_available(self) -> bool:
        return True

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
            {self.close.krl}"""

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        if not self._validated:
            self.open.validate(kb)
            self.close.validate(kb)
            self._validated = True

    @property
    def xml_owner_path(self):
        from at_krl.core.knowledge_base import KnowledgeBase

        owner: KnowledgeBase = self.owner
        return (
            owner.xml_owner_path + f"/IntervalsAndIntervals/Intervals/Interval[{owner.classes.intervals.index(self)}]"
        )
