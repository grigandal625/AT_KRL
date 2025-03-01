from dataclasses import dataclass
from logging import getLogger
from typing import List
from typing import TYPE_CHECKING
from xml.etree.ElementTree import Element

from at_krl.core.simple.simple_operation import SimpleOperation
from at_krl.core.temporal.allen_reference import AllenReference

logger = getLogger(__name__)

if TYPE_CHECKING:
    pass


TEMPORAL_TAGS_SIGNS = {
    # default: interval_interval: True, event_event: False, event_interval: False
    "b": {"event_event": True, "event_interval": True, "inversion": "bi"},
    "bi": {"inversion": "b"},
    "m": {"inversion": "mi"},
    "mi": {"inversion": "m"},
    "s": {"event_interval": True, "inversion": "si"},
    "si": {"inversion": "s"},
    "f": {"inversion": "fi"},
    "fi": {"inversion": "f"},
    "d": {"event_interval": True, "inversion": "di"},
    "di": {"inversion": "d"},
    "o": {"inversion": "oi"},
    "oi": {"inversion": "o"},
    "e": {"event_event": True, "inversion": "e"},
    "a": {"interval_interval": False, "event_interval": True, "inversion": "b"},
}


def get_inversion(op: str) -> str:
    return TEMPORAL_TAGS_SIGNS.get(op, {}).get("inversion")


@dataclass(kw_only=True)
class AllenOperation(SimpleOperation):
    left: AllenReference
    right: AllenReference

    def __post_init__(self):
        self.tag = self.sign
        self.operation_name = self.sign

        # для legacy-тэга попытаемся определить вид операции по знаку
        for_what_matrix = list(self.for_what.values())
        if for_what_matrix.count(True) == 1:
            if self.for_what.get("interval_interval"):
                self.legacy_tag = "IntRel"
            elif self.for_what.get("event_event"):
                self.legacy_tag = "EvRel"
            elif self.for_what.get("event_interval"):
                self.legacy_tag = "EvIntRel"
        # если правая и левая часть известны - можем также сразу определить
        elif self.left.fullfiled and self.right.fullfiled:
            self.fullfill_legacy_tag()
        else:
            logger.warning(f"Can't now determine operation type for {self.krl}. Will be determined in KB validation.")
        # если не вышло, то вид операции определим во время валидации БЗ

    def fullfill_legacy_tag(self):
        if not self.left.fullfiled or not self.right.fullfiled:
            return
        if self.left.target.legacy_tag == "Event" and self.right.target.legacy_tag == "Interval":
            self.legacy_tag = "EvIntRel"
            self.validate_for_what()
        elif self.left.target.legacy_tag == "Interval" and self.right.target.legacy_tag == "Interval":
            self.legacy_tag = "IntRel"
            self.validate_for_what()
        elif self.left.target.legacy_tag == "Event" and self.right.target.legacy_tag == "Event":
            self.legacy_tag = "EvRel"
            self.validate_for_what()
        elif self.left.target.legacy_tag == "Interval" and self.right.target.legacy_tag == "Event":
            left = self.left
            right = self.right
            new_operation = get_inversion(self.sign)

            self.sign = new_operation
            self.left = right
            self.right = left
            self.__post_init__()
            self.validate_for_what()
        else:
            logger.warning(f"Can't now determine operation type for {self.krl}. Will be determined in KB validation.")

    def validate_for_what(self):
        assert self.left.fullfiled, f"Expected fullfilled allen reference {self.left.id} for allen operation"
        assert self.right.fullfiled, f"Expected fullfilled allen reference {self.right.id} for allen operation"
        if self.legacy_tag == "EvIntRel":
            assert self.left.target.legacy_tag == "Event", f'Expected left part of operation "{self.krl}" as event'
            assert (
                self.right.target.legacy_tag == "Interval"
            ), f'Expected right part of operation "{self.krl}" as interval'
            assert self.for_what[
                "event_interval"
            ], f'Expected supporting operation between event and interval for "{self.krl}"'
        elif self.legacy_tag == "EvRel":
            assert self.left.target.legacy_tag == "Event", f'Expected left part of operation "{self.krl}" as event'
            assert self.right.target.legacy_tag == "Event", f'Expected right part of operation "{self.krl}" as event'
            assert self.for_what[
                "event_event"
            ], f'Expected supporting operation between event and event for "{self.krl}"'
        elif self.legacy_tag == "IntRel":
            assert (
                self.left.target.legacy_tag == "Interval"
            ), f'Expected left part of operation "{self.krl}" as interval'
            assert (
                self.right.target.legacy_tag == "Interval"
            ), f'Expected right part of operation "{self.krl}" as interval'
            assert self.for_what[
                "interval_interval"
            ], f'Expected supporting operation between interval and interval for "{self.krl}"'

    @property
    def for_what(self) -> dict:
        _for_what = TEMPORAL_TAGS_SIGNS.get(self.operation_name)
        for_what = {}
        for_what["interval_interval"] = _for_what.get("interval_interval", True)
        for_what["event_event"] = _for_what.get("event_event", False)
        for_what["event_interval"] = _for_what.get("event_interval", False)
        return for_what

    def get_krl(self, *args, **kwargs):
        return f"{self.left.krl} {self.sign} {self.right.krl}"

    @property
    def legacy_attrs(self) -> dict:
        return {"Value": self.operation_name}

    @property
    def legacy_inner_xml(self) -> List[Element]:
        left = Element(self.left.target.legacy_tag)
        left.attrib["Name"] = self.left.id

        right = Element(self.right.target.legacy_tag)
        right.attrib["Name"] = self.right.id

        return [left, right]

    @property
    def legacy_available(self) -> bool:
        return self.legacy_tag in ["EvIntRel", "EvRel", "IntRel"]

    @property
    def is_binary(self) -> bool:
        return True

    def to_simple(self):
        return self
