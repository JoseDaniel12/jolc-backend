from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloVariable(Simbolo):
    def __init__(self, id, valor, tipo, linea, columna):
        Simbolo.__init__(self, id, TipoSimbolo.VARIABLE, linea, columna)
        self.valor = valor
        self.tipo = tipo
