from xml.etree.ElementTree import Element
from at_krl.core.kb_value import Evaluatable, KBValue, NonFactor
from typing import Union


class KBReference(Evaluatable):
    id: str = None
    ref: Union['KBReference', None] = None

    def __init__(self, id: str, ref: Union['KBReference', None] = None, non_factor: Union[NonFactor, None] = None):
        super().__init__(non_factor)
        self.id = id
        self.ref = ref
        self.tag = 'ref'

    def evaluate(self, env, recursively=True, *args, **kwargs) -> 'KBValue':
        return env.get_ref(self.id, recursively=recursively)

    def __dict__(self) -> dict:
        return dict(id=self.id, ref=self.ref.__dict__(), **(super().__dict__())) if self.ref is not None else dict(id=self.id, **(super().__dict__()))

    @property
    def attrs(self) -> dict:
        return dict(id=self.id, **(super().attrs))

    @staticmethod
    def from_dict(d: dict) -> 'KBReference':
        return KBReference(
            d['id'],
            KBReference.from_dict(d['ref']) if d.get('ref', None) else None,
            non_factor=NonFactor.from_dict(d.get('non_factor', None))
        )

    @property
    def inner_krl(self) -> str:
        result = self.id
        ref = self.ref
        while ref is not None:
            result = f'{result}.{ref.id}'
            ref = ref.ref
        return result

    @property
    def inner_xml(self) -> Element:
        return self.ref.xml if self.ref is not None else None

    @staticmethod
    def from_xml(xml: Element) -> 'KBReference':
        return KBReference(
            xml.attrib['id'],
            KBReference.from_xml(xml.find('ref'))
            if xml.find('ref') is not None
            else None
        )

    @staticmethod
    def parse(ref_str: str) -> 'KBReference':
        if ref_str == '':
            return None
        elif '.' in ref_str:
            return KBReference(ref_str[:ref_str.index('.')], KBReference.parse(ref_str[ref_str.index('.')+1:]))
        else:
            return KBReference(ref_str)
