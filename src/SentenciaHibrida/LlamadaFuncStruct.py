from src.Instruccion.ejecutarBloqueIns import  *
from src.Expresion.ResExp import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

memo = {}
primaeraVez = True
def resetMemo():
    global memo
    memo = {}

class LlamadaFuncStruct:
    def __init__(self, id, listaExps, linea, columna):
        self.idSent = getNewId()
        self.id = id
        self.listaExps = listaExps
        self.linea = linea
        self.columna = columna

    def ejecutar(self, ambito):
        res = ResExp(None, None)
        resSimboloLlamada = ambito.getVariable(self.id)
        if resSimboloLlamada is not None:

            if type(resSimboloLlamada) == SimboloFuncion:
                valores = []
                nuevoAmbito = Ambito(ambito, self.id)
                if len(self.listaExps) == len(resSimboloLlamada.listaParams):
                    for i in range(len(self.listaExps)):
                        simboloParam = self.listaExps[i].ejecutar(ambito)
                        if ((simboloParam.tipo == resSimboloLlamada.listaParams[i].tipo or resSimboloLlamada.listaParams[i].tipo is None) or
                            (simboloParam.tipo == TipoDato.NONE and resSimboloLlamada.listaParams[i].tipo == TipoDato.STRUCT)):
                            nuevoAmbito.addVariable(resSimboloLlamada.listaParams[i].id, SimboloVariable(resSimboloLlamada.listaParams[i].id, simboloParam.valor, simboloParam.tipo, self.linea, self.columna))
                            valores.append(simboloParam.valor)
                        else:
                            agregarError(Error(f"Se esperaban tipo {resSimboloLlamada.listaParams[i].tipo.name} y se obtuvo {simboloParam.tipo.name}",self.linea, self.columna))
                            return res
                else:
                    agregarError(Error(f"Se esperaban {len(resSimboloLlamada.listaParams)} parametros y se obtuvieron {len(self.listaExps)}",self.linea, self.columna))
                    return res

                '''
                memoKey = self.id + str(valores) + str(resSimboloLlamada.listaIns)
                if memo.get(memoKey) is None:
                    resIns = ejectuarBloqueIns(resSimboloLlamada.listaIns, nuevoAmbito)
                    memo[memoKey] = resIns
                else:
                    resIns = memo[memoKey]
                '''
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


    # _________________________________________ COMPILACION _________________________________________

    def compilar(self, ambito, sectionCodigo3d):
        res = ResExp(None, None)
        resSimboloLlamada = ambito.getVariable(self.id)
        if resSimboloLlamada is None:
            agregarError(Error(f"La funcion {self.id} no esta definida", self.linea, self.columna))
            return None

        # _________________________________________ FUNCION  _________________________________________

        if type(resSimboloLlamada) == SimboloFuncion:
            nuevoAmbito = Ambito(ambito, self.id)
            if len(self.listaExps) != len(resSimboloLlamada.listaParams):
                agregarError(Error(f"Se esperaban {len(resSimboloLlamada.listaParams)} parametros y se obtuvieron {len(self.listaExps)}",self.linea, self.columna))
                return res

            GenCod3d.addCodigo3d('\n\t/* Inicio de llamada de funcion */ \n', sectionCodigo3d)

            # guardado de temporales
            if len(GenCod3d.temporales_funcion) > 0:
                GenCod3d.addCodigo3d('\n\t/* Inicio de guardado de temporales */ \n', sectionCodigo3d)
                tmp_tempPosStack = GenCod3d.addTemporal()
                for i, temporal in enumerate(GenCod3d.temporales_funcion):
                    GenCod3d.addCodigo3d(f'{tmp_tempPosStack} = sp + {ambito.size + i + 1}; \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'stack[int({tmp_tempPosStack})] = {temporal}; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d('/* Fin de guarado de temporales */ \n\n', sectionCodigo3d)

            #paso de parametros
            temps_params = []
            GenCod3d.addCodigo3d('\n\t/* Inicio de paso de parametros */ \n', sectionCodigo3d)
            tmp_paramPosStack = GenCod3d.addTemporal()
            for i in range(len(self.listaExps)):
                simboloParam = self.listaExps[i].compilar(ambito, sectionCodigo3d)
                if (simboloParam.tipo != resSimboloLlamada.listaParams[i].tipo and resSimboloLlamada.listaParams[i].tipo is not None
                    and not (simboloParam.tipo == TipoDato.NONE and resSimboloLlamada.listaParams[i].tipo == TipoDato.STRUCT)):
                    agregarError(Error(f"Se esperaban tipo {resSimboloLlamada.listaParams[i].tipo} y se obtuvo {simboloParam.tipo.name}",self.linea, self.columna))
                    return res
                temps_params.append(simboloParam.valor)
            for i, p in enumerate(temps_params):
                GenCod3d.addCodigo3d('// Parametro: \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'{tmp_paramPosStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion)+ i + 1}; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'stack[int({tmp_paramPosStack})] = {p}; \n', sectionCodigo3d)
            GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCodigo3d)

            # cambio de ambito
            avance = ambito.size + len(GenCod3d.temporales_funcion)
            GenCod3d.addCodigo3d(f'sp = sp + {avance}; \n', sectionCodigo3d)

            # llamada funcion
            tmp_retrunValue = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{resSimboloLlamada.id}(); \n', sectionCodigo3d)
            GenCod3d.addCodigo3d(f'{tmp_retrunValue} = stack[int(sp)]; \n', sectionCodigo3d)
            res.valor = tmp_retrunValue

            # regreso de ambito
            GenCod3d.addCodigo3d(f'sp = sp - {avance}; \n', sectionCodigo3d)
            GenCod3d.addCodigo3d('/* Fin de llamada de funcion */ \n\n', sectionCodigo3d)

            # se marcan como usados los temporles de la funcion luego de usarse
            for temp in temps_params:
                GenCod3d.limpiar_temps_usados(temp)

            # recuperado de temporales de funcion recursiva
            if len(GenCod3d.temporales_funcion) > 0:
                GenCod3d.addCodigo3d('\n\t/* Inicio de recuperacion de temporales */ \n', sectionCodigo3d)
                tmp_tempPosStack = GenCod3d.addTemporal()
                for i, temporal in enumerate(GenCod3d.temporales_funcion):
                    if temporal[0] == "t":
                        GenCod3d.addCodigo3d(f'{tmp_tempPosStack} = sp + {ambito.size + i + 1}; \n', sectionCodigo3d)
                        GenCod3d.addCodigo3d(f'{temporal} = stack[int({tmp_tempPosStack})]; \n', sectionCodigo3d)
                GenCod3d.temporales_funcion.clear()
                GenCod3d.addCodigo3d('/* Fin de recuperacion de temporales */ \n\n', sectionCodigo3d)

            res.tipo = resSimboloLlamada.tipoRetorno
            if res.tipo == TipoDato.BOOLEANO:
                res.lbl_true = GenCod3d.addLabel()
                res.lbl_false = GenCod3d.addLabel()
                GenCod3d.addCodigo3d(f'if ({res.valor} == 1) {{ goto {res.lbl_true}; }} \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'goto {res.lbl_false}; \n', sectionCodigo3d)
            if res.tipo == TipoDato.STRUCT:
                res.molde = GenCod3d.tipo_struct


        # _________________________________________ STRUCT _________________________________________

        elif type(resSimboloLlamada) == SimboloStruct:
            tmp_posStructHeap = GenCod3d.addTemporal()
            tmp_posPropiedadHeap = GenCod3d.addTemporal()

            # se preparan los datos para empezar a definir el struct
            GenCod3d.addCodigo3d(f'{tmp_posStructHeap} = hp; \n', sectionCodigo3d)
            GenCod3d.addCodigo3d(f'{tmp_posPropiedadHeap} = {tmp_posStructHeap} + 1; // Se establece la posicion inicial de la primer propiedad \n', sectionCodigo3d)
            GenCod3d.addCodigo3d(f'heap[int(hp)] = {len(self.listaExps)}; // En la primera posicion se pone el numero de propiedades  \n', sectionCodigo3d)
            GenCod3d.addCodigo3d(f'hp = hp + {len(self.listaExps) + 1}; // Se reserva el espacio del struct y su tamño \n\n', sectionCodigo3d)

            # se empizan a definir la propiedades del struct
            for i, exp in enumerate(self.listaExps):
                simboloExp = exp.compilar(ambito, sectionCodigo3d)

                # se verifica si hay errores en la propiedad
                if simboloExp is None:
                    return None

                # se marca como usado el temporal de expresion
                GenCod3d.limpiar_temps_usados(simboloExp.valor)

                # se guarda el elemento en el heap, en caso de ser booleano se la su tratamiento
                if simboloExp.tipo == TipoDato.BOOLEANO:
                    lbl_continuar = GenCod3d.addLabel()
                    GenCod3d.addCodigo3d(f'{simboloExp.lbl_true}: \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'heap[int({tmp_posPropiedadHeap})] = 1; \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'goto {lbl_continuar}; \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'{simboloExp.lbl_false}: \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'heap[int({tmp_posPropiedadHeap})] = 0; \n', sectionCodigo3d)
                    GenCod3d.addCodigo3d(f'{lbl_continuar}: \n', sectionCodigo3d)
                    res.lbl_true = GenCod3d.addTemporal()
                    res.lbl_false = GenCod3d.addTemporal()
                else:
                    GenCod3d.addCodigo3d(f'heap[int({tmp_posPropiedadHeap})] = {simboloExp.valor}; \n', sectionCodigo3d)
                GenCod3d.addCodigo3d(f'{tmp_posPropiedadHeap} = {tmp_posPropiedadHeap} + 1; \n', sectionCodigo3d)

            GenCod3d.addCodigo3d('\n', sectionCodigo3d)
            res.valor = tmp_posStructHeap
            res.tipo = TipoDato.STRUCT
            res.molde = resSimboloLlamada


        # se el temporal de llamada como no utilizada
        GenCod3d.temporales_funcion.append(res.valor)
        return res


    # _________________________________________ Arbol CST _________________________________________

    def generateCst(self, idPadre):
        defElementCst(self.idSent, "LLAMADA", idPadre)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "Id", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #listaExps
        if len(self.listaExps) > 0:
            idListaExp = getNewId()
            defElementCst(idListaExp, "LISTA_EXP", self.idSent)
            for exp in self.listaExps:
                exp.generateCst(idListaExp)