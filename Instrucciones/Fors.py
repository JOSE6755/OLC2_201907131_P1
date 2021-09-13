from Abstract.instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Except import Excepcion
from TS.Simbolo import Simbolo
from TS.TablaSimbolos import TablaSimbolos

class Fors(Instruccion):
    def __init__(self,var,opIzq,opDer,instrucciones,cadena,fila,columna):
        self.var=var
        self.opIzq=opIzq
        self.opDer=opDer
        self.instrucciones=instrucciones
        self.cadena=cadena
        self.fila=fila
        self.columna=columna
        
    def interpretar(self, tree, table):
        if self.opIzq!=None and self.opDer!=None:
            izq=self.opIzq.interpretar(tree, table)
            if isinstance(izq,Excepcion):return izq
            der=self.opDer.interpretar(tree, table)
            if isinstance(der,Excepcion):return der
            sim=Simbolo(str(self.var),self.opIzq.tipo,False,False,self.fila,self.columna,izq)
            foT=TablaSimbolos(table)
            verifi=foT.setTabla(sim)
            if isinstance(verifi,Excepcion):return verifi
            nuevaT=TablaSimbolos(foT)
            while izq<=der:
                for inst in self.instrucciones:
                    res=inst.interpretar(tree,table)
                    if isinstance(res,Excepcion):
                        tree.getExcepciones().append(res)
                        tree.updateConsola(res.toString())
                    izq=izq+1
                    sim=Simbolo(str(self.var),self.opIzq.tipo,False,False,self.fila,self.columna,izq)
                    res=nuevaT.actualizarTabla(sim)
                    if isinstance(res,Excepcion):return res