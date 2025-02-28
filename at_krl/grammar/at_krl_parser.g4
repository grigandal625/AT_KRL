parser grammar at_krl_parser;

options { tokenVocab=at_krl_lexer; }

lang_comment: LANG_COMMENT?; // нечувствительость к коментариям #
newline: NEWLINE+;

knowledge_base: newline*? kb_types kb_classes kb_rules;

kb_types: (kb_type newline)*?;
kb_classes: (kb_class newline)*?;
kb_rules: (kb_rule newline)*?;

// ТИПЫ

kb_type:
    TYPE NAME
    newline kb_type_body
    (newline commentary)?;

kb_type_body: numeric_type_body | symbolic_type_body | symbolic_type_body? fuzzy_type_body;

fuzzy_type_body:
    FUZ
    (newline NUMBER)?
    (newline membership_function)+?;

membership_function: mf_def mf_body;

mf_def: STRING NUMBER NUMBER NUMBER? EQUAL?;

mf_body: LBRACE mf_point ((SEMI | COMMA) mf_point)+? (SEMI | COMMA)? RBRACE;

mf_point: NUMBER VBAR NUMBER;

symbolic_type_body:
    SYM
    (newline STRING)+?;

numeric_type_body:
    NUM
    newline FROM NUMBER
    newline TO NUMBER;

// ОБЪЕКТЫ

kb_class:
    OBJECT NAME
    newline kb_class_body
    (newline commentary)?;

kb_class_body: object_body | event_body | interval_body;

object_body:
    (GROUP NAME)? attributes
    (newline commentary)?;

attributes:
    (newline ATTRS)?
    (newline attribute)+?;

attribute: attr_declaration (long_attribute | short_attribute);

short_attribute:
    COLON TYPE? NAME (EQUAL kb_operation)?;

long_attribute:
    newline TYPE NAME
    (newline VALUE newline? kb_operation)?
    (newline commentary)?;

event_body:
    GROUP (EVENT | CASED_EVENT)
    (newline ATTRS)?
    newline occurance_condition
    (newline commentary)?;

occurance_condition: 
    occurance_condition_declaration temporal_attribute_condition
    (newline commentary)?;

interval_body:
    GROUP (INTERVAL | CASED_INTERVAL)
    (newline ATTRS)?
    newline open
    newline close
    (newline commentary)?;

open:
    open_declaration temporal_attribute_condition
    (newline commentary)?;

close:
    close_declaration temporal_attribute_condition
    (newline commentary)?;

occurance_condition_declaration: ATTR? OCCURANCE_CONDITION;
open_declaration: ATTR? OPEN;
close_declaration: ATTR? CLOSE;
attr_declaration: ATTR? NAME;

temporal_attribute_condition
    : (
        ((COLON TYPE? SIMPLE_EXP_TYPE)? EQUAL simple_evaluatable)  // short_open
        |
        (
            newline TYPE SIMPLE_EXP_TYPE 
            newline VALUE newline? simple_evaluatable
        )  // long_open
    );

// простое вычисляемое

simple_value: STRING | NUMBER;

ref_path: NAME (DOT ref_path)?;

simple_ref: ref_path;

simple_operation
    : simple_ref
	| simple_value
    | logical_unary simple_operation
    | simple_operation high_p_math simple_operation
    | simple_operation low_p_math simple_operation
    | simple_operation compare simple_operation
    | simple_operation logical_binary simple_operation
    | MINUS simple_operation
    | LPAR newline? simple_operation newline? RPAR
    ;

simple_evaluatable: simple_operation;

// НЕ-факторы

belief:
    BELIEF LSQB NUMBER (SEMI | COMMA) NUMBER RSQB;

accuracy: ACCURACY NUMBER;
non_factor: belief accuracy | belief | accuracy;

// вычисляемое с НЕ-факторами и логикой аллена

kb_value: (LPAR newline? simple_value non_factor newline? RPAR) | simple_value;

kb_reference: LPAR ref_path non_factor? RPAR | ref_path;

kb_operation // для значений атрибутов объектов (без логики Аллена)
    : kb_reference
    | kb_value
    | MINUS kb_operation non_factor?
    | logical_unary kb_operation non_factor?
    | kb_operation high_p_math kb_operation non_factor?
    | kb_operation low_p_math kb_operation non_factor?
    | kb_operation compare kb_operation non_factor?
    | kb_operation logical_binary kb_operation non_factor?
    | LPAR newline? kb_operation newline? RPAR;

kb_evaluatable // для значений в правилах (с логикой Аллена)
    : kb_reference
    | kb_value
    | MINUS kb_evaluatable non_factor?
    | logical_unary kb_evaluatable non_factor?
    | kb_evaluatable high_p_math kb_evaluatable non_factor?
    | kb_evaluatable low_p_math kb_evaluatable non_factor?
    | kb_evaluatable compare kb_evaluatable non_factor?
    | kb_evaluatable logical_binary kb_evaluatable non_factor? 
    | allen_evaluatable
    | LPAR newline? kb_evaluatable newline? RPAR;

allen_reference: simple_ref;
allen_indexed_reference: allen_reference index?;
allen_attribute_expression
    : allen_indexed_reference DOT (DURATION | OPEN_TACT | CLOSE_TACT | OCCURANCE_TACT)
    | allen_reference DOT (OCCURANCE_COUNT | OPEN_COUNT | CLOSE_COUNT);

index: LSQB evaluatable RSQB;

allen_operation: allen_indexed_reference allen allen_reference;
allen_evaluatable: allen_operation | allen_attribute_expression;

evaluatable: kb_evaluatable;

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

// правила

kb_rule:
    RULE NAME
    (newline TYPE rule_type)?
    newline kb_rule_condition
    newline kb_rule_instructions
    (newline kb_rule_else_instructions)?
    (newline commentary)?;

rule_type: SIMPLE | (PERIODIC ((newline PERIOD) | COLON) NUMBER);

kb_rule_condition: 
    IF 
    newline evaluatable;

kb_rule_instructions:
    THEN 
    (newline instruction)+;

kb_rule_else_instructions:
    ELSE 
    (newline instruction)+;

assign_instruction
    : (ref_path left_assign evaluatable non_factor?) 
    | (evaluatable right_assign ref_path non_factor?)
    ;

instruction: assign_instruction; // | другие типы инструкций

left_assign: LEFT_ASSIGN | EQUAL | COLON_EQ;
right_assign: RIGHT_ASSIGN;
