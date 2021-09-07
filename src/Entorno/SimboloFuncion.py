from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloFuncion(Simbolo):
    def __init__(self, id, listaParams, listaIns):
        Simbolo.__init__(self, id, TipoSimbolo.FUNCION)
        self.listaParams = listaParams
        self.listaIns = listaIns

