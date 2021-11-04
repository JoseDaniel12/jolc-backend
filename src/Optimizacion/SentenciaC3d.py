from abc import ABC, abstractmethod

class SentenciaC3d(ABC):

    def __init__(self, linea):
        self.linea = linea
        self.haveInt = False
        self.is_deleted = False

    @abstractmethod
    def getCode(self):
        pass