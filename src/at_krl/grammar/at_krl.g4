grammar at_krl;

// ---------------------- PARSER RULES ----------------------

instructions: (assign_instruction);

assign_instruction: (
		ref_path ('=' | ':=' | '<-') evaluatable (non_factor|)
	)
	| (evaluatable '->' ref_path (non_factor|));

kb_rule:
	RULE (ALPHANUMERIC | ALPHANUMERIC_U) kb_rule_condition kb_rule_instructions
		kb_rule_else_instructions? kb_rule_comment;

kb_rule_instructions: THEN instructions+;
kb_rule_condition: IF kb_operation;
kb_rule_else_instructions: ELSE instructions+;
kb_rule_comment: COMMENT (.)+?;

belief:
	BELIEF LS_BR (NUMERIC | FRAC) (';' | ',') (NUMERIC | FRAC) RS_BR;
accuracy: ACCURACY (NUMERIC | FRAC);
non_factor: belief accuracy | belief | accuracy ;

kb_operation:
	ref_path '=' evaluatable (non_factor|)
	| kb_reference
	| kb_value
	| kb_operation HIGHP_MATH_SIGN kb_operation (non_factor|)
	| kb_operation LOWP_MATH_SIGN kb_operation (non_factor|)
	| kb_operation COMP_SIGN kb_operation (non_factor|)
	| kb_operation LOG_SIGN kb_operation (non_factor|)
	| L_BR kb_operation R_BR
	| ('-' | '~' | '!' | 'not') kb_operation (non_factor|);

kb_value:
	L_BR kb_value non_factor R_BR
	| STRING
	| NUMERIC
	| FRAC;

ref_path: (ALPHANUMERIC | ALPHANUMERIC_U) (DOT ref_path)?;

kb_reference: L_BR ref_path (non_factor|) R_BR | ref_path;

evaluatable: kb_operation;

// ----------------------- LEXER RULES -----------------------

NEW_LINE: '\r\n';

BELIEF: 'УВЕРЕННОСТЬ';
ACCURACY: 'ТОЧНОСТЬ';
RULE: 'ПРАВИЛО';
IF: 'ЕСЛИ';
THEN: 'ТО';
ELSE: 'ИНАЧЕ';
TYPE: 'ТИП';
OBJECT: 'ОБЪЕКТ';
GROUP: 'ГРУППА';
ATTR: 'АТРИБУТ';
COMMENT: 'КОММЕНТАРИЙ';
INTERVAL: 'ИНТЕРВАЛ';
EVENT: 'СОБЫТИЕ';

LOG_SIGN:
	'&'
	| '&&'
	| 'and'
	| '|'
	| '||'
	| 'or'
	| '!'
	| '~'
	| 'not'
	| 'xor';

COMP_SIGN:
	'='
	| '=='
	| 'eq'
	| '>'
	| 'gt'
	| '>='
	| 'ge'
	| '<'
	| 'lt'
	| '<='
	| 'le'
	| '<>'
	| 'ne';

LOWP_MATH_SIGN: '+' | 'add' | '-' | 'sub';
HIGHP_MATH_SIGN:
	'*'
	| 'mul'
	| '/'
	| 'div'
	| '%'
	| 'mod'
	| '^'
	| '**'
	| 'pow';

DOT: '.';

L_BR: '(';
R_BR: ')';
LS_BR: '[';
RS_BR: ']';
LF_BR: '{';
RF_BR: '}';

LETTER: [a-zA-Zа-яА-Я];

NUMERIC: DIGIT+;

ALPHANUMERIC: [a-zA-Zа-яА-Я0-9]+;
ALPHANUMERIC_U: (LETTER | '_') [a-zA-Zа-яА-Я0-9_]+;

FRAC: [0-9]+ DOT [0-9]+;

WS: [ \n\t\r]+ -> skip;

COMM_CHAR: ( ~[\\"\r\n] | ESCAPE_CHAR);
STRING: '"' COMM_CHAR* '"';

fragment ESCAPE_CHAR: '\\' [0btnfr"'\\];
fragment DIGIT: [0-9];