from src.Entorno.SimboloVariable import *
from src.Entorno.SimboloFuncion import *
from src.Entorno.SimboloStruct import *

class SimboloTabla:
    def __init__(self, nombre, tipo, ambito, fila, columna):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.fila = fila
        self.columna = columna
    
    def getAsSerializable(self):
        return  {
            'nombre': self.nombre,
            'tipo': self.tipo,
            'ambito': self.ambito,
            'fila': self.fila,
            'columna': self.columna
        }

tablaSimbolos = []

def agregarSimboloTabla(simbolo):
    
    tablaSimbolos.append(simbolo)

def getTablaSimbolosAsSerializable():
    res  = []
    for simbolo in tablaSimbolos:
        res.append(simbolo.getAsSerializable())
    return res

def limpiarTablaSimbolos():
    tablaSimbolos.clear()
