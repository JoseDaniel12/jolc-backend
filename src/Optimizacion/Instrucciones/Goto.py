from src.Optimizacion.SentenciaC3d import *

class Goto(SentenciaC3d):
    def __init__(self, etiqueta, linea):
        SentenciaC3d.__init__(self, linea)
        self.etiqueta = etiqueta

    def getCode(self):
        if not self.is_deleted:
            return f'goto {self.etiqueta};'
        return ''