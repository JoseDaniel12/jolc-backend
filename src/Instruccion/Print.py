from src.Instruccion.Instruccion import Instruction
from src.Instruccion.ResIns import ResIns
from src.Tipos.TipoDato import *

class Print(Instruction):
    def __init__(self, listaExp, linea, columna, isEnter = False):
        Instruction.__init__(self, linea, columna)
        self.listaExp = listaExp
        self.isEnter = isEnter

    def ejecutar(self, ambito):
        res = ResIns()
        texto = ""
        for i in range(len(self.listaExp)):
            simboloExp = self.listaExp[i].ejecutar(ambito)
            if simboloExp is None:
                return res
            else:
                texto += simboloExp.getPresentationMode() + " "
            if i == len(self.listaExp) - 1 and len(texto) > 0:
                texto = texto[0:len(texto) - 1]
        if self.isEnter:
            texto += "\n"
        res.textoConsola += texto
        return res
