from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
class Elseif(Instruccion):
    def __init__(self,expresion,inst,fila,columna):
        self.expresion=expresion
        self.inst=inst
        self.fila=fila
        self.columna=columna
    
    def interpretar(self, tree, table):
        con=self.expresion.interpretar(tree,table)
        if isinstance(con,Excepcion):return con
    
    def getInst(self):
        return self.inst