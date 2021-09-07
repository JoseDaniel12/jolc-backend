from datetime import date
today = date.today()
class Error:
    def __init__(self, descripcion, linea, columna ):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
        self.fecha = str(today.day) + "/" + str(today.month) + "/" + str(today.year)

    def getAsString(self):
        return f"Error(Linea: {self.linea}, Columna: {self.columna}, Fecha: {self.fecha}): {self.descripcion}."