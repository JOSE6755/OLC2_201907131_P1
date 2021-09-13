from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos


class Rif(Instruccion):
    def __init__(self, expresion, instif, instelse, instelseif, fila, columna):
        self.expresion = expresion
        self.instif = instif
        self.instelse = instelse
        self.instelseif = instelseif
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        cond = self.expresion.interpretar(tree, table)
        if isinstance(cond, Excepcion):
            return cond

        if self.expresion.tipo == TIPO.BOOLEANO:
            if bool(cond):
                nuevaT = TablaSimbolos(table)
                for inst in self.instif:
                    res = inst.interpretar(tree, nuevaT)
                    if isinstance(res, Excepcion):
                        tree.getExcepciones().append(res)
                        tree.updateConsola(res.toString())
            else:
                if self.instelseif != None:
                    for inst in self.instelseif:
                        cond = inst.expresion.interpretar(tree, table)
                        if cond == True:
                            for ellif in inst.getInst():
                                res = ellif.interpretar(tree, table)
                                if isinstance(res, Excepcion):
                                    tree.getExcepciones().append(res)
                                    tree.updateConsola(res.toString())
                    
                elif self.instelse != None:
                    for inst in self.instelse:
                        res = inst.interpretar(tree, table)
                        if isinstance(res, Excepcion):
                            return res
        else:
            return Excepcion("Semantico", "Tipo d e dato no booleano en If.", self.fila, self.columna)