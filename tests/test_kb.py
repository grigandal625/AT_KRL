from pytest import fixture

from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.models.knowledge_base import KnowledgeBaseModel
from at_krl.xml_models.knowledge_base import KnowledgeBaseLegacyXMLModel
from at_krl.xml_models.knowledge_base import KnowledgeBaseXMLModel


@fixture
def legacy_big_kb():
    return open("./tests/fixtures/xml/legacy_big_kb.xml").read()


@fixture
def actual_small_kb():
    return open("./tests/fixtures/xml/actual_small_kb.xml").read()


@fixture
def small_kb_krl():
    return open("./tests/fixtures/krl/small_kb.kbs").read()


def test_parse_kb(small_kb_krl):
    # Чтение входного файла
    krl_text = small_kb_krl

    kb = KnowledgeBase.from_krl(krl_text)
    assert kb is not None, "Knowledge base is not parsed correctly"
    assert kb.xml_str is not None, "Knowledge base is not xml-serializing correctly"


def test_kb_from_xml(actual_small_kb):
    xml_data = actual_small_kb

    model = KnowledgeBaseXMLModel.from_xml(xml_data)
    assert model is not None, "Knowledge base is not parsed correctly"
    kb = model.to_internal()
    assert kb.xml_str is not None, "Knowledge base is not internal-serializing correctly"

    new_kb_model = KnowledgeBaseXMLModel.from_xml(kb.xml_str)
    assert new_kb_model is not None, "Knowledge base is not parsed correctly from internal representation"
    new_kb = new_kb_model.to_internal()
    assert new_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"

    legacy_kb_model = KnowledgeBaseLegacyXMLModel.from_xml(kb.legacy_xml_str)
    assert legacy_kb_model is not None, "Knowledge base is not parsed correctly from legacy representation"
    legacy_kb = legacy_kb_model.to_internal()
    assert legacy_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"


def test_legacy_xml(legacy_big_kb):
    xml_data = legacy_big_kb

    model = KnowledgeBaseLegacyXMLModel.from_xml(xml_data)
    assert model is not None, "Knowledge base is not parsed correctly"
    kb = model.to_internal()
    assert kb.xml_str is not None, "Knowledge base is not internal-serializing correctly"

    new_kb_model = KnowledgeBaseLegacyXMLModel.from_xml(kb.legacy_xml_str)
    assert new_kb_model is not None, "Knowledge base is not parsed correctly from internal representation"
    new_kb = new_kb_model.to_internal()
    assert new_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"

    actual_kb_model = KnowledgeBaseXMLModel.from_xml(kb.xml_str)
    assert actual_kb_model is not None, "Knowledge base is not parsed correctly from legacy representation"
    actual_kb = actual_kb_model.to_internal()
    assert actual_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"

    krl_kb = KnowledgeBase.from_krl(kb.krl)
    assert krl_kb is not None, "Knowledge base is not parsed correctly"
    assert krl_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"

    kb_data = kb.to_representation()
    dict_kb_model = KnowledgeBaseModel(**kb_data)
    assert dict_kb_model is not None, "Knowledge base is not parsed correctly"
    dict_kb = dict_kb_model.to_internal()
    assert dict_kb.krl == kb.krl, "Knowledge base after repeatly parsing must be equal"
