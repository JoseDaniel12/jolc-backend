from abc import ABC, abstractmethod
from src.Instruccion.ResIns import *
import uuid

class Instruction(ABC):
    def __init__(self, linea, columna):
        self.idSent = uuid.uuid4()
        self.linea = linea
        self.columna = columna
        self.lbl_break = ''
        self.lbl_continue = ''
        self.lbl_return = ''
        self.is_in_function = False

    @abstractmethod
    def ejecutar(self, ambito) -> ResIns:
        pass

    @abstractmethod
    def compilar(self, ambito, sectionCode3d):
        pass

    @abstractmethod
    def generateCst(self, idPadre):
        pass
