from src.Optimizacion.SentenciaC3d import *

class Return(SentenciaC3d):
    def __init__(self, linea):
        SentenciaC3d.__init__(self, linea)

    def getCode(self):
        if not self.is_deleted:
            return 'return;'
        return ''