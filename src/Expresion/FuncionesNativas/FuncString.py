from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *


class FuncString(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None

        res.valor = simboloExp.getPresentationMode()
        if simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
            res.valor = res.valor[1:len(res.valor)-1]
        res.tipo = TipoDato.CADENA

        return res

    def compilar(self, ambito, sectionCode3d):
        agregarError(Error(f"funcion string no implementada", self.linea, self.columna))
        return None

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcString", idPadre)
        self.exp.generateCst(self.idSent)