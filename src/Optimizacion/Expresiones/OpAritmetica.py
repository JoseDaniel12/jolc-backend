from src.Tipos.TipoExpArtimetica import *
from src.Optimizacion.Expresiones.AtomicExp import *
from src.Tipos.TipoDato import *

class OpAritmetica(SentenciaC3d):
    def __init__(self, opIzq, opDer, tipoOp, linea):
        SentenciaC3d.__init__(self, linea)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipoOp = tipoOp

    def desitno_in_operands(self, destino):
        if self.tipoOp != TipoExpAritmetica.UMENOS:
            return destino == self.opIzq.getCode() or destino == self.opDer.getCode()
        else:
            return False

    def is_neutral_op(self):
        if self.tipoOp == TipoExpAritmetica.SUMA or self.tipoOp == TipoExpAritmetica.RESTA:
           return self.opIzq.getCode() == '0' or self.opDer.getCode() == '0'
        elif self.tipoOp == TipoExpAritmetica.MULTIPLICACION:
            return self.opIzq.getCode() == '1' or self.opDer.getCode() == '1'
        elif self.tipoOp == TipoExpAritmetica.DIVISION:
            return self.opDer.getCode() == '1'
        return False

    def get_no_neutral_op(self):
        if self.tipoOp == TipoExpAritmetica.SUMA or self.tipoOp == TipoExpAritmetica.RESTA:
            if self.opIzq.getCode() == '0':
                if self.tipoOp == TipoExpAritmetica.RESTA:
                    self.opDer.valor = 0 - self.opDer.valor
                return self.opDer
            return self.opIzq
        elif self.tipoOp == TipoExpAritmetica.MULTIPLICACION:
            if self.opIzq.getCode() == '1':
                return self.opDer
            return self.opIzq
        elif self.tipoOp == TipoExpAritmetica.DIVISION:
            return self.opIzq

    def get_cheper_expresion(self):
        if self.tipoOp == TipoExpAritmetica.MULTIPLICACION:
            if self.opIzq.getCode() == '0' or self.opDer.getCode() == '0':
                return AtomiExp(0, TipoDato.ENTERO, self.opIzq.linea)
            elif self.opIzq.getCode() == '2':
                self.opIzq = self.opDer
                self.tipoOp = TipoExpAritmetica.SUMA
                return self
            elif self.opDer.getCode() == '2':
                self.opDer = self.opIzq
                self.tipoOp = TipoExpAritmetica.SUMA
                return self
        elif self.tipoOp == TipoExpAritmetica.DIVISION:
            if self.opIzq.getCode() == '0':
                return AtomiExp(0, TipoDato.ENTERO, self.opIzq.linea)
        return None

    def getCode(self):
        if self.tipoOp == TipoExpAritmetica.SUMA:
            return f'{self.opIzq.getCode()} + {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpAritmetica.RESTA:
            return f'{self.opIzq.getCode()} - {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpAritmetica.MULTIPLICACION:
            return f'{self.opIzq.getCode()} * {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpAritmetica.DIVISION:
            return f'{self.opIzq.getCode()} / {self.opDer.getCode()}'
        elif self.tipoOp == TipoExpAritmetica.MODULO:
            return f'math.Mod({self.opIzq.getCode()}, {self.opDer.getCode()})'
        elif self.tipoOp == TipoExpAritmetica.UMENOS:
            return f'-{self.opIzq.getCode()}'