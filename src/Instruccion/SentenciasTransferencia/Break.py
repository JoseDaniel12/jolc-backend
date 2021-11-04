from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class Break(Instruction):
    def __init__(self, linea, columna):
        Instruction.__init__(self, linea, columna)

    def ejecutar(self, ambito):
        res = ResIns()
        res.breakEncontrado = True
        return res


    def compilar(self, ambito, sectionCode3d):
        if self.lbl_break == '':
            agregarError(Error(f"Break no se ecuentra dentro de una funcion", self.linea, self.columna))
            return
        GenCod3d.addCodigo3d(f'goto {self.lbl_break}; \n')


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "break" ,idPadre)