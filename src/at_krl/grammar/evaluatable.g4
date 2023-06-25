grammar evaluatable;

// ---------------------- PARSER RULES ----------------------

kb_value: STRING | DIGIT+ | FRAC;

kb_reference: (ALPHANUMERIC | ALPHANUMERIC_U) (DOT kb_reference)?;

kb_operation: 
    kb_operation HIGHP_MATH_SIGN kb_operation |
    kb_operation LOWP_MATH_SIGN kb_operation |
    kb_operation COMP_SIGN kb_operation |
    kb_operation LOG_SIGN kb_operation |
    kb_reference | 
    kb_value | 
    L_BRACKET kb_operation R_BRACKET;

evaluatable: kb_operation;

// ----------------------- LEXER RULES -----------------------

LOG_SIGN: 
    '&' | 
    '&&' | 
    'and' | 
    '|' | 
    '||' | 
    'or' | 
    '!' | 
    '~' | 
    'not' |
    'xor';

COMP_SIGN: 
    '=' | 
    '==' | 
    'eq' | 
    '>' | 
    'gt' | 
    '>=' | 
    'ge' | 
    '<' | 
    'lt' | 
    '<=' | 
    'le' | 
    '<>' | 
    'ne' ;

LOWP_MATH_SIGN: '+' | 'add' | '-' | 'sub';
HIGHP_MATH_SIGN: 
    '*' | 
    'mul' |
    '/' |
    'div' |
    '%' |
    'mod' |
    '^' |
    '**' |
    'pow';


DOT : '.';

L_BRACKET: '(';
R_BRACKET: ')';

LETTER: [a-zA-Zа-яА-Я];
DIGIT : [0-9];

ALPHANUMERIC: [a-zA-Zа-яА-Я0-9]+;
ALPHANUMERIC_U: (LETTER | '_') [a-zA-Zа-яА-Я0-9_]+;

NUMERIC: [0-9]+;
FRAC: [0-9]+ DOT [0-9]+;

WS: [ \n\t\r]+ -> skip;

STRING : '"' ( ~[\\"\r\n] | ESCAPE_CHAR )* '"' ;
fragment ESCAPE_CHAR : '\\' [0btnfr"'\\];