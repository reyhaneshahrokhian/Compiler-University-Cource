grammar ExampleDSL;

start: program EOF;

program: output? hints? initiate_game bomb_placements;

output:'output:' output_types ;

output_types: 'html' | 'console';

hints: 'hint:' hint_option;

hint_option: 'True' | 'False';

initiate_game: 'game:' width 'X' height;

width: INTEGER;

height: INTEGER;

bomb_placements: ('bomb:' bomb_location)+;

bomb_location: x_location ',' y_location;

x_location: INTEGER;

y_location: INTEGER;

INTEGER: '0' | [1-9]+ [0-9]*;

WS: [ \t\r]+ -> skip;
NEWLINE: ('\n' | '\r\n' | '\r') -> skip;

