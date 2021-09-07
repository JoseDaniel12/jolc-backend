from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

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
            agregarError(Error(f"El la funcion {self.tipoFunc} recibe una parmetro de {TipoDato.ENTERO.name} o un {TipoDato.DECIMAL.name}", self.linea,self.columna))
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
            res.valor = TipoDato.DECIMAL

        return res