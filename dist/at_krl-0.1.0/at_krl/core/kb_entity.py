from xml.etree.ElementTree import Element
from typing import List, Iterable, Union, TYPE_CHECKING
from collections.abc import Iterable as ITR

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


class KBEntity:
    tag: str = None
    _validated: bool = False
    owner: 'KBEntity' = None

    def __dict__(self) -> dict:
        return dict(tag=self.tag)

    @staticmethod
    def from_dict(d: dict) -> 'KBEntity':
        pass

    @property
    def attrs(self) -> dict:
        return {}

    @property
    def inner_xml(self) -> Union[str, Element, List[Element], Iterable[Element], None]:
        return None

    @property
    def krl(self) -> str:
        pass

    def getText(self) -> str:
        return self.krl

    @property
    def xml(self) -> Element:
        result = Element(self.tag, self.attrs)
        inner_xml = self.inner_xml
        if inner_xml is not None:
            if isinstance(inner_xml, str):
                result.text = inner_xml
            elif isinstance(inner_xml, Element):
                result.append(inner_xml)
            elif isinstance(inner_xml, ITR):
                for e in inner_xml:
                    result.append(e)
        return result

    @staticmethod
    def from_xml(xml: Element) -> 'KBEntity':
        pass

    def validate(self, kb: 'KnowledgeBase', *args, **kwargs):
        self._validated = True


    @property
    def xml_owner_path(self) -> str:
        pass

    @property
    def _unknown_ownership(self):
        owner_label = self.owner.id if hasattr(self.owner, 'id') else str(self.owner)
        owner_type = self.owner.__class__.__name__
        return f'''Unknown ownership of {owner_type} {owner_label} for {self}

{owner_type} krl: {self.owner.krl}

{self} krl: {self.krl}'''