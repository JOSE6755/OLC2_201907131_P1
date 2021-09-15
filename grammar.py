

from TS.Tipo import OperadorAritmetico,TIPO,OperadorRelacional
import re
import sys

from TS.Except import Excepcion

#--------------------------------------Lexico---------------------------------------------------------#

errores=[]
reservadas={
    'println':'RPRINTLN',
    'nothing':'RNOTHING',
    'Int64':'RINT',
    'Float64':'RFLOT',
    'Bool':'RBOOL',
    'Char':'RCHAR',
    'String':'RSTRING',
    'if':'RIF',
    'else':'RELSE',
    'elseif':'RELSEIF',
    'end':'REND',
    'while':'RWHILE',
    'for':'RFOR',
    'in':'RIN',
    'function':'RFUNCTION',
    'break':'RBREAK'
}

tokens=[
    'PARAB',
    'PARC',
    'PTCOMA',
    'CADENA',
    'CHAR',
    'ID',
    'IGUALAR',
    'ENTERO',
    'DECIMAL',
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'MOD',
    'POT',
    'UMENOS',
    'MAY',
    'MEN',
    'UNOT',
    'OR',
    'AND',
    'MAYOIGUAL',
    'MENOIGUAL',
    'IGUALES',
    'DIFERENTES',
    'DOSP',
    'DPUNTOS',
    'COMA'
    
]+list(reservadas.values())
t_PARAB=r'\('
t_PARC=r'\)'
t_PTCOMA=r';'
t_MAS=r'\+'
t_MENOS=r'\-'
t_POR=r'\*'
t_DIV=r'\/'
t_MOD=r'\%'
t_POT=r'\^'
t_MAY=r'\>'
t_MEN=r'\<'
t_MAYOIGUAL=r'\>\='
t_MENOIGUAL=r'\<\='
t_IGUALES=r'\=\='
t_DIFERENTES=r'\!\='
t_IGUALAR=r'\='
t_DOSP=r'::'
t_DPUNTOS=r':'
t_UNOT=r'!'
t_OR=r'\|\|'
t_AND=r'\&\&'
t_UMENOS=r'-'
t_COMA=r','


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_COMENTARIO_MULT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count('\n')

def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value,'ID')
     return t

