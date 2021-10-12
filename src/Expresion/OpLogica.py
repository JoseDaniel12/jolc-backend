from src.Tipos.TipoExpLogica import *
from src.Expresion.AtomicExp import *
from src.Compilacion.GenCod3d import *

class OpLogica(Expresion):
    def __init__(self, opIzq, opDer, tipo, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = tipo
        self.lbl_true = ''
        self.lbl_false = ''
        self.lbl_intermedio = ''

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        if self.tipo == TipoExpLogica.NOT:
            simboloOp =  self.opIzq.ejecutar(ambito)
            if simboloOp is None:
                return None
            elif simboloOp.tipo != TipoDato.BOOLEANO:
                agregarError(Error(f"{self.tipo.name} el operador debe ser {TipoDato.BOOLEANO.name}.", self.linea, self.columna))
                return None
            res.valor = not simboloOp.valor
            res.tipo = TipoDato.BOOLEANO
        else:
            simboloOpIzq = self.opIzq.ejecutar(ambito)
            simboloOpDer = self.opDer.ejecutar(ambito)
            if simboloOpIzq.tipo != TipoDato.BOOLEANO  or simboloOpDer.tipo != TipoDato.BOOLEANO:
                agregarError(Error(f"{self.tipo.name} fallido ambos operandos deben ser booleanos.", self.linea, self.columna))
                return None
            res.tipo = TipoDato.BOOLEANO
            if self.tipo == TipoExpLogica.OR:
                res.valor = simboloOpIzq.valor or simboloOpDer.valor
            elif self.tipo == TipoExpLogica.AND:
                res.valor = simboloOpIzq.valor and simboloOpDer.valor
            elif self.tipo == TipoExpLogica.NOT:
                res.valor = not simboloOpIzq.valor
        return res


    def compilar(self, ambito, sectionCodigo3d):
        lbl_intermedio = GenCod3d.addLabel()
        if self.lbl_true == '':
            self.lbl_true = GenCod3d.addLabel()
        if self.lbl_false == '':
            self.lbl_false = GenCod3d.addLabel()
        res = ResExp(None, TipoDato.BOOLEANO)
        res.lbl_true = self.lbl_true
        res.lbl_false = self.lbl_false

        if self.tipo == TipoExpLogica.NOT:
            self.opIzq.lbl_true = self.lbl_false
            self.opIzq.lbl_false = self.lbl_true
            self.opIzq.compilar(ambito, sectionCodigo3d)
        else:
            if self.tipo == TipoExpLogica.AND:
                self.opIzq.lbl_false = self.opDer.lbl_false = self.lbl_false
                self.opDer.lbl_true = self.lbl_true
                self.opIzq.lbl_true = lbl_intermedio
            elif self.tipo == TipoExpLogica.OR:
                self.opIzq.lbl_true = self.opDer.lbl_true = self.lbl_true
                self.opDer.lbl_false = self.lbl_false
                self.opIzq.lbl_false = lbl_intermedio
            self.opIzq.compilar(ambito, sectionCodigo3d)
            GenCod3d.addCodigo3d(f'{lbl_intermedio}: \n', sectionCodigo3d)
            self.opDer.compilar(ambito, sectionCodigo3d)

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, self.tipo.value, idPadre)
        #OpIzq
        if self.opIzq is not None:
            idOpIzq = getNewId()
            defElementCst(idOpIzq, "EXPRESION", self.idSent)
            self.opIzq.generateCst(idOpIzq)
        #opDer
        if self.opDer is not None:
            idOpDer = getNewId()
            defElementCst(idOpDer, "EXPRESION", self.idSent)
            self.opDer.generateCst(idOpDer)
