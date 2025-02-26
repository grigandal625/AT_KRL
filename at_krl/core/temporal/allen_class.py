from dataclasses import dataclass

from at_krl.core.simple.legacy import LegacyMixin
from at_krl.core.simple.simple_class import SimpleClass


@dataclass(kw_only=True)
class AllenClass(SimpleClass, LegacyMixin):
    pass
