TEMPORAL_TAGS_SIGNS = {
    # default: interval_interval: True, event_event: False, event_interval: False
    "b": {"event_event": True, "event_interval": True},
    "bi": {},
    "m": {},
    "mi": {},
    "s": {"event_interval": True},
    "si": {},
    "f": {},
    "fi": {},
    "d": {"event_interval": True},
    "di": {},
    "o": {},
    "oi": {},
    "e": {"event_event": True},
    "a": {"interval_interval": False, "event_interval": True},
}


# class AllenOperationModel(SimpleOperationModel):
#     tag: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]
#     left: AllenReferenceModel
#     right: AllenReferenceModel
#     sign: Literal["b", "bi", "m", "mi", "s", "si", "f", "fi", "d", "di", "o", "oi", "e", "a"]

#     def build_target(self, data):

#         data['left'] = self.left.to_internal()
#         data['right'] = self.right.to_internal()
#         return AllenOperation(**data)
