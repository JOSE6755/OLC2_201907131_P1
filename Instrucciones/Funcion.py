from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Declarar import Declarar
from Instrucciones.Break import Brak
from Instrucciones.Return import Return
class Funcion(Instruccion):
    def __init__(self,nombre,parametros,inst,fila,columna):
        self.nombre=nombre
        self.parametros=parametros
        self.inst=inst
        self.fila=fila
        self.columna=columna
        self.tipo=None
        
    def interpretar(self, tree, table):
        nuevaT=TablaSimbolos(table)
        for inst in self.inst:
            if isinstance(inst,Declarar):
                inst.local=True
            resul=inst.interpretar(tree,nuevaT)
            if isinstance(resul,Excepcion):return resul
            if isinstance(resul, Brak): 
                err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", inst.fila, inst.columna)
                tree.getExcepciones().append(err)
                tree.updateConsola(err.toString())
            if isinstance(resul,Return):
                self.tipo = resul.tipo
                return resul.res      
        
        return None