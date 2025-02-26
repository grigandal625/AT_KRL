from dataclasses import dataclass, field
from collections.abc import Iterable as ITR
from typing import Literal

from at_krl.core.simple.simple_class import SimpleClass
from xml.etree.ElementTree import Element
from at_krl.core.simple.legacy import LegacyMixin


@dataclass(kw_only=True)
class AllenClass(SimpleClass, LegacyMixin):
    pass