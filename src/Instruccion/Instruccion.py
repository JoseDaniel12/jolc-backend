from abc import ABC, abstractmethod
from src.Instruccion.ResIns import *

class Instruction(ABC):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    @abstractmethod
    def ejecutar(self, ambito) -> ResIns:
        pass
