import logging
from dataclasses import dataclass
from dataclasses import field
from typing import Literal
from typing import TYPE_CHECKING

from at_krl.core.kb_value import Evaluatable
from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_reference import SimpleReference


logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class KBReference(Evaluatable, SimpleReference):
    legacy_tag: Literal["ref"] = field(default="ref", init=False)

    @staticmethod
    def from_simple(ref):
        return KBReference(id=ref.id, ref=KBReference.from_simple(ref.ref) if ref.ref else None, non_factor=NonFactor())

    @property
    def legacy_attrs(self):
        return self.attrs

    @property
    def legacy_inner_xml(self):
        return self.get_inner_xml()
