from src.Instruccion.Instruccion import *
from src.Instruccion.Condicionales.BloqueCondicional import *
from src.Instruccion.ejecutarBloqueIns import *
from src.Reportes.Cst import *
from src.Compilacion.GenCod3d import *

class IfCompleto(Instruction):
    def __init__(self, ifSimple: BloqueCondicional, listaElseIf: [BloqueCondicional], linstaInsElse, linea, columna):
        Instruction.__init__(self, linea, columna)
        self.IfSimple = ifSimple
        self.listaElseIf = listaElseIf
        self.listaInsElse = linstaInsElse

    def ejecutar(self, ambito):
        res = ResIns()
        simboloCondicion = self.IfSimple.condicion.ejecutar(ambito)
        if simboloCondicion is not None:
            if simboloCondicion.valor:
                return ejectuarBloqueIns(self.IfSimple.listaIns, ambito)
        else:
            return res

        for elseIf in self.listaElseIf:
            simboloCondicion = elseIf.condicion.ejecutar(ambito)
            if simboloCondicion is not None:
                if simboloCondicion.valor:
                    return  ejectuarBloqueIns(elseIf.listaIns, ambito)
            else:
                return res
        return ejectuarBloqueIns(self.listaInsElse, ambito)


    def compilar(self, ambito, sectionCode3d):
        res = ResIns()
        lbl_finalizar = GenCod3d.addLabel()
        lbl_cuerpoBloque = GenCod3d.addLabel()
        lbl_inicioBloque = ''

        # if_simple
        if len(self.listaElseIf) == 0 and len(self.listaInsElse) == 0:
            self.IfSimple.condicion.lbl_false = lbl_finalizar
        else:
            lbl_inicioBloque = GenCod3d.addLabel()
            self.IfSimple.condicion.lbl_false = lbl_inicioBloque
        self.IfSimple.condicion.lbl_true = lbl_cuerpoBloque
        self.IfSimple.condicion.compilar(ambito, sectionCode3d)
        GenCod3d.addCodigo3d(f'{lbl_cuerpoBloque}: \n', sectionCode3d)
        for ins in self.IfSimple.listaIns:
            ins.lbl_break = self.lbl_break
            ins.lbl_continue = self.lbl_continue
            ins.lbl_return = self.lbl_return
            ins.compilar(ambito, sectionCode3d)

        #lista_else_if
        for i, elseIf in enumerate(self.listaElseIf):
            GenCod3d.addCodigo3d(f'goto {lbl_finalizar}; \n\n', sectionCode3d)
            GenCod3d.addCodigo3d(f'{lbl_inicioBloque}: \n', sectionCode3d)
            lbl_cuerpoBloque = GenCod3d.addLabel()
            if i != len(self.listaElseIf) - 1 or len(self.listaInsElse) > 0:
                lbl_inicioBloque = GenCod3d.addLabel()
            else:
                lbl_inicioBloque = lbl_finalizar
            elseIf.condicion.lbl_true = lbl_cuerpoBloque
            elseIf.condicion.lbl_false = lbl_inicioBloque
            elseIf.condicion.compilar(ambito, sectionCode3d)
            GenCod3d.addCodigo3d(f'{lbl_cuerpoBloque}: \n', sectionCode3d)
            for ins in elseIf.listaIns:
                ins.lbl_break = self.lbl_break
                ins.lbl_continue = self.lbl_continue
                ins.lbl_return = self.lbl_return
                ins.compilar(ambito, sectionCode3d)

        #else
        for i, ins in enumerate(self.listaInsElse):
            ins.lbl_break = self.lbl_break
            ins.lbl_continue = self.lbl_continue
            ins.lbl_return = self.lbl_return
            if i == 0:
                GenCod3d.addCodigo3d(f'goto {lbl_finalizar}; \n\n', sectionCode3d)
                GenCod3d.addCodigo3d(f'{lbl_inicioBloque}: \n', sectionCode3d)
            ins.compilar(ambito, sectionCode3d)

        GenCod3d.addCodigo3d(f'{lbl_finalizar}: \n', sectionCode3d)
        return res


    def generateCst(self, idPadre):
        defElementCst(self.idSent, "IF_COMPLETO", idPadre)
        #ifSimple
        idIfSimple = getNewId()
        defElementCst(idIfSimple, "IF_SIMPLE", self.idSent)
        self.IfSimple.generateCst(idIfSimple)
        #listaElseIf
        if len(self.listaElseIf) > 0:
            idListaElseIf = getNewId()
            defElementCst(idListaElseIf, "Lista_ELSE_IF", self.idSent)
            for bloque in self.listaElseIf:
                bloque.generateCst(idListaElseIf)
        #else
        if len(self.listaInsElse) > 0:
            idElse = getNewId()
            defElementCst(idElse, "ELSE_INS", self.idSent)
            for ins in self.listaInsElse:
                ins.generateCst(idElse)