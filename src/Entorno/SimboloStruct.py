from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloStruct(Simbolo):
    def __init__(self, isMutable, id, propiedades, linea, columna):
        Simbolo.__init__(self, id, TipoSimbolo.STRUCT, linea, columna)
        self.isMutable = isMutable
        self.id = id
        self.propiedades = propiedades
