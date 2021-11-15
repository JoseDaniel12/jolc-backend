from src.Instruccion.Instruccion import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class While(Instruction):
    def __init__(self, condicion, listaIns, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.condicion = condicion
        self.listaIns = listaIns

    def ejecutar(self, ambito):
        contador = 0
        resWhile = ResIns()
        simboloCondicion = self.condicion.ejecutar(ambito)
        if simboloCondicion is None:
            return resWhile
        while simboloCondicion.valor:
            nuevoAmbito = Ambito(ambito, "While")
            resIns = ejectuarBloqueIns(self.listaIns, nuevoAmbito)
            resWhile.textoConsola += resIns.textoConsola
            if resIns.breakEncontrado:
                return resWhile
            elif resIns.returnEncontrado:
                resWhile.returnEncontrado = True
                resWhile.returnSimbolo = resIns.returnSimbolo
                return resWhile
            contador += 1
            simboloCondicion = self.condicion.ejecutar(nuevoAmbito)
            if simboloCondicion is None:
                return resWhile
            elif contador == 10000:
                agregarError(Error(f"Se han superado las 10,000 iteraciones", self.linea, self.columna))
                return resWhile

        return resWhile


    def compilar(self, ambito, sectionCode3d):
        resWhile = ResIns()

        lbl_inicioWhile = GenCod3d.addLabel()
        lbl_instruccionesWhile = GenCod3d.addLabel()
        lbl_finWhile = GenCod3d.addLabel()

        self.condicion.lbl_true = lbl_instruccionesWhile
        self.condicion.lbl_false = lbl_finWhile

        GenCod3d.addCodigo3d(f'{lbl_inicioWhile}: \n', sectionCode3d)
        self.condicion.compilar(ambito, sectionCode3d)
        GenCod3d.addCodigo3d(f'{lbl_instruccionesWhile}: \n', sectionCode3d)
        #compilo mis instrucciones
        nuevoAmbito = Ambito(ambito, "While")
        nuevoAmbito.size += ambito.size
        for ins in self.listaIns:
            ins.lbl_return = self.lbl_return
            ins.lbl_continue = lbl_inicioWhile
            ins.lbl_break = lbl_finWhile
            ins.compilar(nuevoAmbito, sectionCode3d)

        if len(self.listaIns) == 0:
            GenCod3d.addCodigo3d(f'goto {lbl_finWhile}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'goto {lbl_inicioWhile}; \n', sectionCode3d)

        GenCod3d.addCodigo3d(f'{lbl_finWhile}: \n', sectionCode3d)

        return resWhile




    def generateCst(self, idPadre):
        defElementCst(self.idSent, "WHILE", idPadre)
        #Condicion
        idCondicion = getNewId()
        defElementCst(idCondicion, "EXPRESION", self.idSent)
        self.condicion.generateCst(idCondicion)
        #listaIns
        idListaIns = getNewId()
        defElementCst(idListaIns, "LISTA_INS", self.idSent)
        for ins in self.listaIns:
            ins.generateCst(idListaIns)