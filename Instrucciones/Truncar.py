from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
import math
class Truncar(Instruccion):
    def __init__(self,tipo,cadena,fila,columna):
        self.tipo=tipo
        self.cadena=cadena
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        val=self.cadena.interpretar(tree,table)
        if self.cadena.tipo==TIPO.DECIMAL:
            if self.tipo==TIPO.ENTERO:
                return math.trunc(val)
            
        else:return Excepcion("Semantico","La funcion parse es unicamente para String",self.fila,self.columna)
                