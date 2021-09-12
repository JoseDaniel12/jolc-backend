from src.Expresion.Expresion import *
from src.Tipos.TipoExpRelacional import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Errores.TablaErrores import *
from src.Errores.Error import *
from src.Reportes.Cst import *

class OpRelacional(Expresion):
    def __init__(self, opIzq, opDer, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = tipo

    def ejecutar(self, ambito):
        res = ResExp(None, TipoDato.BOOLEANO)
        simboloOpIzq = self.opIzq.ejecutar(ambito)
        simboloOpDer = self.opDer.ejecutar(ambito)
        if simboloOpIzq is None or simboloOpDer is None:
            return None
        try:
            if self.tipo == TipoExpRelacional.MAYORQUE:
                res.valor = simboloOpIzq.valor > simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MENORQUE:
                res.valor = simboloOpIzq.valor < simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MAYORIGUAL:
                res.valor = simboloOpIzq.valor >= simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MENORIGUAL:
                res.valor = simboloOpIzq.valor <= simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.IGUALIGUAL:
                res.valor = simboloOpIzq.valor == simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.NOIGUAL:
                res.valor = simboloOpIzq.valor != simboloOpDer.valor
        except:
            agregarError(Error(f"{self.tipo.value} invalido {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea,  self.columna))
            return None
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, self.tipo.value, idPadre)
        #opIzq
        if self.opIzq is not None:
            idOpIzq  = getNewId()
            defElementCst(idOpIzq, "EXPRESION", self.idSent)
            self.opIzq.generateCst(idOpIzq)
        #opDer
        if self.opDer is not None:
            idOpDer  = getNewId()
            defElementCst(idOpDer, "EXPRESION", self.idSent)
            self.opDer.generateCst(idOpDer)