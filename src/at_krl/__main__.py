import argparse

from antlr4 import CommonTokenStream, InputStream
from at_krl.grammar.at_krlLexer import at_krlLexer
from at_krl.grammar.at_krlParser import at_krlParser
from at_krl.utils.listener import ATKRLListener
from at_krl.utils.error_listener import ATKRLErrorListener
from xml.etree.ElementTree import ElementTree, tostring, indent
import json

from at_krl.core.knowledge_base import KnowledgeBase

MODES = ['atkrl-xml', 'atkrl-json', 'xml-json',
         'json-xml', 'xml-atkrl', 'json-atkrl']

parser = argparse.ArgumentParser(
    prog='at-krl',
    description='Parser and convertor of AT-TECHNOLOGY knowledge representation language')

parser.add_argument(
    'mode', help=f'[REQUIRED] Mode of converting. can be one of {MODES}')
parser.add_argument(
    '-i', '--input', help='[REQUIRED] Input file path to convert')
parser.add_argument('-o', '--output', required=False,
                    help='[NOT REQUIRED] Destination of output file path to convert')
parser.add_argument('-a', '--allen', required=False,
                    help='[NOT REQUIRED] Input or output file path to convert from or to XML temporal (Allen) objects: events and intervals definitions')
parser.add_argument('-f', '--force', required=False, default=False,
                    help='[NOT REQUIRED] A flag to force converting without validation')

def kb_to_xml(kb: KnowledgeBase, output: str = None, allen: str = None, *args, **kwargs):
    output_path = output
    allen_path = allen

    if output_path is not None:
        if allen_path is None:
            kb_xml = kb.get_xml()
        else:
            kb_xml = kb.get_xml(with_allen=False)

        with open(output_path, 'w') as xml_file:
            tree = ElementTree(kb_xml)
            indent(tree, space="\t", level=0)
            xml_file.write(tostring(tree.getroot(), encoding='utf-8').decode())

        if allen_path is not None:
            with open(allen_path, 'w') as allen_file:
                allen_xml = kb.allen_xml
                tree = ElementTree(allen_xml)
                indent(tree, space="\t", level=0)
                allen_file.write(
                    tostring(tree.getroot(), encoding='utf-8').decode())
    else:
        kb_xml = kb.get_xml()
        tree = ElementTree(kb_xml)
        indent(tree, space="\t", level=0)
        print(tostring(tree.getroot(), encoding='utf-8').decode())


def kb_to_krl(kb: KnowledgeBase, output: str = None, *args, **kwargs):
    output_path = output

    if output_path is None:
        print(kb.krl)
    else:
        krl_text = kb.krl
        with open(output_path, 'w') as kb_file:
            kb_file.write(krl_text)


def kb_from_krl(input: str, *args, **kwargs):
    with open(input, 'r') as krl_file:
        krl_text = krl_file.read()

        input_stream = InputStream(krl_text)
        lexer = at_krlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = at_krlParser(stream)

        listener = ATKRLListener()
        parser.addParseListener(listener)
        parser.removeErrorListeners()
        parser.addErrorListener(ATKRLErrorListener())
        tree = parser.knowledge_base()

        if tree.exception:
            print(tree.exception)
            exit(0)
        return listener.KB


def kb_from_xml(input: str, allen: str = None, *args, **kwargs):
    with open(input, 'r') as xml_file:
        tree = ElementTree(file=xml_file)
        kb_xml = tree.getroot()
        allen_xml = None
        if allen is not None:
            with open(allen, 'r') as allen_file:
                allen_tree = ElementTree(file=allen_file)
                allen_xml = allen_tree.getroot()

        return KnowledgeBase.from_xml(kb_xml, allen_xml=allen_xml)


def kb_to_json(kb: KnowledgeBase, output: str = None, *args, **kwargs):
    d = kb.__dict__()
    if output is not None:
        with open(output, 'w') as kb_file:
            kb_file.write(json.dumps(d, indent=4, ensure_ascii=False))
    else:
        print(json.dumps(d, indent=4, ensure_ascii=False))


def kb_from_json(input, *args, **kwargs):
    with open(input, 'r') as f:
        d = json.loads(f.read())
        kb = KnowledgeBase.from_dict(d)
        return kb


if __name__ == "__main__":
    args = parser.parse_args()
    args_dict = vars(args)
    if args_dict.get('mode').startswith('atkrl'):
        kb = kb_from_krl(**args_dict)
    elif args_dict.get('mode').startswith('xml'):
        kb = kb_from_xml(**args_dict)
    elif args_dict.get('mode').startswith('json'):
        kb = kb_from_json(**args_dict)

    kb._raise_on_validation = True
    if not args_dict.get('force'):
        kb.validate()

    if args_dict.get('mode').endswith('krl'):
        kb_to_krl(kb, **args_dict)
    elif args_dict.get('mode').endswith('xml'):
        kb_to_xml(kb, **args_dict)
    elif args_dict.get('mode').endswith('json'):
        kb_to_json(kb, **args_dict)
