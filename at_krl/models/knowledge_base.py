from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.models.kb_entity import KBEntityModel


class KBClasses(KBEntityModel):
    pass


class KnowledgeBaseModel(KBEntityModel):
    # types: List[KBType] = field(init=False, default_factory=list)
    # classes: KBClasses = field(init=False, default_factory=KBClasses)
    # rules: List[KBRule] = field(init=False, default_factory=list)
    # _world: KBClass = field(default=None)

    _raise_on_validation: bool = False
    _validated: bool = False

    def build_target(self, data):
        return KnowledgeBase(**data)
