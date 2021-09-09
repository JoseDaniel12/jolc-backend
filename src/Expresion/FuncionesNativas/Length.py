from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

class Length(Expresion):
    def __init__(self, expArreglo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expArreglo = expArreglo

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.ejecutar(ambito)
        if simboloArreglo is None:
            return None
        elif simboloArreglo.tipo  != TipoDato.ARREGLO:
            agregarError(Error(f"Funcion length recibe un {TipoDato.ARREGLO.name}",self.linea, self.columna))
            return None

        res.valor = len(simboloArreglo.valor)
        res.tipo = TipoDato.ENTERO
        return res


    def generateCst(self, idPadre):
        pass