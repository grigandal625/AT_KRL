import typing
from typing import Any
from typing import ClassVar
from typing import List
from typing import Optional
from typing import Union

from pydantic import model_validator
from pydantic import PrivateAttr
from pydantic_xml import BaseXmlModel
from pydantic_xml import errors
from pydantic_xml.element.native import XmlElement
from pydantic_xml.model import ModelT

from at_krl.xml_models.utils.serializers import MultiTagModelSerializer


class MultiTagXmlModel(BaseXmlModel):
    """
    Базовая модель с поддержкой нескольких XML-тегов.
    """

    __xml_tags__: ClassVar[List[str]] = []
    __abstract__: ClassVar[bool] = False
    _xml_tag: Optional[str] = PrivateAttr(default=None)

    def __init_subclass__(
        cls,
        tags: Optional[Union[str, List[str]]] = None,
        abstract: bool = False,
        **kwargs,
    ):
        cls.__abstract__ = abstract

        # Обработка тегов
        if tags:
            cls.__xml_tags__ = [tags] if isinstance(tags, str) else tags.copy()
        elif not cls.__abstract__:
            # Если теги не указаны и модель не абстрактная, используем имя класса как тег
            cls.__xml_tags__ = [cls.__name__.lower()]

        # Инициализация родительского класса
        kwargs.pop("tag", None)
        super().__init_subclass__(**kwargs)

    @classmethod
    def __build_serializer__(cls):
        if cls.__abstract__ or not cls.__xml_tags__:
            return

        cls.__xml_serializer__ = MultiTagModelSerializer(cls)

    @classmethod
    def from_xml_tree(cls, root, context=None):
        """
        Deserializes an xml element tree to an object of `cls` type.

        :param root: xml element to deserialize the object from
        :param context: pydantic validation context
        :return: deserialized object
        """

        assert cls.__xml_serializer__ is not None, f"model {cls.__name__} is partially initialized"

        if root.tag in cls.__xml_serializer__._element_tags:
            casting = cls.__xml_serializer__.deserialize(
                XmlElement.from_native(root),
                context=context,
                sourcemap={},
                loc=(),
            )

            obj = typing.cast(ModelT, casting)
            return obj
        else:
            raise errors.ParsingError(
                f"root element not found (actual: {root.tag}, expected: {cls.__xml_serializer__.element_name})",
            )

    def model_post_init(self, __context: Any) -> None:
        if self._xml_tag is None and self.__xml_tags__:
            self._xml_tag = self.__xml_tags__[0]

    @model_validator(mode="after")
    def validate_xml_tag(self):
        if self._xml_tag is not None and self._xml_tag not in self.__xml_tags__:
            raise ValueError(f"Invalid XML tag: {self._xml_tag}")
        return self


class MultiTagRootXmlModel(MultiTagXmlModel):
    """
    Корневая модель с поддержкой нескольких тегов.
    """
