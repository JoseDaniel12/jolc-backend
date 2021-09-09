from src.Expresion.Expresion import Expresion
from src.Tipos.TipoExpArtimetica import TipoExpAritmetica
from src.Expresion.ResExp import ResExp
from src.Tipos.TipoDato import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *


class OpAritmetica(Expresion):
    def __init__(self, opIzq, opDer, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = tipo

    def ejecutar(self, ambito):
        res = ResExp("", "")

        simboloOpIzq = self.opIzq.ejecutar(ambito)
        simboloOpDer = None

        if self.tipo != TipoExpAritmetica.UMENOS:
            simboloOpDer = self.opDer.ejecutar(ambito)


        if simboloOpIzq is None or (simboloOpDer is None and self.tipo != TipoExpAritmetica.UMENOS):
            return None

        if self.tipo == TipoExpAritmetica.SUMA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.name} invalida {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor + simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.RESTA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.name} invalida {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor - simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.MULTIPLICACION:
            if simboloOpIzq.tipo == TipoDato.CADENA and simboloOpDer.tipo == TipoDato.CADENA:
                res.tipo = TipoDato.CADENA
                res.valor = simboloOpIzq.valor + simboloOpDer.valor
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.name} invalida {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                    res.valor = simboloOpIzq.valor * simboloOpDer.valor
                else:
                    res.tipo = TipoDato.ENTERO
                    res.valor = simboloOpIzq.valor * simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.DIVISION:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.name} invalida {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}",self.linea, self.columna))
                return None
            else:
                res.tipo = TipoDato.DECIMAL
            res.valor = simboloOpIzq.valor / simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.POTENCIA:
            if simboloOpIzq.tipo == TipoDato.CADENA and simboloOpDer.tipo == TipoDato.ENTERO:
                res.valor = ""
                for i in range(simboloOpDer.valor):
                    res.valor += simboloOpIzq.valor
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.name} invalida {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                else:
                    res.tipo = TipoDato.ENTERO
                res.valor = simboloOpIzq.valor ** simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.MODULO:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.name} invalido {simboloOpIzq.tipo.name} con {simboloOpDer.tipo.name}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor % simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.UMENOS:
            if simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL:
                agregarError(Error(f"{self.tipo.name} invalido con tipo {simboloOpIzq.tipo.name}", self.linea, self.columna))
                return None
            else:
                res.valor = -1 * simboloOpIzq.valor
                res.tipo = simboloOpIzq.tipo
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, self.tipo.name, idPadre)
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