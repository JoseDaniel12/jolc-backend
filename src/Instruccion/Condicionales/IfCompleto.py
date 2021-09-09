from src.Instruccion.Instruccion import *
from src.Instruccion.Condicionales.BloqueCondicional import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Reportes.Cst import *

class IfCompleto(Instruction):
    def __init__(self, ifSimple: BloqueCondicional, listaElseIf: [BloqueCondicional], linstaInsElse, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.IfSimple = ifSimple
        self.listaElseIf = listaElseIf
        self.listaInsElse = linstaInsElse

    def ejecutar(self, ambito):
        res = ResIns()
        simboloCondicion = self.IfSimple.condicion.ejecutar(ambito)
        if simboloCondicion is not None:
            if simboloCondicion.valor:
                return ejectuarBloqueIns(self.IfSimple.listaIns, ambito)
        else:
            return res

        for elseIf in self.listaElseIf:
            simboloCondicion = elseIf.condicion.ejecutar(ambito)
            if simboloCondicion is not None:
                if simboloCondicion.valor:
                    return  ejectuarBloqueIns(elseIf.listaIns, ambito)
            else:
                return res
        return ejectuarBloqueIns(self.listaInsElse, ambito)


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "IF_COMPLETO", idPadre)
        #ifSimple
        idIfSimple = getNewId()
        defElementCst(idIfSimple, "IF_SIMPLE", self.idSent)
        self.IfSimple.generateCst(idIfSimple)
        #listaElseIf
        if len(self.listaElseIf) > 0:
            idListaElseIf = getNewId()
            defElementCst(idListaElseIf, "Lista_ELSE_IF", self.idSent)
            for bloque in self.listaElseIf:
                bloque.generateCst(idListaElseIf)
        #else
        if len(self.listaInsElse) > 0:
            idElse = getNewId()
            defElementCst(idElse, "ELSE_INS", self.idSent)
            for ins in self.listaInsElse:
                ins.generateCst(idElse)