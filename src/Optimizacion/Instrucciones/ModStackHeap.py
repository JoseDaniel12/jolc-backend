from src.Optimizacion.SentenciaC3d import *

class ModStackHeap(SentenciaC3d):
    def __init__(self, stackHeap, expAcceso, expValor, linea):
        SentenciaC3d.__init__(self, linea)
        self.stackHeap = stackHeap
        self.expAcceso = expAcceso
        self.expValor = expValor

    def getCode(self):
        if not self.is_deleted:
            return f'{self.stackHeap}[{self.expAcceso.getCode()}] = {self.expValor.getCode()};'
        return ''