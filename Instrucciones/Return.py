from Abstract.instruccion import Instruccion
from TS.Except import Excepcion

class Return(Instruccion):
    def __init__(self,expresion,fila,columna):
        self.expresion=expresion
        self.fila=fila
        self.columna=columna
        self.tipo=None
        self.res=None
        
    def interpretar(self, tree, table):
        res=self.expresion.interpretar(tree,table)
        if isinstance(res,Excepcion):return res
        self.tipo=self.expresion.tipo
        self.res=res
        
        return self