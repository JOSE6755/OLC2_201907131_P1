from TS.Except import Excepcion


class TablaSimbolos:
    def __init__(self, anterior=None):
        self.tabla = {}
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):
        if simbolo.id in self.tabla:
            return Excepcion("Semantico", "Variable "+simbolo.id+" ya definido", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id] = simbolo
            return None

    def getTabla(self, id):
        tablaActual = self
        while tablaActual != None:
            if id in tablaActual.tabla:
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla:
                tablaActual.tabla[simbolo.id].setValor(simbolo.getValor())
                tablaActual.tabla[simbolo.id].setTipo(simbolo.getTipo())
                return "Variable Actualizada"

            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable no encontrada ", simbolo.fila, simbolo.columna)

    def locales(self, id):
        tablaActual = self
        while tablaActual.anterior != None:
            if id in tablaActual.tabla:
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
        return None


def getTablasLocales(self, id):
    tablaActual = self
    while tablaActual.anterior != None:
        if id in tablaActual.tabla:
            return tablaActual.tabla[id]
        else:
            tablaActual = tablaActual.anterior
    return None


def actualizarGlobal(self, simbolo):
    tablaActual = self
    while tablaActual.anterior != None:
        tablaActual = tablaActual.anterior
    tablaActual.tabla[simbolo.identificador].setValor(simbolo.expresion.valor)
    return None
