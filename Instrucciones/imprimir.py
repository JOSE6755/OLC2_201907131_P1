from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO

class Imprimir(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table)  

        if isinstance(value, Excepcion):
            return value

        if self.expresion.tipo == TIPO.ARREGLO:
            return Excepcion("Semantico", "No se puede imprimir un arreglo completo", self.fila, self.columna)
        elif self.expresion.tipo == TIPO.NULO:
            return Excepcion("Semantico", "Null pointer, no se puede imprimir tipo NULL", self.fila, self.columna)
        tree.updateConsola(value)
        return None