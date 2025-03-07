from dataclasses import dataclass
from typing import TYPE_CHECKING

from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_value import Evaluatable
from at_krl.core.kb_value import KBValue
from at_krl.core.non_factor import NonFactor
from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.core.simple.simple_reference import SimpleReference
from at_krl.core.simple.simple_value import SimpleValue

if TYPE_CHECKING:
    pass


@dataclass(kw_only=True)
class KBOperation(Evaluatable, SimpleOperation):
    def __post_init__(self):
        super().__post_init__()
        self.legacy_tag = self.tag

    @staticmethod
    def from_simple(op: SimpleOperation):
        return KBOperation(
            sign=op.sign,
            left=SIMPLE_TO_EVALUATABLE[op.left.__class__].from_simple(op.left),
            right=SIMPLE_TO_EVALUATABLE[op.right.__class__].from_simple(op.right) if op.right else None,
            non_factor=NonFactor(),
        )

    @property
    def legacy_attrs(self):
        return self.attrs

    @property
    def legacy_available(self) -> bool:
        return True


SIMPLE_TO_EVALUATABLE = {
    SimpleOperation: KBOperation,
    SimpleValue: KBValue,
    SimpleReference: KBReference,
    KBValue: KBValue,
    KBReference: KBReference,
    KBOperation: KBOperation,
}
