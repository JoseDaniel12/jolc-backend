from src.Instruccion.Instruccion import *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *

class Return(Instruction):
    def __init__(self, expresion, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.expresion = expresion

    def ejecutar(self, ambito):
        res = ResIns()
        if self.expresion is None:
            res.returnEncontrado = True
            res.returnSimbolo = ResExp("nothing", TipoDato.NONE)
        else:
            simboloExp = self.expresion.ejecutar(ambito)
            if simboloExp is None:
                return res
            else:
                res.returnEncontrado = True
                res.returnSimbolo = simboloExp
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        if self.expresion is not None:
            simboloExp = self.expresion.compilar(ambito, sectionCode3d)
            GenCod3d.limpiar_temps_usados(simboloExp.valor)
            if simboloExp.tipo == TipoDato.STRUCT:
                GenCod3d.tipo_struct = simboloExp.molde
            elif simboloExp.tipo == TipoDato.BOOLEANO:
                lbl_salida = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int(sp)] = 1; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {lbl_salida}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int(sp)] = 0; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{lbl_salida}:  \n', sectionCode3d)
            else:
                GenCod3d.addCodigo3d(f'stack[int(sp)] = {simboloExp.valor}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'goto {self.lbl_return}; \n\n', sectionCode3d)
        return res

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "return", idPadre)