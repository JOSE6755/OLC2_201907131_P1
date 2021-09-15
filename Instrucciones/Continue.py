from Abstract.instruccion import Instruccion

class contin(Instruccion):
    def __init__(self,fila,columna):
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        pass