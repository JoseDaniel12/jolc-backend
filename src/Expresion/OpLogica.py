from src.Expresion.Expresion import *
from src.Tipos.TipoExpLogica import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Errores.TablaErrores import *
from src.Errores.Error import *
from src.Reportes.Cst import *

class OpLogica(Expresion):
    def __init__(self,opIzq, opDer, tipo, fila, columna):
        Expresion.__init__(self, fila, columna)
        self.opIzq = opIzq
        self.opDer= opDer
        self.tipo = tipo

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        if self.tipo == TipoExpLogica.NOT:
            simboloOp =  self.opIzq.ejecutar(ambito)
            if simboloOp is None:
                return None
            elif simboloOp.tipo != TipoDato.BOOLEANO:
                agregarError(Error(f"{self.tipo.value} el operador debe ser {TipoDato.BOOLEANO.value}.", self.linea, self.columna))
                return None
            res.valor = not simboloOp.valor
            res.tipo = TipoDato.BOOLEANO
        else:
            simboloOpIzq = self.opIzq.ejecutar(ambito)
            simboloOpDer = self.opDer.ejecutar(ambito)
            if simboloOpIzq.tipo != TipoDato.BOOLEANO  or simboloOpDer.tipo != TipoDato.BOOLEANO:
                agregarError(Error(f"{self.tipo.value} fallido ambos operandos deben ser booleanos.", self.linea, self.columna))
                return None
            else:
                res.tipo = TipoDato.BOOLEANO
                if self.tipo == TipoExpLogica.OR:
                    res.valor = simboloOpIzq.valor or simboloOpDer.valor
                elif self.tipo == TipoExpLogica.AND:
                    res.valor = simboloOpIzq.valor and simboloOpDer.valor
                elif self.tipo == TipoExpLogica.NOT:
                    res.valor = not simboloOpIzq.valor
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