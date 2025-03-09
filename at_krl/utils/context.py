from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from at_krl.core.knowledge_base import KnowledgeBase


@dataclass(kw_only=True)
class Context:
    name: str | int
    data: Any = field(default=None)
    kb: Optional["KnowledgeBase"] = field(default=None)
    parent: Optional["Context"] = field(default=None)

    def create_child(self, name, data=None):
        return Context(name=name, data=data, kb=self.kb, parent=self)

    @property
    def root(self):
        ctx = self
        while ctx.parent:
            ctx = ctx.parent
        return ctx

    @property
    def path(self):
        result = [self.name]
        ctx = self.parent
        while ctx:
            result = [ctx.name] + result
            ctx = ctx.parent
        return result
