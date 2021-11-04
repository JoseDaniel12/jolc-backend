from src.Optimizacion.SentenciaC3d import *
from src.Tipos.TipoExpRelacional import *

class OpRelacional(SentenciaC3d):
    def __init__(self, opIzq, opDer, tipoOp, linea):
        SentenciaC3d.__init__(self, linea)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp

    def get_tipo_op_contrario(self):
        if self.tipoOp == TipoExpRelacional.MAYORQUE:
            return TipoExpRelacional.MENORIGUAL
        elif self.tipoOp == TipoExpRelacional.MENORQUE:
            return TipoExpRelacional.MAYORIGUAL
        elif self.tipoOp == TipoExpRelacional.MAYORIGUAL:
            return TipoExpRelacional.MENORQUE
        elif self.tipoOp == TipoExpRelacional.MENORIGUAL:
            return TipoExpRelacional.MAYORQUE
        elif self.tipoOp == TipoExpRelacional.IGUALIGUAL:
            return TipoExpRelacional.NOIGUAL
        elif self.tipoOp == TipoExpRelacional.NOIGUAL:
            return TipoExpRelacional.IGUALIGUAL


    def getCode(self):
        if self.tipoOp == TipoExpRelacional.IGUALIGUAL:
            return f'{self.opIzq.getCode()} == {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpRelacional.MENORIGUAL:
            return f'{self.opIzq.getCode()} <= {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpRelacional.MAYORIGUAL:
            return f'{self.opIzq.getCode()} >= {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpRelacional.MENORQUE:
            return f'{self.opIzq.getCode()} < {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpRelacional.MAYORQUE:
            return f'{self.opIzq.getCode()} > {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpRelacional.NOIGUAL:
            return f'{self.opIzq.getCode()} != {self.opDer.getCode()}'