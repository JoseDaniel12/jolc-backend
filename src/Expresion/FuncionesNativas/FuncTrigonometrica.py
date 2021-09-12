from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

import math

class FuncTrigonometrica(Expresion):
    def __init__(self, tipoFunc, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipoFunc = tipoFunc
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        simboloExp = self.exp.ejecutar(ambito)

        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"El la funcion {self.tipoFunc} recibe una parmetro de {TipoDato.ENTERO.value} o un {TipoDato.DECIMAL.value}", self.linea,self.columna))
            return None

        if self.tipoFunc == "sin":
            res.valor = math.sin(simboloExp.valor)
        elif self.tipoFunc == "cos":
            res.valor = math.cos(simboloExp.valor)
        elif self.tipoFunc == "tan":
            res.valor = math.tan(simboloExp.valor)

        if res.valor - int(res.valor) == 0:
            res.tipo = TipoDato.ENTERO
        else:
            res.tipo = TipoDato.DECIMAL

        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcTrigonometrica", idPadre)
        #tipoFunc
        idTipoFunc = getNewId()
        defElementCst(idTipoFunc, "TIPO_FUNC", self.idSent)
        defElementCst(getNewId(), self.tipoFunc, idTipoFunc)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)