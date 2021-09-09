from src.Instruccion.Instruccion import *
from src.Entorno.SimboloStruct import *
from src.Reportes.Cst import *

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


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "DEC_STRUCT", idPadre)
        #mutabilidad
        if self.isMutable:
            idMutabilidad = getNewId()
            defElementCst(idMutabilidad, "MUTABILIDAD", self.idSent)
            defElementCst(getNewId(), "mutable", idMutabilidad)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "Id", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #listaPropiedades
        if len(self.listaPropiedades) > 0:
            idProp = getNewId()
            defElementCst(idProp, "PROPIEDAD", self.idSent)
            for prop in self.listaPropiedades:
                prop.generateCst(idProp)