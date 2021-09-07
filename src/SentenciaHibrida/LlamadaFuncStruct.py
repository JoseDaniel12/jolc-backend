from src.Entorno.Ambito import *
from src.Instruccion.ejecutarBloqueIns import  *
from src.Errores.TablaErrores import *
from src.Errores.Error import *
from src.Expresion.ResExp import *
from src.Entorno.SimboloFuncion import *
from src.Entorno.SimboloStruct import *
from src.Instruccion.Struct.StructInstance import *

class LlamadaFuncStruct:
    def __init__(self, id, listaExps, linea, columna):
        self.id = id
        self.listaExps = listaExps
        self.linea = linea
        self.columna = columna

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        resSimboloLlamada = ambito.getVariable(self.id)
        if resSimboloLlamada is not None:
            if type(resSimboloLlamada) == SimboloFuncion:
                nuevoAmbito = Ambito(ambito, self.id)
                if len(self.listaExps) == len(resSimboloLlamada.listaParams):
                    for i in range(len(self.listaExps)):
                        simboloParam = self.listaExps[i].ejecutar(ambito)
                        if simboloParam.tipo == resSimboloLlamada.listaParams[i].tipo or resSimboloLlamada.listaParams[i].tipo is None:
                            nuevoAmbito.addVariable(resSimboloLlamada.listaParams[i].id, simboloParam)
                        else:
                            agregarError(Error(
                                f"Se esperaban tipo {resSimboloLlamada.listaParams[i].tipo.name} y se obtuvo {simboloParam.tipo.name}",self.linea, self.columna))
                            return res
                else:
                    agregarError(Error(f"Se esperaban {len(resSimboloLlamada.listaParams)} parametros y se obtuvieron {len(self.listaExps)}",self.linea, self.columna))
                    return res
                resIns = ejectuarBloqueIns(resSimboloLlamada.listaIns, nuevoAmbito)
                res.textoConsola += resIns.textoConsola
                if resIns.returnEncontrado:
                    res = resIns.returnSimbolo
                    return res
                else:
                    res.valor = "nothing"
                    res.tipo = TipoDato.NONE
                    return res
            elif type(resSimboloLlamada) == SimboloStruct:
                valoresPropsInstacia = {}
                for i in range(len(self.listaExps)):
                    simboloExp = self.listaExps[i].ejecutar(ambito)
                    valoresPropsInstacia[resSimboloLlamada.propiedades[i].id] = simboloExp
                return ResExp(StructInstance(self.id, resSimboloLlamada.isMutable,valoresPropsInstacia), TipoDato.STRUCT)
        else:
            agregarError(Error(f"La funcion {self.id} no esta definida", self.linea, self.columna))
            return None