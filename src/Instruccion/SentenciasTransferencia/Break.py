from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *

class Break(Instruction):
    def __init__(self, linea, columna):
        Instruction.__init__(self, linea, columna)

    def ejecutar(self, ambito):
        res = ResIns()
        res.breakEncontrado = True;
        return res


    def generateCst(self, idPadre):
        pass