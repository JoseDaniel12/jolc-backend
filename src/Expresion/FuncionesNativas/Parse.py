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
        elif simboloExp.tipo == self.tipoParseo:
            res.valor = simboloExp.valor
            res.tipo = simboloExp.tipo
        elif simboloExp.tipo == TipoDato.ENTERO and self.tipoParseo == TipoDato.DECIMAL:
            res.valor = float(simboloExp.valor)
            res.tipo = TipoDato.DECIMAL
        elif simboloExp.tipo == TipoDato.DECIMAL and self.tipoParseo == TipoDato.ENTERO:
            res.valor = int(simboloExp.valor)
            res.tipo = TipoDato.ENTERO
        elif (simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER) and self.tipoParseo == TipoDato.ENTERO:
            try:
                res.valor = int(float(simboloExp.valor))
                res.tipo = TipoDato.ENTERO
            except:
                agregarError(Error(f"{simboloExp.valor} no puede ser casteado a {simboloExp.tipo.value}",self.linea, self.columna))
                return None
        elif (simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER) and self.tipoParseo == TipoDato.DECIMAL:
            try:
                res.valor = float(simboloExp.valor)
                res.tipo = TipoDato.DECIMAL
            except:
                agregarError(Error(f"{simboloExp.valor} no puede ser casteado a {simboloExp.tipo.value}",self.linea, self.columna))
                return None
        elif (simboloExp.tipo == TipoDato.ENTERO or simboloExp.tipo == TipoDato.DECIMAL) and self.tipoParseo == TipoDato.CADENA:
            res.valor = str(simboloExp.valor)
            res.tipo = TipoDato.CADENA
        else:
            agregarError(Error(f"{simboloExp.valor} no puede ser casteado a {simboloExp.tipo.value}", self.linea, self.columna))
            return None

        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResExp(None, None)
        simboloExp = self.exp.compilar(ambito, sectionCode3d)

        # reviso si hay errores
        if simboloExp is None:
            return None

        tmp_valorTipoDeseado = GenCod3d.addTemporal()
        if simboloExp.tipo == self.tipoParseo:
            res.tipo = simboloExp.tipo
        elif simboloExp.tipo == TipoDato.ENTERO and self.tipoParseo == TipoDato.DECIMAL:
            GenCod3d.addCodigo3d(f'{tmp_valorTipoDeseado} = float64({simboloExp.valor}); \n', sectionCode3d)
            res.tipo = TipoDato.DECIMAL
        elif simboloExp.tipo == TipoDato.DECIMAL and self.tipoParseo == TipoDato.ENTERO:
            if "math" not in GenCod3d.imports:
                GenCod3d.imports += "\t\"math\" \n"
            tmp_decimales = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tmp_decimales} = math.Mod({simboloExp.valor}, 1); \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_valorTipoDeseado} = {simboloExp.valor} - {tmp_decimales}; \n', sectionCode3d)
            res.tipo = TipoDato.ENTERO
        elif (simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER) and self.tipoParseo == TipoDato.ENTERO:
            pass
        res.valor = tmp_valorTipoDeseado
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcParse", idPadre)
        #tipoParse
        if self.tipoParseo is not None:
            idTipoParse = getNewId()
            defElementCst(idTipoParse, "Tipo_Parseo", self.idSent)
            defElementCst(getNewId(), self.tipoParseo.value, idTipoParse)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)