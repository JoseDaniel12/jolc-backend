from src.Expresion.Expresion import *
from src.Expresion.ResExp import *

class TypeOf(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None

        res.valor = simboloExp.tipo.name
        res.tipo = TipoDato.CADENA

        return res


    def generateCst(self, idPadre):
        pass