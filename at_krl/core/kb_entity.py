from collections.abc import Iterable as ITR
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Iterable
from typing import List
from typing import TYPE_CHECKING
from typing import Union
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBEntity:
    tag: str = field(init=False)
    owner: "KBEntity" = field(init=False, default=None, metadata={"serialize": False}, repr=False)

    _validated: bool = field(init=False, default=False, metadata={"serialize": False})

    def to_representation(self):
        return {
            (f.metadata.get("alias") or f.name): self._represent(getattr(self, f.name))
            for f in fields(self)
            if f.metadata.get("serialize", True)
        }

    @staticmethod
    def _represent(item):
        if isinstance(item, KBEntity):
            return item.to_representation()
        if isinstance(item, list):
            return [KBEntity._represent(i) for i in item]
        if isinstance(item, dict):
            return {key: KBEntity._represent(value) for key, value in item.items()}
        return item

    @property
    def attrs(self) -> dict:
        return {}

    def get_inner_xml(self, *args, **kwargs) -> Union[str, Element, List[Element], Iterable[Element], None]:
        return None

    def get_krl(self, *args, **kwargs) -> str:
        raise NotImplementedError("Not implemented")

    @property
    def krl(self) -> str:
        return self.get_krl()

    def getText(self) -> str:
        return self.krl

    def get_xml(self, *args, **kwargs) -> Element:
        result = Element(self.tag, attrib=self.attrs)
        inner_xml = self.get_inner_xml(*args, **kwargs)
        if inner_xml is not None:
            if isinstance(inner_xml, str):
                result.text = inner_xml
            elif isinstance(inner_xml, Element):
                result.append(inner_xml)
            elif isinstance(inner_xml, ITR):
                for e in inner_xml:
                    result.append(e)
        return result

    @property
    def xml(self):
        return self.get_xml()

    @property
    def xml_str(self):
        return tostring(self.xml, encoding="unicode")

    @property
    def legacy_xml_str(self):
        return tostring(self.get_xml(legacy=True), encoding="unicode")

    def validate(self, kb: "KnowledgeBase", *args, **kwargs):
        raise NotImplementedError("Not implemented")

    @property
    def xml_owner_path(self) -> str:
        raise NotImplementedError("Not implemented")

    @property
    def _unknown_ownership(self):
        owner_label = self.owner.id if hasattr(self.owner, "id") else str(self.owner)
        owner_type = self.owner.__class__.__name__
        return f"""Unknown ownership of {owner_type} {owner_label} for {self}

{owner_type} krl: {self.owner.krl}

{self} krl: {self.krl}"""
