from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
import math
class Float(Instruccion):
    def __init__(self,tipo,fila,columna):
        self.tipo=tipo
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        val=self.tipo.interpretar(tree,table)
        if self.tipo.tipo==TIPO.ENTERO:
            
                return float(val)
            
        else:return Excepcion("Semantico","La funcion parse es unicamente para String",self.fila,self.columna)
                