import time

class Error:
    def __init__(self, descripcion, linea, columna):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.fecha = str(time.strftime('%Y-%m-%d'))
        self.hora = str(time.strftime('%H:%M:%S'))

    def getAsString(self):
        return f"Error(Linea: {self.linea}, Columna: {self.columna}): {self.descripcion}."

    def getAsJson(self):
        return  {
            "descripcion": self.descripcion,
            "linea": self.linea,
            "columna": self.columna,
            "fecha": self.fecha,
            "hora": self.hora,
        }