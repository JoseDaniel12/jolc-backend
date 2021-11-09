from src.Optimizacion.Instrucciones.If import *
from src.Optimizacion.Instrucciones.Goto import *
from src.Optimizacion.Instrucciones.DecVar import *
from src.Optimizacion.Instrucciones.Etiqueta import *
from src.Optimizacion.Reportes.ReporteOptimizacion import *
from src.Optimizacion.Expresiones.OpAritmetica import *


class Optimizador:
    def __init__(self, paquetes, temporales, funciones):
        self.paquetes = paquetes
        self.temporales = temporales
        self.funciones = funciones


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
                                listaIns[0].linea
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
                                listaIns[0].linea
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
                                listaIns[0].linea
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
                                    listaIns[0].linea
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
                                    listaIns[0].linea
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
                        listaIns[0].linea
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
                        listaIns[0].linea
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
                        listaIns[0].linea
                    )
        return regla_aplicada


    def get_codigo_bloque(self, listaIns, incluir_eliminadas = False):
        codigo = ""
        for ins in listaIns:
            if not ins.is_deleted or incluir_eliminadas:
                codigo += ins.getCode()
        return codigo
