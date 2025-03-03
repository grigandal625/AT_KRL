from typing import Any
from typing import Dict
from typing import Mapping
from typing import Optional
from typing import Type
from typing import TYPE_CHECKING

from pydantic_xml import errors
from pydantic_xml.element import XmlElementReader
from pydantic_xml.element import XmlElementWriter
from pydantic_xml.serializers.factories.model import ModelProxySerializer
from pydantic_xml.serializers.factories.model import ModelSerializer
from pydantic_xml.serializers.serializer import Serializer

if TYPE_CHECKING:
    from at_krl.xml_models.utils.models import MultiTagXmlModel


class MultiTagModelSerializer(ModelSerializer):
    """
    Сериализатор для моделей с поддержкой нескольких тегов.
    """

    def __init__(self, model: Type["MultiTagXmlModel"]):
        if not model.__xml_tags__:
            raise ValueError("Model must have at least one XML tag")

        self._model = model
        self._element_tags = model.__xml_tags__
        self._element_name = self._element_tags[0]
        self._ns = model.__xml_ns__
        self._nsmap = model.__xml_nsmap__
        self._field_serializers = self._init_field_serializers()
        self._fields_validation_aliases = {}
        self._fields_serialization_exclude = set()

    @property
    def model(self) -> Type["MultiTagXmlModel"]:
        return self._model

    @property
    def element_name(self) -> str:
        return self._element_name

    @property
    def nsmap(self) -> Optional[Dict[str, str]]:
        return self._nsmap

    @property
    def fields_serializers(self) -> Mapping[str, "Serializer"]:
        return self._field_serializers

    def _init_field_serializers(self) -> Dict[str, "Serializer"]:
        # Логика инициализации сериализаторов полей
        return {}

    def serialize(
        self, element: XmlElementWriter, value: "MultiTagXmlModel", encoded: Dict[str, Any], **kwargs
    ) -> Optional[XmlElementWriter]:
        # Используем сохраненный тег или первый из списка
        tag = value._xml_tag or self._element_tags[0]
        sub_element = element.make_element(tag, nsmap=self._nsmap)
        return super().serialize(sub_element, value, encoded, **kwargs)

    def deserialize(self, element: Optional[XmlElementReader], **kwargs) -> Optional["MultiTagXmlModel"]:
        if element is None:
            return None

        if element.tag not in self._element_tags:
            raise errors.ParsingError(f"Unexpected tag '{element.tag}'. Expected: {self._element_tags}")

        return super().deserialize(element, **kwargs)


class MultiTagModelProxySerializer(ModelProxySerializer):
    """
    Прокси-сериализатор для вложенных моделей с несколькими тегами.
    """

    def __init__(self, model: Type["MultiTagXmlModel"], **kwargs):
        super().__init__(**kwargs)
        self._element_tags = model.__xml_tags__

    def find_element(self, element: XmlElementReader):
        for tag in self._element_tags:
            if (elem := element.find_element(tag, self._search_mode)) is not None:
                return elem
        return None
