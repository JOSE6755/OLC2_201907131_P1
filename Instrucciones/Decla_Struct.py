from Abstract.instruccion import Instruccion
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO
from TS.Except import Excepcion

class Struct(Instruccion):
    def __init__(self,id,mutable, fila, columna,vari=None):
        self.id=id
        self.mutable=mutable
        self.fila=fila
        self.columna=columna
        self.vari=vari
    
    def interpretar(self, tree, table):
        if self.vari!=None:
            dicts={}
            for varis in self.vari:
                if varis.tipo!=None:
                    sim=Simbolo(str(""),varis.tipo,False,False,self.fila,self.columna,"nothing")
                dicts[str(varis.id)]=sim
            
            simbolo=Simbolo(str(self.id),TIPO.STRUCT,False,False,self.fila,self.columna,dicts,self.mutable)
            verifi=table.setTabla(simbolo)
            if isinstance(verifi,Excepcion):return verifi
        return None