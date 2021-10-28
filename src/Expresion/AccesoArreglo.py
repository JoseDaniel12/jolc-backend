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

        if simboloArreglo.tipo == TipoDato.ARREGLO:
            nuevo_mapeo = simboloArreglo.mapeo_tipos_arreglo[:]
            # esto pq se debe poner el mapeo desde la gramtica
            res.tipo = nuevo_mapeo.pop()
            res.mapeo_tipos_arreglo = nuevo_mapeo

        lbl_error = GenCod3d.addLabel()
        lbl_continuar = GenCod3d.addLabel()
        tmp_posHeapInicioArreglo = GenCod3d.addTemporal()
        tmp_tamanoArreglo = GenCod3d.addTemporal()
        tmp_posElementoArreglo = GenCod3d.addTemporal()
        tmp_elemento = GenCod3d.addTemporal()
        GenCod3d.addCodigo3d(f'{tmp_posHeapInicioArreglo} = {simboloArreglo.valor}; // Se obtiene indice de inicio del arreglo en el heap \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tmp_posElementoArreglo} = {tmp_posHeapInicioArreglo} + {simboloAcceso.valor}; // Se obtiene el indice del elemento deseado en el heap del arreglo \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tmp_tamanoArreglo} = heap[int({tmp_posHeapInicioArreglo})]; // Se obtiene el tamaño del arreglo \n',sectionCode3d)
        GenCod3d.addCodigo3d(f'if ({simboloAcceso.valor} < 1) {{ goto {lbl_error}; }} \n',sectionCode3d)
        GenCod3d.addCodigo3d(f'if ({simboloAcceso.valor} > {tmp_tamanoArreglo}) {{ goto {lbl_error}; }} \n', sectionCode3d)

        GenCod3d.addCodigo3d( f'{tmp_elemento} = heap[int({tmp_posElementoArreglo})]; // Se obtiene el elemento deseado \n', sectionCode3d)
        if res.tipo == TipoDato.BOOLEANO:
            res.lbl_true = GenCod3d.addLabel()
            res.lbl_false = GenCod3d.addLabel()
            GenCod3d.addCodigo3d(f'if ({tmp_elemento} == 1) {{ goto {res.lbl_true}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {res.lbl_false}; \n', sectionCode3d)
        if res.tipo == TipoDato.STRUCT:
            res.molde = simboloArreglo.molde

        GenCod3d.addCodigo3d(f'goto {lbl_continuar}; \n', sectionCode3d)

        GenCod3d.addCodigo3d(f'{lbl_error}: \n', sectionCode3d)
        list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "Bounds Error\n"))
        GenCod3d.addCodigo3d(f'{lbl_continuar}: \n', sectionCode3d)

        res.valor = tmp_elemento
        # se guarda temporal no utilizado y se limpian los utilizados
        GenCod3d.temporales_funcion.append(res.valor)
        GenCod3d.limpiar_temps_usados(simboloArreglo.valor)
        GenCod3d.limpiar_temps_usados(simboloAcceso.valor)
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