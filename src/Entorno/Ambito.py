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