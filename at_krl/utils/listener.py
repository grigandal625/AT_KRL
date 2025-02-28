from antlr4.tree.Tree import TerminalNodeImpl

from at_krl.core.knowledge_base import KnowledgeBase
from at_krl.grammar.at_krl_parser import at_krl_parser
from at_krl.grammar.at_krl_parserListener import at_krl_parserListener
from at_krl.utils.listener_parts import evaluatable
from at_krl.utils.listener_parts import general
from at_krl.utils.listener_parts import kb_class
from at_krl.utils.listener_parts import kb_rule
from at_krl.utils.listener_parts import kb_type
from at_krl.utils.listener_parts import non_factor
from at_krl.utils.listener_parts import simple
from at_krl.utils.listener_parts import temporal


def get_number(v: str):
    if "." in v:
        v = float(v)
    else:
        v = int(v)
    return v


class ATKRLListener(
    non_factor.ListenerForNonFactorMixin,
    simple.ListenerForSimpleMixin,
    evaluatable.ListenerForEvaluatableMixin,
    temporal.ListenerForTemporalMixin,
    general.ListenerForGeneralMixin,
    kb_rule.ListenerForKBRuleMixin,
    kb_type.ListenerForKBTypeMixin,
    kb_class.ListenerForKBClassMixin,
    at_krl_parserListener,
):
    KB = None

    def __init__(self, *args, **kwargs):
        at_krl_parserListener.__init__(self, *args, **kwargs)
        self.KB = KnowledgeBase()

    @staticmethod
    def search_context_by_type(children, ctx_type):
        for child in children:
            if isinstance(child, ctx_type):
                return child

    @staticmethod
    def filter_by_types(children, *ctx_types):
        return [child for child in children if any([isinstance(child, ctx_type) for ctx_type in ctx_types])]

    @staticmethod
    def search_terminal_by_token_name(children, token_name):
        for child in children:
            if isinstance(child, TerminalNodeImpl) and at_krl_parser.symbolicNames[child.symbol.type] == token_name:
                return child

    @staticmethod
    def filter_by_token_names(children, *token_names):
        return [
            child
            for child in children
            if any(
                [
                    isinstance(child, TerminalNodeImpl) and at_krl_parser.symbolicNames[child.symbol.type] == token_name
                    for token_name in token_names
                ]
            )
        ]
