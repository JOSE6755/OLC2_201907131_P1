from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from TS.Simbolo import Simbolo
from TS.Tipo import TIPO

class Llamar(Instruccion):
    def __init__(self,id,params,fila,columna):
        self.id = id
        self.params = params
        self.fila=fila
        self.columna=columna
        self.tipo=None
    def interpretar(self, tree, table):
        res=tree.getFuncion(self.id)
        bandera=True
        if res==None:
            struct=table.getTabla(str(self.id))
            if struct==None:
                return Excepcion("Semantico", " No se encontro la funcion." + self.id, self.fila, self.columna)
            else:
                bandera=False

        if bandera==True:
            nuevaT=TablaSimbolos(tree.getTSglobal())
            if len(res.parametros)==len(self.params):
                contador=0
                for param in self.params:
                    resul=param.interpretar(tree,table)
                    if isinstance(resul,Excepcion):return resul
                    if res.parametros[contador]['tipo']==param.tipo: 
                        sim = Simbolo(str(res.parametros[contador]['id']), res.parametros[contador]['tipo'], False,False, self.fila, self.columna, resul)
                        verifi=nuevaT.setTabla(sim)
                        if isinstance(verifi,Excepcion):return verifi
                    
                    else:return Excepcion("Semantico","Tipo de dato diferente en parametros",self.fila,self.columna)     
                    contador+=1
            else:return Excepcion("Semantico","Cantidad de parametros incorrecta",self.fila,self.columna)
        
            val=res.interpretar(tree,nuevaT)
            if isinstance(val,Excepcion):return val

        
            self.tipo=res.tipo
        
        
            return val
        else:
            struct=table.getTabla(str(self.id))
            dicts=struct.getValor()
            dictsaux={}
            lista=[]
            tipos=[]
            for params in self.params:
                result=params.interpretar(tree,table)
                if params.tipo!=None:
                    sim=Simbolo("",params.tipo,False,False,self.fila,self.columna,result)
                    tipos.append(params.tipo)
                lista.append(sim)
            self.tipo=TIPO.STRUCT
            for x in dicts:
                if dicts[x].getTipo!=None:
                    dictsaux[x]=lista[0]
                
                lista.pop(0)
                tipos.pop(0)
            if len(lista)!=0:
                pass
            aux={'datos':dictsaux,'mutable':struct.mutable}
            return aux
            
            
