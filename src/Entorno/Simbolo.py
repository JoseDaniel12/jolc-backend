from abc import ABC

class Simbolo(ABC):
    def __init__(self, id, tipoSimbolo, linea, columna):
        self.id = id
        self.tipoSimbolo = tipoSimbolo
        self.linea = linea
        self.columna = columna
        self.lbl_true = ''
        self.lbl_false = ''
        self.is_param = False
        self.ambito_id = -1