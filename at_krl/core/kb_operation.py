from dataclasses import dataclass
from typing import TYPE_CHECKING

from at_krl.core.kb_value import Evaluatable
from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_operation import SimpleOperation

if TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class KBOperation(Evaluatable, SimpleOperation):
    @staticmethod
    def from_simple(op: SimpleOperation):
        return KBOperation(
            sign=op.sign,
            left=op.left.from_simple(op.left),
            right=op.right.from_simple(op.right) if op.right else None,
            non_factor=NonFactor(),
        )
