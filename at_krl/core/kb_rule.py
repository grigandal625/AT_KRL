from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_value import Evaluatable
from at_krl.core.kb_value import KBValue
from at_krl.core.kb_instruction import KBInstruction
from typing import Iterable, List, TYPE_CHECKING
from xml.etree.ElementTree import Element

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class KBRule(KBEntity):
    id: str
    condition: Evaluatable
    instructions: List[KBInstruction]
    else_instructions: List[KBInstruction]
    meta: str
    desc: str
    evaluated_condition: KBValue | None

    def __init__(self, id, condition: Evaluatable, instructions: List[KBInstruction], else_instructions: List[KBInstruction] | None = None, meta='simple', desc=None):
        self.id = id
        self.tag = 'rule'
        self.condition = condition
        self.condition.owner = self
        self.instructions = instructions
        for instr in self.instructions:
            instr.owner = self
        self.else_instructions = else_instructions if else_instructions is not None and len(
            else_instructions) else None
        if self.else_instructions is not None:
            for else_instr in self.else_instructions:
                else_instr.owner = self
                
        self.meta = meta
        self.desc = desc or id

    @property
    def attrs(self) -> dict:
        return {
            'id': self.id,
            'meta': self.meta,
            'desc': self.desc,
            **(super().attrs)
        }

    @property
    def inner_xml(self) -> str | Element | List[Element] | Iterable[Element] | None:
        res = []

        condition = Element('condition')
        condition.append(self.condition.xml)
        res.append(condition)

        action = Element('action')
        for instruction in self.instructions:
            action.append(instruction.xml)
        res.append(action)

        if (self.else_instructions is not None) and len(self.else_instructions):
            else_action = Element('else-action')
            for instruction in self.else_instructions:
                else_action.append(instruction.xml)
            res.append(else_action)

        return res

    @staticmethod
    def from_xml(xml: Element) -> 'KBRule':
        condition_xml = xml.find('condition')[0]
        condition = Evaluatable.from_xml(condition_xml)
        action_xml = xml.find('action')
        instructions = [KBInstruction.from_xml(
            instruction_xml) for instruction_xml in action_xml]

        else_action_xml = xml.find('else-action')
        else_instructions = None
        if else_action_xml is not None:
            else_instructions = [KBInstruction.from_xml(
                else_instruction_xml) for else_instruction_xml in else_action_xml]

        return KBRule(**xml.attrib, condition=condition, instructions=instructions, else_instructions=else_instructions)

    def __dict__(self) -> dict:
        res = dict(
            condition=self.condition.__dict__(),
            instructions=[instruction.__dict__()
                          for instruction in self.instructions],
            **(self.attrs),
            ** (super().__dict__())
        )
        if self.else_instructions is not None:
            res['else_instructions'] = [instruction.__dict__()
                                        for instruction in self.else_instructions]

        return res

    @staticmethod
    def from_dict(d: dict) -> 'KBRule':
        d.pop('tag', None)
        condition = Evaluatable.from_dict(d.pop('condition'))
        instructions = [KBInstruction.from_dict(
            instruction_dict) for instruction_dict in d.pop('instructions')]
        else_instructions = None
        else_instruction_dict_list = d.pop('else_instructions', None)
        if else_instruction_dict_list is not None and len(else_instruction_dict_list):
            else_instructions = [KBInstruction.from_dict(
                else_instruction_dict) for else_instruction_dict in else_instruction_dict_list]
        return KBRule(
            **d,
            condition=condition,
            instructions=instructions,
            else_instructions=else_instructions
        )

    @property
    def krl(self) -> str:
        action_krl = 'ТО\n    ' + \
            '\n    '.join(
                [instruction.krl for instruction in self.instructions])
        else_action_krl = ''
        if self.else_instructions is not None and len(self.else_instructions):
            else_action_krl = 'ИНАЧЕ\n    ' + \
                '\n    '.join(
                    [instruction.krl for instruction in self.else_instructions]) + '\n'

        return f"""ПРАВИЛО {self.id}
ЕСЛИ
    {self.condition.krl}
{action_krl}
{else_action_krl}КОММЕНТАРИЙ {self.desc}
"""

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.condition.validate(kb, *args, **kwargs)

            for instruct in self.instructions:
                instruct.validate(kb, *args, **kwargs)

            self._validated = True

    @property
    def xml_owner_path(self):
        rule_ids = [r.id for r in self.owner.rules]
        idx = rule_ids.index(self.id)
        return self.owner.xml_owner_path + f'/rules/rule[{idx}]'
