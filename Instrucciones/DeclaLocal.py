from TS.Except import Excepcion
from Abstract.instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO



class DeclaracionLocal(Instruccion):
    def __init__(self,id,fila,columna,tipo,expresion=None):
        self.id=id
        self.tipo=tipo
        self.expresion=expresion
        self.fila=fila
        self.columna=columna
        self.arreglo=False
        self.funcion = False


    def interpretar(self, tree, table):


     if self.expresion == None:
         value = None
         if isinstance(value, Excepcion): return value
         simbolo = Simbolo(str(self.id), TIPO.NULO, self.arreglo,self.funcion, self.fila, self.columna, None)
         result = table.setTabla(simbolo)
         if isinstance(result, Excepcion): 
             res = table.actualizarTabla(simbolo)
             if isinstance(res, Excepcion): return res
         return None
     else:
        value = self.expresion.interpretar(tree, table)  
        if isinstance(value, Excepcion): return value
        simbolo = Simbolo(str(self.id), self.expresion.tipo, self.arreglo,self.funcion, self.fila, self.columna, value)
        result = table.setTabla(simbolo)
        #tree.setSimbolo(simbolo)
        if isinstance(result, Excepcion): 
            res = table.actualizarTabla(simbolo)
            if isinstance(res,Excepcion): return res
        return None