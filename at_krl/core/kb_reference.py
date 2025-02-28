import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from at_krl.core.kb_value import Evaluatable
from at_krl.core.simple.simple_reference import SimpleReference

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass


@dataclass
class KBReference(Evaluatable, SimpleReference):
    pass
