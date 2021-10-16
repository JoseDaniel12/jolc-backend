from src.Expresion.Arreglo import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class AccesoArreglo(Expresion):
    def __init__(self, expArreglo, expAcceso, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expArreglo = expArreglo
        self.expAcceso = expAcceso

    def ejecutar(self, ambito):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.ejecutar(ambito)
        simboloAcceso = self.expAcceso.ejecutar(ambito)

        if simboloAcceso is None or simboloArreglo is None:
            return None
        elif simboloArreglo.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"No se puede acceder a una posicion de una elemeto que no se de tipo {TipoDato.ARREGLO.value}", self.linea,self.columna))
            return None
        elif simboloAcceso.tipo != TipoDato.ENTERO and simboloAcceso.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"El indice de acceso de un arreglo debe ser {TipoDato.ENTERO.value} o un Rango", self.linea,self.columna))
            return None
        elif simboloAcceso.tipo != TipoDato.ARREGLO and (simboloAcceso.valor < 1 or simboloAcceso.valor > len(simboloArreglo.valor)):
            agregarError(Error(f"El indice {simboloAcceso.valor} no se encuentra en un rango aceptado", self.linea, self.columna))
            return None

        if simboloArreglo.tipo != TipoDato.ARREGLO:
            return res
        if simboloAcceso.tipo == TipoDato.ENTERO:
            return simboloArreglo.valor[simboloAcceso.valor - 1]
        elif simboloAcceso.tipo == TipoDato.ARREGLO:
            valores = []
            for i in simboloAcceso.valor:
                valores.append(simboloArreglo.valor[i.valor - 1])
            res.valor = valores
            res.tipo = TipoDato.ARREGLO
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResExp(None, None)

        simboloArreglo = self.expArreglo.compilar(ambito, sectionCode3d)
        simboloAcceso = self.expAcceso.compilar(ambito, sectionCode3d)

        if simboloAcceso is None or simboloArreglo is None:
            return None
        elif simboloArreglo.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"No se puede acceder a una posicion de una elemeto que no se de tipo {TipoDato.ARREGLO.value}",self.linea, self.columna))
            return None
        elif simboloAcceso.tipo != TipoDato.ENTERO and simboloAcceso.tipo != TipoDato.ARREGLO:
            agregarError(Error(f"El indice de acceso de un arreglo debe ser {TipoDato.ENTERO.value} o un Rango", self.linea, self.columna))
            return None

        if simboloArreglo.tipo != TipoDato.ARREGLO or simboloAcceso.tipo != TipoDato.ENTERO:
            return None

        tmp_posHeapInicioArreglo = GenCod3d.addTemporal()
        tmp_posElementoArreglo = GenCod3d.addTemporal()
        tmp_elemento = GenCod3d.addTemporal()
        GenCod3d.addCodigo3d(f'{tmp_posHeapInicioArreglo} = {simboloArreglo.valor} // Se obtiene indice de inicio del arreglo en el heap \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tmp_posElementoArreglo} = {tmp_posHeapInicioArreglo} + {simboloAcceso.valor}; // Se obtiene el indice del elemento deseado del arreglo en el heap \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tmp_elemento} = heap[int({tmp_posElementoArreglo})]; // Se obtiene el elemento deseado \n', sectionCode3d)
        res.valor = tmp_elemento
        nuevo_mapeo = simboloArreglo.mapeo_tipos_arreglo[:]
        res.tipo = nuevo_mapeo.pop()
        if simboloArreglo.tipo == TipoDato.ARREGLO:
            res.mapeo_tipos_arreglo = nuevo_mapeo
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "ACCESO_ARREGLO", idPadre)
        #expArreglo
        idExpArreglo = getNewId()
        defElementCst(idExpArreglo, "ARREGLO", self.idSent)
        self.expArreglo.generateCst(idExpArreglo)
        #expAcceso
        idExpAcceso = getNewId()
        defElementCst(idExpAcceso, "EXP_ACCESO", self.idSent)
        self.expAcceso.generateCst(idExpAcceso)