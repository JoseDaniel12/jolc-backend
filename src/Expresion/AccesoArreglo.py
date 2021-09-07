from src.Expresion.Arreglo import *
from src.Errores.TablaErrores import *

class AccesoArreglo(Expresion):
    def __init__(self, expArreglo: Arreglo, expAcceso,  linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expArreglo = expArreglo
        self.expAcceso = expAcceso

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.ejecutar(ambito)
        simboloAcceso = self.expAcceso.ejecutar(ambito)

        if simboloAcceso is None or simboloArreglo is None:
            return None
        elif simboloArreglo.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"No se puede acceder a una posicion de una elemeto que no se de tipo {TipoDato.ARREGLO.name}", self.linea,self.columna))
            return None
        elif simboloAcceso.tipo != TipoDato.ENTERO and simboloAcceso.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"El indice de acceso de un arreglo debe ser {TipoDato.ENTERO.name} o un Rango", self.linea,self.columna))
            return None
        elif simboloAcceso.tipo != TipoDato.ARREGLO and (simboloAcceso.valor < 1 or simboloAcceso.valor > len(simboloArreglo.valor)):
            agregarError(Error(f"El indice no se encuentra en un rango aceptado", self.linea, self.columna))
            return None

        if simboloArreglo.tipo != TipoDato.ARREGLO:
            return res
        if simboloAcceso.tipo == TipoDato.ENTERO:
            return simboloArreglo.valor[simboloAcceso.valor - 1]
        elif simboloAcceso.tipo == TipoDato.ARREGLO:
            valores = []
            for i in simboloAcceso.valor:
                valores.append(simboloArreglo.valor[i.valor - 1])
            res.valor = valores
            res.tipo = TipoDato.ARREGLO
        return res