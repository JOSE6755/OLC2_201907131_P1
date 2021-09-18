from Abstract.instruccion import Instruccion
from TS.Except import Excepcion
from TS.Tipo import TIPO,OperadorRelacional
class Relacionales(Instruccion):
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
        
        if self.operador==OperadorRelacional.MAYORQUE:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
        elif self.operador==OperadorRelacional.MENORQUE:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)and self.TipoVal(self.opDer,der)
        elif self.operador==OperadorRelacional.MAYORIGUAL:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)>=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq) and self.TipoVal(self.opDer,der)
        elif self.operador==OperadorRelacional.MENORIGUAL:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)<=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq) and self.TipoVal(self.opDer,der)
        elif self.operador==OperadorRelacional.IGUALIGUAL:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)==self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)==self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)==self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)==self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)==self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq) and self.TipoVal(self.opDer,der)
        elif self.operador==OperadorRelacional.DIFERENTE:
            if self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.ENTERO and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.ENTERO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.DECIMAL and self.opDer.tipo==TIPO.DECIMAL:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.CADENA and self.opDer.tipo==TIPO.CADENA:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
            elif self.opIzq.tipo==TIPO.BOOLEANO and self.opDer.tipo==TIPO.BOOLEANO:
                self.tipo=TIPO.BOOLEANO
                return self.TipoVal(self.opIzq,izq)!=self.TipoVal(self.opDer,der)
    
    def TipoVal(self,info,val):
        if info.tipo==TIPO.ENTERO:
            return int(val)
        elif info.tipo==TIPO.DECIMAL:
            return float(val)
        elif info.tipo==TIPO.CADENA:
            return str(val)
        elif info.tipo==TIPO.BOOLEANO:
            return bool(val)
            