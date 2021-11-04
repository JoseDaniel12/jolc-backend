from src.Optimizacion.SentenciaC3d import *

class Parseo(SentenciaC3d):
    def __init__(self, tipoParseo, exp, linea):
        SentenciaC3d.__init__(self, linea)
        self.tipoParseo = tipoParseo
        self.exp = exp

    def getCode(self):
        return f'{self.tipoParseo}({self.exp.getCode()})'