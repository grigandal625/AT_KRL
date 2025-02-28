import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from at_krl.core.kb_value import Evaluatable
from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_reference import SimpleReference

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class KBReference(Evaluatable, SimpleReference):
    @staticmethod
    def from_simple(ref):
        return KBReference(id=ref.id, ref=KBReference.from_simple(ref.ref) if ref.ref else None, non_factor=NonFactor())
