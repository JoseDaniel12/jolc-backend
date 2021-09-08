from abc import ABC

class Simbolo(ABC):
    def __init__(self, id, tipoSimbolo, linea, columna):
        self.id = id
        self.tipoSimbolo = tipoSimbolo
        self.linea = linea
        self.columna = columna
