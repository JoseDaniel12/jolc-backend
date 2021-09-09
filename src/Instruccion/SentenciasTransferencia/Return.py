from src.Instruccion.Instruccion import *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *

class Return(Instruction):
    def __init__(self, expresion, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.expresion = expresion

    def ejecutar(self, ambito):
        res = ResIns()
        if self.expresion is None:
            res.returnEncontrado = True
            res.returnSimbolo = ResExp("nothing", TipoDato.NONE)
        else:
            simboloExp = self.expresion.ejecutar(ambito)
            if simboloExp is None:
                return res
            else:
                res.returnEncontrado = True
                res.returnSimbolo = simboloExp
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "return", idPadre)