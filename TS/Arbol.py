class Arbol:
    def __init__(self,instrucciones):
        self.instrucciones=instrucciones
        self.excepcions=[]
        self.funciones=[]
        self.consola=""
        self.TSglobal=None
        self.variablesGlobales =[]
        
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
    
    def getFunciones(self):
        return self.funciones
    def setFuncion(self,funcion):
        self.funciones.append(funcion)
    
    def getFuncion(self,nombre):
        for fun in self.funciones:
            if fun.nombre==nombre:
                return fun
        return None

    def getGlobal(self, nombre):
        for globales in self.variablesGlobales:
            if globales.id == nombre:
                return globales
        return None
    
    def addGlobal(self, globales):
        self.variablesGlobales.append(globales)