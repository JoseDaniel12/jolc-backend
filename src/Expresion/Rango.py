from src.Expresion.Expresion import *
from src.Tipos.TipoDato import *
from src.Expresion.ResExp import *

class Rango(Expresion):
    def __init__(self, inicio, fin, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.inicio = inicio
        self.fin = fin

    def ejecutar(self, ambito) -> ResExp:
        res = ResExp(None, None)
        simboloInicio = self.inicio.ejecutar(ambito)
        simboloFin = self.fin.ejecutar(ambito)
        if simboloInicio.tipo != TipoDato.ENTERO  or simboloFin.tipo != TipoDato.ENTERO:
            return res
        else:
            valores = []
            for i in range(simboloInicio.valor, simboloFin.valor + 1):
                valores.append(ResExp(i, TipoDato.ENTERO))
            res.valor = valores
            res.tipo = TipoDato.ARREGLO
        return res