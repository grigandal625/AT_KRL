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

kb_type_body: numeric_type_body | symbolic_type_body | fuzzy_type_body;

fuzzy_type_body:
    (symbolic_type_body newline)?
    FUZ
    (newline NUMBER)?
    membership_functions;

membership_function: mf_def mf_body;
membership_functions: (newline membership_function)+?;

mf_def: STRING NUMBER NUMBER NUMBER? EQUAL?;

mf_body: LBRACE mf_point ((SEMI | COMMA) mf_point)+? (SEMI | COMMA)? RBRACE;

mf_point: NUMBER VBAR NUMBER;

symbolic_type_body:
    SYM
    symbolic_type_values;

symbolic_type_values: (newline STRING)+?;

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
    (GROUP NAME)? attributes;

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
    newline occurance_condition;

occurance_condition: 
    occurance_condition_declaration temporal_attribute_condition
    (newline commentary)?;

interval_body:
    GROUP (INTERVAL | CASED_INTERVAL)
    (newline ATTRS)?
    newline open
    newline close;

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

simple_value: STRING | NUMBER | BOOLEAN;

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

kb_value: simple_value non_factor?;

kb_reference: simple_ref non_factor?;

kb_operation // для значений атрибутов объектов (без логики Аллена)
    : kb_reference
    | kb_value
    | MINUS kb_operation
    | logical_unary kb_operation
    | kb_operation high_p_math kb_operation
    | kb_operation low_p_math kb_operation
    | kb_operation compare kb_operation
    | kb_operation logical_binary kb_operation
    | LPAR newline? kb_operation newline? RPAR non_factor?;

kb_evaluatable // для значений в правилах (с логикой Аллена)
    : allen_evaluatable
    | kb_reference
    | kb_value
    | MINUS kb_evaluatable
    | logical_unary kb_evaluatable
    | kb_evaluatable high_p_math kb_evaluatable
    | kb_evaluatable low_p_math kb_evaluatable
    | kb_evaluatable compare kb_evaluatable
    | kb_evaluatable logical_binary kb_evaluatable
    | LPAR newline? kb_evaluatable newline? RPAR non_factor?;

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
    : (DOUBLEVBAR newline?)
    | (VBAR newline?)
    | (DOUBLEAMPER newline?)
    | (AMPER newline?)
    | (AND newline?)
    | (OR newline?)
    | (XOR newline?)
    ;

logical_unary
    : NOT
    | TILDE
    | EXCL;

compare
    : (EQEQUAL newline?)
    | (EQUAL newline?)
    | (EQ newline?)
    | (GREATEREQUAL newline?)
    | (GREATER newline?)
    | (GT newline?)
    | (GE newline?)
    | (LESSEQUAL newline?)
    | (LESS newline?)
    | (LT newline?)
    | (LE newline?)
    | (NE newline?)
    | (NOTEQUAL newline?)
    | (INEQUAL newline?)
    ;

high_p_math
    : (DOUBLESTAR newline?)
    | (MUL newline?)
    | (SLASH newline?)
    | (DIV newline?)
    | (PERCENT newline?)
    | (MOD newline?)
    | (CIRCUMFLEX newline?)
    | (STAR newline?)
    | (POW newline?)
    ;

low_p_math
    : (PLUS newline?)
    | (ADD newline?)
    | (MINUS newline?)
    | (SUB newline?)
    ;

allen
    : (ALLEN_B newline?)
    | (ALLEN_BI newline?)
    | (ALLEN_M newline?)
    | (ALLEN_MI newline?)
    | (ALLEN_S newline?)
    | (ALLEN_SI newline?)
    | (ALLEN_F newline?)
    | (ALLEN_FI newline?)
    | (ALLEN_D newline?)
    | (ALLEN_DI newline?)
    | (ALLEN_O newline?)
    | (ALLEN_OI newline?)
    | (ALLEN_E newline?)
    | (ALLEN_A newline?)
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

rule_type: rule_simple_type | rule_periodic_type;

rule_simple_type: SIMPLE;
rule_periodic_type: rule_periodic_type_def NUMBER;
rule_periodic_type_def: PERIODIC ((newline PERIOD) | COLON);

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
