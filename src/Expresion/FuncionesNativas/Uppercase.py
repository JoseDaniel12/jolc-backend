from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class UpperCase(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.CADENA and simboloExp.tipo != TipoDato.CARACTER:
            agregarError(Error(f"Funcion uppercase recibe una {TipoDato.CADENA.value} o {TipoDato.CARACTER.value}",self.linea, self.columna))
            return None

        res.valor = simboloExp.valor.upper()
        res.tipo = simboloExp.tipo

        return res


    def compilar(self, ambito, sectionCode3d):
        res  = ResExp(None, None)
        simboloExp = self.exp.compilar(ambito, sectionCode3d)

        # se veirifica si hay errores
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.CADENA and simboloExp.tipo != TipoDato.CARACTER:
            agregarError(Error(f"Funcion uppercase recibe una {TipoDato.CADENA.value} o {TipoDato.CARACTER.value}",self.linea, self.columna))
            return None

        GenCod3d.addUpperCase()
        tempStack = GenCod3d.addTemporal()
        tempRetorno = GenCod3d.addTemporal()

        # se convierte a mayusculas
        GenCod3d.addCodigo3d('\n\t/* Inicio de llamada de funcion */ \n', sectionCode3d)

        # paso de parametros
        GenCod3d.addCodigo3d('/* Inicio de paso de parametros */ \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + 1}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloExp.valor}; \n', sectionCode3d)
        GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCode3d)
        # llamada de funcion nativa
        GenCod3d.addCodigo3d(f'sp = sp + {ambito.size}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'uppercase(); \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tempRetorno} = stack[int(sp)]; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'sp = sp - {ambito.size}; \n', sectionCode3d)

        GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCode3d)

        res.valor = tempRetorno
        res.tipo = simboloExp.tipo
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "funcUppercase", idPadre)
        #exp
        idExp = getNewId()
        defElementCst(idExp, "EXPRESION", self.idSent)
        self.exp.generateCst(idExp)