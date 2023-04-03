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

    def agregar_elemento_por_numero_atomico(self, nuevo_elemento):
        if self.primero is None:  # si la lista está vacía, insertar el elemento como primero
            self.primero = Nodo(nuevo_elemento)
            self.ultimo = self.primero
            self.size += 1
            return
        
        # verificar si el elemento ya está en la lista
        actual = self.primero
        while actual is not None:
            if (nuevo_elemento.numeroAtomico == actual.valor.numeroAtomico or
                nuevo_elemento.nombre == actual.valor.nombre or
                nuevo_elemento.simbolo == actual.valor.simbolo):
                return  # el elemento ya está en la lista, no hacer nada
            actual = actual.siguiente

        # buscar la posición adecuada para insertar el nuevo elemento
        actual = self.primero
        while actual is not None:
            if nuevo_elemento.numeroAtomico < actual.valor.numeroAtomico:
                nuevo_nodo = Nodo(nuevo_elemento)
                nuevo_nodo.anterior = actual.anterior
                nuevo_nodo.siguiente = actual
                actual.anterior = nuevo_nodo
                if actual == self.primero:  # si se está insertando como primer elemento, actualizar el puntero al primero
                    self.primero = nuevo_nodo
                else:
                    nuevo_nodo.anterior.siguiente = nuevo_nodo
                self.size += 1
                return
            actual = actual.siguiente

        # si el nuevo elemento tiene un número atómico mayor que todos los elementos de la lista, insertarlo como último
        nuevo_nodo = Nodo(nuevo_elemento)
        nuevo_nodo.anterior = self.ultimo
        self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
        self.size += 1



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