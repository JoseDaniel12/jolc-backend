from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

import math

class FuncLogaritmica(Expresion):
    def __init__(self, tipoFunc, listaExp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipoFunc = tipoFunc
        self.listaExp = listaExp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        if self.tipoFunc == "log10"  and len(self.listaExp) != 1:
            agregarError(Error(f"{self.tipoFunc} solo recibe un parametro",self.linea, self.columna))
            return None
        elif self.tipoFunc == "log" and len(self.listaExp) != 2:
            agregarError(Error(f"{self.tipoFunc} nesecita dos parametros", self.linea, self.columna))
            return None

        simboloBase = None
        simboloValor = None
        if self.tipoFunc == "log10":
            simboloBase =  ResExp(10, TipoDato.ENTERO)
            simboloValor = self.listaExp[0].ejecutar(ambito)
        if self.tipoFunc == "log":
            simboloBase = self.listaExp[0].ejecutar(ambito)
            simboloValor = self.listaExp[1].ejecutar(ambito)

        if simboloBase is None or simboloValor is None:
            return None
        elif simboloBase.tipo != TipoDato.ENTERO and simboloBase.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"{self.tipoFunc} espera una base de tipo {TipoDato.ENTERO.name} o {TipoDato.DECIMAL.name}", self.linea, self.columna))
            return None
        elif simboloValor.tipo != TipoDato.ENTERO and simboloValor.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"{self.tipoFunc} espera un valor de tipo {TipoDato.ENTERO.name} o {TipoDato.DECIMAL.name}", self.linea, self.columna))
            return None

        res.valor = math.log(simboloValor.valor, simboloBase.valor)
        if res.valor - int(res.valor) == 0:
            res.tipo = TipoDato.ENTERO
        else:
            res.tipo = TipoDato.DECIMAL

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcLogaritmica", idPadre)
        #tipoFunc
        idTipoFunc = getNewId()
        defElementCst(idTipoFunc, "TIPO_FUNC", self.idSent)
        defElementCst(getNewId(), self.tipoFunc, idTipoFunc)
        if self.tipoFunc == "log10" and len(self.listaExp) == 1:
            #base
            idValor = getNewId()
            defElementCst(idValor, "VALOR", self.idSent)
            self.listaExp[0].generateCst(idValor)
        elif self.tipoFunc == "log" and len(self.listaExp) == 2:
            #base
            idBase = getNewId()
            defElementCst(idBase, "BASE", self.idSent)
            self.listaExp[0].generateCst(idBase)
            #base
            idValor = getNewId()
            defElementCst(idValor, "VALOR", self.idSent)
            self.listaExp[1].generateCst(idValor)