from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel
from pydantic import RootModel


class KBEntityModel(BaseModel):
    tag: str
    _validated: bool
    owner: Optional["KBEntityModel"]

    def get_data(self):
        data = self.model_dump()
        data.pop("tag")
        return data

    def to_internal(self):
        return self.build_target(self.get_data())

    def build_target(self, data):
        raise NotImplementedError("Not implemented")


T = TypeVar("T")


class KBRootModel(RootModel, Generic[T]):
    def to_internal(self):
        raise NotImplementedError("Not implemented")
