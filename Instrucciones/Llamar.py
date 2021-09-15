from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.TablaSimbolos import TablaSimbolos

class Llamar(Instruccion):
    def __init__(self,id,params,fila,columna):
        self.id = id
        self.params = params
        self.fila=fila
        self.columna=columna
        self.tipo=None
    def interpretar(self, tree, table):
        res=tree.getFuncion(self.id)
        if res==None:
            return Excepcion("Semantico", " No se encontro la funcion." + self.id, self.fila, self.columna)
        val=res.interpretar(tree,table)
        if isinstance(val,Excepcion):return val
        
        self.tipo=res.tipo
        
        return val
