from xml.etree.ElementTree import Element

from at_krl.core.kb_value import KBValue
from at_krl.core.kb_value import Evaluatable, KBValue, NonFactor

from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase

TAGS_SIGNS = {
    "eq": {
        "values": ["=", "==", "eq"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "gt": {
        "values": [">", "gt"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "ge": {
        "values": [">=", "ge"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "lt": {
        "values": ["<", "lt"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "le": {
        "values": ["<=", "le"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "ne": {
        "values": ["<>", "!=", "ne"],
        "is_binary": True,
        "convert_non_factor": True,
        "meta": "eq",
    },
    "and": {
        "values": ["&", "&&", "and"],
        "is_binary": True,
        "meta": "log",
    },
    "or": {
        "values": ["|", "||", "or"],
        "is_binary": True,
        "meta": "log",
    },
    "not": {
        "values": ["~", "!", "not"],
        "is_binary": False,
        "meta": "log",
    },
    "xor": {
        "values": ["xor"],
        "is_binary": True,
        "meta": "log",
    },
    "neg": {
        "values": ["-", "neg"],
        "is_binary": False,
        "meta": "super_math",
    },
    "add": {
        "values": ["+", "add"],
        "is_binary": True,
        "meta": "math",
    },
    "sub": {
        "values": ["-", "sub"],
        "is_binary": True,
        "meta": "math",
    },
    "mul": {
        "values": ["*", "mul"],
        "is_binary": True,
        "meta": "math",
    },
    "div": {
        "values": ["/", "div"],
        "is_binary": True,
        "meta": "math",
    },
    "mod": {
        "values": ["%", "mod"],
        "is_binary": True,
        "meta": "super_math",
    },
    "pow": {
        "values": ["^", "**", "pow"],
        "is_binary": True,
        "meta": "super_math",
    },
}


class KBOperation(Evaluatable):
    left: 'Evaluatable' = None
    right: Union['Evaluatable', None] = None
    op: str = None

    def __init__(self, sign: str, left: 'Evaluatable', right: Union['Evaluatable', None] = None, non_factor: Union['NonFactor', None] = None):
        super().__init__(non_factor=non_factor)
        
        get_is_binary = lambda l, r:  l is not None and r is not None
        
        for op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[op]['values']:
                if TAGS_SIGNS[op]['is_binary'] == get_is_binary(left, right):
                    self.op = op
                    self.tag = op
                    break

        if self.tag is None:
            raise Exception(f"Unknown operation: {sign}")
        self.convert_non_factor = TAGS_SIGNS[self.tag].get(
            'convert_non_factor', False)

        self.left = left
        self.left.owner = self
        if self.is_binary:
            self.right = right
            self.right.owner = self

    @property
    def is_binary(self) -> bool:
        return TAGS_SIGNS[self.op]["is_binary"]

    def __dict__(self) -> dict:
        return dict(
            sign=self.sign, left=self.left.__dict__(), right=self.right.__dict__(), **(super().__dict__())
        ) if self.is_binary else dict(
            sign=self.sign, left=self.left.__dict__(), **(super().__dict__())
        )

    @staticmethod
    def from_dict(d: dict) -> 'KBOperation':
        return KBOperation(
            d.get('sign') or d.get('tag'),
            Evaluatable.from_dict(d['left']),
            Evaluatable.from_dict(d['right']) if d.get(
                'right', None) is not None else None,
            NonFactor.from_dict(d['non_factor']) if d.get(
                'non_factor', None) is not None else None
        )

    @property
    def inner_xml(self) -> Element:
        result = [self.left.xml]
        if self.is_binary:
            result.append(self.right.xml)
        return result

    @staticmethod
    def from_xml(xml: Element) -> 'KBOperation':
        sign = xml.tag
        left = Evaluatable.from_xml(xml[0])
        right = None
        if TAGS_SIGNS[sign]['is_binary']:
            right = Evaluatable.from_xml(xml[1])
        non_factor = NonFactor.from_xml(xml.find('with'))
        return KBOperation(sign, left, right, non_factor)

    @property
    def sign(self):
        return TAGS_SIGNS[self.tag]['values'][0]

    @property
    def inner_krl(self) -> str:
        return f"({self.left.krl}) {self.sign} ({self.right.krl})" if self.is_binary else f"{self.sign} ({self.left.krl})"

    def evaluate(self, env, *args, **kwargs) -> KBValue:
        return TAGS_SIGNS[self.tag]["evaluate"](self, env, *args, **kwargs)

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.left.validate(kb, *args, **kwargs)
            self.right.validate(kb, *args, **kwargs)
            self._validated = True
