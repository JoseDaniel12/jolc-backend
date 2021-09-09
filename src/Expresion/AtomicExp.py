from src.Expresion.Expresion import  Expresion
from src.Expresion.ResExp import ResExp
from src.Tipos.TipoDato import *
from src.Errores.TablaErrores import *
from src.Errores.Error import *
from src.Reportes.Cst import *

class AtomicExp(Expresion):
    def __init__(self, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.tipo = tipo

    def ejecutar(self, ambito):
        if self.tipo == TipoDato.IDENTIFICADOR:
            simbolo = ambito.getVariable(self.valor)
            if simbolo is None:
                agregarError(Error(f"La variable {self.valor} no esta definida", self.linea, self.columna))
                return None
            else:
                return ResExp(simbolo.valor, simbolo.tipo)
        return ResExp(self.valor, self.tipo)


    def generateCst(self, idPadre):
        defElementCst(self.idSent, str(self.valor), idPadre)