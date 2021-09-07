from abc import ABC

class Simbolo(ABC):
    def __init__(self, id, tipoSimbolo):
        self.id = id
        self.tipoSimbolo = tipoSimbolo