def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_CHAR(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|[^\\\'\"])?\'"""
    t.value = t.value[1:-1]
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\\\', '\\')
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Excepcion("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

import ply.lex as lex
lexer = lex.lex()

#----------------------------------------------Sintactico----------------------------------------------#
from Expresiones.Aritmeticas import Aritmeticas
from Expresiones.Relaciones import Relacionales
from Expresiones.Primitivos import Primitivos
from Instrucciones.imprimir import Imprimir
from Expresiones.Identificador import Identificador
from Instrucciones.Declarar import Declarar
from Instrucciones.If import Rif
from Instrucciones.Elseif import Elseif
from Instrucciones.WhileS import Whiless
from Instrucciones.Fors import Fors
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamar import Llamar
from Instrucciones.Break import Brak

precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','MEN','MAY', 'IGUALES','DIFERENTES','MENOIGUAL','MAYOIGUAL'), 
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MOD'),
    ('nonassoc','POT'),
    ('right','UMENOS'),
    )

def p_init(t):
    'init       : instrucciones'
    t[0]=t[1]

def p_instrucciones_instruccion(t):
    'instrucciones  : instrucciones instruccion'
    
    if t[2]!="":
        t[1].append(t[2])
    t[0]=t[1]
def p_instrucciones(t):
    'instrucciones  : instruccion'
    if t[1]=="":
        t[0]=[]
    else:
        t[0]=[t[1]]

def p_instruccion(t):
    '''instruccion  : imprimirins fins
                    | DECLARACIONES fins
                    | if_instr fins
                    | while_instr fins
                    | for_inst fins
                    | funcion_dec fins
                    | llamar_fun fins
                    | BRAK fins
    
    '''
    t[0]=t[1]
def p_fins(t):
    'fins   : PTCOMA'
    t[0]=None
def p_instruccion_error(t):
    'instruccion        : error PTCOMA'
    errores.append(Excepcion("Sintactico","Error Sintactico." + str(t[1].value),t.lineno(1),find_column(input,t.slice[1])))
    t[0] = ""
    
def p_imprimirins(t):
    'imprimirins    : RPRINTLN PARAB expresion PARC'
    t[0]=Imprimir(t[3],t.lineno(1),find_column(input,t.slice[1]))
    
def p_if_instr(t):
    '''if_instr : RIF expresion instrucciones REND'''
    t[0]=Rif(t[2],t[3],None,None,t.lineno(1),find_column(input,t.slice[1]))
    
def p_else_instr(t):
    '''if_instr : RIF expresion instrucciones RELSE instrucciones REND'''
    t[0]=Rif(t[2],t[3],t[5],None,t.lineno(1),find_column(input,t.slice[1]))
def p_else_instr2(t):
    '''if_instr : RIF expresion instrucciones elifinst RELSE instrucciones REND'''
    t[0]=Rif(t[2],t[3],t[6],t[4],t.lineno(1),find_column(input,t.slice[1]))

def p_elifinst(t):
    'elifinst : elifinst elifinstru'
    if t[2]!="":
        t[1].append(t[2])
    t[0]=t[1]
    
def p_elifinst2(t):
    'elifinst : elifinstru'
    if t[1]=="":
        t[0]=[]
    else:
        t[0]=[t[1]]

def p_elifinstru(t):
    'elifinstru : RELSEIF expresion instrucciones'
    t[0]=Elseif(t[2],t[3],t.lineno(1),find_column(input,t.slice[1]))
    
def p_while(t):
    '''while_instr : RWHILE expresion instrucciones REND
    '''
    t[0] = Whiless(t[2],t[3],t.lineno(1),find_column(input,t.slice[1]))

def p_for_inst(t):
    'for_inst : RFOR ID RIN expresion DPUNTOS expresion instrucciones REND '
    t[0]=Fors(t[2],t[4],t[6],t[7],None,t.lineno(1),find_column(input,t.slice[1]))

def p_for_inst_2(t):
    'for_inst : RFOR ID RIN expresion instrucciones REND '
    t[0]=Fors(t[2],None,None,t[5],t[4],t.lineno(1),find_column(input,t.slice[1]))

def p_funcion_dec(t):
    'funcion_dec : RFUNCTION ID PARAB parametros PARC instrucciones REND'
    t[0]=Funcion(str(t[2]),t[4],t[6],t.lineno(1),find_column(input,t.slice[1]))
    
def p_funcion_dec2(t):
    'funcion_dec : RFUNCTION ID PARAB PARC instrucciones REND'
    t[0]=Funcion(str(t[2]),[],t[5],t.lineno(1),find_column(input,t.slice[1]))
def p_parametros(t):
    'parametros : parametros COMA parametro'
    t[1].append(t[3])
    t[0]=t[1]
    
def p_parametros2(t):
    'parametros : parametro'
    t[0]=[t[1]]
    
def p_parametro(t):
    'parametro : ID DOSP TIPOS'
    t[0]={"id":str(t[1]),"tipo":t[3]}
    
def p_llamar_fun(t):
    'llamar_fun : ID PARAB PARC '
    t[0]=Llamar(str(t[1]),[],t.lineno(1),find_column(input,t.slice[1]))
    

def p_DECLARACIONES(t):
    '''DECLARACIONES : DECLA_COM 
                     | DECLA_SIM   
                     '''
    t[0]=t[1]
def p_DECLA_SIM(t):
    'DECLA_SIM : ID IGUALAR expresion '
    t[0]=Declarar(str(t[1]),t[3],None,t.lineno(1),find_column(input,t.slice[1]))
def p_DECLA_COM(t):
    'DECLA_COM : ID IGUALAR expresion DOSP TIPOS '
    t[0]=Declarar(str(t[1]),t[3],t[5],t.lineno(1),find_column(input,t.slice[1]))
    
def p_TIPOS(t):
    '''TIPOS : RINT
             | RFLOT
             | RBOOL
             | RCHAR
             | RSTRING
             '''
    if t[1]=="Int64":
        t[0]=TIPO.ENTERO
    elif t[1]=="Float64":
        t[0]=TIPO.DECIMAL
    elif t[1]=="Bool":
        t[0]=TIPO.BOOLEANO
    elif t[1]=="Char":
        t[0]=TIPO.CARACTER
    elif t[1]=="String":
        t[0]=TIPO.CADENA

def p_expresion(t):
    '''expresion    : expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion POR expresion
                    | expresion DIV expresion
                    | expresion POT expresion
                    | expresion MOD expresion
                    | expresion MAY expresion
                    | expresion MEN expresion
                    | expresion MAYOIGUAL expresion
                    | expresion MENOIGUAL expresion
                    | expresion IGUALES expresion
                    | expresion DIFERENTES expresion
    '''
    if t[2]=="+":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.MAS,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="-":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.MENOS,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="*":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.POR,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="/":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.DIV,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="^":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.POT,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="%":
        t[0]=Aritmeticas(t[1],OperadorAritmetico.MOD,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]==">":
        t[0]=Relacionales(t[1],OperadorRelacional.MAYORQUE,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="<":
        t[0]=Relacionales(t[1],OperadorRelacional.MENORQUE,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]==">=":
        t[0]=Relacionales(t[1],OperadorRelacional.MAYORIGUAL,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="<=":
        t[0]=Relacionales(t[1],OperadorRelacional.MENORIGUAL,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="==":
        t[0]=Relacionales(t[1],OperadorRelacional.IGUALIGUAL,t[3],t.lineno(2),find_column(input, t.slice[2]))
    elif t[2]=="!=":
        t[0]=Relacionales(t[1],OperadorRelacional.DIFERENTE,t[3],t.lineno(2),find_column(input, t.slice[2]))




def p_expresion_agrup(t):
    '''expresion    : PARAB expresion PARC'''
    t[0]=t[2]

def p_expresion_ID(t):
    'expresion : ID'
    t[0]=Identificador(t[1],t.lineno(1),find_column(input,t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivos(TIPO.CADENA,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_caracter(t):
    '''expresion : CHAR'''
    t[0] = Primitivos(TIPO.CHARACTER,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_break(t):
    '''BRAK : RBREAK '''
    t[0] = Brak(t.lineno(1),find_column(input,t.slice[1]))
    
    
import ply.yacc as yacc
parser = yacc.yacc()
input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags= re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

f = open("./entrada.txt", "r")
entrada = f.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

instrucciones = parse(entrada)
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)

for error in errores:
    ast.getExcepciones().append(error)
    
for instruccion in ast.getInstrucciones():
    if isinstance(instruccion,Funcion):
        ast.setFuncion(instruccion)
    

for instruccion in ast.getInstrucciones():
    
    if not isinstance(instruccion,Funcion):
        value = instruccion.interpretar(ast,TSGlobal)

        if isinstance(value, Excepcion) :
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString())

print(ast.getConsola())       

    