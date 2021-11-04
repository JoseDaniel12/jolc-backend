import src.Analizador.ply.yacc as yacc
import src.Analizador.ply.lex as lex

from src.Optimizacion.Optimizador import *

from src.Optimizacion.Instrucciones.DecVar import *
from src.Optimizacion.Expresiones.OpAritmetica import *
from src.Tipos.TipoExpArtimetica import *
from src.Optimizacion.Expresiones.OpLogica import *
from src.Tipos.TipoExpLogica import *
from src.Optimizacion.Expresiones.OpRelacional import *
from src.Tipos.TipoExpRelacional import *
from src.Optimizacion.Expresiones.AtomicExp import *
from src.Optimizacion.Expresiones.Parseo import *
from src.Tipos.TipoDato import *
from src.Optimizacion.Expresiones.AccesoHeapStack import *

from src.Optimizacion.Instrucciones.Funcion import *
from src.Optimizacion.Instrucciones.Print import *
from src.Optimizacion.Instrucciones.Return import *
from src.Optimizacion.Instrucciones.LLamdaFuncion import *
from src.Optimizacion.Instrucciones.Goto import *
from src.Optimizacion.Instrucciones.Etiqueta import *
from src.Optimizacion.Instrucciones.If import *
from src.Optimizacion.Instrucciones.ModStackHeap import *

rw = {
    "package": "PACKAGE",
    "import": "IMPORT",
    "fmt": "FMT",
    "math": "MATH",
    "Mod": "MOD",
    "var": "VAR",
    "stack": "STACK",
    "heap": "HEAP",
    "func": "FUNC",
    "return": "RETURN",
    "if": "IF",
    "goto": "GOTO",
    "int": "INT",
    "float64":  "FLOAT64",
    "Printf": "PRINTF",

}


tokens = [
    'IDENTIFICADOR',
    'ENTERO',
    'DECIMAL',
    'CADENA',

    'MAS',
    'MENOS',
    'ASTERISCO',
    'SLASH',

    'PARENTESIS_A',
    'PARENTESIS_C',
    'CORCHETE_A',
    'CORCHETE_C',
    'LLAVE_A',
    'LLAVE_C',

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

    'PUNTO',
    'DOS_PTS',
    'PT_Y_COMA',
    'COMA',
] + list(rw.values())


# EXPRESIONES_REGULARES
t_MAS = r'\+'
t_MENOS = r'\-'
t_ASTERISCO = r'\*'
t_SLASH = r'\/'

t_OR = r'\|\|'
t_AND = r'\&\&'
t_ADMIRACION = r'\!'

t_MAYORIGUAL = r'\>\='
t_MAYORQUE = r'\>'
t_MENORIGUAL = r'\<\='
t_MENORQUE = r'\<'
t_IGUALIGUAL = r'\=='
t_IGUAL = r'\='
t_NOIGUAL = r'\!\='

t_PARENTESIS_A = r'\('
t_PARENTESIS_C = r'\)'
t_CORCHETE_A = r'\['
t_CORCHETE_C = r'\]'
t_PT_Y_COMA = r'\;'
t_LLAVE_A = r'\{'
t_LLAVE_C = r'\}'

t_PUNTO = r'\.'
t_DOS_PTS = r'\:'
t_COMA = r'\,'


# EXPRESIONES_REGUALRES_CON_ACCIONES
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIO_LINEA(t):
    r'//.*\n'

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

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in rw:
        t.type = rw[t.value]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t\r\f\v'
lexer_optimizacion = lex.lex()

# ________________________________________________PARSER________________________________________________

# PRECEDENCIAS
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'ADMIRACION'),
    ('left', 'IGUALIGUAL', 'NOIGUAL', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'SLASH', 'ASTERISCO'),
    ('right', 'UMENOS'),
    ('left', 'CORCHETE_A', 'CORCHETE_C'),
    ('left', 'PARENTESIS_A', 'PARENTESIS_C'),
    ('left', 'PUNTO'),
)


# GRAMATICA
def p_start(p):
    '''
    start   : PACKAGE IDENTIFICADOR IMPORT PARENTESIS_A lista_imports PARENTESIS_C declaraciones lista_funciones
    '''
    p[0] = Optimizador(p[5], p[7], p[8])


