from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *

class LowerCase(Expresion):
    def __init__(self, exp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.exp = exp

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloExp = self.exp.ejecutar(ambito)
        if simboloExp is None:
            return None
        elif simboloExp.tipo != TipoDato.CADENA and simboloExp.tipo != TipoDato.CARACTER:
            agregarError(Error(f"Funcion uppercase recibe una {TipoDato.CADENA.name} o {TipoDato.CARACTER.name}",self.linea, self.columna))
            return None

        res.valor = simboloExp.valor.lower()
        res.tipo = simboloExp.tipo


        return res