grammar Password;

// Define a start rule
start: checkLengthRule EOF;

// Define a parser rule
checkLengthRule: STRING {if ($STRING.text.length() >= 8) {System.out.println("True");} else {System.out.println("False");}};

// Define a lexer rule for a string
STRING: '"' ~["]* '"';

// Ignore whitespace
WS: [ \t\r\n]+ -> skip;
