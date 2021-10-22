from enum import Enum

class TipoDato(Enum):
    IDENTIFICADOR = 'IDENTIFICADOR'
    ARREGLO = "Array"
    STRUCT  = "Struct"
    NONE = 'Nothing'
    ENTERO = 'Int64'
    DECIMAL = 'Float64'
    BOOLEANO = 'Bool'
    CARACTER = 'Char'
    CADENA = "String"
