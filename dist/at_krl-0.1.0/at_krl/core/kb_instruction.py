from at_krl.core.kb_entity import KBEntity
from at_krl.core.kb_value import Evaluatable
from at_krl.core.kb_reference import KBReference
from at_krl.core.non_factor import NonFactor
from xml.etree.ElementTree import Element

from typing import Iterable, List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class KBInstruction(KBEntity):
    non_factor: Union[NonFactor, None] = None
    convert_non_factor: bool = True

    def __init__(self, non_factor: Union[NonFactor, None] = None) -> None:
        super().__init__()
        self.non_factor = non_factor if non_factor is not None else NonFactor()

    def perform(self, env, *args, **kwargs):
        pass

    @staticmethod
    def from_xml(xml: Element) -> 'KBInstruction':
        if xml.tag == 'assign':
            return AssignInstruction.from_xml(xml)
        raise

    @staticmethod
    def from_dict(d: dict) -> 'KBInstruction':
        if d.get('tag', 'assign') == 'assign':
            return AssignInstruction.from_dict(d)
        raise


class AssignInstruction(KBInstruction):

    def __init__(self, ref: KBReference, value: Evaluatable, non_factor: Union[NonFactor, None] = None) -> None:
        super().__init__(non_factor)
        self.tag = 'assign'
        self.ref = ref
        if self.ref is not None:
            self.ref.owner = self
        self.ref.convert_non_factor = False
        self.value = value
        self.value.owner = self

    @property
    def inner_xml(self) -> str | Element | List[Element] | Iterable[Element] | None:
        return [
            self.ref.xml,
            self.value.xml,
            self.non_factor.xml
        ] if self.convert_non_factor else [
            self.ref.xml,
            self.value.xml
        ]

    @property
    def krl(self) -> str:
        return f'{self.ref.krl} = ({self.value.krl}) {self.non_factor.krl}'

    @staticmethod
    def from_xml(xml: Element) -> 'AssignInstruction':
        ref = KBReference.from_xml(xml.find('ref'))
        value = Evaluatable.from_xml(xml[1])
        non_factor = NonFactor.from_xml(xml.find('with'))
        return AssignInstruction(ref, value, non_factor)

    def __dict__(self) -> dict:
        return dict(
            ref=self.ref.__dict__(),
            value=self.value.__dict__(),
            non_factor=self.non_factor.__dict__(),
            **(super().__dict__())
        )

    @staticmethod
    def from_dict(d: dict) -> 'AssignInstruction':
        return AssignInstruction(
            KBReference.from_dict(d['ref']),
            Evaluatable.from_dict(d['value']),
            NonFactor.from_dict(d.get('non_factor', None))
        )

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        if not self._validated:
            self.ref.validate(kb, *args, **kwargs)
            self.value.validate(kb, *args, **kwargs)
            self._validated = True
