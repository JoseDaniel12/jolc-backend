from src.Entorno.Simbolo import *
from src.Tipos.TipoSimbolo import *

class SimboloFuncion(Simbolo):
    def __init__(self, id, listaParams, listaIns, linea, columna, tipoRetorno):
        Simbolo.__init__(self, id, TipoSimbolo.FUNCION, linea, columna)
        self.listaParams = listaParams
        self.listaIns = listaIns
        self.tipoRetorno = tipoRetorno
