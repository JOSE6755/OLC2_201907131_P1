from Abstract.instruccion import Instruccion
from TS.Tipo import TIPO
from TS.Except import Excepcion
from TS.Simbolo import Simbolo
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Declarar import Declarar
from Instrucciones.Break import Brak

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
                    if isinstance(inst,Declarar):
                        inst.local=True
                    res=inst.interpretar(tree,nuevaT)
                    if isinstance(res,Excepcion):
                        tree.getExcepciones().append(res)
                        tree.updateConsola(res.toString())
                    if isinstance(res,Brak):return None
                izq=izq+1
                sim=Simbolo(str(self.var),self.opIzq.tipo,False,False,self.fila,self.columna,izq)
                res=foT.actualizarTabla(sim)
                if isinstance(res,Excepcion):return res
        elif self.cadena!=None:
            cad=self.cadena.interpretar(tree,table)
            if isinstance(cad,Excepcion):return cad
            if self.cadena.tipo==TIPO.CADENA:
                sim=Simbolo(str(self.var),self.cadena.tipo,False,False,self.fila,self.columna,"")
                tablita=TablaSimbolos(table)
                verifi=tablita.setTabla(sim)
                if isinstance(verifi,Excepcion):return verifi
                Ntab=TablaSimbolos(tablita)
                for carac in cad:
                    sim=Simbolo(str(self.var),self.cadena.tipo,False,False,self.fila,self.columna,carac)
                    res=Ntab.actualizarTabla(sim)
                    if isinstance(res,Excepcion):res
                    for inst in self.instrucciones:
                        resul=inst.interpretar(tree,Ntab)
                        if isinstance(resul,Excepcion):
                            tree.getExcepciones().append(resul)
                            tree.updateConsola(resul.toString())
                        