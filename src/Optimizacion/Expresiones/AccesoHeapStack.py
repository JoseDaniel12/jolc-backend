from src.Optimizacion.SentenciaC3d import *

class AccesoHeapStack(SentenciaC3d):
    def __init__(self, heapStack, exp, linea):
        SentenciaC3d.__init__(self, linea)
        self.heapStack = heapStack
        self.exp = exp

    def getCode(self):
        return f'{self.heapStack}[{self.exp.getCode()}]'