import logging
from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.kb_value import Evaluatable
from at_krl.core.kb_value import NonFactor
from at_krl.core.simple.simple_reference import SimpleReference

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass


@dataclass
class KBReference(Evaluatable, SimpleReference):
    id: str
    ref: Optional["KBReference"] = field(default=None)

    @property
    def attrs(self) -> dict:
        return dict(id=self.id)

    @staticmethod
    def from_dict(d: dict) -> "KBReference":
        return KBReference(
            d["id"],
            KBReference.from_dict(d["ref"]) if d.get("ref", None) else None,
            non_factor=NonFactor.from_dict(d.get("non_factor", None)),
        )

    @property
    def inner_xml(self) -> Element:
        return self.ref.xml if self.ref is not None else None
