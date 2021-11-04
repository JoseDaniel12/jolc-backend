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
                codigo_ins =  ins.getCode()
                if codigo_ins != '':
                    codigo += '\t' + ins.getCode() + '\n'
            codigo += '}'
            return codigo
        return ''