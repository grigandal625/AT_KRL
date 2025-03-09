from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from pydantic import RootModel

from at_krl.utils.context import Context


class KBEntityModel(BaseModel):
    tag: str
    _validated: bool

    def get_data(self, context: Context):
        data = self.model_dump()
        data.pop("tag")
        return data

    def to_internal(self, context: Context):
        return self.build_target(self.get_data(context), context)

    def build_target(self, data, context: Context):
        raise NotImplementedError("Not implemented")


T = TypeVar("T")


class KBRootModel(RootModel[T], Generic[T]):
    def to_internal(self, context: Context):
        raise NotImplementedError("Not implemented")
