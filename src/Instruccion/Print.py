from src.Instruccion.Instruccion import Instruction
from src.Instruccion.ResIns import ResIns
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

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

    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        texto = ""
        for i in range(len(self.listaExp)):
            simboloExp = self.listaExp[i].compilar(ambito, sectionCode3d)
            if simboloExp is None:
                return res
            elif simboloExp.tipo == TipoDato.ENTERO or simboloExp.tipo == TipoDato.DECIMAL:
                GenCod3d.addCodigo3d(f'fmt.Print({simboloExp.valor}); \n', sectionCode3d)
            elif simboloExp.tipo == TipoDato.NONE:
                GenCod3d.addCodigo3d('fmt.Printf("%c", 110); \n', sectionCode3d)
                GenCod3d.addCodigo3d('fmt.Printf("%c", 117); \n', sectionCode3d)
                GenCod3d.addCodigo3d('fmt.Printf("%c", 108); \n', sectionCode3d)
                GenCod3d.addCodigo3d('fmt.Printf("%c", 108); \n', sectionCode3d)
            elif simboloExp.tipo == TipoDato.BOOLEANO:
                lbl_finalizar = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCode3d)
                list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "true"))
                GenCod3d.addCodigo3d(f'goto {lbl_finalizar}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCode3d)
                list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "false"))
                GenCod3d.addCodigo3d(f'{lbl_finalizar}: \n')
            elif simboloExp.tipo == TipoDato.CADENA:
                GenCod3d.addPrintString()
                tempStack = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloExp.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp + {ambito.size}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'printString(); \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {ambito.size}; \n', sectionCode3d)
                pass

        if self.isEnter:
            GenCod3d.addCodigo3d(f'fmt.Printf("%c", 10); \n', sectionCode3d)
        GenCod3d.addCodigo3d('\n', sectionCode3d)
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "print", idPadre)
        for exp in self.listaExp:
            exp.generateCst(self.idSent)
