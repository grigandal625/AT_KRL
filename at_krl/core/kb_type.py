from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.fuzzy.membership_function import MembershipFunction
from at_krl.core.kb_entity import KBEntity

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class KBType(KBEntity):
    id: str = field(default=None)
    desc: str = field(default=None)
    tag: str = "type"

    @property
    def meta(self):
        return "abstract"

    @property
    def krl_type(self):
        return "АБСТРАКТНЫЙ"

    @property
    def krl(self):
        return f"""ТИП {self.id}
{self.krl_type}
{self.inner_krl}
КОММЕНТАРИЙ {self.desc}
"""

    @property
    def inner_krl(self):
        return ""

    @property
    def attrs(self) -> dict:
        return {"id": self.id, "meta": self.meta, "desc": self.desc, **super().attrs}

    @staticmethod
    def from_xml(xml: Element) -> "KBType":
        if (xml.attrib.get("meta") == "numeric") or (xml.attrib.get("meta") == "number"):
            return KBNumericType.from_xml(xml)
        elif (xml.attrib.get("meta") == "string") or (xml.attrib.get("meta") == "symbolic"):
            return KBSymbolicType.from_xml(xml)
        elif xml.attrib.get("meta") == "fuzzy":
            return KBFuzzyType.from_xml(xml)

    @staticmethod
    def from_dict(d: dict) -> "KBType":
        if (d.get("meta") == "numeric") or (d.get("meta") == "number"):
            return KBNumericType.from_dict(d)
        elif (d.get("meta") == "string") or (d.get("meta") == "symbolic"):
            return KBSymbolicType.from_dict(d)
        elif d.get("meta") == "fuzzy":
            return KBFuzzyType.from_dict(d)

    def validate_value(self, value) -> bool:
        return False

    @property
    def xml_owner_path(self):
        owner: "KnowledgeBase" = self.owner
        return owner.xml_owner_path + f"/types/type[{[t.id for t in owner.types].index(self.id)}]"


@dataclass(kw_only=True)
class KBNumericType(KBType):
    _from: float | int = field(default=None)
    _to: float | int = field(default=None)

    @property
    def meta(self):
        return "number"

    @property
    def krl_type(self):
        return "ЧИСЛО"

    @property
    def inner_krl(self):
        return f"""ОТ {self._from}
ДО {self._to}"""

    @property
    def inner_xml(self) -> List[Element]:
        f = Element("from")
        f.text = str(self._from)
        t = Element("to")
        t.text = str(self._to)
        return [f, t]

    @staticmethod
    def from_xml(xml: Element) -> "KBNumericType":
        from_ = float(xml.find("from").text)
        to_ = float(xml.find("to").text)
        id = xml.attrib.get("id")
        desc = xml.attrib.get("desc", None)
        return KBNumericType(id, from_, to_, desc=desc)

    @staticmethod
    def from_dict(d: dict) -> "KBNumericType":
        id = d.get("id")
        desc = d.get("desc", None)
        from_ = d.get("from")
        to_ = d.get("to")
        return KBNumericType(id, from_, to_, desc=desc)

    def validate_value(self, value) -> bool:
        from at_krl.core.kb_value import Evaluatable

        if isinstance(value, Evaluatable):
            return True
        try:
            value = float(value)
        except ValueError:
            pass

        return isinstance(value, int) or isinstance(value, float)


@dataclass(kw_only=True)
class KBSymbolicType(KBType):
    values: List[str] = field(default_factory=list)

    @property
    def meta(self):
        return "string"

    @property
    def krl_type(self):
        return "СИМВОЛ"

    @property
    def inner_krl(self):
        return '"' + '"\n"'.join(self.values) + '"'

    @property
    def inner_xml(self) -> List[Element]:
        res = []
        for v in self.values:
            value = Element("value")
            value.text = str(v)
            res.append(value)
        return res

    @staticmethod
    def from_xml(xml: Element) -> "KBSymbolicType":
        return KBSymbolicType(id=xml.attrib.get("id"), desc=xml.attrib.get("desc", None), values=[v.text for v in xml])

    @staticmethod
    def from_dict(d: dict) -> "KBSymbolicType":
        return KBSymbolicType(
            id=d.get("id"),
            desc=d.get("desc", None),
            values=d.get("values", []),
        )

    def validate_value(self, value) -> bool:
        return True


@dataclass(kw_only=True)
class KBFuzzyType(KBType):
    membership_functions: List[MembershipFunction] = field(default_factory=list)

    def __post_init__(self):
        for mf in self.membership_functions:
            mf.owner = self

    @property
    def meta(self):
        return "fuzzy"

    @property
    def krl_type(self):
        return "НЕЧЕТКИЙ"

    @property
    def inner_krl(self):
        return f"{len(self.membership_functions)}\n" + "\n".join([mf.krl for mf in self.membership_functions])

    @property
    def inner_xml(self) -> List[Element] | Iterable[Element]:
        return [mf.xml for mf in self.membership_functions]

    @staticmethod
    def from_xml(xml: Element) -> "KBFuzzyType":
        return KBFuzzyType(
            id=xml.attrib.get("id"),
            desc=xml.attrib.get("desc", None),
            membership_functions=[MembershipFunction.from_xml(parameter) for parameter in xml],
        )

    @staticmethod
    def from_dict(d: dict) -> "KBFuzzyType":
        return KBFuzzyType(
            id=d.get("id"),
            desc=d.get("desc", None),
            membership_functions=[
                MembershipFunction.from_dict(parameter) for parameter in d.get("membership_functions", [])
            ],
        )

    def validate_value(self, value) -> bool:
        from at_krl.core.kb_value import Evaluatable

        if isinstance(value, Evaluatable):
            return True
        if isinstance(value, MembershipFunction):
            return True
        else:
            return str(value) in [mf.name for mf in self.membership_functions]
