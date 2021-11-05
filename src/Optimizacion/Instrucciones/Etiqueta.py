from src.Optimizacion.SentenciaC3d import *

class Etiqueta(SentenciaC3d):
    def __init__(self, id, linea):
        SentenciaC3d.__init__(self, linea)
        self.id = id

    def getCode(self):
        if not self.is_deleted:
            return f'{self.id}: \n'
        return '// Instrucción eliminada \n'