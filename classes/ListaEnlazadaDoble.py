class ListaEnlazadaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamaño += 1

    def eliminar_nodo(self, valor):
        actual = self.cabeza
        while actual is not None:
            if actual.valor == valor:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def iterar_lista(self):
        actual = self.cabeza
        while actual is not None:
            valor = actual.valor
            actual = actual.siguiente
            yield valor

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
        self.anterior = None