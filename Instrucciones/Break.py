from Abstract.instruccion import Instruccion

class Brak(Instruccion):
    def __init__(self,fila,columna):
        self.fila=fila
        self.columna=columna
    
    def interpretar(self, tree, table):
        return self