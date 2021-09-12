from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *

class TypeOf(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None

        if simboloExp.tipo == TipoDato.STRUCT:
            res.valor = simboloExp.valor.tipoStruct
        else:
            res.valor = simboloExp.tipo.value
        res.tipo = TipoDato.CADENA

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcTypeOf", idPadre)
        #expresion
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)