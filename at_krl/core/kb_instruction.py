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

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBInstruction(KBEntity):
    tag: str = field(init=False, default="instruction")
    non_factor: Optional[NonFactor] = field(default_factory=NonFactor)

    @property
    def inner_xml(self) -> Element:
        return self.non_factor.xml


@dataclass(kw_only=True)
class AssignInstruction(KBInstruction):
    tag: Literal["assign"] = field(init=False, default="assign")
    ref: KBReference
    value: Evaluatable

    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        return [self.ref.xml, self.value.xml, self.non_factor.xml]

    def get_krl(self, *args, **kwargs) -> str:
        return f"{self.ref.to_simple().krl} = ({self.value.get_krl(*args, **kwargs)}) {self.non_factor.krl}"

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        if not self._validated:
            self.ref.validate(kb, *args, **kwargs)
            self.value.validate(kb, *args, **kwargs)
            self._validated = True
