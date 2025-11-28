# ArduinoMexa Compiler

Compilador y Entorno de Desarrollo (IDE) que traduce instrucciones en lenguaje natural (español) a código nativo de Arduino, facilitando la programación de sistemas embebidos.

## Información del Curso
Materia: Programación de Sistemas de Base 2
Institución:UNIVERSIDAD AUTONOMA DE TAMAULIPAS FACULTAD DE INGENIERIA TAMPICO
Grado y Grupo: 9º Semestre - Grupo J
Profesor: Ing. Dante Adolfo Muñoz Quintero

## Integrantes del Equipo
1. Pérez Cristino Víctor Alejandro - a2213332152
2. De La Cruz Márquez Rodrigo - a2213332192
3. Lorenzo Sánchez Lexiss - a2213332176
4. Juárez Beltrán Moisés Eduardo - a2213332172

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:
* `/src`: Código fuente del compilador (Lexer, Parser, Visitor y GUI).
* `/docs`: Documentación técnica y manual de usuario.
* `/examples`: Casos de prueba.
    * `/valid`: Ejemplos de código correctos.
    * `/invalid`: Ejemplos con errores intencionales para pruebas.
    * `/expected`: Archivos `.ino` generados exitosamente.
* `/tests`: Scripts de pruebas automatizadas.

## Requisitos y Dependencias
Para ejecutar este proyecto se requiere:
* Python 3.8 o superior.
* Librería ANTLR4.
* Tkinter (Generalmente incluido en la instalación de Python).
* Arduino IDE

## Instrucciones de Compilación y Ejecución
1. Abrir una terminal en la carpeta raíz del proyecto.
2. Instalar dependencias

##Ejempos de uso
1.-LOOP
    valor = LEERSENSOR(A0);
    MOVERSERVO(9, valor);
    ESPERAR(50);

2.-LOOP
    PRENDERLED(13, 1);
    ESPERAR(3000);
    
    APAGARLED(13);
    PRENDERLED(12, 1);
    ESPERAR(1000);
    
    APAGARLED(12);
    PRENDERLED(11, 1);
    TOCARBUZZER(8, 440);
    ESPERAR(500);
    TOCARBUZZER(8, 0); 
    ESPERAR(2500);
    APAGARLED(11);