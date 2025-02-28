from at_krl.core.kb_instruction import AssignInstruction
from at_krl.core.kb_rule import KBRule
from at_krl.grammar.at_krl_parser import at_krl_parser


class ListenerForKBRuleMixin:
    def exitInstruction(self, ctx: at_krl_parser.InstructionContext):
        ctx.content = ctx.children[0].content

    def exitAssign_instruction(self, ctx: at_krl_parser.Assign_instructionContext):
        ref_path_child = self.search_context_by_type(ctx.children, at_krl_parser.Ref_pathContext)
        value_child = self.search_context_by_type(ctx.children, at_krl_parser.EvaluatableContext)
        non_factor_child = self.search_context_by_type(ctx.children, at_krl_parser.Non_factorContext)
        instruction = AssignInstruction(ref=ref_path_child.content, value=value_child.content)
        if non_factor_child:
            instruction.non_factor = non_factor_child.content

        ctx.content = instruction

    def exitKb_rule_condition(self, ctx: at_krl_parser.Kb_rule_conditionContext):
        ctx.content = self.search_context_by_type(ctx.children, at_krl_parser.EvaluatableContext).content

    def exitKb_rule_instructions(self, ctx: at_krl_parser.Kb_rule_instructionsContext):
        ctx.content = [child.content for child in self.filter_by_types(ctx.children, at_krl_parser.InstructionContext)]

    def exitKb_rule_else_instructions(self, ctx: at_krl_parser.Kb_rule_else_instructionsContext):
        ctx.content = [child.content for child in self.filter_by_types(ctx.children, at_krl_parser.InstructionContext)]

    def exitRule_type(self, ctx: at_krl_parser.Rule_typeContext):
        periodic_child = self.search_context_by_type(ctx.children, at_krl_parser.Rule_periodic_typeContext)
        if periodic_child:
            ctx.content = {"type": "periodic", "period": periodic_child.content}
        ctx.content = {"type": "simple"}

    def exitRule_periodic_type(self, ctx: at_krl_parser.Rule_periodic_typeContext):
        ctx.content = int(ctx.children[-1].getText())

    def exitKb_rule(self, ctx: at_krl_parser.Kb_ruleContext):
        type_child = self.search_context_by_type(ctx.children, at_krl_parser.Rule_typeContext)
        condition_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_rule_conditionContext)
        instructions_child = self.search_context_by_type(ctx.children, at_krl_parser.Kb_rule_instructionsContext)
        else_instructions_child = self.search_context_by_type(
            ctx.children, at_krl_parser.Kb_rule_else_instructionsContext
        )
        commentary_child = self.search_context_by_type(ctx.children, at_krl_parser.CommentaryContext)

        id = ctx.children[1].getText()
        condition = condition_child.content
        instructions = instructions_child.content
        else_instructions = else_instructions_child.content if else_instructions_child else None
        period = type_child.content.get("period") if type_child else None
        desc = commentary_child.content if commentary_child else None

        rule = KBRule(
            id=id,
            condition=condition,
            instructions=instructions,
            else_instructions=else_instructions,
            period=period,
            desc=desc,
        )

        self.KB.add_rule(rule)
        ctx.content = rule
