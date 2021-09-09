import uuid

class SimboloTabla:
    def __init__(self, nombre, tipo, ambito, fila, columna):
        self.nombre = nombre
        self.tipo = tipo
        self.ambito = ambito
        self.fila = fila
        self.columna = columna
    
    def getAsSerializable(self):
        return  {
            'id': uuid.uuid4(),
            'nombre': self.nombre,
            'tipo': self.tipo,
            'ambito': self.ambito,
            'fila': self.fila,
            'columna': self.columna
        }

    def isEquals(self, simbolo):
        if (self.nombre == simbolo.nombre and
            self.ambito == simbolo.ambito and
            self.fila == simbolo.fila):
            return True
        return False


tablaSimbolos = []
def agregarSimboloTabla(simbolo):
    for s in tablaSimbolos:
        if s.isEquals(simbolo):
            s.tipo = simbolo.tipo
            return
    tablaSimbolos.append(simbolo)

def getTablaSimbolosAsSerializable():
    res  = []
    for simbolo in tablaSimbolos:
        res.append(simbolo.getAsSerializable())
    return res

def limpiarTablaSimbolos():
    tablaSimbolos.clear()
