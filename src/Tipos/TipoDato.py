from enum import Enum

class TipoDato(Enum):
    IDENTIFICADOR = 'IDENTIFICADOR'
    ARREGLO = "ARREGLO"
    STRUCT  = "STRUCT"
    NONE = 'None'
    ENTERO = 'Int64'
    DECIMAL = 'Float64'
    BOOLEANO = 'Bool'
    CARACTER = 'Char'
    CADENA = "String"
