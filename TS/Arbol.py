class Arbol:
    def __init__(self,instrucciones):
        self.instrucciones=instrucciones
        self.excepcions=[]
        self.consola=""
        self.TSglobal=None
        
    def getInstrucciones(self):
        return self.instrucciones
    
    def setInstrcciones(self,instrucciones):
        self.instrucciones=instrucciones
    
    def getExcepciones(self):
        return self.excepcions
    def setExcepciones(self,excepciones):
        self.excepcions=excepciones
    def getConsola(self):
        return self.consola
    def setConsola(self,consola):
        self.consola=consola
        
    def updateConsola(self,cadena):
        self.consola += str(cadena)+"\n"
        
    def getTSglobal(self):
        return self.TSglobal
    def setTSglobal(self,TSglobal):
        self.TSglobal=TSglobal