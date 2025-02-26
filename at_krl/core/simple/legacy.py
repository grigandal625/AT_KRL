from collections.abc import Iterable
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Union
from xml.etree.ElementTree import Element


@dataclass(kw_only=True)
class LegacyMixin:
    legacy_tag: str = field(init=False)

    @property
    def legacy_attrs(self) -> str:
        raise NotImplementedError("Not implemented")

    @property
    def legacy_inner_xml(self) -> Union[str, Element, List[Element], Iterable[Element], None]:
        raise NotImplementedError("Not implemented")

    @property
    def legacy_xml(self) -> Element:
        if not self.legacy_avalible:
            raise ValueError(f"Legacy representation is not avalible for {self.krl}")
        result = Element(self.legacy_tag, self.legacy_attrs)
        inner_xml = self.legacy_inner_xml
        if inner_xml is not None:
            if isinstance(inner_xml, str):
                result.text = inner_xml
            elif isinstance(inner_xml, Element):
                result.append(inner_xml)
            elif isinstance(inner_xml, Iterable):
                for e in inner_xml:
                    result.append(e)
        return result

    @property
    def legacy_avalible(self) -> bool:
        raise NotImplementedError("Not implemented")
