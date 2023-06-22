from at_krl.core.kb import KBEntity
from at_krl.core.kb_value import Evaluatable
from at_krl.core.kb_reference import KBReference
from at_krl.core.non_factor import NonFactor
from xml.etree.ElementTree import Element


from typing import Union


class KBInstruction(KBEntity):
    non_factor: Union[NonFactor, None] = None
    convert_non_factor: bool = True

    def __init__(self, non_factor: Union[NonFactor, None] = None) -> None:
        super().__init__()
        self.non_factor = non_factor if non_factor is not None else NonFactor()

    def perform(self, env, *args, **kwargs):
        pass



class AssignInstruction(KBInstruction):

    def __init__(self, ref: KBReference, value: Evaluatable, non_factor: Union[NonFactor, None] = None) -> None:
        super().__init__(non_factor)
        self.tag = 'assign'


