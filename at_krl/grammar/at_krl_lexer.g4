lexer grammar at_krl_lexer;

BELIEF                : 'УВЕРЕННОСТЬ';
ACCURACY              : 'ТОЧНОСТЬ';
RULE                  : 'ПРАВИЛО';
IF                    : 'ЕСЛИ';
THEN                  : 'ТО';
ELSE                  : 'ИНАЧЕ';
TYPE                  : 'ТИП';
OBJECT                : 'ОБЪЕКТ';
GROUP                 : 'ГРУППА';
ATTR                  : 'АТРИБУТ';
ATTRS                 : 'АТРИБУТЫ';
VALUE                 : 'ЗНАЧЕНИЕ';
INTERVAL              : 'ИНТЕРВАЛ';
CASED_INTERVAL        : 'Интервал';
EVENT                 : 'СОБЫТИЕ';
CASED_EVENT           : 'Событие';
OCCURANCE_CONDITION   : 'УслВозн';
OPEN                  : 'УслНач';
CLOSE                 : 'УслОконч';
DURATION              : 'ДЛИТЕЛЬНОСТЬ';
OCCURANCE_COUNT       : 'КОЛ_ВОЗН';
OPEN_COUNT            : 'КОЛ_НАЧ';
CLOSE_COUNT           : 'КОЛ_ОКОНЧ';
OPEN_TACT             : 'ТАКТ_НАЧ'; 
CLOSE_TACT            : 'ТАКТ_ОКОНЧ';
OCCURANCE_TACT        : 'ТАКТ_ВОЗН';
SIMPLE_EXP_TYPE       : 'ЛогВыр';
SIMPLE                : 'ОБЫЧНОЕ';
PERIODIC              : 'ПЕРИОДИЧЕСКОЕ';
PERIOD                : 'ПЕРИОД'; 

SYM: 'СИМВОЛ';
NUM: 'ЧИСЛО';
FUZ: 'НЕЧЕТКИЙ';

FROM: 'ОТ';
TO: 'ДО';

LPAR             : '(';
LSQB             : '[';
LBRACE           : '{';
RPAR             : ')';
RSQB             : ']';
RBRACE           : '}';
COLON            : ':';
COMMA            : ',';
SEMI             : ';';
PLUS             : '+';
LEFT_ASSIGN      : '<-';
RIGHT_ASSIGN     : '->';
MINUS            : '-';
STAR             : '*';
SLASH            : '/';
DOUBLEVBAR       : '||';
VBAR             : '|';
DOUBLEAMPER      : '&&';
AMPER            : '&';
LESS             : '<';
GREATER          : '>';
COLON_EQ         : ':=';
EQUAL            : '=';
DOT              : '.';
PERCENT          : '%';
BACKQUOTE        : '`';
EQEQUAL          : '==';
INEQUAL          : '<>';
NOTEQUAL         : '!=';
LESSEQUAL        : '<=';
GREATEREQUAL     : '>=';
TILDE            : '~';
CIRCUMFLEX       : '^';
DOUBLESTAR       : '**';
AND              : 'and';
OR               : 'or';
XOR              : 'xor';
NOT              : 'not';
MOD              : 'mod';
DIV              : 'div';
ADD              : 'add';
SUB              : 'sub';
MUL              : 'mul';
POW              : 'pow';
EQ               : 'eq';
LT               : 'lt';
GT               : 'gt';
LE               : 'le';
GE               : 'ge';
NE               : 'ne';
EXCL             : '!';

ALLEN_B  : 'b';
ALLEN_BI : 'bi';
ALLEN_M  : 'm';
ALLEN_MI : 'mi';
ALLEN_S  : 's';
ALLEN_SI : 'si';
ALLEN_F  : 'f';
ALLEN_FI : 'fi';
ALLEN_D  : 'd';
ALLEN_DI : 'di';
ALLEN_O  : 'o';
ALLEN_OI : 'oi';
ALLEN_E  : 'e';
ALLEN_A  : 'a';

COMMENT: 'КОММЕНТАРИЙ' -> pushMode(COMMENT_MODE);

NAME : IDENTIFIER;

NUMBER
   : '-'? (INTEGER
   | FLOAT_NUMBER
   | IMAG_NUMBER)
   ;

STRING : STRING_LITERAL;
LANG_COMMENT : '#' ~[\r\n]* -> skip;
WS : [ \t\f]+ -> channel(HIDDEN);

NEWLINE : ('\r'? '\n');

mode COMMENT_MODE;
COMMENT_DATA : ~[\r\n]+ -> popMode;

fragment STRING_LITERAL : SHORT_STRING | LONG_STRING;


fragment SHORT_STRING: ["] SHORT_STRING_ITEM_FOR_DOUBLE_QUOTE* ["];

fragment LONG_STRING
    : ["]["]["] LONG__STRING_ITEM*? ["]["]["] // nongreede
    ;

fragment SHORT_STRING_ITEM_FOR_SINGLE_QUOTE : SHORT_STRING_CHAR_NO_SINGLE_QUOTE | ESCAPE_SEQ;
fragment SHORT_STRING_ITEM_FOR_DOUBLE_QUOTE : SHORT_STRING_CHAR_NO_DOUBLE_QUOTE | ESCAPE_SEQ;

fragment LONG__STRING_ITEM : LONG_STRING_CHAR | ESCAPE_SEQ;

fragment SHORT_STRING_CHAR_NO_SINGLE_QUOTE : ~[\\\r\n'];          // <any source character except "\" or newline or single quote>
fragment SHORT_STRING_CHAR_NO_DOUBLE_QUOTE : ~[\\\r\n"];          // <any source character except "\" or newline or double quote>
fragment LONG_STRING_CHAR  : ~'\\';                               // <any source character except "\">

fragment ESCAPE_SEQ : ESCAPE_SEQ_NEWLINE | '\\' [\u0000-\u007F];

fragment ESCAPE_SEQ_NEWLINE : BACKSLASH_NEWLINE;

fragment BACKSLASH_NEWLINE : '\\' NEWLINE;

fragment INTEGER         : DECIMAL_INTEGER;
fragment DECIMAL_INTEGER : NON_ZERO_DIGIT DIGIT* | '0';
fragment NON_ZERO_DIGIT  : [1-9];

fragment FLOAT_NUMBER   : POINT_FLOAT;
fragment POINT_FLOAT    : INT_PART? FRACTION | INT_PART '.';
fragment INT_PART       : DIGIT+;
fragment FRACTION       : '.' DIGIT+;

fragment IMAG_NUMBER : (FLOAT_NUMBER | INT_PART) ('j' | 'J');

fragment IDENTIFIER : (LETTER | '_') (LETTER | DIGIT | '_')*;
fragment LETTER     : LOWERCASE | UPPERCASE;
fragment LOWERCASE  : [a-zа-я];
fragment UPPERCASE  : [A-ZА-Я];
fragment DIGIT      : [0-9];
