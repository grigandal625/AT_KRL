from at_krl.core.kb_type import KBSymbolicType, KBNumericType, KBFuzzyType
from antlr4.tree.Tree import TerminalNodeImpl
import json

from at_krl.core.fuzzy.membership_function import MFPoint, MembershipFunction

from at_krl.grammar.at_krl_parser import at_krl_parser

def get_number(v: str):
    if "." in v:
        v = float(v)
    else:
        v = int(v)
    return v

class ListenerForKBTypeMixin:
    def exitMf_point(self, ctx: at_krl_parser.Mf_pointContext):
        x = get_number(ctx.children[0].getText())
        y = get_number(ctx.children[2].getText())
        ctx.content = MFPoint(x=x, y=y)

    def exitMembership_function(self, ctx: at_krl_parser.Membership_functionContext):
        mf_name = json.loads(ctx.children[0].children[0].getText())
        min = get_number(ctx.children[0].children[1].getText())
        max = get_number(ctx.children[0].children[2].getText())

        mf_points = [c.content for c in self.filter_by_types(ctx.children[1].children, at_krl_parser.Mf_pointContext)]

        ctx.content = MembershipFunction(name=mf_name, min=min, max=max, points=mf_points)

    def exitMembership_functions(self, ctx: at_krl_parser.Membership_functionsContext):
        ctx.content = [child.content for child in self.filter_by_types(ctx.children, at_krl_parser.Membership_functionContext)]

    def exitFuzzy_type_body(self, ctx: at_krl_parser.Fuzzy_type_bodyContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.Membership_functionsContext).content

    def exitSymbolic_type_values(self, ctx: at_krl_parser.Symbolic_type_valuesContext):
        ctx.content = [json.loads(child.getText()) for child in self.filter_by_types(ctx.children, TerminalNodeImpl)]

    def exitSymbolic_type_body(self, ctx: at_krl_parser.Symbolic_type_bodyContext):
        ctx.content = ctx.children[1].content

    def exitNumeric_type_body(self, ctx: at_krl_parser.Numeric_type_bodyContext):
        from_value = get_number(ctx.children[3].getText())
        to_value = get_number(ctx.children[6].getText())

        ctx.content = [from_value, to_value]

    def exitKb_type_body(self, ctx: at_krl_parser.Kb_type_bodyContext):
        fuzzy_context = self.search_context_by_type(ctx.children, at_krl_parser.Fuzzy_type_bodyContext)
        numeric_context = self.search_context_by_type(ctx.children, at_krl_parser.Numeric_type_bodyContext)
        symbolic_context = self.search_context_by_type(ctx.children, at_krl_parser.Symbolic_type_bodyContext)

        if fuzzy_context is not None:
            ctx.content = {'meta': 'fuzzy', 'membership_functions': fuzzy_context.content}
        elif numeric_context is not None:
            ctx.content = {'meta': 'numeric', 'from_': numeric_context.content[0], 'to_': numeric_context.content[1]}
        elif symbolic_context is not None:
            ctx.content = {'meta': 'symbolic', 'values': symbolic_context.content}
        else:
            raise ValueError("No type body found in KB_type_body")

    def exitKb_type(self, ctx: at_krl_parser.Kb_typeContext):
        name = ctx.children[1].getText()

        commentary_child = self.search_context_by_type(ctx.children, at_krl_parser.CommentaryContext)
        desc = commentary_child.content if commentary_child else None

        body = self.search_context_by_type(ctx.children, at_krl_parser.Kb_type_bodyContext).content
        type_classes = {
            'fuzzy': KBFuzzyType,
            'numeric': KBNumericType,
            'symbolic': KBSymbolicType
        }
        meta = body.pop('meta')

        type_class = type_classes[meta]
        kb_type = type_class(id=name, **body, desc=desc)
        
        self.KB.types.append(kb_type)

        ctx.content = kb_type
