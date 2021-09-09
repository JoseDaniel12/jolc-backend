from src.Instruccion.Instruccion import *

class Continue(Instruction):
    def __init__(self, linea, columna):
        Instruction.__init__(self, linea, columna)

    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        res.continueEncontrado = True
        return res


    def generateCst(self, idPadre):
        pass