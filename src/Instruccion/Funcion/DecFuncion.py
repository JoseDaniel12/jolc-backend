from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
from src.Entorno.SimboloFuncion import *
from src.Entorno.Simbolo import *
from src.Errores.TablaErrores import *
from src.Entorno.SimboloVariable import *

class DecFuncion(Instruction):
    def __init__(self, id, listaParams, listaIns, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.id = id
        self.listaParams = listaParams
        self.listaIns = listaIns


    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        simboloFunc = SimboloFuncion(self.id, self.listaParams, self.listaIns)
        simboloExistente = ambito.getVariable(self.id)
        if simboloExistente is not None and type(simboloExistente) == SimboloVariable:
            agregarError(Error(f"Redefinicion invalida de {self.id}", self.linea,self.columna))
            return res
        else:
            ambito.addVariable(self.id, simboloFunc)
        return res