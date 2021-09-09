from src.Reportes.Cst import *

class BloqueCondicional:
    def __init__(self, condicion, listaIns, linea, columna):
        self.idSent = getNewId()
        self.condicion = condicion
        self.listaIns = listaIns
        self.linea = linea
        self.columna = columna


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "BLOQUE_COND", idPadre)
        #condicion
        idCondicion = getNewId()
        defElementCst(idCondicion, "CONDICION", self.idSent)
        self.condicion.generateCst(idCondicion)
        #listIns
        if len(self.listaIns) > 0:
            idListaIns = getNewId()
            defElementCst(idListaIns, "LISTA_INS", self.idSent)
            for ins in self.listaIns:
                ins.generateCst(idListaIns)