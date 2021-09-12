from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

import math

class Trunc(Expresion):
    def __init__(self, tipo, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipo = tipo
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif self.tipo is not None and (self.tipo != TipoDato.ENTERO and self.tipo != TipoDato.DECIMAL):
            agregarError(Error(f"Al truncar solo se puede retornar un {TipoDato.ENTERO.value} o un {TipoDato.DECIMAL.value}",self.linea, self.columna))
            return None
        elif simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"No se puede truncar un valor que no sea tipo {TipoDato.ENTERO.value} o un {TipoDato.DECIMAL.value}",self.linea, self.columna))
            return None

        res.valor = math.trunc(simboloExp.valor)
        if self.tipo is not None:
            res.tipo = self.tipo
        else:
            if res.valor - int(res.valor) == 0:
                res.tipo = TipoDato.ENTERO
            else:
                res.tipo = TipoDato.DECIMAL
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcTrunc", idPadre)
        #tipo
        if self.tipo is not None:
            idTipo = getNewId()
            defElementCst(idTipo, "TIPO", self.idSent)
            defElementCst(getNewId(), self.tipo.value, idTipo)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)