from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO,OperadorAritmetico


class Aritmeticas(Instruccion):
    def __init__(self,opIzq,operador,opDer,fila,columna):
        self.opIzq=opIzq
        self.operador=operador
        self.opDer=opDer
        self.fila=fila
        self.columna=columna
        self.tipo=None
    
    def interpretar(self, tree, table):
        izq=self.opIzq.interpretar(tree,table)
        if isinstance(izq,Excepcion): return izq
        if self.opDer!=None:
            der=self.opDer.interpretar(tree,table)
            if isinstance(der,Excepcion): return der
        
        if self.operador==OperadorAritmetico.MAS:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return self.TipoVal(self.opIzq,izq)+self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)+self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)+self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)+self.TipoVal(self.opDer,der)
            return Excepcion("Semantico","Tipo Erroneo de operacion para +",self.fila,self.columna)
        elif self.operador==OperadorAritmetico.MENOS:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return self.TipoVal(self.opIzq,izq)-self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)-self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)-self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)-self.TipoVal(self.opDer,der)
            return Excepcion("Semantico","Tipo Erroneo de operacion para -",self.fila,self.columna)
        elif self.operador==OperadorAritmetico.POR:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return self.TipoVal(self.opIzq,izq)*self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)*self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)*self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)*self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.CADENA
                return self.TipoVal(self.opIzq,izq)+self.TipoVal(self.opDer,der)
        elif self.operador==OperadorAritmetico.DIV:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return self.TipoVal(self.opIzq,izq)/self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)/self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)/self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)/self.TipoVal(self.opDer,der)
        elif self.operador==OperadorAritmetico.POT:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return pow(self.TipoVal(self.opIzq,izq),self.TipoVal(self.opDer,der))
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return pow(self.TipoVal(self.opIzq,izq),self.TipoVal(self.opDer,der))
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return pow(self.TipoVal(self.opIzq,izq),self.TipoVal(self.opDer,der))
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return pow(self.TipoVal(self.opIzq,izq),self.TipoVal(self.opDer,der))
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.CADENA
                x=self.TipoVal(self.opDer,der)
                y=self.TipoVal(self.opIzq,izq)
                st=""
                for i in range(x):
                    st+=y
                return str(st)
        elif self.operador==OperadorAritmetico.MOD:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.ENTERO
                return self.TipoVal(self.opIzq,izq)%self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)%self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)%self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.DECIMAL
                return self.TipoVal(self.opIzq,izq)%self.TipoVal(self.opDer,der)
            
            
                
                
    def TipoVal(self,info,val):
        if info.tipo==TIPO.ENTERO:
            return int(val)
        elif info.tipo==TIPO.DECIMAL:
            return float(val)
        elif info.tipo==TIPO.BOOLEANO:
           return bool(val)
        elif info.tipo==TIPO.CADENA:
            return str(val)
        
        
        