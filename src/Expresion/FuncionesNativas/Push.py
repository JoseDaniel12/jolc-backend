from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class Push(Expresion):
    def __init__(self, expArreglo, expValor, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expArreglo = expArreglo
        self.expValor = expValor

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.ejecutar(ambito)
        simboloValor = self.expValor.ejecutar(ambito)
        if simboloArreglo is None or simboloValor is None:
            return None
        elif simboloArreglo.tipo  != TipoDato.ARREGLO:
            agregarError(Error(f"No se pude hacer un push a un elemento que no es {TipoDato.ARREGLO.value}",self.linea, self.columna))
            return None

        simboloArreglo.valor.append(simboloValor)
        res.valor = simboloArreglo.valor
        res.tipo = TipoDato.ARREGLO
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcPush", idPadre)
        #expArreglo
        idExpArreglo = getNewId()
        defElementCst(idExpArreglo, "EXP_ARREGLO", self.idSent)
        self.expArreglo.generateCst(idExpArreglo)