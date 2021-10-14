from src.Errores.TablaErrores import *

class GenCod3d(object):
    numTemporales = -1
    numLabels = -1
    sp = 0
    hp = 0
    temporales = []
    codigo3d = ""
    funciones3d = ""
    funcNativas3d = ""
    nativasAgregadas = []
    temporales_funcion = []
    etiquetas_retorno = {}

    @staticmethod
    def limpiar_temps_usados(temporal):
        if temporal in GenCod3d.temporales_funcion:
            GenCod3d.temporales_funcion.reverse()
            GenCod3d.temporales_funcion.remove(temporal)
            GenCod3d.temporales_funcion.reverse()


    @staticmethod
    def getCodigo3d():
        codigo = getTablaErroresAsComents()
        codigo += "package main \n"
        codigo += "import ( \n"
        codigo += " \t\"fmt\"\n"
        codigo += ") \n\n"
        codigo += "var stack[1000000]float64; \n"
        codigo += "var heap[1000000]float64; \n"
        codigo += "var sp, hp float64; \n"

        if len(GenCod3d.temporales) > 0:
            codigo += f'var {", ".join(GenCod3d.temporales)} float64; \n'
        codigo += "\n"

        codigo += GenCod3d.funcNativas3d + '\n'

        codigo += GenCod3d.funciones3d + '\n'

        codigo += "func main() { \n"
        codigo += GenCod3d.codigo3d
        codigo += "}"

        return codigo

    @staticmethod
    def resetCompileData():
        GenCod3d.numTemporales = -1
        GenCod3d.numLabels = -1
        GenCod3d.sp = 0
        GenCod3d.hp = 0
        GenCod3d.temporales.clear()
        GenCod3d.codigo3d = ""
        GenCod3d.funciones3d = ""
        GenCod3d.funcNativas3d  = ""
        GenCod3d.nativasAgregadas.clear()
        GenCod3d.temporales_funcion.clear()

    @staticmethod
    def addComentario(self, comentario):
        GenCod3d.codigo3d += f'//{comentario}\n'

    @staticmethod
    def addTemporal():
        GenCod3d.numTemporales += 1
        temp = f't{GenCod3d.numTemporales}'
        GenCod3d.temporales.append(temp)
        return temp

    @staticmethod
    def addLabel():
        GenCod3d.numLabels += 1
        temp = f'l{GenCod3d.numLabels}'
        return temp

    @staticmethod
    def addCodigo3d(codigo, sectionCode3d = "main"):
        if sectionCode3d == "main":
            GenCod3d.codigo3d += f'\t{codigo}'
        elif sectionCode3d == "funciones":
            GenCod3d.funciones3d += f'\t{codigo}'

    @staticmethod
    def resetCodigo3d():
        GenCod3d.codigo3d = ""

    @staticmethod
    def addPrintString():
        lbl_impChar = GenCod3d.addLabel()
        lbl_finalizar = GenCod3d.addLabel()
        ultimoTemp = GenCod3d.temporales[len(GenCod3d.temporales) - 1]
        temp_parametro = GenCod3d.addTemporal()
        temp_posHeap = GenCod3d.addTemporal()
        temp_Caracter = GenCod3d.addTemporal()
        codigo = "func printString() { \n"
        codigo += f'\t{temp_parametro} = sp; \n'
        codigo += f'\t{temp_posHeap} = stack[int({temp_parametro})]; \n'
        codigo += f'\t{lbl_impChar}: \n'
        codigo += f'\t{temp_Caracter} = heap[int({temp_posHeap})]; \n'
        codigo += f'\tif ({temp_Caracter} == -1) {{ goto {lbl_finalizar}; }} \n'
        codigo += f'\tfmt.Printf("%c", int({temp_Caracter})); \n'
        codigo += f'\t{temp_posHeap} = {temp_posHeap} + 1; \n'
        codigo += f'\tgoto  {lbl_impChar}; \n'
        codigo += f'\t{lbl_finalizar}: \n'
        codigo += '} \n'
        if "printString" not in GenCod3d.nativasAgregadas:
            GenCod3d.nativasAgregadas.append("printString")
            GenCod3d.funcNativas3d += "\n" + codigo

    @staticmethod
    def addConcatString():
        lbl_concatCadenaUno = GenCod3d.addLabel()
        lbl_concatCadenaDos = GenCod3d.addLabel()
        lbl_finalizar = GenCod3d.addLabel()
        tmp_heapCopia = GenCod3d.addTemporal()
        tmp_stack = GenCod3d.addTemporal()
        tmp_posHeapCharCadenaUno = GenCod3d.addTemporal()
        tmp_posHeapCharCadenaDos = GenCod3d.addTemporal()
        tmp_caracter = GenCod3d.addTemporal()

        codigo = '\n' + 'func concatString() { \n'
        codigo += '\t' +  f'{tmp_heapCopia} = hp; \n'
        codigo += '\t' +  f'{tmp_stack} = sp + 1; \n'
        codigo += '\t' +  f'{tmp_posHeapCharCadenaUno} = stack[int({tmp_stack})]; \n'
        codigo += '\t' +  f'{tmp_stack} = sp + 2; \n'
        codigo += '\t' +  f'{tmp_posHeapCharCadenaDos} = stack[int({tmp_stack})]; \n'

        # se concatena la cadena uno
        codigo += '\t' +  f'{lbl_concatCadenaUno}:  \n'
        codigo += '\t' +  f'{tmp_caracter} = heap[int({tmp_posHeapCharCadenaUno})];  \n'
        codigo += '\t' + f'if ({tmp_caracter} == -1) {{ goto {lbl_concatCadenaDos}; }} \n'
        codigo += '\t' + f'heap[int(hp)] = {tmp_caracter}; \n'
        codigo += '\t' + f'hp = hp + 1; \n'
        codigo += '\t' + f'{tmp_posHeapCharCadenaUno} = {tmp_posHeapCharCadenaUno} + 1; \n'
        codigo += '\t' + f'goto {lbl_concatCadenaUno}; \n'

        # se concatena la cadena dos
        codigo += '\t' + f'{lbl_concatCadenaDos}:  \n'
        codigo += '\t' + f'{tmp_caracter} = heap[int({tmp_posHeapCharCadenaDos})];  \n'
        codigo += '\t' + f'if ({tmp_caracter} == -1) {{ goto {lbl_finalizar}; }} \n'
        codigo += '\t' + f'heap[int(hp)] = {tmp_caracter}; \n'
        codigo += '\t' + f'hp = hp + 1; \n'
        codigo += '\t' + f'{tmp_posHeapCharCadenaDos} = {tmp_posHeapCharCadenaDos} + 1; \n'
        codigo += '\t' +f'goto {lbl_concatCadenaDos}; \n'

        #finalizar
        codigo += '\t' + f'{lbl_finalizar}:  \n'
        codigo += '\t' + f'heap[int(hp)] = -1;   \n'
        codigo += '\t' + f'hp = hp + 1; \n'
        codigo += '\t' + f'stack[int(sp)] = {tmp_heapCopia}; \n'
        codigo += '} \n'

        if "concatString" not in GenCod3d.nativasAgregadas:
            GenCod3d.nativasAgregadas.append("concatString")
            GenCod3d.funcNativas3d += codigo

    @staticmethod
    def addPotencia():
        lbl_potenciar = GenCod3d.addLabel()
        lbl_guardarRetrono = GenCod3d.addLabel()
        lbl_setResAsUno = GenCod3d.addLabel()
        lbl_finalizar = GenCod3d.addLabel()
        tmp_posStackParam = GenCod3d.addTemporal()
        tmp_paramUno = GenCod3d.addTemporal()
        tmp_paramDos = GenCod3d.addTemporal()
        tmp_copiaBase = GenCod3d.addTemporal()
        temp_menosUno = GenCod3d.addTemporal()

        codigo = '\n' +"func potencia() { \n"
        codigo += '\t' + f'{tmp_posStackParam} = sp + 1; \n'
        codigo += '\t' + f'{tmp_paramUno} = stack[int({tmp_posStackParam})]; \n'
        codigo += '\t' + f'{tmp_copiaBase} = {tmp_paramUno}; \n'
        codigo += '\t' + f'{tmp_posStackParam} = sp + 2; \n'
        codigo += '\t' + f'{tmp_paramDos} = stack[int({tmp_posStackParam})]; \n'
        codigo += '\t' + f'if ({tmp_paramDos} == 0) {{ goto {lbl_setResAsUno}; }} \n'
        codigo += '\t' + f'if ({tmp_paramDos} > 0) {{ goto {lbl_potenciar}; }} \n'

        #invertir base
        codigo += '\t' + f'{tmp_paramUno} = 1 / {tmp_paramUno}; \n'
        codigo += '\t' + f'{tmp_copiaBase} = {tmp_paramUno}; \n'
        codigo += '\t' + f'{temp_menosUno} = -1; \n'
        codigo += '\t' + f'{tmp_paramDos} = {temp_menosUno} * {tmp_paramDos}; \n'

        #potenciar
        codigo += '\t' + f'{lbl_potenciar}: \n'
        codigo += '\t' + f'if ({tmp_paramDos} == 1) {{ goto {lbl_guardarRetrono}; }} \n'
        codigo += '\t' + f'{tmp_paramUno} = {tmp_paramUno} * {tmp_copiaBase}; \n'
        codigo += '\t' + f'{tmp_paramDos} = {tmp_paramDos} - 1; \n'
        codigo += '\t' + f'goto {lbl_potenciar}; \n'

        #guardar resultado
        codigo += '\t' + f'{lbl_guardarRetrono}: \n'
        codigo += '\t' + f'stack[int(sp)] = {tmp_paramUno}; \n'
        codigo += '\t' + f'goto {lbl_finalizar}; \n'

        #colocar respuesta como uno
        codigo += '\t' + f'{lbl_setResAsUno}: \n'
        codigo += '\t' + 'stack[int(sp)] = 1; \n'

        #terminar
        codigo += '\t' + f'{lbl_finalizar}: \n'
        codigo += '} \n'

        if "potenciar" not in GenCod3d.nativasAgregadas:
            GenCod3d.nativasAgregadas.append("potenciar")
            GenCod3d.funcNativas3d += codigo

    @staticmethod
    def addPowString(ambito):
        GenCod3d.addConcatString()
        lbl_concatenar = GenCod3d.addLabel()
        tmp_posStackParam = GenCod3d.addTemporal()
        tmp_posHeapCadena = GenCod3d.addTemporal()
        tmp_caracter = GenCod3d.addTemporal()
        tmp_potencia = GenCod3d.addTemporal()
        tmp_stack = GenCod3d.addTemporal()

        codigo = '\n' + "func powString() { \n"
        codigo += '\t' + f'{tmp_posStackParam} = sp + 1; \n'
        codigo += '\t' + f'{tmp_posHeapCadena} = stack[int({tmp_posStackParam})]; \n'
        codigo += '\t' + f'{tmp_posStackParam} = sp + 2; \n'
        codigo += '\t' + f'{tmp_potencia} = stack[int({tmp_posStackParam})]; \n'
        #concater caracter por caracter
        tmp_posCadenaPotenciada = GenCod3d.addTemporal()
        codigo += '\t' + f'{tmp_posCadenaPotenciada} = {tmp_posHeapCadena}; \n'

        #concatenar
        codigo += '\t' + f'{lbl_concatenar}: \n'
        #llmada funcion nativa
        tempStack = GenCod3d.addTemporal()
        tempRetorno = GenCod3d.addTemporal()
        #seteo los parametros
        codigo += '\t' + f'{tempStack} = sp + {ambito.size + 1}; \n'
        codigo += '\t' + f'stack[int({tempStack})] = {tmp_posHeapCadena}; \n'
        codigo += '\t' + f'{tempStack} = {tempStack} + 1; \n'
        codigo += '\t' + f'stack[int({tempStack})] = {tmp_posCadenaPotenciada}; \n'
        #pongo el stack en su posicion ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
        codigo += '\t' + f'sp = sp + {ambito.size}; \n'
        codigo += '\t' + f'concatString(); \n'
        codigo += '\t' + f'{tempRetorno} = stack[int(sp)]; \n'
        codigo += '\t' + f'sp = sp - {ambito.size}; \n'
        #guardo el reorno
        codigo += '\t' + f'{tmp_posCadenaPotenciada} = {tempRetorno}; \n'
        codigo += '\t' + f'{tmp_potencia} = {tmp_potencia} - 1; \n'
        codigo += '\t' + f'if ({tmp_potencia} > 1) {{ goto {lbl_concatenar}; }} \n'
        codigo += '} \n'

        if "powString" not in GenCod3d.nativasAgregadas:
            GenCod3d.nativasAgregadas.append("powString")
            GenCod3d.funcNativas3d += codigo
        return tempRetorno

    @staticmethod
    def addCompareStrings():
        lbl_repetir = GenCod3d.addLabel()
        lbl_validarIgualdad = GenCod3d.addLabel()
        lbl_dengarIgualdad = GenCod3d.addLabel()
        lbl_finzalidzar = GenCod3d.addLabel()
        tmp_posStackParam = GenCod3d.addTemporal()
        tmp_posHeapCharUno = GenCod3d.addTemporal()
        tmp_posHeapCharDos = GenCod3d.addTemporal()
        tmp_charUno = GenCod3d.addTemporal()
        tmp_charDos = GenCod3d.addTemporal()

        codigo = '\n' + "func compareStrings() { \n"
        codigo += '\t' + f'{tmp_posStackParam} = sp + 1; \n'
        codigo += '\t' + f'{tmp_posHeapCharUno} = stack[int({tmp_posStackParam})]; \n'
        codigo += '\t' + f'{tmp_posStackParam} = sp + 2; \n'
        codigo += '\t' + f'{tmp_posHeapCharDos} = stack[int({tmp_posStackParam})]; \n'

        #comparacion
        codigo += '\t' + f'{lbl_repetir}: \n'
        codigo += '\t' + f'{tmp_charUno} = heap[int({tmp_posHeapCharUno})]; \n'
        codigo += '\t' + f'{tmp_charDos} = heap[int({tmp_posHeapCharDos})]; \n'
        codigo += '\t' + f'if ({tmp_charUno} != {tmp_charDos}) {{ goto {lbl_dengarIgualdad}; }} \n'
        codigo += '\t' + f'if ({tmp_charUno} != -1) {{ goto {lbl_validarIgualdad}; }} \n'
        codigo += '\t' + f'{tmp_posHeapCharUno} = {tmp_posHeapCharUno} + 1; \n'
        codigo += '\t' + f'{tmp_posHeapCharDos} = {tmp_posHeapCharDos} + 1; \n'
        codigo += '\t' + f'goto {lbl_repetir}; \n'

        #validar
        codigo += '\t' + f'{lbl_validarIgualdad}: \n'
        codigo += '\t' + f'stack[int(sp)] = 1; \n'
        codigo += '\t' + f'goto {lbl_finzalidzar}; \n'
        #denegaar
        codigo += '\t' + f'{lbl_dengarIgualdad}: \n'
        codigo += '\t' + f'stack[int(sp)] = 0; \n'

        #finalidzar
        codigo += '\t' + f'{lbl_finzalidzar}: \n'
        codigo += '} \n'

        if "compareStrings" not in GenCod3d.nativasAgregadas:
            GenCod3d.nativasAgregadas.append("compareStrings")
            GenCod3d.funcNativas3d += codigo
