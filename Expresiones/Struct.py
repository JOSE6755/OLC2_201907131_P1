from typing import Dict
from Abstract.instruccion import Instruccion
from TS.Except import Excepcion



class AcceStruct(Instruccion):
    def __init__(self, identifi, fila, columna,claves):
        self.identifi = identifi
        self.fila = fila
        self.columna = columna
        self.tipo=None
        self.claves=claves

    def interpretar(self, tree, table):
        tablita = table.getTabla(self.identifi)

        if tablita == None:
            return Excepcion("Semantico", "Variable " + self.identifi + " no encontrada.", self.fila, self.columna)
        
        self.tipo=tablita.getTipo()
        dicts=tablita.getValor()
        valor=0
        for x in self.claves:
            try:
                if isinstance(x,Dict):
                    
                    valor=dicts[x]
                else:
                    valor=dicts[x].getValor()
                    self.tipo=dicts[x].getTipo()
            except:
                return Excepcion("Semantico","No se a podido acceder al dato solicitado",self.fila,self.columna)
        return valor
            
                
                