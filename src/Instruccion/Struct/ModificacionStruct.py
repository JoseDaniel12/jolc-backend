from src.Instruccion.Instruccion import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *
from src.Tipos.TipoDato import *

class ModificacionStruct(Instruction):
    def __init__(self, expStruct, idProp, expValor, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.expStruct = expStruct
        self.idProp = idProp
        self.expValor  = expValor

    def ejecutar(self, ambito):
        res = ResIns()
        simboloStruct = self.expStruct.ejecutar(ambito)
        simboloValor = self.expValor.ejecutar(ambito)
        if simboloStruct is None or simboloValor is None:
            return res
        elif simboloStruct.tipo != TipoDato.STRUCT:
            agregarError(Error(f"{simboloStruct.tipo.value} no cuenta con la propiedad {self.idProp}", self.linea, self.columna))
            return res
        elif simboloStruct.valor.propiedades.get(self.idProp) is None:
            agregarError(Error(f"{simboloStruct.valor.tipoStruct} no cuentra con la propiedad {self.idProp}", self.linea, self.columna))
            return res
        elif not simboloStruct.valor.isMutable:
            agregarError(Error(f"{simboloStruct.valor.tipoStruct} es inmutable", self.linea,self.columna))
            return res
        simboloPropStruct = simboloStruct.valor.propiedades[self.idProp]
        simboloPropStruct.valor = simboloValor.valor
        simboloPropStruct.tipo = simboloValor.tipo
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        tmp_posPropStruct = GenCod3d.addTemporal()
        simboloStruct = self.expStruct.compilar(ambito, sectionCode3d)
        structMole = ambito.getVariable(simboloStruct.molde.id)

        if simboloStruct is None:
            return res
        elif not structMole.isMutable:
            agregarError(Error(f"{structMole.id} es inmutable", self.linea, self.columna))
            return res

        simboloValor = self.expValor.compilar(ambito, sectionCode3d)
        indice_prop_desada = -1
        for i, prop in enumerate(structMole.propiedades):
            if prop.id == self.idProp:
                indice_prop_desada = i + 1
                res.tipo = prop.tipo
                break


        GenCod3d.addCodigo3d(f'{tmp_posPropStruct} = {simboloStruct.valor} + {indice_prop_desada}; // posicion de elemento accedido \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'heap[int({tmp_posPropStruct})] = {simboloValor.valor}; // cambito de valor \n', sectionCode3d)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "MOD_STRUCT", idPadre)
        #expStruct
        idExpStruct = getNewId()
        defElementCst(idExpStruct, "EXP_STRUCT", self.idSent)
        self.expStruct.generateCst(idExpStruct)
        #idProp
        idProp = getNewId()
        defElementCst(idProp, "PROPIEDAD", self.idSent)
        defElementCst(getNewId(), self.idProp, idProp)
        #expValro
        idExpValor = getNewId()
        defElementCst(idExpValor, "EXP_VALOR", self.idSent)
        self.expValor.generateCst(idExpValor)