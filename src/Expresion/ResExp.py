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
            texto = "["
            for i in range(len(self.valor)):
                texto += self.valor[i].getPresentationMode()
                if i != len(self.valor) - 1:
                    texto += ", "
            texto += "]"
            return texto
        elif self.tipo == TipoDato.STRUCT:
            texto = self.valor.tipoStruct + "("
            contador = 0
            for key in self.valor.propiedades:
                texto += self.valor.propiedades[key].getPresentationMode()
                if contador != len(self.valor.propiedades) - 1:
                    texto += ", "
                contador += 1
            texto += ")"
            return texto
        else:
            if self.tipo == TipoDato.CADENA:
                return "\"" + self.valor + "\""
            elif self.tipo  ==  TipoDato.CARACTER:
                return "\'" + self.valor + "\'"
            return str(self.valor)
