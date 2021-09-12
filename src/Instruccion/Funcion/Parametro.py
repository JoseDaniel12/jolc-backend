from src.Reportes.Cst import *

class Parametro:
    def __init__(self, id, tipo, linea, columna):
        self.idSent = getNewId()
        self.id = id
        self.id = id
        self.tipo = tipo
        self.linea = linea
        self.columna = columna


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "PARAMETRO", idPadre)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "ID", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #tipo
        if self.tipo is not None:
            idTipo = getNewId()
            defElementCst(idTipo, "TIPO", self.idSent)
            defElementCst(getNewId(), self.tipo.value, idTipo)