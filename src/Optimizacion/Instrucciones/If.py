from src.Optimizacion.SentenciaC3d import *

class If(SentenciaC3d):
    def __init__(self, exp, etiqueta, linea):
        SentenciaC3d.__init__(self, linea)
        self.exp = exp
        self.etiqueta = etiqueta

    def getCode(self):
        if not self.is_deleted:
            return f'if ({self.exp.getCode()}) {{ goto {self.etiqueta}; }} \n'
        return '// Instrucción eliminada \n'