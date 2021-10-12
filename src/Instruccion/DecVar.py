from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
from src.Entorno.Ambito import *
from src.Entorno.SimboloVariable import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *
from src.Tipos.TipoDato import *

class DecVar(Instruction):
    def __init__(self, refAmbito, id, expresion, tipo,  linea, columna, conValor=True):
        Instruction.__init__(self, linea, columna)
        self.refAmbito = refAmbito
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.conValor = conValor

    def ejecutar(self, ambito: Ambito):
        res = ResIns()
        if self.conValor:
            simboloExp = self.expresion.ejecutar(ambito)
            if simboloExp is None:
                return res
            elif simboloExp.tipo != self.tipo and self.tipo is not None:
                agregarError(Error(f"Se esperaba {self.tipo} y se obtuvo {simboloExp.tipo}", self.linea, self.columna))
                return  res

            if self.refAmbito == "global":
                ambito.getAmbitoGlobal().addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna))
            else:
                if not ambito.existeSimbolo(self.id):
                    ambito.addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna))
                else:
                    existente = ambito.getVariable(self.id)
                    existente.valor = simboloExp.valor
                    existente.tipo  = simboloExp.tipo
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        if self.conValor:
            simboloExp = self.expresion.compilar(ambito, sectionCode3d)
            if simboloExp is None:
                return res
            elif simboloExp.tipo != self.tipo and self.tipo is not None:
                agregarError(Error(f"Se esperaba {self.tipo} y se obtuvo {simboloExp.tipo}", self.linea, self.columna))
                return  res

            if self.refAmbito == "global":
                posSimboloAmbito = ambito.getAmbitoGlobal().addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna))
                GenCod3d.addCodigo3d(f'stack[{posSimboloAmbito}] = {simboloExp.valor}; \n\n', sectionCode3d)
            else:
                if not ambito.existeSimbolo(self.id):
                    simbolo = SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna)
                    posSimboloAmbito = ambito.addVariable(self.id, simbolo)
                    if simboloExp.tipo == TipoDato.BOOLEANO:
                        lbl_salida = GenCod3d.addLabel()
                        accesoStack = f'stack[{posSimboloAmbito}]'
                        if ambito.nombre != 'GLOBAL':
                            tmp_varPosStack = GenCod3d.addTemporal()
                            GenCod3d.addCodigo3d(f'{tmp_varPosStack} = sp + {ambito.size}; \n', sectionCode3d)
                            accesoStack = f'stack[int({tmp_varPosStack})]'
                        GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'{accesoStack} = 1; \n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'goto {lbl_salida}; \n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'{accesoStack} = 0; \n\n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'{lbl_salida}:  \n', sectionCode3d)
                    else:
                        if ambito.nombre == "GLOBAL":
                            GenCod3d.addCodigo3d(f'stack[{posSimboloAmbito}] = {simboloExp.valor}; \n\n', sectionCode3d)
                        else:
                            tmp_stackDeclaration = GenCod3d.addTemporal()
                            GenCod3d.addCodigo3d(f'{tmp_stackDeclaration} = sp + {ambito.size}; \n', sectionCode3d)
                            GenCod3d.addCodigo3d(f'stack[{tmp_stackDeclaration}] = {simboloExp.valor}; \n\n', sectionCode3d)
                else:
                    existente = ambito.getVariable(self.id)
                    existente.valor = simboloExp.valor
                    existente.tipo  = simboloExp.tipo
                    GenCod3d.addCodigo3d(f'stack[{existente.posAmbito}] = {simboloExp.valor}; \n\n', sectionCode3d)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "DECLARACION", idPadre)
        #refAmbito
        if self.refAmbito is not None:
            idRefAmbito = getNewId()
            defElementCst(idRefAmbito, "REF_AMBITO", self.idSent)
            defElementCst(getNewId(), self.refAmbito, idRefAmbito)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "ID", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #valor
        if self.conValor:
            idValor = getNewId()
            defElementCst(idValor, "VALOR", self.idSent)
            self.expresion.generateCst(idValor)
        #tipo
        if self.tipo is not None:
            idTipo = getNewId()
            defElementCst(idTipo, "TIPO", self.idSent)
            defElementCst(getNewId(), self.tipo.value, idTipo)
