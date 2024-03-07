lexer grammar at_krlLexer;

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

LETTER: [a-zA-Zа-яА-Я];

NUMERIC: DIGIT+;

ALPHANUMERIC: [a-zA-Zа-яА-Я0-9]+;
ALPHANUMERIC_U: (LETTER | '_') [a-zA-Zа-яА-Я0-9_]+;

FRAC: [0-9]+ '.' [0-9]+;

COMM_CHAR: ( ~[\\"\r\n] | ESCAPE_CHAR);
STRING: '"' COMM_CHAR* '"';

fragment ESCAPE_CHAR: '\\' [0btnfr"'\\];
fragment DIGIT: [0-9];