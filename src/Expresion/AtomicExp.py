from src.Expresion.Expresion import  Expresion
from src.Expresion.ResExp import ResExp
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *
from src.Tipos.TipoDato import *

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

            # de no ser nulo se limpia el temporal
            GenCod3d.limpiar_temps_usados(simbolo.valor)

            tempString = GenCod3d.addTemporal()
            accesoStack = f'stack[{simbolo.posAmbito}]'
            if simbolo.ambito.nombre != "GLOBAL":
                tmp_varPosStack = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d(f'{tmp_varPosStack} = sp + {simbolo.posAmbito}; \n', sectionCode3d)
                accesoStack = f'stack[int({tmp_varPosStack})]'
            GenCod3d.addCodigo3d(f'{tempString} = {accesoStack}; \n', sectionCode3d)

            # se guarda valores adiciones petencientes a un arrelgo
            if simbolo.tipo == TipoDato.BOOLEANO:
                simbolo.lbl_true = GenCod3d.addLabel()
                simbolo.lbl_false = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'if ({tempString} == 1) {{ goto {simbolo.lbl_true}; }} \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {simbolo.lbl_false}; \n', sectionCode3d)
                res.lbl_true = simbolo.lbl_true
                res.lbl_false = simbolo.lbl_false
            elif simbolo.tipo == TipoDato.ARREGLO:
                res.mapeo_tipos_arreglo = simbolo.mapeo_tipos_arreglo[:]
                res.molde = simbolo.molde
            elif simbolo.tipo == TipoDato.STRUCT:
                res.molde = simbolo.molde

            res.valor = tempString
            res.tipo = simbolo.tipo
            res.posAmbito = simbolo.posAmbito

        elif self.tipo == TipoDato.NONE:
            res.valor =  "-1"
            res.tipo = self.tipo

        elif self.tipo == TipoDato.BOOLEANO:
            res.tipo = TipoDato.BOOLEANO
            if self.lbl_true == '':
                self.lbl_true = GenCod3d.addLabel()
            if self.lbl_false == '':
                self.lbl_false = GenCod3d.addLabel()
            if self.valor:
                res.valor = "1"
                GenCod3d.addCodigo3d(f'goto {self.lbl_true}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {self.lbl_false}; \n', sectionCode3d)
            else:
                res.valor = "0"
                GenCod3d.addCodigo3d(f'goto {self.lbl_false}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'goto {self.lbl_true}; \n', sectionCode3d)
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
            res.valor = str(self.valor)
            res.tipo = self.tipo

        GenCod3d.temporales_funcion.append(res.valor)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, str(self.valor), idPadre)