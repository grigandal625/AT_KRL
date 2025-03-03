from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Literal
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
    tag: str = field(init=False, default="type")
    meta: str = field(init=False, default="abstract")
    krl_type: str = field(init=False, default="АБСТРАКТНЫЙ", metadata={"serialize": False})

    def get_krl(self, *args, **kwargs):
        return f"""ТИП {self.id}
{self.krl_type}
{self.inner_krl}
КОММЕНТАРИЙ {self.desc or self.id}
"""

    @property
    def inner_krl(self):
        raise NotImplementedError("Not implemented")

    @property
    def attrs(self) -> dict:
        return {"id": self.id, "meta": self.meta, "desc": self.desc or self.id}

    def validate_value(self, value) -> bool:
        raise NotImplementedError("Not implemented")

    @property
    def xml_owner_path(self):
        owner: "KnowledgeBase" = self.owner
        return owner.xml_owner_path + f"/types/type[{[t.id for t in owner.types].index(self.id)}]"


@dataclass(kw_only=True)
class KBNumericType(KBType):
    from_: float | int = field(metadata={"alias": "from"})
    to_: float | int = field(metadata={"alias": "to"})
    meta: Literal["number"] = field(init=False, default="number")
    krl_type: str = field(init=False, default="ЧИСЛО", metadata={"serialize": False})

    @property
    def inner_krl(self):
        return f"""    ОТ {self.from_}
    ДО {self.to_}"""

    def get_inner_xml(self, *args, **kwargs) -> List[Element]:
        f = Element("from")
        f.text = str(self.from_)
        t = Element("to")
        t.text = str(self.to_)
        return [f, t]

    def validate_value(self, value) -> bool:
        from at_krl.core.simple.simple_value import SimpleValue
        from at_krl.core.simple.simple_evaluatable import SimpleEvaluatable

        if isinstance(value, SimpleValue):
            try:
                float(value.content)
            except ValueError:
                return False
        elif isinstance(value, SimpleEvaluatable):
            return True

        try:
            value = float(value.content)
        except ValueError:
            return False

        return isinstance(value, int) or isinstance(value, float)


@dataclass(kw_only=True)
class KBSymbolicType(KBType):
    values: List[str]
    meta: Literal["string"] = field(init=False, default="string")
    krl_type: str = field(init=False, default="СИМВОЛ", metadata={"serialize": False})

    @property
    def inner_krl(self):
        return '    "' + '"\n"'.join(self.values) + '"'

    def get_inner_xml(self, *args, **kwargs) -> List[Element]:
        res = []
        for v in self.values:
            value = Element("value")
            value.text = str(v)
            res.append(value)
        return res

    def validate_value(self, value) -> bool:
        return True


@dataclass(kw_only=True)
class KBFuzzyType(KBType):
    membership_functions: List[MembershipFunction]
    meta: Literal["fuzzy"] = field(init=False, default="fuzzy")
    krl_type: str = field(init=False, default="НЕЧЕТКИЙ", metadata={"serialize": False})

    def __post_init__(self):
        for mf in self.membership_functions:
            mf.owner = self

    @property
    def inner_krl(self):
        return f"{len(self.membership_functions)}\n" + "    \n".join([mf.krl for mf in self.membership_functions])

    def get_inner_xml(self, *args, **kwargs) -> List[Element] | Iterable[Element]:
        return [mf.xml for mf in self.membership_functions]

    def validate_value(self, value) -> bool:
        from at_krl.core.kb_value import Evaluatable

        if isinstance(value, MembershipFunction):
            return True
        if not isinstance(value, Evaluatable):
            return str(value) in [mf.name for mf in self.membership_functions]
        else:
            return True
