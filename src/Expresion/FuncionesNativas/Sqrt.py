from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

import math

class Sqrt(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"La funcion nativa sqrt recibe como parametro un {TipoDato.ENTERO.value} o un {TipoDato.Decimal.value}",self.linea, self.columna))
            return None

        res.valor = math.sqrt(simboloExp.valor)
        if res.valor - int(res.valor) == 0:
            res.tipo = TipoDato.ENTERO
        else:
            res.tipo = TipoDato.DECIMAL
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcSqrt", idPadre)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)