from xml.etree.ElementTree import Element
from at_krl.core.kb_entity import KBEntity
from at_krl.core.non_factor import NonFactor

from typing import Union
import json
from copy import deepcopy


class Evaluatable(KBEntity):
    non_factor: NonFactor = None
    convert_non_factor: bool = None

    def __init__(self, non_factor: Union['NonFactor', None] = None):
        self.convert_non_factor = non_factor is not None
        if non_factor is None:
            non_factor = NonFactor()
        self.non_factor = non_factor
        self.non_factor.owner = self

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
        raise ValueError("Unknown evaluatable tag: " + xml.tag)

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
        if (self.non_factor.initialized or self.convert_non_factor and not self.non_factor.initialized) and not self.non_factor.is_default:
            result = result + ' ' + self.non_factor.krl
        return result

    @property
    def inner_krl(self) -> str:
        pass

    @property
    def xml_owner_path(self) -> str:
        from at_krl.core.kb_rule import KBRule
        if isinstance(self.owner, KBRule):
            if self.owner.condition != self:
                raise ValueError(self._unknown_ownership)
            return self.owner.xml_owner_path + '/condition/' + self.tag
        
        from at_krl.core.kb_operation import KBOperation
        if isinstance(self.owner, KBOperation):
            if (self.owner.left != self) and (self.owner.right != self):
                raise ValueError(self._unknown_ownership)
            if self.owner.is_binary:
                if self.owner.left.__class__ == self.owner.right.__class__:
                    index = '0' if self.owner.left == self else '1'
                    return self.owner.xml_owner_path + '/' + self.tag + f'[{index}]'
                
        from at_krl.core.kb_instruction import AssignInstruction
        if isinstance(self.owner, AssignInstruction):
            if (self.owner.value != self) and (self.owner.ref != self):
                raise ValueError(self._unknown_ownership)
            if self.owner.ref.__class__ == self.owner.value.__class__:
                index = '0' if self.owner.ref == self else '1'
                return self.owner.xml_owner_path + '/' + self.tag + f'[{index}]'

        return self.owner.xml_owner_path + '/' + self.tag


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
        nf_dict = d.get('non_factor', None)
        nf = None
        if nf_dict is not None:
            nf = NonFactor.from_dict(nf_dict)
        return KBValue(d['content'], non_factor=nf)

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
        return KBValue(xml.text) # TODO: non_factor ???
    
    def copy(self):
        if self.non_factor is not None:
            return KBValue(deepcopy(self.content), NonFactor(
                self.non_factor.belief, 
                self.non_factor.probability, 
                self.non_factor.accuracy
            ))
        return KBValue(deepcopy(self.content))
