from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *

class Arreglo(Expresion):
    def __init__(self, listaExps, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.listaExps = listaExps

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
        return res


    def compilar(self, ambito, sectionCodigo3d):
        res = ResExp(None, None)
        valores = []
        tmp_posVectorHeap = GenCod3d.addTemporal()
        tmp_posElementoHeap = GenCod3d.addTemporal()
        GenCod3d.addCodigo3d(f'{tmp_posVectorHeap} = hp; \n')
        GenCod3d.addCodigo3d(f'{tmp_posElementoHeap} = {tmp_posVectorHeap} + 1; \n')
        GenCod3d.addCodigo3d(f'heap[int({tmp_posElementoHeap})] = {len(self.listaExps)}; \n')
        GenCod3d.addCodigo3d(f'hp = hp + {len(self.listaExps) + 1}; \n\n')

        for exp in self.listaExps:
            simboloExp = exp.compilar(ambito, sectionCodigo3d)
            if simboloExp is None:
                return None
            GenCod3d.addCodigo3d(f'heap[int({tmp_posElementoHeap})] = {simboloExp.valor}; \n')
            GenCod3d.addCodigo3d(f'{tmp_posElementoHeap} = {tmp_posVectorHeap} + 1; \n')
            valores.append(simboloExp)

        res.valor = tmp_posVectorHeap
        res.tipo = TipoDato.ARREGLO
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "ARREGLO", idPadre)
        if len(self.listaExps) > 0:
            for exp in self.listaExps:
                exp.generateCst(self.idSent)