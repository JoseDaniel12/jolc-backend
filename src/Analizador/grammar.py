import src.Analizador.ply.yacc as yacc
import src.Analizador.ply.lex as lex

from src.Instruccion.Print import  *
from src.Expresion.OpAritemtica import *
from src.Expresion.AtomicExp import *
from src.Tipos.TipoExpArtimetica import *
from src.Expresion.OpRelacional import *
from src.Tipos.TipoExpRelacional import *
from src.Instruccion.DecVar import *
from src.Instruccion.Condicionales.IfCompleto import *
from src.Instruccion.Condicionales.BloqueCondicional import *
from src.Instruccion.Bucles.While import *
from src.Expresion.Rango import *
from src.Instruccion.Bucles.For import *
from src.Instruccion.Funcion.Parametro import *
from src.Instruccion.Funcion.DecFuncion import *
from src.Expresion.AccesoArreglo import *
from src.SentenciaHibrida.LlamadaFuncStruct import *
from src.Expresion.OpLogica import *
from src.Instruccion.SentenciasTransferencia.Return import *
from src.Instruccion.SentenciasTransferencia.Break import *
from src.Instruccion.SentenciasTransferencia.Continue import *
from src.Instruccion.ModificacionArreglo import *
from src.Instruccion.Struct.DecStruct import *
from src.Instruccion.Struct.ModificacionStruct import *
from src.Expresion.AccesoStruct import *
from src.Expresion.FuncionesNativas.FuncTrigonometrica import *
from src.Expresion.FuncionesNativas.FuncLogaritmica import *
from src.Expresion.FuncionesNativas.Sqrt import *
from src.Expresion.FuncionesNativas.Parse import *
from src.Expresion.FuncionesNativas.Trunc import *
from src.Expresion.FuncionesNativas.Float import *
from src.Expresion.FuncionesNativas.FuncString import *
from src.Expresion.FuncionesNativas.FuncTypeOf import *
from src.Expresion.FuncionesNativas.Push import *
from src.Expresion.FuncionesNativas.Pop import *
from src.Expresion.FuncionesNativas.Length import *
from src.Expresion.FuncionesNativas.Uppercase import *
from src.Expresion.FuncionesNativas.LowerCase import *
from src.Reportes.Cst import *

res = {
    "listaIns": []
}

# ________________________________________________SACANNER________________________________________________

# PALABRAS_RESERVADAS
rw = {
    'print': 'PRINT',
    'println': 'PRINTLN',
    'nothing': 'NOTHING',
    'if': 'IF',
    'elseif': 'ELSEIF',
    'else': 'ELSE',
    'end': 'END',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',

    'None': 'None',
    'Int64': 'Int64',
    'Float64': 'Float64',
    'Bool': 'Bool',
    'Char': 'Char',
    'String': 'String',

    'global': 'GLOBAL',
    'local': 'LOCAL',
    'struct': 'STRUCT',
    'mutable': 'MUTABLE',

    'log10': 'LOG10',
    'log': 'LOG',
    'sin': 'SIN',
    'cos': 'COS',
    'tan': 'TAN',
    'sqrt': 'SQRT',

    'parse': 'PARSE',
    'trunc': 'TRUNC',
    'float': 'FLOAT',
    'string': 'STRING',
    'typeof': 'TYPEOF',
    'push': 'PUSH',
    'pop': 'POP',
    'length': 'LENGTH',
    'uppercase': 'UPPERCASE',
    'lowercase': 'LOWERCASE'

}

# TOKENS
tokens = [
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',

    'MAS',
    'MENOS',
    'ASTERISCO',
    'SLASH',
    'MODULO',
    'SOMBRERO',

    'PARENTESIS_A',
    'PARENTESIS_C',
    'CORCHETE_A',
    'CORCHETE_C',
    'DOBLE_DOS_PTS',
    'DOS_PTS',
    'PT_Y_COMA',
    'COMA',

    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'IGUAL',
    'NOIGUAL',
    'OR',
    'AND',
    'ADMIRACION',
    
    'IDENTIFICADOR',
    'TRUE',
    'FALSE',
    'PUNTO'
] + list(rw.values())

# EXPRESIONES_REGULARES
t_MAS = r'\+'
t_MENOS = r'\-'
t_ASTERISCO = r'\*'
t_SLASH = r'\/'
t_MODULO = r'\%'
t_SOMBRERO = r'\^'

