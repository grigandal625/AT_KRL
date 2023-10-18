from xml.etree.ElementTree import Element
from at_krl.core.kb import KBEntity
from at_krl.core.non_factor import NonFactor

from typing import Union
import json


class Evaluatable(KBEntity):
    non_factor: NonFactor = None
    convert_non_factor: bool = None

    def __init__(self, non_factor: Union['NonFactor', None] = None):
        self.convert_non_factor = non_factor is not None
        if non_factor is None:
            non_factor = NonFactor()
        self.non_factor = non_factor

    def __dict__(self) -> dict:
        result = super().__dict__()
        if self.non_factor.initialized or self.convert_non_factor and not self.non_factor.initialized:
            result.update({'non_factor': self.non_factor.__dict__()})
        return result

    @property
    def xml(self) -> Element:
        result = super().xml
        if self.non_factor.initialized or self.convert_non_factor and not self.non_factor.initialized:
            result.append(self.non_factor.xml)
        return result

    @staticmethod
    def from_xml(xml: Element) -> 'Evaluatable':
        if xml.tag == 'value':
            return KBValue.from_xml(xml)
        if xml.tag == 'ref':
            from at_krl.core.kb_reference import KBReference
            return KBReference.from_xml(xml)
        from at_krl.core.kb_operation import KBOperation, TAGS_SIGNS
        if xml.tag in TAGS_SIGNS:
            return KBOperation.from_xml(xml)

        from at_krl.core.temporal.kb_allen_operation import TEMPORAL_TAGS_SIGNS, KBAllenOperation
        if xml.tag in ['EvRel', 'IntRel', 'EvIntRel']:
            return KBAllenOperation.from_xml(xml)
        raise Exception("Unknown evaluatable tag: " + xml.tag)

    @staticmethod
    def from_dict(d: dict) -> 'Evaluatable':
        if d['tag'] == 'value':
            return KBValue.from_dict(d)
        if d['tag'] == 'ref':
            from at_krl.core.kb_reference import KBReference
            return KBReference.from_dict(d)
        from at_krl.core.kb_operation import KBOperation, TAGS_SIGNS
        if d['tag'] in TAGS_SIGNS:
            return KBOperation.from_dict(d)
        from at_krl.core.temporal.kb_allen_operation import TEMPORAL_TAGS_SIGNS, KBAllenOperation
        if d.get('tag', None) in [
            'EvRel', 'IntRel', 'EvIntRel'
        ] or d.get('Value', None) in TEMPORAL_TAGS_SIGNS or d.get('sign', None) in TEMPORAL_TAGS_SIGNS:
            return KBAllenOperation.from_dict(d)
        raise ValueError("Unknown evaluatable tag: " + d['tag'])

    def evaluate(self, *args, **kwargs) -> 'KBValue':
        pass

    @property
    def krl(self):
        result = self.inner_krl
        if self.non_factor.initialized or self.convert_non_factor and not self.non_factor.initialized:
            result = result + ' ' + self.non_factor.krl
        return result

    @property
    def inner_krl(self) -> str:
        pass


class KBValue(Evaluatable):
    content = None

    def __init__(self, content, non_factor: Union['NonFactor', None] = None):
        super().__init__(non_factor)
        self.content = content
        self.tag = 'value'

    def __dict__(self) -> dict:
        return dict(content=self.content, **(super().__dict__()))

    def evaluate(self, *args, **kwargs) -> 'KBValue':
        return self

    @staticmethod
    def from_dict(d: dict) -> 'KBValue':
        return KBValue(d['content'], d.get('non_factor', None))

    @property
    def inner_krl(self) -> str:
        try:
            result = json.dumps(self.content, ensure_ascii=False)
        except:
            result = json.dumps(str(self.content), ensure_ascii=False)
        return result

    @property
    def inner_xml(self) -> str:
        return str(self.content)

    @staticmethod
    def from_xml(xml: Element) -> 'KBValue':
        return KBValue(xml.text)
