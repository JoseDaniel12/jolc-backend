import uuid

optimizaciones = []

class Optimizacion:
    def __init__(self, tipo, regla, codOriginal, codOptimizado, linea):
        self.tipo = tipo
        self.regla = regla
        self.codOriginal = codOriginal
        self.codOptimizado = codOptimizado
        self.linea = linea

    def getAsSerializable(self):
        return {
            'key': uuid.uuid4(),
            'tipo': self.tipo,
            'regla': self.regla,
            'codOriginal': self.codOriginal,
            'codOptimizado': self.codOptimizado,
            'linea': self.linea
        }


def agregarOptimizacion(tipo, regla, codOriginal, codOptimizado, linea):
    optimizaciones.append(Optimizacion(tipo, regla, codOriginal, codOptimizado, linea))


def getReporteOptimizacionAsSerializable():
    res = []
    global optimizaciones
    for optimizacion in optimizaciones:
        res.append(optimizacion.getAsSerializable())
    return res


def limpiarReporteOptimizacion():
    optimizaciones.clear()
