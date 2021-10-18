from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

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
            agregarError(Error(f"Funcion length recibe un {TipoDato.ARREGLO.value}",self.linea, self.columna))
            return None

        res.valor = len(simboloArreglo.valor)
        res.tipo = TipoDato.ENTERO
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResExp(None, None)
        simboloArreglo = self.expArreglo.compilar(ambito, sectionCode3d)

        # se verifica que no hayan errores
        if simboloArreglo is None:
            return None
        elif simboloArreglo.tipo  != TipoDato.ARREGLO:
            agregarError(Error(f"Funcion length recibe un {TipoDato.ARREGLO.value}",self.linea, self.columna))
            return None

        # Se obtine la longitud del arreglo
        tmp_lenArreglo = GenCod3d.addTemporal()
        GenCod3d.addCodigo3d(f'{tmp_lenArreglo} = heap[int({simboloArreglo.valor})]; \n', sectionCode3d)
        res.valor = tmp_lenArreglo
        res.tipo = TipoDato.ENTERO
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcLength", idPadre)
        #expArreglo
        idExpSrreglo = getNewId()
        defElementCst(idExpSrreglo, "EXP_ARREGLO", self.idSent)
        self.expArreglo.generateCst(idExpSrreglo)