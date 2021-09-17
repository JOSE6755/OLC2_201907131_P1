from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
from math import log
class LOGN(Instruccion):
    def __init__(self,opizq,opder,fila,columna):
        self.opizq=opizq
        self.opder=opder
        self.fila=fila
        self.columna=columna
        self.tipo=None
        
    def interpretar(self, tree, table):
        val=self.opizq.interpretar(tree,table)
        val2=self.opder.interpretar(tree,table)
        if (self.opizq.tipo==TIPO.ENTERO or self.opizq.tipo==TIPO.DECIMAL) and (self.opder.tipo==TIPO.DECIMAL or self.opder.tipo==TIPO.ENTERO):
            self.tipo=TIPO.DECIMAL
            return log(val,val2)