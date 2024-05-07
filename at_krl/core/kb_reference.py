from xml.etree.ElementTree import Element
from at_krl.core.kb_value import Evaluatable, KBValue, NonFactor
from typing import Union, TYPE_CHECKING

from at_krl.exceptions.kb_exception import KBValidationError
import logging

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase
    from at_krl.core.kb_class import KBInstance


class KBReference(Evaluatable):
    id: str = None
    ref: Union['KBReference', None] = None

    def __init__(self, id: str, ref: Union['KBReference', None] = None, non_factor: Union[NonFactor, None] = None):
        super().__init__(non_factor=non_factor)
        self.id = id
        self.ref = ref
        if self.ref is not None:
            self.ref.owner = self
        self.tag = 'ref'

    def evaluate(self, env, recursively=True, *args, **kwargs) -> 'KBValue':
        return env.get_ref(self.id, recursively=recursively)

    def __dict__(self) -> dict:
        return dict(
            id=self.id,
            ref=self.ref.__dict__(),
            **(super().__dict__())
        ) if self.ref is not None else dict(
            id=self.id,
            **(super().__dict__())
        )

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

    def validate(self, kb: 'KnowledgeBase', *args, inst: 'KBInstance' = None, **kwargs):
        inst = inst or kb.world.create_instance(
            kb, 'world_inst', kb.world.desc, ignore_validation=True)
        self._validated = self._validate(
            inst, raise_on_validation=kb._raise_on_validation)

    def _validate(self, inst: 'KBInstance', raise_on_validation: bool) -> bool:
        for p in inst.properties_instances:
            if p.id == self.id:
                if self.ref:
                    self._validated = self.ref._validate(
                        p, raise_on_validation)
                else:
                    self._validated = True
                break
        if not self._validated:
            msg = f'Error while validating reference "{self.id}" of {self.krl} with instance {inst.id}'
            logger.warning(msg)
            if raise_on_validation:
                raise KBValidationError(msg, kb_entity=self)
        return self._validated
