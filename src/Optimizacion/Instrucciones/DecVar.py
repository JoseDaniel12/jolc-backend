from src.Optimizacion.SentenciaC3d import *

class DecVar(SentenciaC3d):
    def __init__(self, destino, expresion, linea):
        SentenciaC3d.__init__(self, linea)
        self.destino = destino
        self.expresion = expresion

    def getCode(self):
        if self.is_deleted:
            return '// Instrucción eliminada \n'
        return f'{self.destino} = {self.expresion.getCode()}; \n'