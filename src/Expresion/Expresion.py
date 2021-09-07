from abc import ABC, abstractmethod
from src.Entorno.Simbolo import *

class Expresion(ABC):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    @abstractmethod
    def ejecutar(self, ambito) -> Simbolo:
        pass
