from src.Tipos.TipoDato import *
from src.Instruccion.Instruccion import *
from src.Instruccion.ResIns import *
from src.Entorno.Ambito import *
from src.Errores.TablaErrores import *
from src.Reportes.TablaSimbolos import *
from src.Errores.Error import *
from src.Entorno.SimboloVariable import *
from src.Instruccion.Struct.StructInstance import *

class DecVar(Instruction):
    def __init__(self, refAmbito, id, expresion, tipo,  linea, columna, conValor=True):
        Instruction.__init__(self, linea, columna)
        self.refAmbito = refAmbito
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.conValor = conValor

    def ejecutar(self, ambito: Ambito):
        res = ResIns()
        if self.conValor:
            simboloExp = self.expresion.ejecutar(ambito)

            if simboloExp is None:
                return res
            elif simboloExp.tipo != self.tipo and self.tipo is not None:
                agregarError(Error(f"Se esperaba {self.tipo} y se obtuvo {simboloExp.tipo}", self.linea, self.columna))
                return  res

            if self.refAmbito == "global":
                ambito.getAmbitoGlobal().addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo))
            else:
                if not ambito.existeSimbolo(self.id):
                    ambito.addVariable(self.id, SimboloVariable(self.id, simboloExp.valor, simboloExp.tipo, self.linea, self.columna))
                else:
                    existente = ambito.getVariable(self.id)
                    existente.valor = simboloExp.valor
                    existente.tipo  = simboloExp.tipo

        return res
