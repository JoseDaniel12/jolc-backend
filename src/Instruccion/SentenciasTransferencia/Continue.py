from src.Instruccion.Instruccion import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class Continue(Instruction):
    def __init__(self, linea, columna):
        Instruction.__init__(self, linea, columna)

    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        res.continueEncontrado = True
        return res

    def compilar(self, ambito, sectionCode3d):
        GenCod3d.addCodigo3d(f'goto {self.lbl_continue}; \n')

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "continue", idPadre)