def p_lista_imports(p):
    '''
    lista_imports   : lista_imports CADENA
                    | CADENA
    '''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_declaraciones(p):
    '''
    declaraciones   : declaraciones declaracion
                    | declaracion
    '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_declaracion(p):
    '''
    declaracion : VAR STACK CORCHETE_A ENTERO CORCHETE_C FLOAT64 PT_Y_COMA
                | VAR HEAP CORCHETE_A ENTERO CORCHETE_C FLOAT64 PT_Y_COMA
                | VAR lista_ids FLOAT64 PT_Y_COMA
    '''
    if len(p) == 5:
        p[0] = p[2]
    else:
        p[0] = None


def p_lista_ids(p):
    '''
    lista_ids   : lista_ids COMA IDENTIFICADOR
                | IDENTIFICADOR
    '''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_lista_fucniones(p):
    '''
    lista_funciones    : lista_funciones funcion
                        | funcion
    '''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

# _____________________________________________ INSTRUCCIONES _____________________________________________

def p_funcion(p):
    '''
    funcion : FUNC IDENTIFICADOR PARENTESIS_A PARENTESIS_C LLAVE_A lista_instrucciones LLAVE_C
    '''
    p[0] = Funcion(p[2], p[6], p.lineno(1))


def p_lista_instrucciones(p):
    '''
    lista_instrucciones : lista_instrucciones instruccion
                        | instruccion
    '''
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = [p[1]]


def p_asignacion(p):
    '''
    instruccion : IDENTIFICADOR IGUAL expresion PT_Y_COMA
    '''
    p[0] = DecVar(p[1], p[3], p.lineno(1))


def p_modificacion_stack_stack(p):
    '''
    instruccion : STACK CORCHETE_A expresion CORCHETE_C IGUAL expresion PT_Y_COMA
                | HEAP CORCHETE_A expresion CORCHETE_C IGUAL expresion PT_Y_COMA
    '''
    p[0] = ModStackHeap(p[1], p[3], p[6], p.lineno(1))


def p_if(p):
    '''
    instruccion : IF PARENTESIS_A expresion PARENTESIS_C LLAVE_A GOTO IDENTIFICADOR PT_Y_COMA LLAVE_C
    '''
    p[0] = If(p[3], p[7], p.lineno(1))


def p_etiqueta(p):
    '''
    instruccion : IDENTIFICADOR DOS_PTS
    '''
    p[0] = Etiqueta(p[1],  p.lineno(1))


def p_goto(p):
    '''
    instruccion : GOTO IDENTIFICADOR PT_Y_COMA
    '''
    p[0] = Goto(p[2], p.lineno(1))


def p_llamada_funcion(p):
    '''
    instruccion : IDENTIFICADOR PARENTESIS_A PARENTESIS_C PT_Y_COMA
    '''
    p[0] = LlamadaFuncion(p[1], p.lineno(1))


def p_return(p):
    '''
    instruccion : RETURN PT_Y_COMA
    '''
    p[0] = Return(p.lineno(1))


def p_print(p):
    '''
    instruccion : FMT PUNTO PRINTF PARENTESIS_A CADENA COMA expresion PARENTESIS_C PT_Y_COMA
    '''
    p[0] = Print(p[5], p[7], p.lineno(1))


# _____________________________________________ EXPRESIONES _____________________________________________

def p_expresion_atomica(p):
    '''
    expresion   : IDENTIFICADOR
                | ENTERO
                | DECIMAL
    '''
    if p.slice[1].type == 'IDENTIFICADOR':
        p[0] = AtomiExp(p[1], TipoDato.IDENTIFICADOR, p.lineno(1))
    elif p.slice[1].type == 'ENTERO':
        p[0] = AtomiExp(p[1], TipoDato.ENTERO, p.lineno(1))
    elif p.slice[1].type == 'DECIMAL':
        p[0] = AtomiExp(p[1], TipoDato.DECIMAL, p.lineno(1))


def p_expresion_aritemetica(p):
    '''
    expresion   : expresion MAS expresion
                | expresion MENOS expresion
                | expresion ASTERISCO expresion
                | expresion SLASH expresion
                | MENOS expresion %prec UMENOS
    '''
    if p[2] == '+':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.SUMA, p.lineno(1))
    elif p[2] == '-':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.RESTA, p.lineno(1))
    elif p[2] == '*':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.MULTIPLICACION, p.lineno(1))
    elif p[2] == '/':
        p[0] = OpAritmetica(p[1], p[3], TipoExpAritmetica.DIVISION, p.lineno(1))
    else:
        p[0] = OpAritmetica(p[2], None, TipoExpAritmetica.UMENOS, p.lineno(1))


def p_modulo(p):
    '''
    expresion   : MATH PUNTO MOD PARENTESIS_A expresion COMA expresion PARENTESIS_C
    '''
    p[0] = OpAritmetica(p[5], p[7], TipoExpAritmetica.MODULO, p.lineno(1))


def p_expresion_logia(p):
    '''
    expresion   : expresion AND expresion
                | expresion OR expresion
                | ADMIRACION expresion
    '''
    if p.slice[2].type == 'AND':
        p[0] = OpLogica(p[1], p[3], TipoExpLogica.AND, p.lineno(1))
    elif p.slice[2].type == 'OR':
        p[0] = OpLogica(p[1], p[3], TipoExpLogica.OR, p.lineno(1))
    else:
        p[0] = OpLogica(p[1], None, TipoExpLogica.NOT, p.lineno(1))


def p_expresion_relacional(p):
    '''
    expresion   : expresion IGUALIGUAL expresion
                | expresion MENORIGUAL expresion
                | expresion MAYORIGUAL expresion
                | expresion MAYORQUE expresion
                | expresion MENORQUE expresion
                | expresion NOIGUAL expresion
    '''
    if p[2] == '==':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.IGUALIGUAL, p.lineno(1))
    elif p[2] == '<=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MENORIGUAL, p.lineno(1))
    elif p[2] == '>=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MAYORIGUAL, p.lineno(1))
    elif p[2] == '>':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MAYORQUE, p.lineno(1))
    elif p[2] == '<':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.MENORQUE, p.lineno(1))
    elif p[2] == '!=':
        p[0] = OpRelacional(p[1], p[3], TipoExpRelacional.NOIGUAL, p.lineno(1))


def p_parseo(p):
    '''
    expresion   : INT PARENTESIS_A expresion PARENTESIS_C
                | FLOAT64 PARENTESIS_A expresion PARENTESIS_C
    '''
    p[0] = Parseo(p[1], p[3], p.lineno(1))


def p_acceso_stack_heap(p):
    '''
    expresion   : STACK CORCHETE_A expresion CORCHETE_C
                | HEAP CORCHETE_A expresion CORCHETE_C
    '''
    p[0] = AccesoHeapStack(p[1], p[3], p.lineno(1))


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


# ________________________________________________PARSE_METHOD________________________________________________

parser_optimizacion = yacc.yacc()

def parseCode3d(entrada):
    optimizador = parser_optimizacion.parse(entrada, lexer = lexer_optimizacion)
    return optimizador