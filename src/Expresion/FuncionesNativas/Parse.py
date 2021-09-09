from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *


class Parse(Expresion):
    def __init__(self, tipoParseo, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.tipoParseo = tipoParseo
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.CADENA:
            agregarError(Error(f"La funcion parse solo parse cadenas",self.linea, self.columna))
            return None
        elif self.tipoParseo != TipoDato.ENTERO and self.tipoParseo != TipoDato.DECIMAL:
            agregarError(Error(f"Solo se puede parsear una cadena a {TipoDato.ENTERO.name} o {TipoDato.DECIMAL.name}",self.linea, self.columna))
            return None

        if self.tipoParseo == TipoDato.ENTERO:
            try:
                res.valor = int(float(simboloExp.valor))
            except:
                agregarError(Error(f"{simboloExp.valor} no puede ser casteado a un tipo numerico",self.linea, self.columna))
                return None 
            res.tipo = TipoDato.ENTERO
        else:
            res.valor = float(simboloExp.valor)
            res.tipo = TipoDato.DECIMAL

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcParse", idPadre)