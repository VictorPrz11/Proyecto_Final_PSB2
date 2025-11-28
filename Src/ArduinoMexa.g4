grammar ArduinoMexa;

// --- Reglas del parser ---

program
    : bloqueEstatico bloqueLoop EOF  // Alternativa 1: Con setup y loop
    | bloqueLoop EOF               // Alternativa 2: Solo con loop
    ;

bloqueEstatico
    : ESTATICO sentencia
    ;

bloqueLoop
    : LOOP sentencia
    ;

// Sentencia sin llaves
sentencia
    : (statement SEMICOLON)+
    ;

// Lista de statements — AHORA ETIQUETADOS
statement
    : prenderled       #stmtPrenderled
    | apagarled        #stmtApagarled
    | leersensor       #stmtLeersensor
    | moverservo       #stmtMoverServo
    | esperar          #stmtEsperar
    | asignacion       #stmtAsignacion
    | condicion        #stmtCondicion
    | tocarbuzzer      #stmtBuzzer
    | escribirlcd      #stmtEscribirLCD
    | encendermotor    #stmtMotorOn
    | apagarmotor      #stmtMotorOff
    | activarrele      #stmtReleOn
    | desactivarrele   #stmtReleOff
    | prenderrgb       #stmtRgbOn
    | apagarrgb        #stmtRgbOff
    ;

// --- Instrucciones originales ---
prenderled     
    : PRENDERLED LPAREN expr COMMA expr RPAREN
    ;

apagarled      
    : APAGARLED LPAREN expr RPAREN
    ;

leersensor     
    : ID AS LEERSENSOR LPAREN expr RPAREN
    ;

moverservo     
    : MOVERSERVO LPAREN expr COMMA expr RPAREN
    ;

esperar        
    : ESPERAR LPAREN expr RPAREN
    ;

asignacion     
    : ID AS expr
    ;

condicion
    : SI LPAREN expr comparador expr RPAREN ENTONCES
      (sentencia | LBRACE sentencia+ RBRACE)
    ;

// --- Instrucciones nuevas ---
tocarbuzzer    
    : TOCARBUZZER LPAREN expr COMMA expr RPAREN
    ;

escribirlcd    
    : ESCRIBIRLCD LPAREN expr COMMA expr COMMA STRING RPAREN
    ;

encendermotor  
    : ENCENDERMOTOR LPAREN expr COMMA expr RPAREN
    ;

apagarmotor    
    : APAGARMOTOR LPAREN expr RPAREN
    ;

activarrele    
    : ACTIVARRELE LPAREN expr RPAREN
    ;

desactivarrele 
    : DESACTIVARRELE LPAREN expr RPAREN
    ;

prenderrgb     
    : PRENDERRGB LPAREN expr COMMA expr COMMA expr COMMA expr RPAREN
    ;

apagarrgb      
    : APAGARRGB LPAREN expr COMMA expr COMMA expr RPAREN
    ;

// --- Expresiones ---
expr
    : termino ((ADD | SUB) termino)*
    ;

termino
    : factor ((MUL | DIV) factor)*
    ;

factor
    : INT
    | ID
    | STRING
    | LPAREN expr RPAREN
    ;

comparador
    : EQ | NEQ | LT | LE | GT | GE
    ;

// --- Tokens ---

PRENDERLED      : 'PRENDERLED' ;
APAGARLED       : 'APAGARLED' ;
LEERSENSOR      : 'LEERSENSOR' ;
MOVERSERVO      : 'MOVERSERVO' ;
ESPERAR         : 'ESPERAR' ;
SI              : 'SI' ;
ENTONCES        : 'ENTONCES' ;
TOCARBUZZER     : 'TOCARBUZZER' ;
ESCRIBIRLCD     : 'ESCRIBIRLCD' ;
ENCENDERMOTOR   : 'ENCENDERMOTOR' ;
APAGARMOTOR     : 'APAGARMOTOR' ;
ACTIVARRELE     : 'ACTIVARRELE' ;
DESACTIVARRELE  : 'DESACTIVARRELE' ;
PRENDERRGB      : 'PRENDERRGB' ;
APAGARRGB       : 'APAGARRGB' ;

ESTATICO        : 'ESTATICO' ;
LOOP            : 'LOOP' ;

EQ              : '==' ;
NEQ             : '!=' ;
LT              : '<' ;
LE              : '<=' ;
GT              : '>' ;
GE              : '>=' ;
AS              : '=' ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

LPAREN      : '(' ;
RPAREN      : ')' ;
COMMA       : ',' ;
SEMICOLON   : ';' ;

LBRACE      : '{' ;
RBRACE      : '}' ;

ID          : [a-zA-Z_][a-zA-Z_0-9]* ;
INT         : [0-9]+ ;
STRING      : '"' (~["\r\n] | '\\"')* '"' ;

WS          : [ \t\r\n]+ -> skip ;
COMMENT     : '//' ~[\r\n]* -> skip ;
