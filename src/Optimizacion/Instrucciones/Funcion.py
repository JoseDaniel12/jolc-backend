from src.Optimizacion.SentenciaC3d import *

class Funcion(SentenciaC3d):
    def __init__(self, id, listaIns, linea):
        SentenciaC3d.__init__(self, linea)
        self.id = id
        self.listaIns = listaIns

    def getCode(self):
        if not self.is_deleted:
            codigo = f'func {self.id}() {{ \n'
            for ins in self.listaIns:
                if not ins.is_deleted:
                    codigo += '\t' + ins.getCode()
            codigo += '} \n'
            return codigo
        return '// Instrucción eliminada \n'