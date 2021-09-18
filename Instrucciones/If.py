from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Declarar import Declarar
from Instrucciones.Break import Brak
from Instrucciones.Return import Return

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
                    if isinstance(inst,Declarar):
                        inst.local=True
                    res = inst.interpretar(tree, nuevaT)
                    if isinstance(res, Excepcion):
                        tree.getExcepciones().append(res)
                        tree.updateConsola(res.toString())
                    if isinstance(res,Brak):return res
                    if isinstance(res,Return):return res
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
                                if isinstance(res,Brak):return res
                                if isinstance(res,Return):return res
                    if self.instelse != None:
                        for instr in self.instelse:
                            result = instr.interpretar(tree,table)
                            if isinstance(result,Excepcion): return result  
                    
                elif self.instelse != None:
                    for inst in self.instelse:
                        res = inst.interpretar(tree, table)
                        if isinstance(res, Excepcion):
                            return res
                        if isinstance(res,Brak):return res
                        if isinstance(res,Return):return res
        else:
            return Excepcion("Semantico", "Tipo d e dato no booleano en If.", self.fila, self.columna)
