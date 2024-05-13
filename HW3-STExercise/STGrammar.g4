grammar STGrammar;

start: assigns  EOF;
assigns: assign NEWLINE assigns | assign;
assign: ID '=' expr;
expr returns[rule_type= str()]:
    expr ADD expr |
    expr SUB expr |
    term
    ;
term returns[rule_type= str()]:
    term MUL term |
    term DIV term |
    factor
        ;
factor returns[rule_type = str()]:
    STRING #factor_is_string|
    sign? INTEGER #factor_is_integer|
    sign? FLOAT #factor_is_float|
    LPAREN expr RPAREN #factor_is_expression|
    ID #factor_is_id
    ;

sign: ('+'|'-');

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
//NUMERICALVALUE: FLOAT | INTEGER;
STRING: '"'.*?'"';
FLOAT:[0-9]*'.'[0-9]+;
INTEGER:[0-9]+;
WS: [ \t\r]+ -> skip;
NEWLINE : '\n';
ID : [a-z,A-Z]([a-z,A-Z] | [0-9])*;