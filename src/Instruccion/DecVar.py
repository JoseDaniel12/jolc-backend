from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
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

            # veririfco que no hayan errores en la expresion a asignar
            if simboloExp is None:
                return res
            elif simboloExp.tipo != self.tipo and self.tipo is not None:
                agregarError(Error(f"Se esperaba {self.tipo} y se obtuvo {simboloExp.tipo}", self.linea, self.columna))
                return  res

            # si no tiene errores marco el temporal como utilizado
            GenCod3d.limpiar_temps_usados(simboloExp.valor)

            # revisa en que ambito se esta declarando la valirable
            if self.refAmbito == "global":
                posSimboloAmbito = ambito.getAmbitoGlobal().addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna))
                GenCod3d.addCodigo3d(f'stack[int({posSimboloAmbito})] = {simboloExp.valor}; \n\n', sectionCode3d)
            else:
                # se identifica si la variable ya existia (asignacion) o no (declaracion)
                if ambito.existeSimbolo(self.id):
                    existente = ambito.getVariable(self.id)
                    existente.valor = simboloExp.valor
                    existente.tipo  = simboloExp.tipo
                    ambitoVariable = ambito.getAmbitoSimbolo(self.id)
                    if ambitoVariable.nombre == 'GLOBAL':
                        GenCod3d.addCodigo3d(f'stack[{existente.posAmbito}] = {simboloExp.valor}; \n\n', sectionCode3d)
                    else:
                        tmp_varPosStack = GenCod3d.addTemporal()
                        GenCod3d.addCodigo3d(f'{tmp_varPosStack} = sp + {existente.posAmbito + 1}; \n', sectionCode3d)
                        GenCod3d.addCodigo3d(f'stack[int({tmp_varPosStack})] = {simboloExp.valor}; \n\n', sectionCode3d)
                else:
                    simbolo = SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna)

                    # se guarda propiedades adicionales en caso de ser arreglo
                    simbolo.mapeo_tipos_arreglo = simboloExp.mapeo_tipos_arreglo
                    res.mapeo_tipos_arreglo = simboloExp.mapeo_tipos_arreglo
                    # se guarda porpiedad adicional en caso de ser un struct
                    simbolo.molde = simboloExp.molde
                    res.molde = simboloExp.molde
                    # leugo de agregar todas las propiedades adicionales se insereta al ambito
                    posSimboloAmbito = ambito.addVariable(self.id, simbolo)

                    # si es booleano se realiza paso adicional para su asignacion por el uso de etiquetas
                    if simboloExp.tipo == TipoDato.BOOLEANO:
                        lbl_salida = GenCod3d.addLabel()
                        accesoStack = f'stack[int({posSimboloAmbito})]'
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
                        # si es una declaracion en un ambito no global se realiza paso adicional
                        if ambito.nombre == "GLOBAL":
                            GenCod3d.addCodigo3d(f'stack[int({posSimboloAmbito})] = {simboloExp.valor}; \n\n', sectionCode3d)
                        else:
                            tmp_stackDeclaration = GenCod3d.addTemporal()
                            GenCod3d.addCodigo3d(f'{tmp_stackDeclaration} = sp + {ambito.size}; \n', sectionCode3d)
                            GenCod3d.addCodigo3d(f'stack[int({tmp_stackDeclaration})] = {simboloExp.valor}; \n\n', sectionCode3d)
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
