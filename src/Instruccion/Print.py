from src.Instruccion.Instruccion import Instruction
from src.Instruccion.ResIns import ResIns
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *

textoConsola = ""

def clearTextoConsola():
    global textoConsola
    textoConsola = ""

def addTextoConsola(texto):
    global textoConsola
    textoConsola += texto

def getTextoConsola():
    global textoConsola
    return textoConsola

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
                valorImpreison = simboloExp.getPresentationMode()
                if simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
                    valorImpreison = valorImpreison[1:len(valorImpreison)-1]
                texto += valorImpreison
        if self.isEnter:
            texto += "\n"
        res.textoConsola += texto
        global textoConsola
        addTextoConsola(texto)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "print", idPadre)
        for exp in self.listaExp:
            exp.generateCst(self.idSent)
