from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

class AccesosStruct(Expresion):
    def __init__(self, expStruct, idProp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expStruct = expStruct
        self.idProp =   idProp

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        simboloStruct = self.expStruct.ejecutar(ambito)
        if simboloStruct is None:
            return None
        elif simboloStruct.tipo != TipoDato.STRUCT:
            agregarError(Error(f"No se puede acceder a un propiedad de un elemento que no sea {TipoDato.STRUCT.name}", self.linea,self.columna))
            return None
        elif simboloStruct.valor.propiedades.get(self.idProp) is None:
            agregarError(Error(f"{simboloStruct.valor.tipoStruct} no cuentra con la propiedad {self.idProp}", self.linea, self.columna))
            return None
        else:
            res = simboloStruct.valor.propiedades[self.idProp]
        return res


    def generateCst(self, idPadre):
        pass