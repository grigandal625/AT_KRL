from xml.etree.ElementTree import Element
from at_krl.core.kb_entity import KBEntity


def num(v):
    i = int(v)
    f = float(v)

    if i == f:
        return i
    return f


class NonFactor(KBEntity):
    belief: float = None
    probability: float = None
    accuracy: float = None
    initialized: bool = None

    def __init__(self, belief: float = None, probability: float = None, accuracy: float = None, *args, **kwargs):
        self.belief = num(belief if belief is not None else 50)
        self.probability = num(
            probability if probability is not None else 100)
        self.accuracy = num(accuracy if accuracy is not None else 0)
        self.tag = 'with'
        self.initialized = (belief is not None) and (
            probability is not None) or (accuracy is not None)

    def __dict__(self) -> dict:
        return dict(
            belief=self.belief,
            probability=self.probability,
            accuracy=self.accuracy,
            **super().__dict__()
        )

    @staticmethod
    def from_dict(d: dict | None) -> 'NonFactor':
        if d is None:
            return NonFactor()
        return NonFactor(**d)

    @property
    def is_default(self):
        return self.belief == 50 and self.probability == 100 and self.accuracy == 0

    @property
    def attrs(self) -> dict:
        return {
            'belief': str(self.belief),
            'probability': str(self.probability),
            'accuracy': str(self.accuracy)
        }

    @staticmethod
    def from_xml(xml: Element | None) -> 'NonFactor':
        return NonFactor(
            belief=xml.attrib.get('belief', None),
            probability=xml.attrib.get('probability', None),
            accuracy=xml.attrib.get('accuracy', None),
        ) if xml is not None else NonFactor()

    @property
    def krl(self) -> str:
        return f'УВЕРЕННОСТЬ [{self.belief}; {self.probability}] ТОЧНОСТЬ {self.accuracy}'

    @property
    def xml_owner_path(self):
        return self.owner.xml_owner_path + '/with'