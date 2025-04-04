from collections.abc import Iterable
from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Union
from xml.etree.ElementTree import Element


@dataclass(kw_only=True)
class LegacyMixin:
    legacy_tag: str = field(init=False, repr=False, metadata={"serialize": False})

    @property
    def legacy_attrs(self) -> str:
        return {}

    @property
    def legacy_inner_xml(self) -> Union[str, Element, List[Element], Iterable[Element], None]:
        raise NotImplementedError("Not implemented")

    @property
    def legacy_xml(self) -> Element:
        if not self.legacy_available:
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
    def legacy_available(self) -> bool:
        return True

    def get_xml(self, *args, legacy=False, **kwargs):
        if legacy:
            return self.legacy_xml
        else:
            return super().get_xml(*args, **kwargs)
