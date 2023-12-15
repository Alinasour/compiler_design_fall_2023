grammar recognizer;

// Start rule
startRule: (NATIONAL_NUMBER | EMAIL | POSTAL_CODE | DECIMAL_NUMBER | SOFTWARE_VERSION | WEBSITE_ADDRESS)+ EOF;

// Lexer rules
NATIONAL_NUMBER: [0-9]{3}[0-9]{2}('-'[0-9]{4});
EMAIL: [a-zA-Z0-9._%+-]+[@][a-zA-Z0-9.-]+.[a-zA-Z]{2,};
POSTAL_CODE: [0-9]{5}([0-9]{4})?;
DECIMAL_NUMBER: [0-9]+(.[0-9]+)?;
SOFTWARE_VERSION: 'v' [0-9]+(.[0-9]+)*;
WEBSITE_ADDRESS: 'http://' [a-zA-Z0-9.-]+;

// Ignore spaces and tabs
WS: [ \t]+ -> skip;