t_MAYORIGUAL= r'\>\='
t_MAYORQUE = r'\>'
t_MENORIGUAL= r'\<\='
t_MENORQUE = r'\<'
t_IGUALIGUAL = r'\=='
t_IGUAL = r'\='
t_NOIGUAL = r'\!\='

t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_CORCHETE_A = r'\['
t_CORCHETE_C = r'\]'
t_DOBLE_DOS_PTS = r'::'
t_DOS_PTS =  r'\:'
t_PT_Y_COMA = r'\;'
t_COMA = r'\,'

t_OR = r'\|\|'
t_AND = r'\&\&'
t_ADMIRACION = r'\!'
t_PUNTO = r'\.'

# EXPRESIONES_REGUALRES_CON_ACCIONES
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r'\'.*\''
    t.value = t.value[1:-1]
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in rw:
        t.type = rw[t.value]
    elif t.value == 'true':
        t.value = True
        t.type = 'TRUE'
    elif t.value == 'false':
        t.value = False
        t.type = 'FALSE'
    return t

def t_TRUE(t):
    r'true'
    return True

def t_FALSE(t):
    r'false'
    return False

def t_COMENTARIO_DOBLE(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')
    t.lexer.pos = 0

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1
    t.lexer.pos = 0

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.lexer.pos = 0
    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore=' \t\r\f\v'
lex.lex()


# ________________________________________________PARSER________________________________________________

# PRECEDENCIAS
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'ADMIRACION'),
    ('left', 'IGUALIGUAL', 'NOIGUAL', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'SLASH', 'ASTERISCO'),
    ('left', 'MODULO', 'SOMBRERO'),
    ('right', 'UMENOS'),
    ('left', 'CORCHETE_A', 'CORCHETE_C'),
    ('left', 'PARENTESIS_A', 'PARENTESIS_C'),

)

# GRAMATICA
def p_start(p):
    '''
    start   : listaInstrucciones
    '''
    p[0] = p[1]
    p.lexer.lineno = 1
    p.lexer.pos = 1
    return p[0]

def p_lista_instrucciones(p):
    '''
    listaInstrucciones  : listaInstrucciones instruccion
                        | instruccion
    '''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = [p[1]]


def p_instrucion(p):
    '''
    instruccion  : instruccion PT_Y_COMA
                | funcion_print
                | declarar_var
                | instruccion_if
                | while
                | for
                | dec_funcion
                | llamda_funcion
                | return
                | break
                | continue
                | modificacion_arreglo
                | declaracion_struct
                | modificacion_struct
    '''
    p[0] = p[1]


def p_funcion_print(p):
    '''
    funcion_print   : PRINT PARENTESIS_A listaExpresiones PARENTESIS_C
                    | PRINTLN PARENTESIS_A listaExpresiones PARENTESIS_C
                    | PRINT PARENTESIS_A PARENTESIS_C
                    | PRINTLN PARENTESIS_A PARENTESIS_C
    '''
    if p.slice[1].type == 'PRINT':
        if len(p) == 5:
            p[0] = Print(p[3], p.lineno(1), p.lexpos(0))
        else:
            p[0] = Print([], p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'PRINTLN':
        if len(p) == 5:
            p[0] = Print(p[3], p.lineno(1), p.lexpos(0), isEnter=True)
        else:
            p[0] = Print([], p.lineno(1), p.lexpos(0), isEnter=True)

def p_return(p):
    '''
    return  : RETURN expresion
            | RETURN
    '''
    if len(p) == 3:
        p[0] = Return(p[2], p.lineno(1), p.lexpos(0))
    elif len(p) == 2:
        p[0] = Return(None, p.lineno(1), p.lexpos(0))

def p_break(p):
    '''
    break   : BREAK
    '''
    p[0] = Break(p.lineno(1), p.lexpos(0))

def p_continue(p):
    '''
    continue    : CONTINUE
    '''
    p[0] = Continue(p.lineno(1), p.lexpos(0))

def p_listaExpresiones(p):
    '''
    listaExpresiones    : listaExpresiones COMA expresion
                        | expresion
    '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = [p[1]]


def p_expresion(p):
    '''
    expresion   : llamda_funcion
                | acceso_strcut
                | funciones_nativas
    '''
    p[0] = p[1]

def p_expresion_agrupada(p):
    '''
    expresion    : PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = p[2]

def p_operacion_binaria_aritmetica(p):
    '''
    expresion  : expresion MAS expresion
                | expresion MENOS expresion
                | expresion ASTERISCO expresion
                | expresion SLASH expresion
                | expresion MODULO expresion
                | expresion SOMBRERO expresion
    '''
    if p[2] == '+':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.SUMA, p.lineno(1), p.lexpos(0))
    elif p[2] == '-':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.RESTA, p.lineno(1), p.lexpos(0))
    elif p[2] == '*':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.MULTIPLICACION, p.lineno(1), p.lexpos(0))
    elif p[2] == '/':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.DIVISION, p.lineno(1), p.lexpos(0))
    elif p[2] == '^':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.POTENCIA, p.lineno(1), p.lexpos(0))
    elif p[2] == '%':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.MODULO, p.lineno(1), p.lexpos(0))

