from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Brak

class Whiless(Instruccion):
    def __init__(self,expresion,instr,fila,columna):
        self.expresion=expresion
        self.instr=instr
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        while True:
            cond=self.expresion.interpretar(tree,table)
            if isinstance(cond,Excepcion):return cond
            if self.expresion.tipo==TIPO.BOOLEANO:
                if cond==True:
                    nuevaT=TablaSimbolos(table)
                    for inst in self.instr:
                        res=inst.interpretar(tree,nuevaT)
                        if isinstance(res,Excepcion):
                            tree.getExcepciones().append(res)
                            tree.updateConsola(res.toString())
                        if isinstance(res,Brak):return None
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)
