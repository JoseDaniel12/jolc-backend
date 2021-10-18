from src.Expresion.Expresion import  Expresion
from src.Expresion.ResExp import ResExp
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class AtomicExp(Expresion):
    def __init__(self, valor, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.valor = valor
        self.tipo = tipo
        self.lbl_true = ''
        self.lbl_false = ''


    def ejecutar(self, ambito):
        if self.tipo == TipoDato.IDENTIFICADOR:
            simbolo = ambito.getVariable(self.valor)
            if simbolo is None:
                agregarError(Error(f"La variable {self.valor} no esta definida", self.linea, self.columna))
                return None
            return ResExp(simbolo.valor, simbolo.tipo)
        return ResExp(self.valor, self.tipo)


    def compilar(self, ambito, sectionCode3d):
        res = ResExp("", "")

        if self.tipo == TipoDato.IDENTIFICADOR:
            simbolo = ambito.getVariable(self.valor)

            if simbolo is None:
                agregarError(Error(f"La variable {self.valor} no esta definida", self.linea, self.columna))
                return None

            tempString = GenCod3d.addTemporal()
            accesoStack = f'stack[{simbolo.posAmbito}]'
            if simbolo.ambito_id == ambito.id and ambito.nombre != 'GLOBAL':
                tmp_varPosStack = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d(f'{tmp_varPosStack} = sp + {simbolo.posAmbito + 1}; \n', sectionCode3d)
                accesoStack = f'stack[int({tmp_varPosStack})]'
            GenCod3d.addCodigo3d(f'{tempString} = {accesoStack}; \n', sectionCode3d)

            if simbolo.tipo == TipoDato.BOOLEANO:
                simbolo.lbl_true = GenCod3d.addLabel()
                simbolo.lbl_false = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'if ({tempString} == 1) {{ goto {simbolo.lbl_true}; }} \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {simbolo.lbl_false}; \n', sectionCode3d)
            res.valor = tempString
            res.tipo = simbolo.tipo

            if sectionCode3d == "funciones":
                GenCod3d.temporales_funcion.append(tempString)
            return res

        if self.tipo == TipoDato.NONE:
            self.valor = "NULL"

        elif self.tipo == TipoDato.BOOLEANO:
            if self.lbl_true == '':
                self.lbl_true = GenCod3d.addLabel()
            if self.lbl_false == '':
                self.lbl_false = GenCod3d.addLabel()
            if self.valor:
                GenCod3d.addCodigo3d(f'goto {self.lbl_true}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {self.lbl_false}; \n', sectionCode3d)
            else:
                GenCod3d.addCodigo3d(f'goto {self.lbl_false}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {self.lbl_true}; \n', sectionCode3d)
            res = ResExp(None, TipoDato.BOOLEANO)
            res.lbl_true = self.lbl_true
            res.lbl_false = self.lbl_false
            return res

        elif self.tipo == TipoDato.CADENA or self.tipo == TipoDato.CARACTER:
            tempHeap = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tempHeap} = hp; \n', sectionCode3d)
            for caracter in self.valor:
                GenCod3d.addCodigo3d(f'heap[int(hp)] = {ord(caracter)}; \n', sectionCode3d)
                GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
            GenCod3d.addCodigo3d('heap[int(hp)] = -1; \n', sectionCode3d)
            GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
            self.valor = tempHeap
            res.valor  = self.valor
            res.tipo = self.tipo

        else:
            res.valor = self.valor
            res.tipo = self.tipo

        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, str(self.valor), idPadre)