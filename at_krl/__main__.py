import argparse
import json
import logging
from xml.dom import minidom
from xml.etree.ElementTree import tostring

from at_krl.core.knowledge_base import KnowledgeBase

MODES = ["atkrl-xml", "atkrl-json", "xml-json", "json-xml", "xml-atkrl", "json-atkrl"]

parser = argparse.ArgumentParser(
    prog="at-krl", description="Parser and convertor of AT-TECHNOLOGY knowledge representation language"
)

parser.add_argument("mode", help=f"[REQUIRED] Mode of converting. can be one of {MODES}")
parser.add_argument("-i", "--input", help="[REQUIRED] Input file path to convert")
parser.add_argument("-o", "--output", required=False, help="[NOT REQUIRED] Destination of output file path to convert")
parser.add_argument(
    "-a",
    "--allen",
    required=False,
    help=(
        "[NOT REQUIRED] Input or output file path to convert from or "
        + "to XML temporal (Allen) objects: events and intervals definitions"
    ),
)
parser.add_argument(
    "-l",
    "--legacy",
    required=False,
    default=False,
    help=("[NOT REQUIRED] A flag that indicates " + " whether legacy xml data provided"),
)


def kb_to_xml(kb: KnowledgeBase, output: str = None, allen: str = None, legacy: bool = False, *args, **kwargs):
    output_path = output
    allen_path = allen

    with_allen = False
    if allen_path:
        with_allen = True
        legacy = True

    kb_xml = kb.get_xml(with_allen=with_allen, legacy=legacy)

    if output_path is not None:
        with open(output_path, "w", encoding="utf-8") as xml_file:
            parsed = minidom.parseString(tostring(kb_xml, encoding="unicode"))
            xml_file.write(parsed.toprettyxml(indent="    "))

        if allen_path is not None:
            with open(allen_path, "w", encoding="utf-8") as allen_file:
                allen_xml = kb.get_allen_xml(legacy=True)
                parsed = minidom.parseString(tostring(allen_xml, encoding="unicode"))
                allen_file.write(parsed.toprettyxml(indent="    "))
    else:
        print(minidom.parseString(tostring(kb_xml, encoding="unicode")).toprettyxml(indent="    "))


def kb_to_krl(kb: KnowledgeBase, output: str = None, *args, **kwargs):
    output_path = output

    if output_path is None:
        print(kb.krl)
    else:
        krl_text = kb.krl
        with open(output_path, "w", encoding="utf-8") as kb_file:
            kb_file.write(krl_text)


def kb_from_krl(input: str, *args, **kwargs):
    with open(input, "r", encoding="utf-8") as krl_file:
        krl_text = krl_file.read()
        return KnowledgeBase.from_krl(krl_text)


def kb_from_xml(input: str, allen: str = None, legacy: bool = False, *args, **kwargs):
    with open(input, "r", encoding="utf-8") as xml_file:
        kb_xml = xml_file.read()
        allen_xml = None
        if allen is not None:
            with open(allen, "r", encoding="utf-8") as allen_file:
                allen_xml = allen_file.read()
                legacy = True
        return KnowledgeBase.from_xml(kb_xml, allen_xml=allen_xml, legacy=legacy)


def kb_to_json(kb: KnowledgeBase, output: str = None, *args, **kwargs):
    d = kb.to_representation()
    if output is not None:
        with open(output, "w", encoding="utf-8") as kb_file:
            kb_file.write(json.dumps(d, indent=4, ensure_ascii=False))
    else:
        print(json.dumps(d, indent=4, ensure_ascii=False))


def kb_from_json(input, *args, **kwargs):
    with open(input, "r", encoding="utf-8") as f:
        d = json.loads(f.read())
        kb = KnowledgeBase.from_json(d)
        return kb


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict.get("mode").startswith("atkrl"):
        kb = kb_from_krl(**args_dict)
    elif args_dict.get("mode").startswith("xml"):
        kb = kb_from_xml(**args_dict)
    elif args_dict.get("mode").startswith("json"):
        kb = kb_from_json(**args_dict)

    kb._raise_on_validation = True
    # if not args_dict.get("force"):
    #     kb.validate()

    if args_dict.get("mode").endswith("krl"):
        kb_to_krl(kb, **args_dict)
    elif args_dict.get("mode").endswith("xml"):
        kb_to_xml(kb, **args_dict)
    elif args_dict.get("mode").endswith("json"):
        kb_to_json(kb, **args_dict)
