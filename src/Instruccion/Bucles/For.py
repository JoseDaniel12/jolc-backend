from src.Instruccion.Instruccion import *
from src.Entorno.Ambito import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Entorno.SimboloVariable import *
from src.Reportes.Cst import *
from src.Expresion.Rango import *

class For(Instruction):
    def __init__(self, id, expresion, listaIns, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.id = id
        self.expresion = expresion
        self.listaIns = listaIns

    def ejecutar(self, ambito) -> ResIns:
        res = ResIns()
        simboloExp = self.expresion.ejecutar(ambito)

        if simboloExp is None:
            return res

        if simboloExp.tipo == TipoDato.CADENA:
            lista = list(simboloExp.valor)
            simboloExp.valor =  map(lambda x: ResExp(x, TipoDato.CARACTER), lista)

        for i in simboloExp.valor:
            nuevoAmbito = Ambito(ambito, "For")
            nuevoAmbito.addVariable(self.id, SimboloVariable(self.id, i.valor, i.tipo, self.linea, self.columna))
            resIns = ejectuarBloqueIns(self.listaIns, nuevoAmbito)
            res.textoConsola += resIns.textoConsola
            if resIns.breakEncontrado:
                return res
            elif resIns.returnEncontrado:
                res.returnEncontrado = True
                res.returnSimbolo = resIns.returnSimbolo
                return res
        return res


    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        simboloExp = None
        nuevoAmbito = Ambito(ambito, "For")
        lbl_inicioFor = GenCod3d.addLabel()
        lbl_insFor = GenCod3d.addLabel()
        lbl_finFor = GenCod3d.addLabel()

        tmp_variabelIteracion = GenCod3d.addTemporal()
        tmp_punteroCadenaOrignal = GenCod3d.addTemporal()

        tmp_tamanoArreglo = GenCod3d.addTemporal()
        tmp_indiceRelativoElemArr = GenCod3d.addTemporal()
        tmp_punteroElemArrHeap = GenCod3d.addTemporal()
        tmp_elementoArreglo = GenCod3d.addTemporal()

        tmp_valorFinal = GenCod3d.addTemporal()

        posSimbolo = -1

        # declaracion de la variable i
        if type(self.expresion) == Rango:
            tmp_posStackVar = GenCod3d.addTemporal()
            simboloInicio = self.expresion.inicio.compilar(nuevoAmbito, sectionCode3d)
            simboloFin = self.expresion.fin.compilar(nuevoAmbito, sectionCode3d)
            simboloVariabelIteracion = SimboloVariable(self.id, simboloFin.valor, TipoDato.ENTERO, self.linea, self.columna)
            posSimbolo = nuevoAmbito.addVariable(self.id, simboloVariabelIteracion)
            GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {simboloInicio.valor}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_valorFinal} = {simboloFin.valor}; \n', sectionCode3d)
        else:
            simboloExp = self.expresion.compilar(ambito, sectionCode3d)
            if simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
                tmp_caracter = GenCod3d.addTemporal()
                tmp_heapRespaldo = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d(f'{tmp_punteroCadenaOrignal} = stack[int({simboloExp.valor})]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_caracter} = heap[int({tmp_punteroCadenaOrignal})]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_heapRespaldo} = hp; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'heap[int(hp)] = {tmp_caracter}; \n', sectionCode3d)
                GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
                GenCod3d.addCodigo3d('heap[int(hp)] = -1; \n', sectionCode3d)
                GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
                simboloVariabelIteracion = SimboloVariable(self.id, tmp_heapRespaldo, TipoDato.CARACTER, self.linea, self.columna)
                posSimbolo = nuevoAmbito.addVariable(self.id, simboloVariabelIteracion)
                GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {tmp_heapRespaldo}; \n\n', sectionCode3d)
            elif simboloExp.tipo == TipoDato.ARREGLO:
                GenCod3d.addCodigo3d(f'{tmp_tamanoArreglo} = heap[int({simboloExp.valor})]; // tamaño del vector \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_punteroElemArrHeap} = {simboloExp.valor} + 1; // pos primer elemento \n', sectionCode3d)
                nuevo_mapeo = simboloExp.mapeo_tipos_arreglo[:]
                tipo = nuevo_mapeo.pop()
                simboloVariabelIteracion = SimboloVariable(self.id, tmp_punteroElemArrHeap, tipo, self.linea, self.columna)
                simboloVariabelIteracion.mapeo_tipos_arreglo = nuevo_mapeo
                posSimbolo = nuevoAmbito.addVariable(self.id, simboloVariabelIteracion)
                GenCod3d.addCodigo3d(f'{tmp_elementoArreglo} = heap[int({tmp_punteroElemArrHeap})]; // elemento \n',sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {tmp_elementoArreglo}; // se declara i \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_indiceRelativoElemArr} = 1; // indice relativo  \n\n', sectionCode3d)

        # inicio cuerpo de ciclo
        GenCod3d.addCodigo3d(f'{lbl_inicioFor}: \n', sectionCode3d)

        # condicion
        if type(self.expresion) == Rango:
            GenCod3d.addCodigo3d(f'{tmp_variabelIteracion} = stack[{posSimbolo}]; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'if ({tmp_variabelIteracion} <= {tmp_valorFinal}) {{ goto {lbl_insFor}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {lbl_finFor}; \n', sectionCode3d)
        elif simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
            tmp_caracter = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tmp_variabelIteracion} = stack[{posSimbolo}]; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_caracter} = heap[int({tmp_punteroCadenaOrignal})]; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'if ({tmp_caracter} != -1) {{ goto {lbl_insFor}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {lbl_finFor}; \n', sectionCode3d)
        elif simboloExp.tipo == TipoDato.ARREGLO:
            GenCod3d.addCodigo3d(f'if ({tmp_indiceRelativoElemArr} <= {tmp_tamanoArreglo}) {{ goto {lbl_insFor}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {lbl_finFor}; \n', sectionCode3d)

        # cuerpo instrucciones
        GenCod3d.addCodigo3d(f'{lbl_insFor}: \n', sectionCode3d)
        for ins in self.listaIns:
            ins.lbl_break = lbl_finFor
            ins.lbl_continue = lbl_inicioFor
            ins.lbl_return = self.lbl_return
            ins.compilar(nuevoAmbito, sectionCode3d)

        # actualizacion de la variable de iteracion
        if type(self.expresion) == Rango:
            GenCod3d.addCodigo3d(f'{tmp_variabelIteracion} = {tmp_variabelIteracion} + 1; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {tmp_variabelIteracion}; \n', sectionCode3d)
        elif simboloExp.tipo == TipoDato.CADENA or simboloExp.tipo == TipoDato.CARACTER:
            tmp_caracter = GenCod3d.addTemporal()
            tmp_heapRespaldo = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tmp_punteroCadenaOrignal} = {tmp_punteroCadenaOrignal} + 1; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_caracter} = heap[int({tmp_punteroCadenaOrignal})]; \n')
            GenCod3d.addCodigo3d(f'{tmp_heapRespaldo} = hp; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'heap[int(hp)] = {tmp_caracter}; \n', sectionCode3d)
            GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
            GenCod3d.addCodigo3d('heap[int(hp)] = -1; \n', sectionCode3d)
            GenCod3d.addCodigo3d('hp = hp + 1; \n', sectionCode3d)
            simboloVariabelIteracion = SimboloVariable(self.id, tmp_heapRespaldo, TipoDato.CARACTER, self.linea, self.columna)
            GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {tmp_heapRespaldo}; \n\n', sectionCode3d)
        elif simboloExp.tipo == TipoDato.ARREGLO:
            GenCod3d.addCodigo3d(f'{tmp_indiceRelativoElemArr} = {tmp_indiceRelativoElemArr} + 1; // inc indice realtivo \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_punteroElemArrHeap} = {tmp_punteroElemArrHeap} + 1; // inc puntero elemento \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_elementoArreglo} = heap[int({tmp_punteroElemArrHeap})]; // elemento nuevo \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'stack[{posSimbolo}] = {tmp_elementoArreglo}; // se declara i \n', sectionCode3d)
        # final del ciclo
        GenCod3d.addCodigo3d(f'goto {lbl_inicioFor}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'goto {lbl_finFor}; \n', sectionCode3d)
        GenCod3d.addCodigo3d(f'{lbl_finFor}: \n', sectionCode3d)

        return res



    def generateCst(self, idPadre):
        defElementCst(self.idSent, "FOR", idPadre)
        #id
        idIdentificador = getNewId()
        defElementCst(idIdentificador, "ID_VAR", self.idSent)
        defElementCst(getNewId(), self.id, idIdentificador)
        #expreio
        idExpreison = getNewId()
        defElementCst(idExpreison, "EXPRESION", self.idSent)
        self.expresion.generateCst(idExpreison)
        #listaIns
        idListaIns = getNewId()
        defElementCst(idListaIns, "LISTA_INS", self.idSent)
        for ins in self.listaIns:
            ins.generateCst(idListaIns)