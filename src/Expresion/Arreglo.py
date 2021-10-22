from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *

class Arreglo(Expresion):
    def __init__(self, listaExps, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.listaExps = listaExps
        self.arreglo_padre = None
        self.mapeo_tipos_arreglo = []

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        valores = []
        for exp in self.listaExps:
            simboloExp = exp.ejecutar(ambito)
            if simboloExp is not None:
                valores.append(simboloExp)
            else:
                return None
        res.valor = valores
        res.tipo = TipoDato.ARREGLO
        res.es_elemento_arreglo = False
        return res


    def compilar(self, ambito, sectionCodigo3d):
        res = ResExp(None, None)
        tmp_posVectorHeap = GenCod3d.addTemporal()
        tmp_posElementoHeap = GenCod3d.addTemporal()
        GenCod3d.addCodigo3d(f'{tmp_posVectorHeap} = hp; \n', sectionCodigo3d)
        GenCod3d.addCodigo3d(f'{tmp_posElementoHeap} = {tmp_posVectorHeap} + 1; // Se establece la posicion del primer elemento \n', sectionCodigo3d)
        GenCod3d.addCodigo3d(f'heap[int(hp)] = {len(self.listaExps)}; // En la primera posicion se pone el tamño del vector  \n', sectionCodigo3d)
        GenCod3d.addCodigo3d(f'hp = hp + {len(self.listaExps) + 1}; // Se reserva el espacio del vector y su tamño \n\n', sectionCodigo3d)

        tipo_de_elementos = TipoDato.NONE
        for i, exp in enumerate(self.listaExps):
            exp.arreglo_padre = self
            simboloExp = exp.compilar(ambito, sectionCodigo3d)
            if simboloExp is None:
                return None
            # define de que tipo son los elementos del arreglo
            if i == len(self.listaExps) - 1:
                self.mapeo_tipos_arreglo +=  simboloExp.mapeo_tipos_arreglo

            # se guarda el valor del elemento del arreglo en el heap
            if simboloExp.tipo == TipoDato.BOOLEANO:
                lbl_continuar = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'heap[int({tmp_posElementoHeap})] = 1; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'goto {lbl_continuar}; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'heap[int({tmp_posElementoHeap})] = 0; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'{lbl_continuar}: \n', sectionCodigo3d)
                res.lbl_true = GenCod3d.addTemporal()
                res.lbl_false = GenCod3d.addTemporal()
            else:
                GenCod3d.addCodigo3d(f'heap[int({tmp_posElementoHeap})] = {simboloExp.valor}; \n', sectionCodigo3d)
            GenCod3d.addCodigo3d(f'{tmp_posElementoHeap} = {tmp_posElementoHeap} + 1; \n', sectionCodigo3d)
            tipo_de_elementos = simboloExp.tipo

        self.mapeo_tipos_arreglo.append(tipo_de_elementos)
        GenCod3d.addCodigo3d('\n', sectionCodigo3d)
        res.valor = tmp_posVectorHeap
        res.tipo = TipoDato.ARREGLO
        res.mapeo_tipos_arreglo = self.mapeo_tipos_arreglo
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "ARREGLO", idPadre)
        if len(self.listaExps) > 0:
            for exp in self.listaExps:
                exp.generateCst(self.idSent)