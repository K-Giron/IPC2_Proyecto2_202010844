from classes.Elemento import Elemento


class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar(self, valor):
        if self.primero is None:
            self.primero = self.ultimo = Nodo(valor)
        else:
            self.ultimo.siguiente = Nodo(valor)
            self.ultimo.siguiente.anterior = self.ultimo
            self.ultimo = self.ultimo.siguiente
        self.size += 1
# funciones para elementos---------------------------------------------------------------------------------
    def ordenar_por_numero_atomico(self):
        if self.size < 2:
            return
            
        actual = self.primero
        while actual.siguiente is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if actual.valor.numeroAtomico > siguiente.valor.numeroAtomico:
                    # intercambiar los valores de los nodos
                    temp = actual.valor
                    actual.valor = siguiente.valor
                    siguiente.valor = temp
                siguiente = siguiente.siguiente
            actual = actual.siguiente

    def imprimirElementos(self):
        actual = self.primero
        while actual is not None:
            print(actual.valor.numeroAtomico, actual.valor.simbolo, actual.valor.nombre)
            actual = actual.siguiente

#-------------------------------------------------------------------------------------------
    def listar(self):
        actual = self.primero
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
        self.anterior = None