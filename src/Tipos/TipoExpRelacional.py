from enum import Enum

class TipoExpRelacional(Enum):
    MAYORQUE= ">"
    MENORQUE = "<"
    MAYORIGUAL = ">="
    MENORIGUAL = "<="
    IGUALIGUAL = "=="
    NOIGUAL = "!="