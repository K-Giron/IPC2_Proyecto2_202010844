from classes.ListaEnlazadaDoble import ListaEnlazadaDoble

class Compuesto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listaElementos = ListaEnlazadaDoble()