def p_expresion_umenos(p):
    '''
    expresion   : MENOS expresion %prec UMENOS
    '''
    p[0] = OpAritmetica(p[2], None, TipoExpAritmetica.UMENOS, p.lineno(1), p.lexpos(0))

def p_operacion_logica(p):
    '''
    expresion   : expresion OR expresion
                | expresion AND expresion
                | ADMIRACION expresion
    '''
    if p.slice[2].type == 'OR':
        p[0] = OpLogica(p[1], p[3], TipoExpLogica.OR, p.lineno(1), p.lexpos(0))
    elif p.slice[2].type == 'AND':
        p[0] = OpLogica(p[1], p[3], TipoExpLogica.AND, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'ADMIRACION':
        p[0] = OpLogica(p[2], None, TipoExpLogica.NOT, p.lineno(1), p.lexpos(0))

def p_operacion_relacional(p):
    '''
    expresion  : expresion MAYORQUE expresion
                | expresion MENORQUE expresion
                | expresion MAYORIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion IGUALIGUAL expresion
                | expresion NOIGUAL expresion
    '''
    if p[2] == '>':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MAYORQUE, p.lineno(1), p.lexpos(0))
    elif p[2] == '<':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MENORQUE, p.lineno(1), p.lexpos(0))
    elif p[2] == '>=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MAYORIGUAL, p.lineno(1), p.lexpos(0))
    elif p[2] == '<=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MENORIGUAL, p.lineno(1), p.lexpos(0))
    elif p[2] == '==':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.IGUALIGUAL, p.lineno(1), p.lexpos(0))
    elif p[2] == '!=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.NOIGUAL, p.lineno(1), p.lexpos(0))

def p_expresion_arreglo(p):
    '''
    expresion   : CORCHETE_A listaExpresiones CORCHETE_C
    '''
    p[0] = Arreglo(p[2], p.lineno(1), p.lexpos(0))

def p_acceso_arreglo(p):
    '''
    expresion   : expresion CORCHETE_A expresion CORCHETE_C
    '''
    p[0] = AccesoArreglo(p[1], p[3], p.lineno(1), p.lexpos(0))

def p_expresion_rango(p):
    '''
    expresion   : expresion DOS_PTS expresion
    '''
    p[0] = Rango(p[1], p[3], p.lineno(1), p.lexpos(0))

