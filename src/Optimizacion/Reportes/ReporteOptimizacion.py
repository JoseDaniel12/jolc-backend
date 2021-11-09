import uuid


class ReporteOptimizacion:
        optimizaciones = []

        @staticmethod
        def agregarOptimizacion(tipo, regla, codOriginal, codOptimizado, linea):
            ReporteOptimizacion.optimizaciones.append(Optimizacion(tipo, regla, codOriginal, codOptimizado, linea))

        @staticmethod
        def getReporteOptimizacionAsSerializable():
            res = []
            for optimizacion in ReporteOptimizacion.optimizaciones:
                res.append(optimizacion.getAsSerializable())
            print(res)
            return res

        @staticmethod
        def limpiarReporteOptimizacion():
            ReporteOptimizacion.optimizaciones.clear()


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