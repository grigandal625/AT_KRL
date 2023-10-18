from at_krl.core.kb_value import KBValue
from at_krl.core.kb_reference import KBReference
from at_krl.core.kb_operation import KBOperation

from xml.etree.ElementTree import tostring, fromstring


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