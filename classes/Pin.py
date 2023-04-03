from ListaEnlazadaDoble import ListaEnlazadaDoble

class Pin:
    def __init__(self, id) -> None:
        self.id = id
        self.listaElementos = ListaEnlazadaDoble()