from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class UpperCase(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.CADENA and simboloExp.tipo != TipoDato.CARACTER:
            agregarError(Error(f"Funcion uppercase recibe una {TipoDato.CADENA.value} o {TipoDato.CARACTER.value}",self.linea, self.columna))
            return None

        res.valor = simboloExp.valor.upper()
        res.tipo = simboloExp.tipo

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcUppercase", idPadre)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)