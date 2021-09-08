from src.Instruccion.Struct.StructInstance import StructInstance
from src.Entorno.SimboloFuncion import SimboloFuncion
from src.Entorno.SimboloStruct import SimboloStruct
from src.Entorno.SimboloVariable import SimboloVariable
from src.Reportes.TablaSimbolos import *


class Ambito:
    def __init__(self, anterior, nombre):
        self.anterior = anterior
        self.nombre = nombre
        self.variables = {}
        self.funciones = {}
        self.estructuras = {}

    def getAmbitoGlobal(self):
        ambitoActual = self
        while not (ambitoActual.anterior is None):
            ambitoActual = ambitoActual.anterior
        return ambitoActual

    def addVariable(self, id, simbolo):
        if type(simbolo) == SimboloVariable:
            if type(simbolo.valor) == StructInstance:
                agregarSimboloTabla(SimboloTabla(id, simbolo.valor.tipoStruct, self.getAsString(), simbolo.linea, simbolo.columna))
            else:
                agregarSimboloTabla(SimboloTabla(id, simbolo.tipo.name, self.getAsString(), simbolo.linea, simbolo.columna))
        elif type(simbolo) == SimboloFuncion:
            agregarSimboloTabla(SimboloTabla(id, "funcion", self.getAsString(), simbolo.linea, simbolo.columna))
        elif type(simbolo) == SimboloStruct:
            agregarSimboloTabla(SimboloTabla(id, "struct", self.getAsString(), simbolo.linea, simbolo.columna))
        self.variables[id] = simbolo

    def existeSimbolo(self, id):
        ambitoActual = self
        while ambitoActual is not None:
            if id in ambitoActual.variables:
                return True
            ambitoActual = ambitoActual.anterior
        return False

    def getVariable(self, id):
        ambitoActual = self
        while ambitoActual is not None:
            if id in ambitoActual.variables:
                return ambitoActual.variables[id]
            ambitoActual = ambitoActual.anterior
        return None

    def getAsString(self):
        listaAmbitos = []
        ambitoActual = self
        while ambitoActual is not None:
            listaAmbitos.append(ambitoActual.nombre)
            ambitoActual = ambitoActual.anterior 
        listaAmbitos.reverse()
        return "_".join(listaAmbitos)