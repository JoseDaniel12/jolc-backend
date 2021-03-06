from src.Expresion.Expresion import Expresion
from src.Tipos.TipoExpArtimetica import TipoExpAritmetica
from src.Expresion.ResExp import ResExp
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *


class OpAritmetica(Expresion):
    def __init__(self, opIzq, opDer, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = tipo

    def ejecutar(self, ambito):
        res = ResExp("", "")

        # se compila el simbolo izquierdo eld derecho se deja en nulo en caso de ser expresion unaria
        simboloOpIzq = self.opIzq.ejecutar(ambito)
        simboloOpDer = None

        # se consigue el operando derecho si no es expresion unaria
        if self.tipo != TipoExpAritmetica.UMENOS:
            simboloOpDer = self.opDer.ejecutar(ambito)

        # se verifica que no haya errores
        if simboloOpIzq is None or (simboloOpDer is None and self.tipo != TipoExpAritmetica.UMENOS):
            return None

        # se realiza la operacion segun su tipo

        if self.tipo == TipoExpAritmetica.SUMA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor + simboloOpDer.valor

        elif self.tipo == TipoExpAritmetica.RESTA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor - simboloOpDer.valor

        elif self.tipo == TipoExpAritmetica.MULTIPLICACION:
            if simboloOpIzq.tipo == TipoDato.CADENA and simboloOpDer.tipo == TipoDato.CADENA:
                res.tipo = TipoDato.CADENA
                res.valor = simboloOpIzq.valor + simboloOpDer.valor
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                    res.valor = simboloOpIzq.valor * simboloOpDer.valor
                else:
                    res.tipo = TipoDato.ENTERO
                    res.valor = simboloOpIzq.valor * simboloOpDer.valor

        elif self.tipo == TipoExpAritmetica.DIVISION:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}",self.linea, self.columna))
                return None
            else:
                res.tipo = TipoDato.DECIMAL
            res.valor = simboloOpIzq.valor / simboloOpDer.valor
        elif self.tipo == TipoExpAritmetica.POTENCIA:
            if (simboloOpIzq.tipo == TipoDato.CADENA or simboloOpIzq.tipo == TipoDato.CARACTER) and simboloOpDer.tipo == TipoDato.ENTERO:
                res.valor = ""
                for i in range(simboloOpDer.valor):
                    res.valor += simboloOpIzq.valor
                res.tipo = TipoDato.CADENA
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                else:
                    res.tipo = TipoDato.ENTERO
                res.valor = simboloOpIzq.valor ** simboloOpDer.valor

        elif self.tipo == TipoExpAritmetica.MODULO:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalido {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            res.valor = simboloOpIzq.valor % simboloOpDer.valor

        elif self.tipo == TipoExpAritmetica.UMENOS:
            if simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL:
                agregarError(Error(f"{self.tipo.value} invalido con tipo {simboloOpIzq.tipo.value}", self.linea, self.columna))
                return None
            else:
                res.valor = -1 * simboloOpIzq.valor
                res.tipo = simboloOpIzq.tipo

        return res

    # _________________________________________ COMPILACION _________________________________________

    def compilar(self, ambito, sectionCode3d):
        res = ResExp("", "")

        # se compila el simbolo izquierdo eld derecho se deja en nulo en caso de ser expresion unaria
        simboloOpIzq = self.opIzq.compilar(ambito, sectionCode3d)
        simboloOpDer = None

        # se consigue el operando derecho si no es expresion unaria
        if self.tipo != TipoExpAritmetica.UMENOS:
            simboloOpDer = self.opDer.compilar(ambito, sectionCode3d)

        # se verifica que no haya errores
        if simboloOpIzq is None or (simboloOpDer is None and self.tipo != TipoExpAritmetica.UMENOS):
            return None

        # se realiza la operacion segun su tipo

        if self.tipo == TipoExpAritmetica.SUMA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            tempDestino = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tempDestino} = {simboloOpIzq.valor} + {simboloOpDer.valor}; \n', sectionCode3d)
            res.valor = tempDestino

        elif self.tipo == TipoExpAritmetica.RESTA:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            tempDestino = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tempDestino} = {simboloOpIzq.valor} - {simboloOpDer.valor}; \n', sectionCode3d)
            res.valor = tempDestino

        elif self.tipo == TipoExpAritmetica.MULTIPLICACION:
            if simboloOpIzq.tipo == TipoDato.CADENA and simboloOpDer.tipo == TipoDato.CADENA:
                res.tipo = TipoDato.CADENA
                GenCod3d.addConcatString()
                tempStack = GenCod3d.addTemporal()
                tempHeap = GenCod3d.addTemporal()
                tempRetorno = GenCod3d.addTemporal()
                # paso de parametros a la funcion nartiva
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion) + 1}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpIzq.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion) + 2}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpDer.valor}; \n', sectionCode3d)
                # llamada de funcion nariva
                avanceAmbito = ambito.size + len(GenCod3d.temporales_funcion)
                GenCod3d.addCodigo3d(f'sp = sp + {avanceAmbito}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'concatString(); \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempRetorno} = stack[int(sp)]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {avanceAmbito}; \n', sectionCode3d)
                res.valor = tempRetorno
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                else:
                    res.tipo = TipoDato.ENTERO
                tempDestino = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d(f'{tempDestino} = {simboloOpIzq.valor} * {simboloOpDer.valor}; \n', sectionCode3d)
                res.valor = tempDestino

        elif self.tipo == TipoExpAritmetica.DIVISION:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}",self.linea, self.columna))
                return None
            res.tipo = TipoDato.DECIMAL
            lbl_dividir = GenCod3d.addLabel()
            lbl_error = GenCod3d.addLabel()
            lbl_finalizaer = GenCod3d.addLabel()
            tmp_numerador = GenCod3d.addTemporal()
            tmp_denominador = GenCod3d.addTemporal()
            tempDestino = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'if ({simboloOpDer.valor} != 0) {{ goto {lbl_dividir}; }} \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {lbl_error}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{lbl_dividir}: \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_numerador} = {simboloOpIzq.valor}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tmp_denominador} = {simboloOpDer.valor}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{tempDestino} = {tmp_numerador} / {tmp_denominador}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'goto {lbl_finalizaer}; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{lbl_error}: \n', sectionCode3d)
            list(map(lambda c: GenCod3d.addCodigo3d(f'fmt.Printf("%c", {ord(c)}); \n', sectionCode3d), "Math error\n"))
            GenCod3d.addCodigo3d(f'{tempDestino} = 0; \n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{lbl_finalizaer}: \n', sectionCode3d)
            res.valor = tempDestino

        elif self.tipo == TipoExpAritmetica.POTENCIA:
            if (simboloOpIzq.tipo == TipoDato.CADENA or simboloOpIzq.tipo == TipoDato.CARACTER) and simboloOpDer.tipo == TipoDato.ENTERO:
                res.tipo = TipoDato.CADENA
                GenCod3d.addPowString(ambito)
                tempStack = GenCod3d.addTemporal()
                tempRetorno = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d('\n\t/* Inicio de llamada fucnion */ \n', sectionCode3d)

                GenCod3d.addCodigo3d('\n\t/* Inicio de paso de parametros */ \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + 1}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpIzq.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + 2}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpDer.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCode3d)

                GenCod3d.addCodigo3d(f'sp = sp + {ambito.size}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'powString(); \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempRetorno} = stack[int(sp)]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {ambito.size}; \n', sectionCode3d)

                GenCod3d.addCodigo3d('/* Fin de llamada de funcion */ \n\n', sectionCode3d)
                res.valor = tempRetorno
            else:
                if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                    (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                    agregarError(Error(f"{self.tipo.value} invalida {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                    return None
                elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                    res.tipo = TipoDato.DECIMAL
                else:
                    res.tipo = TipoDato.ENTERO
                GenCod3d.addPotencia(ambito)
                tempStack = GenCod3d.addTemporal()
                tempRetorno = GenCod3d.addTemporal()
                GenCod3d.addCodigo3d('\n\t/* Inicio de llamada de funcion */ \n', sectionCode3d)

                # paso de parametros
                GenCod3d.addCodigo3d('/* Inicio de paso de parametros */ \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + 1}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpIzq.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempStack} = sp + {ambito.size + 2}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tempStack})] = {simboloOpDer.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCode3d)
                # llamada de funcion nativa
                GenCod3d.addCodigo3d(f'sp = sp + {ambito.size}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'potencia(); \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tempRetorno} = stack[int(sp)]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {ambito.size}; \n', sectionCode3d)

                GenCod3d.addCodigo3d('/* Fin de llamada de funcion */ \n\n', sectionCode3d)
                res.valor = tempRetorno

        elif self.tipo == TipoExpAritmetica.MODULO:
            if ((simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL) or
                (simboloOpDer.tipo != TipoDato.ENTERO and simboloOpDer.tipo != TipoDato.DECIMAL)):
                agregarError(Error(f"{self.tipo.value} invalido {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea, self.columna))
                return None
            elif simboloOpIzq.tipo == TipoDato.DECIMAL or simboloOpDer.tipo == TipoDato.DECIMAL:
                res.tipo = TipoDato.DECIMAL
            else:
                res.tipo = TipoDato.ENTERO
            if "math" not in GenCod3d.imports:
                GenCod3d.imports += "\t\"math\" \n"
            tempDestino = GenCod3d.addTemporal()
            GenCod3d.addCodigo3d(f'{tempDestino} = math.Mod({simboloOpIzq.valor}, {simboloOpDer.valor}); \n', sectionCode3d)
            res.valor = tempDestino

        elif self.tipo == TipoExpAritmetica.UMENOS:
            if simboloOpIzq.tipo != TipoDato.ENTERO and simboloOpIzq.tipo != TipoDato.DECIMAL:
                agregarError(Error(f"{self.tipo.value} invalido con tipo {simboloOpIzq.tipo.value}", self.linea, self.columna))
                return None
            tempDestino = GenCod3d.addTemporal()
            res.tipo = simboloOpIzq.tipo
            GenCod3d.addCodigo3d(f'{tempDestino} = 0 - {simboloOpIzq.valor}; \n', sectionCode3d)
            res.valor = tempDestino

        # se guarda temporal no utilizado y se limpian los utilizados
        if sectionCode3d == "funciones":
            GenCod3d.temporales_funcion.append(res.valor)
            if simboloOpIzq is not None:
                GenCod3d.limpiar_temps_usados(simboloOpIzq.valor)
            if simboloOpDer is not None:
                GenCod3d.limpiar_temps_usados(simboloOpDer.valor)
        return res


    # _________________________________________ Arbol CST _________________________________________

    def generateCst(self, idPadre):
        defElementCst(self.idSent, self.tipo.value, idPadre)
        #opIzq
        if self.opIzq is not None:
            idOpIzq  = getNewId()
            defElementCst(idOpIzq, "EXPRESION", self.idSent)
            self.opIzq.generateCst(idOpIzq)
        #opDer
        if self.opDer is not None:
            idOpDer  = getNewId()
            defElementCst(idOpDer, "EXPRESION", self.idSent)
            self.opDer.generateCst(idOpDer)