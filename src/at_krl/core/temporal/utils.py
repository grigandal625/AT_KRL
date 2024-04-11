from xml.etree.ElementTree import Element
from at_krl.core.kb_class import KBInstance
from at_krl.core.kb_value import Evaluatable, KBValue
from at_krl.core.kb_operation import KBOperation, TAGS_SIGNS
from at_krl.core.kb_reference import KBReference
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class SimpleEvaluatable(Evaluatable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.convert_non_factor = False
        if self.non_factor is not None:
            self.non_factor.initialized = False

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleEvaluatable':
        if xml.tag in ['Number', 'TruthVal', 'String']:
            return SimpleValue.from_xml(xml)
        elif xml.tag == 'Attribute':
            return SimpleReference.from_xml(xml)
        elif xml.tag in ['EqOp', 'LogOp', 'ArOp']:
            return SimpleOperation.from_xml(xml)

    @staticmethod
    def from_dict(d: dict) -> 'SimpleEvaluatable':
        if d.get('tag') in ['Number', 'TruthVal', 'String']:
            return SimpleValue.from_dict(d)
        elif d.get('tag') == 'Attribute':
            return SimpleReference.from_dict(d)
        elif d.get('tag') in ['EqOp', 'LogOp', 'ArOp']:
            return SimpleOperation.from_dict(d)


class SimpleValue(KBValue, SimpleEvaluatable):
    def __init__(self, content):
        super().__init__(content)
        if isinstance(content, bool):
            self.tag = 'TruthVal'
        elif isinstance(content, float) or isinstance(content, int):
            self.tag = 'Number'
        elif isinstance(content, str):
            self.tag = 'String'
        

    @property
    def inner_xml(self) -> str:
        return None

    @property
    def attrs(self) -> dict:
        if self.tag == 'TruthVal':
            return 'TRUE' if self.content else 'FALSE'
        return {'Value': str(self.content)}

    def __dict__(self) -> dict:
        res = super().__dict__()
        res['Value'] = res.pop('content', None)
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleValue':
        if xml.tag == 'Number':
            if '.' in xml.attrib.get('Value'):
                return SimpleValue(float(xml.attrib.get('Value')))
            return SimpleValue(int(xml.attrib.get('Value')))
        elif xml.tag == 'TruthVal':
            if isinstance(xml.attrib.get('Value'), bool):
                return SimpleValue(xml.attrib.get('Value'))
            return SimpleValue((xml.attrib.get('Value') != 'FALSE') and (xml.attrib.get('Value') != 'False'))
        elif xml.tag == 'String':
            return SimpleValue(xml.attrib.get('Value'))

    @staticmethod
    def from_dict(d: dict) -> 'SimpleValue':
        if d.get('tag') == 'Number':
            return SimpleValue(d.get('Value'))
        elif d.get('tag') == 'TruthVal':
            if isinstance(d.get('Value'), bool):
                return SimpleValue(d.get('Value'))    
            return SimpleValue((d.get('Value') != 'FALSE') and (d.get('Value') != 'False'))
        elif d.get('tag') == 'String':
            return SimpleValue(d.get('Value'))


class SimpleReference(KBReference, SimpleEvaluatable):
    def __init__(self, id: str, ref: KBReference = None):
        super().__init__(id, ref)
        self.tag = 'Attribute'

    @property
    def attrs(self) -> dict:
        return {'Value': self.inner_krl}

    @property
    def inner_xml(self) -> None:
        return None

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('id', None)
        res.pop('ref', None)
        res['Value'] = self.inner_krl
        return res

    @staticmethod
    def build_ref(ref_ids: List[str]):
        ref = None
        for ref_id in reversed(ref_ids):
            ref = KBReference(ref_id, ref)
        return ref

    @staticmethod
    def parse(ref_str: str) -> 'SimpleReference':
        res = KBReference.parse(ref_str)
        return SimpleReference(id=res.id, ref=res.ref)

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleReference':
        ref_path = xml.attrib.get('Value')
        refs = ref_path.split('.')
        return SimpleReference(id=refs[0], ref=SimpleReference.build_ref(refs[1:]))

    @staticmethod
    def from_dict(d: dict) -> KBReference:
        ref_path = d.get('Value')
        refs = ref_path.split('.')
        return SimpleReference(id=refs[0], ref=SimpleReference.build_ref(refs[1:]))

    def validate(self, kb: 'KnowledgeBase', *args, inst: KBInstance = None, **kwargs):
        return KBReference.validate(self, kb, *args, inst=inst, **kwargs)


class SimpleOperation(KBOperation, SimpleEvaluatable):
    left: SimpleEvaluatable = None
    right: SimpleEvaluatable | None = None

    def __init__(self, sign: str, left: SimpleEvaluatable, right: SimpleEvaluatable | None):
        super().__init__(sign, left, right)
        self.convert_non_factor = False
        self.config(sign, left, right)

    def config(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def sign(self):
        return TAGS_SIGNS[self.op]['values'][0]

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleOperation':
        if xml.tag == 'EqOp':
            return SimpleEqOperation.from_xml(xml)
        elif xml.tag == 'LogOp':
            return SimpleLogOperation.from_xml(xml)
        elif xml.tag == 'ArOp':
            return SimpleArOperation.from_xml(xml)

    @staticmethod
    def from_dict(d: dict) -> 'SimpleOperation':
        if 'tag' not in d:
            if 'Value' in d:
                sign = d.get('Value')
            else:
                sign = d.get('sign')
            for op, data in TAGS_SIGNS.items():
                if sign in data['values']:
                    if data['meta'] in ['eq', 'log', 'math']:
                        d['tag'] = {
                            'eq': 'EqOp',
                            'log': 'LogOp',
                            'math': 'ArOp',
                        }[data['meta']]
                        d['Value'] = op
                        break

        if d.get('tag') == 'EqOp':
            return SimpleEqOperation.from_dict(d)
        elif d.get('tag') == 'LogOp':
            return SimpleLogOperation.from_dict(d)
        elif d.get('tag') == 'ArOp':
            return SimpleArOperation.from_dict(d)

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        return KBOperation.validate(self, kb, *args, **kwargs)
    
    @staticmethod
    def operation_class_by_sign(sign):
        meta = [v['meta'] for v in TAGS_SIGNS.values() if sign in v['values']][0]
        return {
            'eq': SimpleEqOperation,
            'log': SimpleLogOperation,
            'math': SimpleArOperation,
        }[meta]


class SimpleEqOperation(SimpleOperation):
        
    def config(self, sign, *args, **kwargs):
        avalible_signs = [
            s for s, v in TAGS_SIGNS.items() if v.get('meta', None) == 'eq']

        if self.op not in avalible_signs:
            raise ValueError(
                f'Unknown sign "{sign}" to create a {self.__class__.__name__}')

        self.tag = 'EqOp'

    @property
    def attrs(self) -> dict:
        return {'Value': self.op}

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('sign', None)
        res['Value'] = self.op
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleEqOperation':
        sign = xml.attrib.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[_op]['values']:
                op = _op
                break
        left = SimpleEvaluatable.from_xml(xml[0])
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_xml(xml[1])
        return SimpleEqOperation(sign, left, right)

    @staticmethod
    def from_dict(d: dict) -> 'SimpleEqOperation':
        sign = d.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[_op]['values']:
                op = _op
                break
        left = SimpleEvaluatable.from_dict(d.get('left'))
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_dict(d.get('right'))
        return SimpleEqOperation(sign, left, right)


class SimpleLogOperation(SimpleOperation):
    def __init__(self, sign: str, left: SimpleEvaluatable, right: SimpleEvaluatable | None):
        sg = sign.lower()
        super().__init__(sg, left, right)
        
    def config(self, sign, *args, **kwargs):
        avalible_signs = [
            s for s, v in TAGS_SIGNS.items() if v.get('meta', None) == 'log']
        if self.op not in avalible_signs:
            raise ValueError(
                f'Unknown sign "{sign}" to create a {self.__class__.__name__}')

        self.tag = 'LogOp'

    @property
    def attrs(self) -> dict:
        return {'Value': self.op.upper()}

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('sign', None)
        res['Value'] = self.op.upper()
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleLogOperation':
        sign = xml.attrib.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign.lower() in TAGS_SIGNS[_op]['values']:
                op = _op
                break

        left = SimpleEvaluatable.from_xml(xml[0])
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_xml(xml[1])
        return SimpleLogOperation(sign, left, right)

    @staticmethod
    def from_dict(d: dict) -> 'SimpleLogOperation':
        sign = d.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign.lower() in TAGS_SIGNS[_op]['values']:
                op = _op
                break

        left = SimpleEvaluatable.from_dict(d.get('left'))
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_dict(d.get('right'))
        return SimpleLogOperation(sign, left, right)


class SimpleArOperation(SimpleOperation):
    def __init__(self, sign: str, left: SimpleEvaluatable, right: SimpleEvaluatable | None):
        sg = sign.lower()
        super().__init__(sg, left, right)
        
    def config(self, sign, *args, **kwargs):
        avalible_signs = [
            s for s, v in TAGS_SIGNS.items() if v.get('meta', None) == 'math']
        if self.op not in avalible_signs:
            raise ValueError(
                f'Unknown sign "{sign}" to create a {self.__class__.__name__}')
        self.tag = 'ArOp'

    @property
    def attrs(self) -> dict:
        return {'Value': self.sign}

    def __dict__(self) -> dict:
        res = super().__dict__()
        res.pop('sign', None)
        res['Value'] = self.sign
        return res

    @staticmethod
    def from_xml(xml: Element) -> 'SimpleArOperation':
        sign = xml.attrib.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[_op]['values']:
                op = _op

        left = SimpleEvaluatable.from_xml(xml[0])
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_xml(xml[1])
        return SimpleArOperation(sign, left, right)

    @staticmethod
    def from_dict(d: dict) -> 'SimpleArOperation':
        sign = d.get('Value')
        op = None
        for _op in TAGS_SIGNS:
            if sign in TAGS_SIGNS[_op]['values']:
                op = _op
        left = SimpleEvaluatable.from_dict(d.get('left'))
        right = None
        if TAGS_SIGNS[op]['is_binary']:
            right = SimpleEvaluatable.from_dict(d.get('right'))
        return SimpleArOperation(sign, left, right)
