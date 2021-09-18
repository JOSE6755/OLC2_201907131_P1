from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        #value = self.expresion.interpretar(tree, table)  
        texto=""
        for value in self.expresion:
            val=value.interpretar(tree,table)
            texto+=str(val)
            if isinstance(val,Excepcion):return val
            if value.tipo==TIPO.NULO:
                return Excepcion("Nulo","Valor nulo en una expresion",self.fila,self.columna)
        
        tree.updateConsola(texto)
        return None