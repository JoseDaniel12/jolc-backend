from src.Instruccion.ResIns import *

def ejectuarBloqueIns(listaIns, ambito):
    res = ResIns()
    for instruccion in listaIns:
        respuesta = instruccion.ejecutar(ambito)
        res.textoConsola += respuesta.textoConsola
        if respuesta.breakEncontrado:
            res.breakEncontrado = True
            return res
        elif respuesta.continueEncontrado:
            res.continueEncontrado = True
            return res
        elif respuesta.returnEncontrado:
            res.returnEncontrado = True
            res.returnSimbolo = respuesta.returnSimbolo
            return res
    return res


    def generateCst(self, idPadre):
        pass