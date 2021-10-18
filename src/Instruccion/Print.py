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

            #marco el temporal de la expresion a imprimir como utilizado
            GenCod3d.limpiar_temps_usados(simboloExp.valor)

            if simboloExp.tipo == TipoDato.ENTERO:
                GenCod3d.addCodigo3d(f'fmt.Printf("%d", int({simboloExp.valor})); \n', sectionCode3d)
            elif simboloExp.tipo == TipoDato.DECIMAL:
                GenCod3d.addCodigo3d(f'fmt.Printf("%f", {simboloExp.valor}); \n', sectionCode3d)
            elif simboloExp.tipo == TipoDato.NONE:
                list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "nothing"))
            elif simboloExp.tipo == TipoDato.BOOLEANO:
                lbl_finalizar = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCode3d)
                list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "true"))
                GenCod3d.addCodigo3d(f'goto {lbl_finalizar}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCode3d)
                list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "false"))
                GenCod3d.addCodigo3d(f'{lbl_finalizar}: \n')
            elif simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
                GenCod3d.addPrintString()
                GenCod3d.addCodigo3d(f'\n\t/* Inicio paso de parametros */ \n', sectionCode3d)
                tmp_paramPosStack = GenCod3d.addTemporal()
                posParamStack = ambito.size + len(GenCod3d.temporales_funcion)
                GenCod3d.addCodigo3d(f'{tmp_paramPosStack} = sp + {posParamStack + 1}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tmp_paramPosStack})] = {simboloExp.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'/* Fin paso de parametros */ \n', sectionCode3d)
                # llamada de funcion nativa
                avanceAmbito = ambito.size + len(GenCod3d.temporales_funcion)
                GenCod3d.addCodigo3d(f'\n\t/* Inicio llamda a nativa de impresion */ \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp + {avanceAmbito}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'printString(); \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {avanceAmbito}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'/* Fin llamda a nativa de impresion */ \n\n', sectionCode3d)

        if self.isEnter:
            GenCod3d.addCodigo3d(f'fmt.Printf("%c", 10); \n', sectionCode3d)

        GenCod3d.addCodigo3d('\n', sectionCode3d)
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "print", idPadre)
        for exp in self.listaExp:
            exp.generateCst(self.idSent)
