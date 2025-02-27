from dataclasses import dataclass
from typing import TYPE_CHECKING

from at_krl.core.kb_value import Evaluatable
from at_krl.core.simple.simple_operation import SimpleOperation

if TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class KBOperation(Evaluatable, SimpleOperation):
    pass
