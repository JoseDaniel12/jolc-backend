from src.Optimizacion.SentenciaC3d import *
from src.Tipos.TipoExpLogica import *

class OpLogica(SentenciaC3d):
    def __init__(self, opIzq, opDer, tipoOp, linea):
        SentenciaC3d.__init__(self, linea)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp

    def getCode(self):
        if self.tipoOp == TipoExpLogica.AND:
            return f'{self.opIzq.getCode()} && {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpLogica.OR:
            return f'{self.opIzq.getCode()} || {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpLogica.NOT:
            return f'!{self.opIzq.getCode()}'