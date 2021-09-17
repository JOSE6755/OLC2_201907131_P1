
from typing import Dict
from TS.Except import Excepcion
from TS.Simbolo import Simbolo
from Abstract.instruccion import Instruccion
from TS.Tipo import TIPO



class Declarar(Instruccion):
    def __init__(self, id, expresion, tipo, fila, columna):
        self.id = id
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.local=False

    def interpretar(self, tree, table):
        valor = self.expresion.interpretar(tree, table)
        
        if isinstance(valor, Excepcion):
            return valor
        
        if isinstance(valor,Dict):
            simbolo=Simbolo(str(self.id),TIPO.STRUCT,False,False,self.fila,self.columna,valor['datos'],valor['mutable'])
            res=table.setTabla(simbolo)
            if isinstance(res,Excepcion):return res
        elif self.expresion.tipo == self.tipo:
            sim = Simbolo(str(self.id), self.tipo, False, False, self.fila, self.columna, valor)
            verifi = table.setTabla(sim)
            if isinstance(verifi, Excepcion):
                return verifi
        elif self.tipo == None:
            if self.local==True:
                sim = Simbolo(str(self.id), self.expresion.tipo, False,False, self.fila, self.columna, valor)
                res=table.locales(str(sim.id))
                if res!=None:
                    resu=table.actualizarTabla(sim)
                    if isinstance(resu,Excepcion):return resu
                else:
                    resu=table.setTabla(sim)
                    if isinstance(resu,Excepcion):return resu
                return None
            else:
                sim = Simbolo(str(self.id), self.expresion.tipo, False,False, self.fila, self.columna, valor)
                verifi=table.actualizarTabla(sim)
                if isinstance(verifi,Excepcion):
                    res=table.setTabla(sim)
                    if isinstance(res,Excepcion):
                        return res
        
            
        else:
            return Excepcion("Semantico", "Tipos no coinciden.", self.fila, self.columna)
