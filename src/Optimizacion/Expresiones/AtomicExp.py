from src.Optimizacion.SentenciaC3d import *
from src.Tipos.TipoDato import *

class AtomiExp(SentenciaC3d):
    def __init__(self, valor, tipo, linea):
        SentenciaC3d.__init__(self, linea)
        self.valor = valor
        self.tipo = tipo

    def getCode(self):
        return f'{self.valor}'