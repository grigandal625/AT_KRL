from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Literal
from typing import Optional
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from pydantic import Field

from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_instruction import KBInstruction
from at_krl.core.kb_value import KBValue
from at_krl.models.kb_value import EvaluatableModel

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase
    from at_krl.core.kb_class import KBClass


@dataclass(kw_only=True)
class KBRule(KBEntity):
    tag: Literal["rule"] = Field(default="rule")

    id: str
    condition: EvaluatableModel
    #
    instructions: List[KBInstruction]
    else_instructions: Optional[List[KBInstruction]] = field(default_factory=list)
    meta: Literal["simple", "periodic"] = field(default_factory="simple")
    period: Optional[int] = field(default=None)
    desc: Optional[str] = field(default=None)

    evaluated_condition: Optional[KBValue] = field(default=None, init=False, metadata={"serialize": False})

    @property
    def attrs(self) -> dict:
        return {"id": self.id, "meta": self.meta, "desc": self.desc or self.id}

    @property
    def inner_xml(self) -> str | Element | List[Element] | Iterable[Element] | None:
        res = []

        condition = Element("condition")
        condition.append(self.condition.xml)
        res.append(condition)

        action = Element("action")
        for instruction in self.instructions:
            action.append(instruction.xml)
        res.append(action)

        if (self.else_instructions is not None) and len(self.else_instructions):
            else_action = Element("else-action")
            for instruction in self.else_instructions:
                else_action.append(instruction.xml)
            res.append(else_action)

        return res

    @property
    def krl(self) -> str:
        action_krl = "ТО\n    " + "\n    ".join([instruction.krl for instruction in self.instructions])
        else_action_krl = ""
        if self.else_instructions is not None and len(self.else_instructions):
            else_action_krl = (
                "ИНАЧЕ\n    " + "\n    ".join([instruction.krl for instruction in self.else_instructions]) + "\n"
            )

        return f"""ПРАВИЛО {self.id}
ЕСЛИ
    {self.condition.krl}
{action_krl}
{else_action_krl}КОММЕНТАРИЙ {self.desc}
"""

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        if not self._validated:
            self.condition.validate(kb, *args, **kwargs)

            for instruct in self.instructions:
                instruct.validate(kb, *args, **kwargs)

            if self.else_instructions is not None:
                for instruct in self.else_instructions:
                    instruct.validate(kb, *args, **kwargs)

            self._validated = True

    @property
    def xml_owner_path(self):
        owner: KBClass = self.owner
        rule_ids = [r.id for r in owner.rules]
        idx = rule_ids.index(self.id)
        return self.owner.xml_owner_path + f"/rules/rule[{idx}]"
