from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

import math

class Trunc(Expresion):
    def __init__(self, tipo, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"La funcion nativa sqrt recibe como parametro un {TipoDato.ENTERO.name} o un {TipoDato.Decimal.name}",self.linea, self.columna))
            return None

        res.valor = math.sqrt(simboloExp.valor)
        if res.valor - int(res.valor):
            res.tipo = TipoDato.ENTERO
        else:
            res.tipo = TipoDato.DECIMAL
        return res
