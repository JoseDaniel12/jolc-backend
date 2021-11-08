from src.Expresion.Expresion import *
from src.Tipos.TipoExpRelacional import *
from src.Expresion.ResExp import *
from src.Tipos.TipoDato import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class OpRelacional(Expresion):
    def __init__(self, opIzq, opDer, tipo, linea, columna):
        Expresion.__init__(self, linea, columna)
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = tipo
        self.lbl_true = ''
        self.lbl_false = ''

    def ejecutar(self, ambito):
        res = ResExp(None, TipoDato.BOOLEANO)
        simboloOpIzq = self.opIzq.ejecutar(ambito)
        simboloOpDer = self.opDer.ejecutar(ambito)
        if simboloOpIzq is None or simboloOpDer is None:
            return None
        try:
            if self.tipo == TipoExpRelacional.MAYORQUE:
                res.valor = simboloOpIzq.valor > simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MENORQUE:
                res.valor = simboloOpIzq.valor < simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MAYORIGUAL:
                res.valor = simboloOpIzq.valor >= simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.MENORIGUAL:
                res.valor = simboloOpIzq.valor <= simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.IGUALIGUAL:
                res.valor = simboloOpIzq.valor == simboloOpDer.valor
            elif self.tipo == TipoExpRelacional.NOIGUAL:
                res.valor = simboloOpIzq.valor != simboloOpDer.valor
        except:
            agregarError(Error(f"{self.tipo.value} invalido {simboloOpIzq.tipo.value} con {simboloOpDer.tipo.value}", self.linea,  self.columna))
            return None
        return res


    def compilar(self, ambito, sectionCode3d):
        if self.lbl_true == '':
            self.lbl_true = GenCod3d.addLabel()
        if self.lbl_false == '':
            self.lbl_false = GenCod3d.addLabel()
        res = ResExp(None, TipoDato.BOOLEANO)
        res.lbl_true = self.lbl_true
        res.lbl_false = self.lbl_false

        simboloOpIzq = self.opIzq.compilar(ambito, sectionCode3d)
        simboloOpDer = self.opDer.compilar(ambito, sectionCode3d)
        if simboloOpIzq is None or simboloOpDer is None:
            return None
        elif TipoDato.BOOLEANO in [simboloOpIzq.tipo, simboloOpDer.tipo]:
            agregarError(Error(f"Las operaciones relaciones no aceptan Booleanos", self.linea, self.columna))
            return None

        if self.tipo == TipoExpRelacional.MAYORQUE:
            GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} > {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)
        elif self.tipo == TipoExpRelacional.MENORQUE:
            GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} < {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)
        elif self.tipo == TipoExpRelacional.MAYORIGUAL:
            GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} >= {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)
        elif self.tipo == TipoExpRelacional.MENORIGUAL:
            GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} <= {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)
        elif self.tipo == TipoExpRelacional.IGUALIGUAL:
            # en caso de ser una igualdad entre cadaneas
            if ((simboloOpIzq.tipo == TipoDato.CADENA or simboloOpIzq.tipo == TipoDato.CARACTER) and
                (simboloOpDer.tipo == TipoDato.CADENA or simboloOpDer.tipo == TipoDato.CARACTER)):

                GenCod3d.addCompareStrings()
                tmp_paramPosStack = GenCod3d.addTemporal()
                tmp_retorno = GenCod3d.addTemporal()

                GenCod3d.addCodigo3d('\n\t/* Inicio de llamada fucnion nativa compareStrings */ \n', sectionCode3d)

                #establecer parametros
                GenCod3d.addCodigo3d('\n\t/* Inicio de paso de parametros */ \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_paramPosStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion) + 1}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'stack[int({tmp_paramPosStack})] = {simboloOpIzq.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_paramPosStack} = sp + {ambito.size + len(GenCod3d.temporales_funcion) + 2}; \n')
                GenCod3d.addCodigo3d(f'stack[int({tmp_paramPosStack})] = {simboloOpDer.valor}; \n', sectionCode3d)
                GenCod3d.addCodigo3d('/* Fin de paso de parametros */ \n\n', sectionCode3d)

                #llamar funcion
                avanceAmbito = ambito.size + len(GenCod3d.temporales_funcion)
                GenCod3d.addCodigo3d(f'sp = sp + {avanceAmbito}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'compareStrings() ; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{tmp_retorno} = stack[int(sp)]; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'sp = sp - {avanceAmbito}; \n', sectionCode3d)
                GenCod3d.addCodigo3d(f'if ({tmp_retorno} == 1) {{ goto {self.lbl_true}; }} \n', sectionCode3d)

                GenCod3d.addCodigo3d('/* Fin de llamada de funcion nativa compareStrings */ \n\n', sectionCode3d)
            else:
                GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} == {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)
        elif self.tipo == TipoExpRelacional.NOIGUAL:
            GenCod3d.addCodigo3d(f'if ({simboloOpIzq.valor} != {simboloOpDer.valor}) {{ goto {self.lbl_true}; }} \n', sectionCode3d)

        GenCod3d.addCodigo3d(f'goto {self.lbl_false}; \n', sectionCode3d)
        GenCod3d.limpiar_temps_usados(simboloOpIzq.valor)
        GenCod3d.limpiar_temps_usados(simboloOpDer.valor)
        return res


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