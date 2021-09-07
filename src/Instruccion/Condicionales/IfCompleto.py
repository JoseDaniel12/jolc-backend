from src.Instruccion.Instruccion import *
from src.Instruccion.Condicionales.BloqueCondicional import *
from src.Instruccion.ejecutarBloqueIns import *

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

