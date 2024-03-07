grammar at_krl;

// some lexer rules

ALLEN_SIGN:
	'b'
	| 'bi'
	| 'm'
	| 'mi'
	| 's'
	| 'si'
	| 'f'
	| 'fi'
	| 'd'
	| 'di'
	| 'o'
	| 'oi'
	| 'e'
	| 'a';

LOG_SIGN:
	'&&'
	| '&'
	| 'and'
	| '||'
	| '|'
	| 'or'
	| '!'
	| '~'
	| 'not'
	| 'xor';

COMP_SIGN:
	'=='
	| '='
	| 'eq'
	| '>='
	| '>'
	| 'gt'
	| 'ge'
	| '<>'
	| '<='
	| '<'
	| 'lt'
	| 'le'
	| 'ne';

HIGHP_MATH_SIGN:
	'**'
	| '*'
	| 'mul'
	| '/'
	| 'div'
	| '%'
	| 'mod'
	| '^'
	| 'pow';

LOWP_MATH_SIGN: '-' | 'add' | '+' | 'sub';

// PARSER RULES

knowledge_base: kb_types kb_classes kb_rules EOF;

kb_types: kb_type*?;
kb_classes: kb_class*?;
kb_rules: kb_rule*?;

commentary: COMMENT (~('\r\n'))+? NEW_LINE;

instructions: (assign_instruction);

assign_instruction: (
		ref_path ('=' | ':=' | '<-') evaluatable (non_factor |)
	)
	| (evaluatable '->' ref_path (non_factor |));

kb_rule:
	RULE (ALPHANUMERIC | ALPHANUMERIC_U) kb_rule_condition kb_rule_instructions
		kb_rule_else_instructions? commentary;

kb_rule_instructions: THEN instructions+;
kb_rule_condition: IF kb_operation;
kb_rule_else_instructions: ELSE instructions+;

belief:
	BELIEF LS_BR (NUMERIC | FRAC) (';' | ',') (NUMERIC | FRAC) RS_BR;
accuracy: ACCURACY (NUMERIC | FRAC);
non_factor: belief accuracy | belief | accuracy;

kb_operation:
	ref_path '=' kb_value (non_factor |)
	| kb_value '=' ref_path (non_factor |)
	| ref_path '=' ref_path (non_factor |)
	| kb_value '=' kb_value (non_factor |)
	| kb_reference
	| kb_value
	| kb_operation HIGHP_MATH_SIGN kb_operation (non_factor |)
	| kb_operation LOWP_MATH_SIGN kb_operation (non_factor |)
	| kb_operation COMP_SIGN kb_operation (non_factor |)
	| kb_operation LOG_SIGN kb_operation (non_factor |)
	| L_BR kb_operation R_BR
	| ('-' | '~' | '!' | 'not') kb_operation (non_factor |)
	| kb_allen_operation;

kb_allen_operation: (ALPHANUMERIC | ALPHANUMERIC_U) ALLEN_SIGN (
		ALPHANUMERIC
		| ALPHANUMERIC_U
	);

simple_operation:
	simple_value '=' ref_path
	| ref_path '=' ref_path
	| ref_path '=' simple_value
	| simple_ref
	| simple_value
	| simple_operation HIGHP_MATH_SIGN simple_operation (
		non_factor
		|
	)
	| simple_operation '-' simple_operation (non_factor |)
	| simple_operation LOWP_MATH_SIGN simple_operation (
		non_factor
		|
	)
	| simple_operation COMP_SIGN simple_operation (non_factor |)
	| simple_operation LOG_SIGN simple_operation (non_factor |)
	| L_BR simple_operation R_BR
	| ('~' | '!' | 'not') simple_operation;

simple_evaluatable: simple_operation;

simple_value: STRING | NUMERIC | FRAC;

kb_value: L_BR kb_value non_factor R_BR | simple_value;

ref_path: (ALPHANUMERIC | ALPHANUMERIC_U) (DOT ref_path)?;

simple_ref: ref_path;

kb_reference: L_BR simple_ref (non_factor |) R_BR | simple_ref;

evaluatable: kb_operation;

kb_type:
	TYPE (ALPHANUMERIC | ALPHANUMERIC_U) kb_type_body commentary;

kb_type_body:
	symbolic_type_body? fuzzy_type_body
	| symbolic_type_body
	| numeric_type_body;

symbolic_type_body: SYM (STRING)+?;
numeric_type_body:
	NUM FROM (NUMERIC | FRAC) TO (NUMERIC | FRAC);
fuzzy_type_body: FUZ NUMERIC membersip_function+?;

membersip_function: mf_def mf_body;

mf_def: STRING (NUMERIC | FRAC) (NUMERIC | FRAC) NUMERIC? '='?;
mf_point: (NUMERIC | FRAC) '|' (NUMERIC | FRAC);
mf_body:
	LF_BR (mf_point ((';' | ',') mf_point)*? (';' | ',')?) RF_BR;

kb_class:
	OBJECT (ALPHANUMERIC | ALPHANUMERIC_U) kb_class_body commentary;
kb_class_body: event_body | interval_body | object_body;

event_body:
	GROUP (EVENT | CASED_EVENT) ATTRS? OCCURANCE_CONDITION SIMPLE_EXP_TYPE VALUE simple_evaluatable
		commentary;

interval_body:
	GROUP (INTERVAL | CASED_INTERVAL) ATTRS? OPEN SIMPLE_EXP_TYPE VALUE simple_evaluatable CLOSE
		SIMPLE_EXP_TYPE VALUE simple_evaluatable commentary;

object_body: (GROUP (ALPHANUMERIC | ALPHANUMERIC_U))? attributes;
attributes: (ATTRS)? attribute+?;
attribute:
	ATTR (ALPHANUMERIC | ALPHANUMERIC_U) TYPE (
		ALPHANUMERIC
		| ALPHANUMERIC_U
	) (VALUE evaluatable)? commentary;

// LEXER RULES

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
ATTRS: 'АТРИБУТЫ';
COMMENT: 'КОММЕНТАРИЙ';
VALUE: 'ЗНАЧЕНИЕ';
INTERVAL: 'ИНТЕРВАЛ';
CASED_INTERVAL: 'Интервал';
EVENT: 'СОБЫТИЕ';
CASED_EVENT: 'Событие';
OCCURANCE_CONDITION: 'АТРИБУТ УслВозн';
OPEN: 'АТРИБУТ УслНач';
CLOSE: 'АТРИБУТ УслОконч';
SIMPLE_EXP_TYPE: 'ТИП ЛогВыр';

SYM: 'СИМВОЛ';
NUM: 'ЧИСЛО';
FUZ: 'НЕЧЕТКИЙ';

FROM: 'ОТ';
TO: 'ДО';

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

FRAC: [0-9]+ '.' [0-9]+;

NEW_LINE: '\r\n';
WS: [ \n\t\r]+ -> skip;

NO_NEWLINE: ~[\r\n];

COMM_CHAR: ( ~[\\"\r\n] | ESCAPE_CHAR);
STRING: '"' COMM_CHAR* '"';

fragment ESCAPE_CHAR: '\\' [0btnfr"'\\];
fragment DIGIT: [0-9];