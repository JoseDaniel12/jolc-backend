from src.Optimizacion.Instrucciones.If import *
from src.Optimizacion.Instrucciones.Goto import *
from src.Optimizacion.Instrucciones.DecVar import *
from src.Optimizacion.Instrucciones.Etiqueta import *
from src.Optimizacion.Reportes.ReporteOptimizacion import *
from src.Optimizacion.Expresiones.OpAritmetica import *
from src.Optimizacion.Bloque import *
from src.Tipos.TipoDato import *


class Optimizador:
    def __init__(self, paquetes, temporales, funciones):
        self.paquetes = paquetes
        self.temporales = temporales
        self.funciones = funciones
        self.bloques = []


    def getCode(self):
        codigo = 'package main \n'

        codigo += 'import ( \n'
        for paquete in self.paquetes:
            codigo += '\t\"' + paquete + '\"\n'
        codigo += ') \n\n'

        codigo += 'var stack[1000000]float64; \n'
        codigo += 'var heap[1000000]float64; \n'
        codigo += 'var sp, hp float64; \n'
        if len(self.temporales) > 0:
            codigo += 'var ' + ', '.join(self.temporales) + ' float64; \n'
        codigo += '\n'


        for funcion in self.funciones:
            codigo += funcion.getCode() + '\n'

        return codigo


        # _________________________________________ MIRILLA _________________________________________

    def optimizarMirilla(self):
        for funcion in self.funciones:
            tamano_mirilla = 20
            if tamano_mirilla > len(funcion.listaIns):
                tamano_mirilla = len(funcion.listaIns)

            # segun el enuncaido se deben dar 10 pasadas para la optimizacion
            for i in range(10):
                regla_aplicada = False
                indice_sentencia = 0
                while indice_sentencia + tamano_mirilla <= len(funcion.listaIns):
                    regla_aplicada = regla_aplicada or self.mirillaRelga1(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla], funcion.listaIns)
                    regla_aplicada = regla_aplicada or self.mirillaRegla4(funcion.listaIns[indice_sentencia: indice_sentencia + tamano_mirilla], funcion.listaIns)
                    regla_aplicada = regla_aplicada or self.mirillaRegla2(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla], funcion.listaIns)
                    regla_aplicada = regla_aplicada or self.mirillaRegla3(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla], funcion.listaIns)
                    regla_aplicada = regla_aplicada or self.mirillaRegla5(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla], funcion.listaIns)
                    regla_aplicada = regla_aplicada or self.mirillaRegla6(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla])
                    regla_aplicada = regla_aplicada or self.mirillaRegla7(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla])
                    regla_aplicada = regla_aplicada or self.mirillaRegla8(funcion.listaIns[indice_sentencia : indice_sentencia + tamano_mirilla])
                    indice_sentencia += 1

                # si no hubieron optimizaciones en la pasada se aumenta el tamaño de la mirilla
                if not regla_aplicada:
                    tamano_mirilla += 20

            for i, ins in enumerate(funcion.listaIns):
                if type(ins) is Goto and i + 1 < len(funcion.listaIns):
                    if type(funcion.listaIns[i + 1]) is Goto:
                        funcion.listaIns[i + 1].is_deleted = True

            codigo_funcion = self.get_codigo_bloque(funcion.listaIns)
            for ins in funcion.listaIns:
                if type(ins) is Etiqueta:
                    goto_to_etiqueta = f'goto {ins.id};'
                    if goto_to_etiqueta not in codigo_funcion:
                        ins.is_deleted = True


    def mirillaRelga1(self, listaIns, ins_completas):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is DecVar and not ins.is_deleted:
                ins_siguientes = listaIns[i + 1: len(listaIns)]
                for j, ins_siguiente in enumerate(ins_siguientes):
                    if type(ins_siguiente) is DecVar and not ins_siguiente.is_deleted:
                        if (ins.destino == ins_siguiente.expresion.getCode() and
                            ins_siguiente.destino ==  ins.expresion.getCode()):
                            codigo_original = self.get_codigo_bloque(listaIns[i : i + j + 2])
                            regla_aplicada = ins_siguiente.is_deleted = True
                            codigo_optimizado = self.get_codigo_bloque(listaIns[i : i + j + 2], True)
                            agregarOptimizacion(
                                "Mirilla",
                                "Regla 1",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )
                    elif type(ins_siguiente) is Etiqueta and not ins_siguiente.is_deleted:
                        break
        return regla_aplicada


    def mirillaRegla2(self, listaIns, ins_completas):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is Goto and not ins.is_deleted:
                lista_siguientes_ins = listaIns[i + 1: len(listaIns)]
                for j, ins_siguiente in enumerate(lista_siguientes_ins):
                    if type(ins_siguiente) is Etiqueta and not ins_siguiente.is_deleted:
                        if ins.etiqueta == ins_siguiente.id:
                            codigo_original = self.get_codigo_bloque(listaIns[i : i + j + 2])
                            ins.is_deleted = True
                            for k in range(j):
                                lista_siguientes_ins[k].is_deleted = True
                            regla_aplicada = True
                            codigo_optimizado = self.get_codigo_bloque(listaIns[i : i + j + 2], True)
                            agregarOptimizacion(
                                "Mirilla",
                                "Regla 2",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )
                        else:
                            if f'goto {ins_siguiente.id};' in self.get_codigo_bloque(ins_completas):
                                break
        return regla_aplicada


    def mirillaRegla3(self, listaIns, ins_completas):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if i + 2 < len(listaIns):
                if type(ins) is If and not ins.is_deleted:
                    ins_siguiente = listaIns[i + 1]
                    if (type(ins_siguiente) is Goto and not ins_siguiente.is_deleted and
                        type(listaIns[i + 2]) is Etiqueta and  not listaIns[i + 2].is_deleted):
                        if  listaIns[i + 2].id == ins.etiqueta:
                            codigo_original = self.get_codigo_bloque(listaIns[i: i + 3])
                            ins.exp.tipoOp = ins.exp.get_tipo_op_contrario()
                            ins.etiqueta = ins_siguiente.etiqueta
                            ins_siguiente.is_deleted = True
                            if f'goto {listaIns[i + 2].id};' not in self.get_codigo_bloque(ins_completas):
                                listaIns[i + 2].is_deleted = True
                            regla_aplicada =  True
                            codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + 3], True)
                            agregarOptimizacion(
                                "Mirilla",
                                "Regla 3",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )
        return regla_aplicada


    def mirillaRegla4(self, listaIns, insFuncion):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is Goto and not ins.is_deleted:
                listaInsSiguinetes = listaIns[i + 1 : len(listaIns)]
                for j, ins_siguiente in enumerate(listaInsSiguinetes):
                    if type(ins_siguiente) is Etiqueta and not ins_siguiente.is_deleted and j + 1 < len(listaInsSiguinetes):
                        ins_siguiente_siguiente = listaInsSiguinetes[j + 1]
                        if type(ins_siguiente_siguiente) is Goto and not ins_siguiente_siguiente.is_deleted:
                            if ins.etiqueta == ins_siguiente.id:
                                codigo_original = self.get_codigo_bloque(listaIns[i: i + j + 3])
                                ins.etiqueta = ins_siguiente_siguiente.etiqueta
                                if f'goto {ins_siguiente.id};' not in self.get_codigo_bloque(insFuncion):
                                    ins_siguiente.is_deleted = True
                                    ins_siguiente_siguiente.is_deleted = True
                                regla_aplicada = True
                                codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + j + 3])
                                agregarOptimizacion(
                                    "Mirilla",
                                    "Regla 4",
                                    codigo_original,
                                    codigo_optimizado,
                                    ins.linea
                                )
        return regla_aplicada


    def mirillaRegla5(self, listaIns, insFuncion):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is If and not ins.is_deleted:
                listaInsSiguinetes = listaIns[i : len(listaIns)]
                for j, ins_siguiente in enumerate(listaInsSiguinetes):
                    if type(ins_siguiente) is Etiqueta and not ins_siguiente.is_deleted and j + 1 < len(listaInsSiguinetes):
                        ins_siguiente_siguiente = listaInsSiguinetes[j + 1]
                        if type(ins_siguiente_siguiente) is Goto and not ins_siguiente_siguiente.is_deleted:
                            if ins.etiqueta == ins_siguiente.id:
                                codigo_original = self.get_codigo_bloque(listaIns[i: i + j + 2])
                                ins.etiqueta = ins_siguiente_siguiente.etiqueta
                                regla_aplicada = True
                                if f'goto {ins_siguiente.id};' not in self.get_codigo_bloque(insFuncion):
                                    ins_siguiente.is_deleted = ins_siguiente_siguiente.is_deleted = True
                                codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + j + 2], True)
                                agregarOptimizacion(
                                    "Mirilla",
                                    "Regla 5",
                                    codigo_original,
                                    codigo_optimizado,
                                    ins.linea
                                )
        return regla_aplicada

    def mirillaRegla6(self, listaIns):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is OpAritmetica:
                if ins.expresion.desitno_in_operands(ins.destino) and ins.expresion.is_neutral_op():
                    codigo_original = self.get_codigo_bloque(listaIns[i : i + 1])
                    regla_aplicada = ins.is_deleted = True
                    codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + 1], True)
                    agregarOptimizacion(
                        "Mirilla",
                        "Regla 6",
                        codigo_original,
                        codigo_optimizado,
                        ins.linea
                    )
        return regla_aplicada


    def mirillaRegla7(self, listaIns):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is OpAritmetica:
                if not ins.expresion.desitno_in_operands(ins.destino) and ins.expresion.is_neutral_op():
                    codigo_original = self.get_codigo_bloque(listaIns[i: i + 1])
                    ins.expresion = ins.expresion.get_no_neutral_op()
                    codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + 1], True)
                    regla_aplicada = True
                    agregarOptimizacion(
                        "Mirilla",
                        "Regla 7",
                        codigo_original,
                        codigo_optimizado,
                        ins.linea
                    )
        return regla_aplicada


    def mirillaRegla8(self, listaIns):
        regla_aplicada = False
        for i, ins in enumerate(listaIns):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is OpAritmetica:
                codigo_original = self.get_codigo_bloque(listaIns[i: i + 1])
                cheper_exp = ins.expresion.get_cheper_expresion()
                if cheper_exp is not None:
                    ins.expresion = cheper_exp
                    regla_aplicada = True
                    codigo_optimizado = self.get_codigo_bloque(listaIns[i: i + 1], True)
                    agregarOptimizacion(
                        "Mirilla",
                        "Regla 8",
                        codigo_original,
                        codigo_optimizado,
                        ins.linea
                    )
        return regla_aplicada


    def get_codigo_bloque(self, listaIns, incluir_eliminadas = False):
        codigo = ""
        for ins in listaIns:
            if not ins.is_deleted or incluir_eliminadas:
                codigo += ins.getCode()
        return codigo

    # _________________________________________ BLOQUES _________________________________________

    def optimizar_bloques(self):
        self.inicar_bloques()
        for bloques_funcion in self.bloques:
            for i, bloque in enumerate(bloques_funcion):
                self.bloques_regla1(bloque)
                self.bloques_regla2(bloque)
                self.bloques_regla3(bloque, i, bloques_funcion)
                self.bloques_regla4(bloque)


    def inicar_bloques(self):
        self.bloques = []
        self.generar_bloques()


    def generar_bloques(self):
        self.generar_lideres()
        self.crear_bloques()
        self.conectar_bloques()


    def generar_lideres(self):
        for funcion in self.funciones:
            funcion.listaIns[0].es_lider = True
            anterior_es_goto = False
            for ins in funcion.listaIns:
                if anterior_es_goto:
                    ins.es_lider = True
                    anterior_es_goto = False
                if type(ins) is Goto or type(ins) is If:
                    anterior_es_goto = True


    def crear_bloques(self):
        for funcion in self.funciones:
            bloques_funcion = []
            bloque = None
            for ins in funcion.listaIns:
                if ins.es_lider:
                    if bloque is not None:
                        bloques_funcion.append(bloque)
                    bloque = Bloque(ins)
                bloque.instrucciones.append(ins)
            bloques_funcion.append(bloque)
            self.bloques.append(bloques_funcion)


    def conectar_bloques(self):
        for bloques_funcion in self.bloques:
            bloque_previo = None
            for bloque in bloques_funcion:
                if bloque_previo is None:
                    bloque_previo = bloque
                    continue
                bloque_previo.siguientes.append(bloque)
                bloque_previo = bloque

            for bloque in bloques_funcion:
                ultima_ins_bloque = bloque.instrucciones[len(bloque.instrucciones) - 1]
                if type(ultima_ins_bloque) is Goto or type(ultima_ins_bloque) is If:
                    etiqueta = ultima_ins_bloque.etiqueta
                    for bloque_confirmacion in bloques_funcion:
                        if type(bloque_confirmacion.primera_ins) is Etiqueta and bloque_confirmacion.primera_ins.id == etiqueta:
                            bloque.siguientes.append(bloque_confirmacion)
                            break


    def bloques_regla1(self, bloque):
        for i, ins in enumerate(bloque.instrucciones):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is OpAritmetica:
                if ins.expresion.desitno_in_operands(ins.destino):
                    continue
                ins_siguientes = bloque.instrucciones[i + 1 : len(bloque.instrucciones)]
                for j, ins_siguiente in enumerate(ins_siguientes):
                    if type(ins_siguiente) is DecVar and not ins_siguiente.is_deleted:
                        if ins.expresion.getCode() == ins_siguiente.expresion.getCode():
                            codigo_intermedio = self.get_codigo_bloque(bloque.instrucciones[i + 1 : i + 1 + j])
                            opIzqCodigo = ins.expresion.opIzq.getCode()
                            opDerCodigo = ins.expresion.opDer.getCode()
                            if opIzqCodigo in codigo_intermedio:
                                try:
                                    int(opIzqCodigo)
                                except:
                                    break
                            elif opDerCodigo in codigo_intermedio:
                                try:
                                    int(opDerCodigo)
                                except:
                                    break
                            codigo_original = ins.getCode() + ins_siguiente.getCode()
                            ins_siguiente.expresion = AtomiExp(ins.destino, TipoDato.DECIMAL, ins.linea)
                            codigo_optimizado =  ins.getCode() + ins_siguiente.getCode()
                            agregarOptimizacion(
                                "Bloques",
                                "Regla 1",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )


    def bloques_regla2(self, bloque):
        for i, ins in enumerate(bloque.instrucciones):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is AtomiExp and ins.expresion.tipo == TipoDato.IDENTIFICADOR:
                ins_siguientes = bloque.instrucciones[i + 1 : len(bloque.instrucciones)]
                for j, ins_siguiente in enumerate(ins_siguientes):
                    if type(ins_siguiente) is DecVar and not ins_siguiente.is_deleted and type(ins_siguiente.expresion) is OpAritmetica:
                        codigo_intermedio = self.get_codigo_bloque(bloque.instrucciones[i + 1 : i + 1 + j])
                        if ins.expresion.getCode() in codigo_intermedio:
                            break
                        regla_aplicada = False
                        codigo_original = ins.getCode()
                        codigo_optimizado = ''
                        if ins_siguiente.expresion.opIzq.valor == ins.destino:
                            codigo_original += ins_siguiente.getCode()
                            ins_siguiente.expresion.opIzq.valor = ins.expresion.valor
                            codigo_optimizado = ins.getCode() + ins_siguiente.getCode()
                            regla_aplicada = True
                        elif ins_siguiente.expresion.opDer is not None and ins_siguiente.expresion.opDer.valor == ins.destino:
                            codigo_original += ins_siguiente.getCode()
                            ins_siguiente.expresion.opDer.valor = ins.expresion.valor
                            codigo_optimizado = ins.getCode() + ins_siguiente.getCode()
                            regla_aplicada = True
                        if regla_aplicada:
                            agregarOptimizacion(
                                "Bloques",
                                "Regla 2",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )


    def bloques_regla3(self, bloque, indice_bloue, bloques_funcion):
        codigo_siguiente = ''
        for b in bloques_funcion[indice_bloue + 1: len(bloques_funcion)]:
            codigo_siguiente += self.get_codigo_bloque(b.instrucciones)
        for i, ins in enumerate(bloque.instrucciones):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is AtomiExp and ins.expresion.tipo == TipoDato.IDENTIFICADOR:
                ins_siguientes = bloque.instrucciones[i + 1 : len(bloque.instrucciones)]
                codigo_siguiente += self.get_codigo_bloque(bloque.instrucciones[i + 1 : len(bloque.instrucciones)])
                if str(ins.destino) not in codigo_siguiente:
                    codigo_original = ins.getCode()
                    ins.is_deleted = True
                    codigo_optimizado = ins.getCode()
                    agregarOptimizacion(
                        "Bloques",
                        "Regla 3",
                        codigo_original,
                        codigo_optimizado,
                        ins.linea
                    )


    def bloques_regla4(self, bloque):
        for i, ins in enumerate(bloque.instrucciones):
            if type(ins) is DecVar and not ins.is_deleted and type(ins.expresion) is AtomiExp and (ins.expresion.tipo == TipoDato.DECIMAL or ins.expresion.tipo == TipoDato.ENTERO):
                ins_siguientes = bloque.instrucciones[i + 1 : len(bloque.instrucciones)]
                for j, ins_siguiente in enumerate(ins_siguientes):
                    if type(ins_siguiente) is DecVar and not ins_siguiente.is_deleted and type(ins_siguiente.expresion) is OpAritmetica:
                        if ins.destino == ins_siguiente.destino:
                            break
                        regla_aplicada = False
                        codigo_original = ''
                        codigo_optimizado = ''
                        if ins_siguiente.expresion.opIzq.valor == ins.destino:
                            codigo_original = ins.getCode() + ins_siguiente.getCode()
                            ins_siguiente.expresion.opIzq = ins.expresion
                            regla_aplicada = ins.is_deleted = True
                            codigo_optimizado = ins.getCode() + ins_siguiente.getCode()
                        elif ins_siguiente.expresion.opDer is not None and ins_siguiente.expresion.opDer.valor == ins.destino:
                            codigo_original =  ins.getCode() + ins_siguiente.getCode()
                            ins_siguiente.expresion.opDer = ins.expresion
                            regla_aplicada = ins.is_deleted = True
                            codigo_optimizado = ins.getCode() + ins_siguiente.getCode()
                        if regla_aplicada:
                            agregarOptimizacion(
                                "Bloques",
                                "Regla 4",
                                codigo_original,
                                codigo_optimizado,
                                ins.linea
                            )