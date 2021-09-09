from abc import ABC, abstractmethod
from src.Instruccion.ResIns import *
import uuid

class Instruction(ABC):
    def __init__(self, linea, columna):
        self.idSent = uuid.uuid4()
        self.linea = linea
        self.columna = columna

    @abstractmethod
    def ejecutar(self, ambito) -> ResIns:
        pass

    @abstractmethod
    def generateCst(self, idPadre):
        pass
