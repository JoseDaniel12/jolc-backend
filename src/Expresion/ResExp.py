from src.Tipos.TipoDato import *

class ResExp:
    def __init__(self, valor, tipo):
        self.textoConsola = "" #eliminar al poner global los prints
        self.breakEncontrado = ""
        self.continueEncontrado = ""
        self.returnEncontrado = ""
        self.valor = valor
        self.tipo = tipo

    def getPresentationMode(self):
        if self.tipo == TipoDato.ARREGLO:
            valoresPresentacion = []
            for simbolo in self.valor:
                valoresPresentacion.append(simbolo.getPresentationMode())
            return valoresPresentacion
        elif self.tipo == TipoDato.STRUCT:
            texto = self.valor.tipoStruct + "("
            contador = 0
            for key in self.valor.propiedades:
                texto += str(self.valor.propiedades[key].getPresentationMode())
                if contador != len(self.valor.propiedades) - 1:
                    texto += ", "
                contador += 1
            texto += ")"
            return texto
        else:
            return self.valor
