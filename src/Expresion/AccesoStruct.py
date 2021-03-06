from src.Expresion.Expresion import *
from src.Expresion.ResExp import *
from src.Errores.TablaErrores import *
from src.Reportes.Cst import *

class AccesosStruct(Expresion):
    def __init__(self, expStruct, idProp, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.expStruct = expStruct
        self.idProp =   idProp

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        simboloStruct = self.expStruct.ejecutar(ambito)
        if simboloStruct is None:
            return None
        elif simboloStruct.tipo != TipoDato.STRUCT:
            agregarError(Error(f"No se puede acceder a un propiedad de un elemento que no sea {TipoDato.STRUCT.value}", self.linea,self.columna))
            return None
        elif simboloStruct.valor.propiedades.get(self.idProp) is None:
            agregarError(Error(f"{simboloStruct.valor.tipoStruct} no cuentra con la propiedad {self.idProp}", self.linea, self.columna))
            return None
        else:
            res = simboloStruct.valor.propiedades[self.idProp]
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResExp(None, None)
        simboloStruct = self.expStruct.compilar(ambito, sectionCode3d)
        if simboloStruct is None:
            agregarError(Error(f"No se puede acceder a un tipo que no sea Struct", self.linea,self.columna))
            return None

        # marco el temporal del struct como utilizado
        GenCod3d.limpiar_temps_usados(simboloStruct.valor)

        tmp_posHeapInicioStruct = GenCod3d.addTemporal()
        tmp_posPropStruct = GenCod3d.addTemporal()
        tmp_prop = GenCod3d.addTemporal()
        indice_prop_desada = -1

        for i, prop in enumerate(simboloStruct.molde.propiedades):
            if prop.id == self.idProp:
                indice_prop_desada = i + 1
                res.tipo = prop.tipo
                res.molde = ambito.getVariable(prop.tipoStruct) # ERROR ERROR ERROR ERROR
                res.mapeo_tipos_arreglo = prop.mapeo_tipos_arreglo
                break

        GenCod3d.addCodigo3d(f'{tmp_posHeapInicioStruct} = {simboloStruct.valor}; // Se obtiene indice de inicio del struct en el heap \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{tmp_posPropStruct} = {tmp_posHeapInicioStruct} + {indice_prop_desada}; // Se obtiene el indice de la propiedad deseada del struct en el heap \n', sectionCode3d)
        GenCod3d.addCodigo3d( f'{tmp_prop} = heap[int({tmp_posPropStruct})]; // Se obtiene la propiedad deseada \n', sectionCode3d)
        if res.tipo == TipoDato.BOOLEANO:
            res.lbl_true = GenCod3d.addLabel()
            res.lbl_false = GenCod3d.addLabel()
            GenCod3d.addCodigo3d(f'if ({tmp_prop} == 1) {{ goto {res.lbl_true}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {res.lbl_false}; \n', sectionCode3d)
        res.valor = tmp_prop
        GenCod3d.temporales_funcion.append(res.valor)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "ACCESO_STRUCT", idPadre)
        #expStruct
        idExpStruct = getNewId()
        defElementCst(idExpStruct, "EXP_STRUCT", self.idSent)
        self.expStruct.generateCst(idExpStruct)
        #idProp
        idProp = getNewId()
        defElementCst(idProp, "Id", self.idSent)
        defElementCst(getNewId(), self.idProp, idProp)