from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
import math
class Strings(Instruccion):
    def __init__(self,cadena,fila,columna):
        self.cadena=cadena
        self.fila=fila
        self.columna=columna
        self.tipo=TIPO.CADENA
        
    def interpretar(self, tree, table):
        val=self.cadena.interpretar(tree,table)
        if self.cadena.tipo!=TIPO.STRUCT:
            
            return str(val)
            
        else:return Excepcion("Semantico","La funcion parse es unicamente para String",self.fila,self.columna)
                