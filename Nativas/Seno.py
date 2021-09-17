from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
from math import *
class SENO(Instruccion):
    def __init__(self,expresion,fila,columna):
        self.expresion=expresion
        self.fila=fila
        self.columna=columna
        self.tipo=None
        
    def interpretar(self, tree, table):
        val=self.expresion.interpretar(tree,table)
        if self.expresion.tipo==TIPO.ENTERO or self.expresion.tipo==TIPO.DECIMAL:
            self.tipo=TIPO.DECIMAL
            return sin(val)