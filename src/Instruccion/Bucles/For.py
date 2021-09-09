from src.Instruccion.Instruccion import *
from src.Entorno.Ambito import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Entorno.SimboloVariable import *

class For(Instruction):
    def __init__(self, id, expresion, listaIns, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.id = id
        self.expresion = expresion
        self.listaIns = listaIns

    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        simboloExp = self.expresion.ejecutar(ambito)

        if simboloExp is None:
            return res

        if simboloExp.tipo == TipoDato.CADENA:
            lista = list(simboloExp.valor)
            simboloExp.valor =  map(lambda x: ResExp(x, TipoDato.CARACTER), lista)

        for i in simboloExp.valor:
            nuevoAmbito = Ambito(ambito, "For")
            nuevoAmbito.addVariable(self.id, SimboloVariable(self.id, i.valor, i.tipo, self.linea, self.columna))
            resIns = ejectuarBloqueIns(self.listaIns, nuevoAmbito)
            res.textoConsola += resIns.textoConsola
            if resIns.breakEncontrado:
                return res
            elif res.returnSimbolo:
                res.returnEncontrado = True
                res.returnSimbolo = resIns.returnSimbolo
                return res
        return res


    def generateCst(self, idPadre):
        pass