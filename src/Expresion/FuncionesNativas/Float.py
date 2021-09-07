from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

import math

class Float(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.ENTERO:
            agregarError(Error(f"La funcion float recibe como parametro un {TipoDato.ENTERO.name}",self.linea, self.columna))
            return None

        res.valor = float(simboloExp.valor)
        res.tipo = TipoDato.DECIMAL

        return res
