from classes.ListaEnlazadaDoble import ListaEnlazadaDoble

class Maquinas:
    def __init__(self, nombre, pines,elementos):
        self.nombre = nombre
        self.pines = pines
        self.elementos = elementos
        self.listaPines= ListaEnlazadaDoble()