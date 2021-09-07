from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *

class Arreglo(Expresion):
    def __init__(self, listaExps, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.listaExps = listaExps

    def ejecutar(self, ambito) -> ResExp:
        res = ResExp(None, None)
        valores = []
        for exp in self.listaExps:
            simboloExp = exp.ejecutar(ambito)
            if simboloExp is not None:
                valores.append(simboloExp)
            else:
                return None
        res.valor = valores
        res.tipo = TipoDato.ARREGLO
        return res

