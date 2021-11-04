from src.Optimizacion.SentenciaC3d import *

class Print(SentenciaC3d):
    def __init__(self, tipoImpresion, expresion, linea):
        SentenciaC3d.__init__(self, linea)
        self.tipoImpresion = tipoImpresion
        self.expresion = expresion

    def getCode(self):
        if not self.is_deleted:
            return f'fmt.Printf("{self.tipoImpresion}", {self.expresion.getCode()});'
        return ''