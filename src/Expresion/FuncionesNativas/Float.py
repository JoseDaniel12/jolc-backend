from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class Float(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.ENTERO:
            agregarError(Error(f"La funcion float recibe como parametro un {TipoDato.ENTERO.value}",self.linea, self.columna))
            return None

        res.valor = float(simboloExp.valor)
        res.tipo = TipoDato.DECIMAL

        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResExp(None, None)
        simboloExp = self.exp.compilar(ambito, sectionCode3d)

        # reviso si hay errores
        if simboloExp is None:
            return None
        if simboloExp.tipo != TipoDato.ENTERO and simboloExp.tipo != TipoDato.DECIMAL:
            agregarError(Error(f"La funcion float recibe como parametro un {TipoDato.ENTERO.value}",self.linea, self.columna))
            return None

        tmp_valor = GenCod3d.addTemporal()
        # se hace la conversion
        GenCod3d.addCodigo3d(f'{tmp_valor} = float64({simboloExp.valor}); \n', sectionCode3d)

        res.valor = tmp_valor
        res.tipo = TipoDato.DECIMAL
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "float", idPadre)
        #expresion
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)