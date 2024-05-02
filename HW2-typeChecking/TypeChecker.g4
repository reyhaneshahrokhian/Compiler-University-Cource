grammar TypeChecker;
start:
    expr EOF
    ;

expr returns [type=str()]:
    expr '+' term  #expr1
    | expr '-' term  #expr2
    | term #expr3
    ;

term returns [type=str()]:
    term '*' fact  #term1
    | term '/' fact #term2
    | fact #term3
    ;

fact returns [type=str()]:
     STRING #factString
    |INTEGER #factInteger
    |FLOAT #factFloat
    |'('expr')' #factExpr;

/* Lexical rules*/
Plus: '+';
MINUS: '-';
MUL: '*';
DIVIDE: '/';
ASSIGN: '=';

STRING:'"' .*? '"';
INTEGER: [0-9]+;
FLOAT:[0-9]*'.'[0-9]+;

Whitespace: [ \t]+ -> channel(HIDDEN);
Newline: '\n' -> skip;



