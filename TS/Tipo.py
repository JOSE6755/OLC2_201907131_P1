from enum import Enum

class TIPO(Enum):
    ENTERO = 1
    DECIMAL = 2
    BOOLEANO = 3
    CARACTER = 4
    CADENA = 5
    NULO = 6
    ARREGLO = 7
    STRUCT = 8

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIV = 4
    POT = 5
    MOD = 6
    UMENOS = 7

class OperadorRelacional(Enum):
    MENORQUE = 1
    MAYORQUE = 2
    MENORIGUAL = 3
    MAYORIGUAL = 4
    IGUALIGUAL = 5
    DIFERENTE = 6

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3
    