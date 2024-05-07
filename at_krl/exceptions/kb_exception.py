from at_krl.core.kb_entity import KBEntity


class KBError(Exception):
    kb_entity: KBEntity = None

    def __init__(self, *args, kb_entity: KBEntity=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.kb_entity = kb_entity


class KBValidationError(KBError):
    pass