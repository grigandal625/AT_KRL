from xml.etree.ElementTree import Element

from at_krl.core.kb_value import KBValue
from at_krl.core.kb_value import Evaluatable, KBValue, NonFactor

from typing import Union

TAGS_SIGNS = {
    "eq": {
        "values": ["=", "==", "eq"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "gt": {
        "values": [">", "gt"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "ge": {
        "values": [">=", "ge"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "lt": {
        "values": ["<", "lt"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "le": {
        "values": ["<=", "le"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "ne": {
        "values": ["<>", "ne"],
        "is_binary": True,
        "convert_non_factor": True,
    },
    "and": {
        "values": ["&", "&&", "and"],
        "is_binary": True,
    },
    "or": {
        "values": ["|", "||", "or"],
        "is_binary": True,
    },
    "not": {
        "values": ["!", "~", "not"],
        "is_binary": False,
    },
    "xor": {
        "values": ["xor"],
        "is_binary": True,
    },
    "neg": {
        "values": ["-", "neg"],
        "is_binary": False,
    },
    "add": {
        "values": ["+", "add"],
        "is_binary": True,
    },
    "sub": {
        "values": ["-", "sub"],
        "is_binary": True,
    },
    "mul": {
        "values": ["*", "mul"],
        "is_binary": True,
    },
    "div": {
        "values": ["/", "div"],
        "is_binary": True,
    },
    "mod": {
        "values": ["%", "mod"],
        "is_binary": True,
    },
    "pow": {
        "values": ["^", "**", "pow"],
        "is_binary": True,
    },
}

class KBOperation(Evaluatable):
    left: 'Evaluatable' = None
    right: Union['Evaluatable', None] = None

    def __init__(self, sign: str, left: 'Evaluatable', right: Union['Evaluatable', None] = None, non_factor: Union['NonFactor', None] = None):
        super().__init__(non_factor=non_factor)
        for op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[op]['values']:
                self.tag = op
        if self.tag is None:
            raise Exception(f"Unknown operation: {sign}")
        self.convert_non_factor = TAGS_SIGNS[self.tag].get('convert_non_factor', False)

        self.left = left
        if self.is_binary:
            self.right = right

    @property
    def is_binary(self) -> bool:
        return TAGS_SIGNS[self.tag]["is_binary"]

    def __dict__(self) -> dict:
        return dict(
            sign=self.sign, left=self.left.__dict__(), right=self.right.__dict__(), **(super().__dict__())
        ) if self.is_binary else dict(
            sign=self.sign, left=self.left.__dict__(), **(super().__dict__())
        )
    
    @staticmethod
    def from_dict(d: dict) -> 'KBOperation':
        return KBOperation(
            d['sign'], 
            Evaluatable.from_dict(d['left']), 
            Evaluatable.from_dict(d['right']) if d.get('right', None) is not None else None,
            NonFactor.from_dict(d['non_factor']) if d.get('non_factor', None) is not None else None
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