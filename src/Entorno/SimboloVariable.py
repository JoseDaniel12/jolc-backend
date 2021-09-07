from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloVariable(Simbolo):
    def __init__(self, id, valor, tipo):
        Simbolo.__init__(self, id, TipoSimbolo.VARIABLE)
        self.valor = valor
        self.tipo = tipo
