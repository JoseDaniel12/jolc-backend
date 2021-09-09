from abc import ABC, abstractmethod
from src.Entorno.Simbolo import *
import uuid

class Expresion(ABC):
    def __init__(self, linea, columna):
        self.idSent = uuid.uuid4();
        self.linea = linea
        self.columna = columna

    @abstractmethod
    def ejecutar(self, ambito) -> Simbolo:
        pass


    @abstractmethod
    def generateCst(self, idPadre):
        pass