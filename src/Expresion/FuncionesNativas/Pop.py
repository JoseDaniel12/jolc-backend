from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class Pop(Expresion):
    def __init__(self, expArreglo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expArreglo = expArreglo

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.ejecutar(ambito)
        if simboloArreglo is None:
            return None
        elif simboloArreglo.tipo  != TipoDato.ARREGLO:
            agregarError(Error(f"No se pude hacer un pop a un elemento que no es {TipoDato.ARREGLO.name}",self.linea, self.columna))
            return None

        res = simboloArreglo.valor.pop()
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcPop", idPadre)