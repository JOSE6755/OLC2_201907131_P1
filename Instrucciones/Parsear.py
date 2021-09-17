from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO

class Parsear(Instruccion):
    def __init__(self,tipo,cadena,fila,columna):
        self.tipo=tipo
        self.cadena=cadena
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        val=self.cadena.interpretar(tree,table)
        if self.cadena.tipo==TIPO.CADENA:
            if self.tipo==TIPO.ENTERO:
                return int(val)
            elif self.tipo==TIPO.DECIMAL:
                return float(val)
            else:return Excepcion("Semantico","Tipo de dato a convertir incorrecto",self.fila,self.columna)
        else:return Excepcion("Semantico","La funcion parse es unicamente para String",self.fila,self.columna)
                