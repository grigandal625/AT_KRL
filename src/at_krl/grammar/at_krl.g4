grammar at_krl;

// ---------------------- PARSER RULES ----------------------

belief:
	BELIEF LS_BR (NUMERIC | FRAC) (';' | ',') (NUMERIC | FRAC) RS_BR;
accuracy: ACCURACY (NUMERIC | FRAC);
non_factor: belief | accuracy | belief accuracy;

kb_value:
	L_BR kb_value non_factor R_BR
	| STRING
	| NUMERIC
	| FRAC;

kb_reference:
	L_BR kb_reference non_factor R_BR
	| (ALPHANUMERIC | ALPHANUMERIC_U) (DOT kb_reference)?;

kb_operation:
	('-' | '~' | '!' | 'not') kb_operation non_factor?
	| kb_operation HIGHP_MATH_SIGN kb_operation non_factor?
	| kb_operation LOWP_MATH_SIGN kb_operation non_factor?
	| kb_operation COMP_SIGN kb_operation non_factor?
	| kb_operation LOG_SIGN kb_operation non_factor?
	| kb_reference
	| kb_value
	| L_BR kb_operation R_BR;

evaluatable: kb_operation;

// ----------------------- LEXER RULES -----------------------

BELIEF: 'УВЕРЕННОСТЬ';
ACCURACY: 'ТОЧНОСТЬ';

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

STRING: '"' ( ~[\\"\r\n] | ESCAPE_CHAR)* '"';
fragment ESCAPE_CHAR: '\\' [0btnfr"'\\];
fragment DIGIT: [0-9];