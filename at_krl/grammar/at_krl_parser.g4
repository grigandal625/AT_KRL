parser grammar at_krl_parser;

options { tokenVocab=at_krl_lexer; }

knowledge_base: kb_types kb_classes;

kb_types: (kb_type NEWLINE)*?;
kb_classes: (kb_class NEWLINE)*?;

// ТИПЫ

kb_type:
    TYPE NAME
    NEWLINE kb_type_body
    (NEWLINE commentary)?;

kb_type_body: numeric_type_body | symbolic_type_body | symbolic_type_body? fuzzy_type_body;

fuzzy_type_body:
    FUZ
    (NEWLINE NUMBER)?
    (NEWLINE membership_function)+?;

membership_function: mf_def mf_body;

mf_def: STRING NUMBER NUMBER NUMBER? EQUAL?;

mf_body: LBRACE mf_point ((SEMI | COMMA) mf_point)+? (SEMI | COMMA)? RBRACE;

mf_point: NUMBER VBAR NUMBER;

symbolic_type_body:
    SYM
    (NEWLINE STRING)+?;

numeric_type_body:
    NUM
    NEWLINE FROM NUMBER
    NEWLINE TO NUMBER;

// ОБЪЕКТЫ

kb_class:
    OBJECT NAME
    NEWLINE kb_class_body
    (NEWLINE commentary)?;

kb_class_body: object_body;

object_body:
    (GROUP NAME)?
    NEWLINE attributes
    (NEWLINE commentary)?;

attributes:
    ATTRS?
    (NEWLINE attribute)+?;

attribute: long_attribute | short_attribute;

short_attribute:
    ATTR? NAME COLON TYPE? NAME (EQUAL evaluatable)?;

long_attribute:
    ATTR NAME
    NEWLINE TYPE NAME
    (NEWLINE VALUE evaluatable)?
    (NEWLINE commentary)?;

// простое вычисляемое

simple_value: STRING | NUMBER;

ref_path: NAME (DOT ref_path)?;

simple_ref: ref_path;

simple_operation
    : simple_value EQUAL ref_path
    | ref_path EQUAL ref_path
	| ref_path EQUAL simple_value
	| simple_ref
	| simple_value
    | logical_unary simple_operation
    | simple_operation high_p_math simple_operation
    | simple_operation low_p_math simple_operation
    | simple_operation compare simple_operation
    | simple_operation logical_binary simple_operation
    | MINUS simple_operation
    | LPAR NEWLINE? simple_operation NEWLINE? RPAR
    ;

simple_evaluatable: simple_operation;

// НЕ-факторы

belief:
    BELIEF LSQB NUMBER (SEMI | COMMA) NUMBER RSQB;

accuracy: ACCURACY NUMBER;
non_factor: belief accuracy | belief | accuracy;

// вычисляемое с НЕ-факторами и логикой аллена

kb_value: LPAR NEWLINE? kb_value non_factor NEWLINE? RPAR | STRING | NUMBER;

kb_reference: LPAR ref_path non_factor? RPAR | ref_path;

kb_operation
    : ref_path EQUAL kb_value non_factor?
    | kb_value EQUAL ref_path non_factor?
    | kb_value EQUAL kb_value non_factor?
    | kb_reference
    | kb_value
    | LPAR NEWLINE? kb_operation NEWLINE? RPAR
    | MINUS kb_operation non_factor?
    | logical_unary kb_operation non_factor?
    | kb_operation high_p_math non_factor?
    | kb_operation low_p_math non_factor?
    | kb_operation compare non_factor?
    | kb_allen_operation;

allen_reference: NAME index?;

index: LSQB NUMBER RSQB;

kb_allen_operation
    : allen_reference allen allen_reference
    | allen_reference DOT DURATION
    | NAME DOT OCCURANCE_COUNT;

evaluatable: kb_operation;

logical_binary
    : DOUBLEVBAR
    | VBAR
    | DOUBLEAMPER
    | AMPER
    | AND
    | OR
    | XOR
    ;

logical_unary
    : NOT
    | TILDE
    | EXCL;

compare
    : EQEQUAL
    | EQUAL
    | EQ
    | GREATEREQUAL
    | GREATER
    | GT
    | GE
    | LESSEQUAL
    | LESS
    | LT
    | LE
    | NE
    | NOTEQUAL
    | INEQUAL
    ;

high_p_math
    : DOUBLESTAR
    | MUL
    | SLASH
    | DIV
    | PERCENT
    | MOD
    | CIRCUMFLEX
    | STAR
    | POW;

low_p_math
    : PLUS
    | ADD
    | MINUS
    | SUB
    ;

allen
    : ALLEN_B
    | ALLEN_BI
    | ALLEN_M
    | ALLEN_MI
    | ALLEN_S
    | ALLEN_SI
    | ALLEN_F
    | ALLEN_FI
    | ALLEN_D
    | ALLEN_DI
    | ALLEN_O
    | ALLEN_OI
    | ALLEN_E
    | ALLEN_A
    ;

commentary: COMMENT COMMENT_DATA;