def p_expresion_atomica_nothing(p):
    '''
    expresion   : NOTHING
                | ENTERO
                | DECIMAL
                | TRUE
                | FALSE
                | CARACTER
                | CADENA
                | IDENTIFICADOR
    '''
    if p.slice[1].type == 'NOTHING':
        p[0] = AtomicExp(p[1], TipoDato.NONE, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'ENTERO':
        p[0] = AtomicExp(p[1], TipoDato.ENTERO, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'DECIMAL':
        p[0] = AtomicExp(p[1], TipoDato.DECIMAL, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'TRUE' or p.slice[1].type == 'FALSE':
        p[0] = AtomicExp(p[1], TipoDato.BOOLEANO, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'CARACTER':
        p[0] = AtomicExp(p[1], TipoDato.CARACTER, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type == 'CADENA':
        p[0] = AtomicExp(p[1], TipoDato.CADENA, p.lineno(1), p.lexpos(0))
    elif p.slice[1].type  == 'IDENTIFICADOR':
        p[0] = AtomicExp(p[1], TipoDato.IDENTIFICADOR, p.lineno(1), p.lexpos(0))

def p_modificacion_arreglo(p):
    '''
    modificacion_arreglo    : expresion CORCHETE_A expresion CORCHETE_C IGUAL expresion
    '''
    p[0] = ModificacionArreglo(p[1], p[3], p[6], p.lineno(1), p.lexpos(0))

def p_delcarar_Var(p):
    '''
    declarar_var    : referencia_ambito IDENTIFICADOR IGUAL expresion DOBLE_DOS_PTS tipo
                    | referencia_ambito IDENTIFICADOR IGUAL expresion
                    | IDENTIFICADOR IGUAL expresion DOBLE_DOS_PTS tipo
                    | IDENTIFICADOR IGUAL expresion
    '''
    if len(p) == 7:
        p[0] = DecVar(p[1], p[2], p[4], p[6], p.lineno(1), p.lexpos(0))
    elif len(p) == 5:
        p[0] = DecVar(p[1], p[2], p[4], None, p.lineno(1), p.lexpos(0))
    elif len(p) == 6:
        p[0] = DecVar("local", p[1], p[3], p[5], p.lineno(1), p.lexpos(0))
    elif len(p) == 4:
        p[0] = DecVar("local", p[1], p[3], None, p.lineno(1), p.lexpos(0))

def p_declarar_var_sin_valor(p):
    '''
    declarar_var    : referencia_ambito IDENTIFICADOR DOBLE_DOS_PTS tipo
                    | referencia_ambito IDENTIFICADOR
                    | IDENTIFICADOR DOBLE_DOS_PTS tipo
                    | IDENTIFICADOR
    '''
    if len(p) == 5:
        p[0] = DecVar(p[1], p[2], None, p[4], p.lineno(1), p.lexpos(0), False)
    elif len(p) == 3:
        p[0] = DecVar(p[1], p[2], None, None, p.lineno(1), p.lexpos(0), False)
    elif len(p) == 4:
            p[0] = DecVar(None, p[1], None, p[3], p.lineno(1), p.lexpos(0), False)
    elif len(p) == 2:
        p[0] = DecVar(None, p[1], None, None, p.lineno(1), p.lexpos(0), False)

def p_referencia_ambito(p):
    '''
    referencia_ambito   : GLOBAL
                        | LOCAL
    '''
    p[0] = p[1]

def p_tipo(p):
    '''
    tipo    : None
            | Int64
            | Float64
            | Bool
            | Char
            | String
            | IDENTIFICADOR
    '''
    if p[1] == 'None':
        p[0] = TipoDato.NONE
    elif p[1] == 'Int64':
        p[0] = TipoDato.ENTERO
    elif p[1] == 'Float64':
        p[0] = TipoDato.DECIMAL
    elif p[1] == 'Bool':
        p[0] = TipoDato.BOOLEANO
    elif p[1] == 'Char':
        p[0] = TipoDato.CARACTER
    elif p[1] == 'String':
        p[0] = TipoDato.CADENA
    elif p[1] =='IDENTIFICADOR':
        p[0] = None


def  p_instruccion_if(p):
    '''
    instruccion_if  : if_simple END
                    | if_simple else END
                    | if_simple lista_else_if END
                    | if_simple lista_else_if else END

    '''
    if len(p) == 3:
        p[0] = IfCompleto(p[1], [], [], p.lineno(1), p.lexpos(0))
    elif len(p) == 4:
        if p.slice[2].type == 'else':
            p[0] = IfCompleto(p[1], [], p[2], p.lineno(1), p.lexpos(0))
        elif p.slice[2].type == 'lista_else_if':
            p[0] = IfCompleto(p[1], p[2], [], p.lineno(1), p.lexpos(0))
    elif len(p) == 5:
        p[0] = IfCompleto(p[1], p[2], p[3], p.lineno(1), p.lexpos(0))

def p_if_simple(p):
    '''
    if_simple   : IF expresion listaInstrucciones
                | IF expresion
    '''
    if len(p) == 4:
        p[0] = BloqueCondicional(p[2], p[3], p.lineno(1), p.lexpos(0))
    elif len(p) == 3:
        p[0] = BloqueCondicional(p[2], [], p.lineno(1), p.lexpos(0))

def p_else(p):
    '''
    else    : ELSE listaInstrucciones
            | ELSE
    '''
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 2:
        p[0] = []

def p_lista_else_if(p):
    '''
    lista_else_if   : lista_else_if else_if
                    | else_if
    '''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_else_if(p):
    '''
    else_if : ELSEIF expresion listaInstrucciones
            | ELSEIF expresion
    '''
    if len(p) == 4:
        p[0] = BloqueCondicional(p[2], p[3], p.lineno(1), p.lexpos(0))
    elif len(p) == 3:
        p[0] = BloqueCondicional(p[2], [], p.lineno(1), p.lexpos(0))

def p_while(p):
    '''
    while   : WHILE expresion listaInstrucciones END
    while   : WHILE expresion END
    '''
    if len(p) == 5:
        p[0] = While(p[2], p[3], p.lineno(1), p.lexpos(0))
    elif len(p) == 4:
        p[0] = While(p[2], [], p.lineno(1), p.lexpos(0))


def p_for(p):
    '''
    for : FOR IDENTIFICADOR IN expresion listaInstrucciones END
        | FOR IDENTIFICADOR IN expresion END
    '''
    if len(p) == 7:
        p[0] = For(p[2], p[4], p[5], p.lineno(1), p.lexpos(0))
    elif len(p) == 6:
        pass

def p_dec_funcion(p):
    '''
    dec_funcion : FUNCTION IDENTIFICADOR PARENTESIS_A listaParametros PARENTESIS_C listaInstrucciones END
                | FUNCTION IDENTIFICADOR PARENTESIS_A PARENTESIS_C listaInstrucciones END
                | FUNCTION IDENTIFICADOR PARENTESIS_A listaParametros PARENTESIS_C END
                | FUNCTION IDENTIFICADOR PARENTESIS_A PARENTESIS_C END
    '''
    if len(p) == 8:
        p[0] = DecFuncion(p[2], p[4], p[6], p.lineno(1), p.lexpos(0))
    elif len(p) == 7 and p.slice[4].type == 'PARENTESIS_C':
        p[0] = DecFuncion(p[2], [], p[5], p.lineno(1), p.lexpos(0))
    elif len(p) == 7:
        p[0] = DecFuncion(p[2], p[4], [], p.lineno(1), p.lexpos(0))
    elif len(p) == 6:
        p[0] = DecFuncion(p[2], [], [], p.lineno(1), p.lexpos(0))

def p_lista_parametros(p):
    '''
    listaParametros : listaParametros COMA parametro
                    | parametro
    '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = [p[1]]

def p_parametro(p):
    '''
    parametro   : IDENTIFICADOR DOBLE_DOS_PTS tipo
                | IDENTIFICADOR
    '''
    if len(p) == 4:
        p[0] = Parametro(p[1], p[3], p.lineno(1), p.lexpos(0))
    elif len(p) == 2:
        p[0] = Parametro(p[1], None, p.lineno(1), p.lexpos(0))

def p_llamda_funcion(p):
    '''
    llamda_funcion  : IDENTIFICADOR PARENTESIS_A listaExpresiones PARENTESIS_C
                    | IDENTIFICADOR PARENTESIS_A PARENTESIS_C
    '''
    if len(p) == 5:
        p[0] = LlamadaFuncStruct(p[1], p[3], p.lineno(1), p.lexpos(0))
    if len(p) == 4:
        p[0] = LlamadaFuncStruct(p[1], [], p.lineno(1), p.lexpos(0))

def p_declaracion_struct(p):
    '''
    declaracion_struct  : STRUCT IDENTIFICADOR lista_propiedades END
                        | MUTABLE STRUCT IDENTIFICADOR lista_propiedades END
    '''
    if len(p) == 5:
        p[0] = DecStruct(False, p[2], p[3], p.lineno(1), p.lexpos(0))
    elif len(p) == 6:
        p[0] = DecStruct(True, p[3], p[4], p.lineno(1), p.lexpos(0))


def p_lista_propiedades_struct(p):
    '''
    lista_propiedades   : lista_propiedades parametro PT_Y_COMA
                        | parametro PT_Y_COMA
    '''
    if len(p) == 4:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = [p[1]]

def p_propiedad_modificacion_struct(p):
    '''
    modificacion_struct : expresion PUNTO IDENTIFICADOR IGUAL expresion
    '''
    p[0] = ModificacionStruct(p[1], p[3], p[5], p.lineno(1), p.lexpos(0))

def p_acceso_propiead_struct(p):
    '''
    acceso_strcut   : expresion PUNTO IDENTIFICADOR
    '''
    p[0] = AccesosStruct(p[1], p[3], p.lineno(1), p.lexpos(0))

def p_funciones_nativas(p):
    '''
    funciones_nativas   : funciones_trigonometrica
                        | funcion_logaritmica
                        | funcion_sqrt
                        | funcion_parse
                        | funcion_trunc
                        | funcion_float
                        | funcion_string
                        | funcion_type_of
                        | funcion_push
                        | funcion_pop
                        | funcion_length
                        | funcion_upper_case
                        | funcion_lower_case
    '''
    p[0] = p[1]

def p_funcion_trigonometrica(p):
    '''
    funciones_trigonometrica    : SIN PARENTESIS_A expresion PARENTESIS_C
                                | COS PARENTESIS_A expresion PARENTESIS_C
                                | TAN PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = FuncTrigonometrica(p[1], p[3], p.lineno(1), p.lexpos(0))

def p_fucnion_logaritmica(p):
    '''
    funcion_logaritmica : LOG10 PARENTESIS_A listaExpresiones PARENTESIS_C
                        | LOG PARENTESIS_A listaExpresiones  PARENTESIS_C
    '''
    p[0] = FuncLogaritmica(p[1], p[3], p.lineno(1), p.lexpos(0))

def p_function_sqrt(p):
    '''
    funcion_sqrt    : SQRT PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = Sqrt(p[3], p.lineno(1), p.lexpos(0))

def p_function_parse(p):
    '''
    funcion_parse   : PARSE PARENTESIS_A tipo COMA expresion PARENTESIS_C
    '''
    p[0] = Parse(p[3], p[5], p.lineno(1), p.lexpos(0))

def p_function_trunc(p):
    '''
    funcion_trunc   : TRUNC PARENTESIS_A tipo COMA expresion PARENTESIS_C
    '''
    p[0] = Trunc(p[3], p[5], p.lineno(1), p.lexpos(0))

def p_function_float(p):
    '''
    funcion_float   : FLOAT PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = Float(p[3], p.lineno(1), p.lexpos(0))

def p_function_string(p):
    '''
    funcion_string   : STRING PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = FuncString(p[3], p.lineno(1), p.lexpos(0))

def p_function_type_of(p):
    '''
    funcion_type_of   : TYPEOF PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = TypeOf(p[3], p.lineno(1), p.lexpos(0))

def p_function_push(p):
    '''
    funcion_push   : PUSH ADMIRACION PARENTESIS_A expresion COMA expresion PARENTESIS_C
    '''
    p[0] = Push(p[4], p[6], p.lineno(1), p.lexpos(0))

def p_function_pop(p):
    '''
        funcion_pop   : POP ADMIRACION PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = Pop(p[4], p.lineno(1), p.lexpos(0))

def p_function_length(p):
    '''
        funcion_length   : LENGTH PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = Length(p[3], p.lineno(1), p.lexpos(0))

def p_function_upper_case(p):
    '''
        funcion_upper_case   : UPPERCASE PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = UpperCase(p[3], p.lineno(1), p.lexpos(0))

def p_function_lower_case(p):
    '''
        funcion_lower_case   : LOWERCASE PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = LowerCase(p[3], p.lineno(1), p.lexpos(0))


def p_error(p):
    if p:
        agregarError(Error(f"Accion sintactica con problemas", p.lineno, p.lexpos))
        print("Syntax error at '%s'" %p.value)
    else:
        print("Syntax error at EOF")




# ________________________________________________PARSE_METHOD________________________________________________
parser = yacc.yacc()

def armarCst(entrada):
    limpiarCst()
    listaIns = parser.parse(entrada)
    idPadre = uuid.uuid4()
    defNodoCst(idPadre, "LISTA_INS")
    for ins in listaIns:
        ins.generateCst(idPadre)
    return cst


def parse(entrada):
    limpiarTablaErrores()
    limpiarTablaSimbolos()

    listaIns = []
    listaIns = parser.parse(entrada)

    textoSalida  = ""
    ambitoGlobal = Ambito(None, "GLOBAL")
    for ins in listaIns:
        textoSalida += ins.ejecutar(ambitoGlobal).textoConsola
    textoSalida = getTablaErroresAsString() + textoSalida

    resCompilado = {
        "textoSalida": textoSalida,
        "tablaErrores": getTablaErroresAsJson(),
        "tablaSimbolos": getTablaSimbolosAsSerializable(),
    }

    return resCompilado
