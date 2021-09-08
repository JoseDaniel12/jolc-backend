from src.Instruccion.Instruccion import *
from src.Entorno.SimboloVariable import *
from src.Entorno.SimboloStruct import *

class DecStruct(Instruction):
    def __init__(self, isMutable, id, listaPropiedades,  linea, columna):
        Instruction.__init__(self, linea, columna)
        self.isMutable = isMutable
        self.id = id
        self.listaPropiedades = listaPropiedades

    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        simboloStruct = SimboloStruct(self.isMutable, self.id, self.listaPropiedades, self.linea, self.columna)
        ambito.addVariable(self.id, simboloStruct)
        return res
