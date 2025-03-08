from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_value import Evaluatable
from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_reference import SimpleReference

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBInstruction(KBEntity):
    tag: str = field(init=False, default="instruction")
    non_factor: Optional[NonFactor] = field(default_factory=NonFactor)

    def get_inner_xml(self, *args, **kwargs) -> Element:
        return self.non_factor.xml


@dataclass(kw_only=True)
class AssignInstruction(KBInstruction):
    tag: Literal["assign"] = field(init=False, default="assign")
    ref: KBReference
    value: Evaluatable

    def __post_init__(self):
        if isinstance(self.ref, SimpleReference):
            self.ref = KBReference.from_simple(self.ref)

    def get_inner_xml(self, *args, **kwargs) -> List[Element] | Iterable[Element]:
        legacy = kwargs.get("legacy")
        kwargs["legacy"] = False
        ref_xml = self.ref.get_xml(*args, **kwargs)
        kwargs["legacy"] = legacy
        value_xml = self.value.get_xml(*args, **kwargs)
        return [ref_xml, value_xml, self.non_factor.xml]

    def get_krl(self, *args, **kwargs) -> str:
        return f"{self.ref.to_simple().krl} = ({self.value.get_krl(*args, **kwargs)}) {self.non_factor.krl}"

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        if not self._validated:
            self.ref.validate(kb, *args, **kwargs)
            self.value.validate(kb, *args, **kwargs)
            self._validated = True
