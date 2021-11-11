from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *


class FuncString(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None

        res.valor = simboloExp.getPresentationMode()
        if simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
            res.valor = res.valor[1:len(res.valor)-1]
        res.tipo = TipoDato.CADENA

        return res

    def compilar(self, ambito, sectionCode3d):
        # agregarError(Error(f"funcion string no implementada", self.linea, self.columna))
        # return None
        res = ResExp(None, None)
        simboloExp = self.exp.compilar(ambito, sectionCode3d)
        if simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"funcion string solo trabaja con tipos numericos", self.linea, self.columna))
            return None
        res.tipo = TipoDato.CADENA
        GenCod3d.addToString()
        if "math" not in GenCod3d.imports:
            GenCod3d.imports += "\t\"math\" \n"
        tempStack = GenCod3d.addTemporal()
        tempHeap = GenCod3d.addTemporal()
        tempRetorno = GenCod3d.addTemporal()
        # paso de parametros a la funcion nartiva
        GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion) + 1}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloExp.valor}; \n', sectionCode3d)
        # llamada de funcion nativa
        avanceAmbito = ambito.size + len(GenCod3d.temporales_funcion)
        GenCod3d.addCodigo3d(f'sp = sp + {avanceAmbito}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'toString(); \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tempRetorno} = stack[int(sp)]; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'sp = sp - {avanceAmbito}; \n', sectionCode3d)
        res.valor = tempRetorno
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcString", idPadre)
        self.exp.generateCst(self.idSent)