from Abstract.instruccion import Instruccion
from TS.Except import Excepcion


class Identificador(Instruccion):
    def __init__(self, identifi, fila, columna):
        self.identifi = identifi
        self.fila = fila
        self.columna = columna
        self.tipo=None

    def interpretar(self, tree, table):
        tablita = table.getTabla(self.identifi)

        if tablita == None:
            return Excepcion("Semantico", "Variable " + self.identifi + " no encontrada.", self.fila, self.columna)
        
        self.tipo=tablita.getTipo()
        
        return tablita.getValor()
