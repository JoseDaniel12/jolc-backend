from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloStruct(Simbolo):
    def __init__(self, isMutable, id, propiedades):
        Simbolo.__init__(self, id, TipoSimbolo.STRUCT)
        self.isMutable = isMutable
        self.id = id
        self.propiedades = propiedades
