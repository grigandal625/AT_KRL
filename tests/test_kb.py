from at_krl.core.kb_value import KBValue
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_operation import KBOperation, TAGS_SIGNS

from xml.etree.ElementTree import tostring, fromstring

from antlr4 import CommonTokenStream, InputStream
from at_krl.grammar.at_krlLexer import at_krlLexer
from at_krl.grammar.at_krlParser import at_krlParser
from at_krl.utils.listener import ATKRLListener
from at_krl.utils.error_listener import ATKRLErrorListener


def test_kb_value_from_xml():
    xml = fromstring("<value>test</value>")
    kb_value = KBValue.from_xml(xml)
    
    assert kb_value.content == "test"
    assert kb_value.krl == "\"test\""
    assert kb_value.xml.text == "test"
    assert kb_value.xml.tag == "value"
    print('\n\n')
    print('----------------------- TESTS --------------------------------')
    print('\n')
    print('VALUE KRL:', kb_value.krl)
    print('VALUE XML:', tostring(kb_value.xml).decode("utf-8"))


def test_kb_reference_from_xml():
    xml = fromstring("""
        <ref id="OBJECT_1">
            <ref id="PROPERTY_1" />
        </ref>
    """)
    kb_reference = KBReference.from_xml(xml)
    assert kb_reference.id == "OBJECT_1"
    assert kb_reference.ref.id == "PROPERTY_1"
    assert kb_reference.xml.tag == "ref"
    assert kb_reference.xml.attrib["id"] == "OBJECT_1"
    assert kb_reference.ref.xml.tag == "ref"
    assert kb_reference.ref.xml.attrib["id"] == "PROPERTY_1"
    print('\n')
    print('REF KRL:', kb_reference.krl)
    print('REF XML:', tostring(kb_reference.xml).decode("utf-8"))


def test_operation_from_xml():
    xml = fromstring("""
    <or>    
        <eq>
            <ref id="OBJECT_1">
                <ref id="PROPERTY_1" />
            </ref>
            <value>test</value>
        </eq>
        <ne>
            <ref id="OBJECT_1">
                <ref id="PROPERTY_2" />
            </ref>
            <value>5</value>
            <with belief="10" probability="15" accuracy="0"/>
        </ne>
    </or>
    """)
    kb_operation = KBOperation.from_xml(xml)

    assert kb_operation.tag == "or"
    print('\n')
    print('OP KRL:', kb_operation.krl)
    print('OP XML:', tostring(kb_operation.xml).decode("utf-8"))
    print('OP DICT:', kb_operation.__dict__())

    d = kb_operation.__dict__()
    o = KBOperation.from_dict(d)

    assert o.sign == kb_operation.sign
    # assert kb_operation.krl == o.krl

    print('OP KRL:', o.krl)


def print_v_xml_paths(op: KBOperation):
    if op.tag in TAGS_SIGNS:
        print_v_xml_paths(op.left)
        if op.is_binary:
            print_v_xml_paths(op.right)
    print(op.xml_owner_path)

def test_examples():
    with open('example/test.kbs') as krl_file:
        krl_text = krl_file.read() # считываем текст БЗ
        input_stream = InputStream(krl_text)
        lexer = at_krlLexer(input_stream) # создаем лексер
        stream = CommonTokenStream(lexer)
        parser = at_krlParser(stream) # создаем парсер

        listener = ATKRLListener()
        parser.addParseListener(listener) # добавляем лисенер

        error_listener = ATKRLErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        tree = parser.knowledge_base() # даем команду распарсить БЗ

        # После этого в объекте listener в свойсте KB будет загруженная бз

        kb = listener.KB

        print('------ KB ------')
        for t in kb.types: # пеатаем все типы
            print(t.id)
            print(t.xml_owner_path)
        
        for p in kb.world.properties: # печатаем все объекты
            print(p.id, p.type_or_class_id)
            print(p.xml_owner_path)
            print(p._type_or_class.xml_owner_path)

        for i in kb.classes.intervals: # печатаем все интервалы
            print(i.id)
            print(i.xml_owner_path)

        for e in kb.classes.events: # печатаем все события
            print(e.id)
            print(e.xml_owner_path)

        for r in kb.world.rules: # печатаем все правила
            print(r.id)
            print(r.xml_owner_path)
            print_v_xml_paths(r.condition)
            

            