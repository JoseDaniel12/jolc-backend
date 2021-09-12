from src.Instruccion.Instruccion import *
from src.Errores.TablaErrores import *
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *

class ModificacionArreglo(Instruction):
    def __init__(self, expArreglo, expIndice, expValor, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.expArreglo = expArreglo
        self.expIndice = expIndice
        self.expValor = expValor

    def ejecutar(self, ambito):
        res = ResIns()
        simboloArreglo = self.expArreglo.ejecutar(ambito)
        simboloExpIndice = self.expIndice.ejecutar(ambito)
        if simboloArreglo is None or simboloExpIndice is None:
            return res
        elif simboloArreglo.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"No se puede acceder a una posicion de una elemeto que no se de tipo {TipoDato.ARREGLO.value}", self.linea,self.columna))
            return res
        elif simboloExpIndice.tipo != TipoDato.ENTERO:
            agregarError(Error(f"El indice de acceso de un arreglo debe ser {TipoDato.ENTERO.value}", self.linea,self.columna))
            return res
        elif simboloExpIndice.valor < 1 or simboloExpIndice.valor > len(simboloArreglo.valor):
            agregarError(Error(f"El indice no se encuentra en un rango aceptado", self.linea, self.columna))
            return res
        simboloValor = self.expValor.ejecutar(ambito)
        if simboloValor is None:
            return res
        simboloArreglo.valor[simboloExpIndice.valor - 1] = simboloValor
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "MOD_ARREGLO", idPadre)
        #expArreglo
        idExpArreglo = getNewId()
        defElementCst(idExpArreglo, "EXP_ARREGLO", self.idSent)
        self.expArreglo.generateCst(idExpArreglo)
        #expIndice
        idExpIndice = getNewId()
        defElementCst(idExpIndice, "EXP_INDICE", self.idSent)
        self.expIndice.generateCst(idExpIndice)
        #expValor
        idExpValor = getNewId()
        defElementCst(idExpValor, "EXP_VALOR", self.idSent)
        self.expValor.generateCst(idExpValor)