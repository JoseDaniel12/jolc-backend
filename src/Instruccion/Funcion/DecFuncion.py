from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
from src.Entorno.SimboloFuncion import *
from src.Errores.TablaErrores import *
from src.Entorno.SimboloVariable import *
from src.Reportes.Cst import *

class DecFuncion(Instruction):
    def __init__(self, id, listaParams, listaIns, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.id = id
        self.listaParams = listaParams
        self.listaIns = listaIns


    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        simboloFunc = SimboloFuncion(self.id, self.listaParams, self.listaIns, self.linea, self.columna)
        simboloExistente = ambito.getVariable(self.id)
        if simboloExistente is not None and type(simboloExistente) == SimboloVariable:
            agregarError(Error(f"Redefinicion invalida de {self.id}", self.linea,self.columna))
            return res
        else:
            ambito.addVariable(self.id, simboloFunc)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "DEC_FUNC", idPadre)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "Id", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #listaParams
        if len(self.listaParams) > 0:
            idListaParams = getNewId()
            defElementCst(idListaParams, "LISTA_PARAMS", self.idSent)
            for param in self.listaParams:
                param.generateCst(idListaParams)
        #listaIns
        if len(self.listaIns) > 0:
            idListaIns = getNewId()
            defElementCst(idListaIns, "INS_FUNC", self.idSent)
            for ins in self.listaIns:
                ins.generateCst(idListaIns)