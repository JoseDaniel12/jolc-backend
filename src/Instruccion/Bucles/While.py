from src.Instruccion.Instruccion import *
from src.Entorno.Ambito import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Errores.TablaErrores import *

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


    def generateCst(self, idPadre):
        pass