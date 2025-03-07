from typing import Optional

from pydantic_xml import attr

from at_krl.xml_models.kb_entity import KBEntityXMLModel


class SimpleClassXMLModel(KBEntityXMLModel, tag="class"):
    id: str = attr()
    # group: Optional[str] = attr(default=None)
    desc: Optional[str] = attr(default=None)
