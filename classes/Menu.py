from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from classes.ListaEnlazadaDoble import ListaEnlazadaDoble
from classes.Elemento import Elemento

class Menu:

    elementosIngresados = ListaEnlazadaDoble()
    compuestosIngresados = ListaEnlazadaDoble()
    maquinasIngresadas = ListaEnlazadaDoble()

    def __init__(self) -> None:
        self.opciones=[
            ' Cargar un archivo XML de entrada',
            ' Generar archivo XML de salida',
            ' Gestión de elementos químicos',
            ' Gestión de compuestos',
            ' Gestión de máquinas',
            ' Ayuda',
            ' Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('              __________________________           ')
        print('             |        Proyecto 2        |          ')
        print('             |        Compuestos        |          ')
        print('             |--------------------------|          \n')

        i = 0

        for opcion in self.opciones:
            i = i + 1
            print("\t",i," - "+opcion)
        
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        self.ejecutarOpcion(opcion)


    def pausa(self):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False)

    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            filename = askopenfilename()
            objetoXml = minidom.parse(filename)
            self.procesarInformacion(objetoXml)
            self.pausa()
        elif(opcion=='2'):
            self.graficarMuestra(self.muestraAnalizada)
            self.pausa()
        elif(opcion=='3'):
            self.analizarMuestra()
            self.pausa()
        elif(opcion=='6'):
            espera = input('\n\tUSAC - S1\n\tProyecto 1\n\tDesarrollado por Kevin Girón-202010844...')
            self.pausa()  
        elif(opcion=='7'):
            quit()
        else:
            self.mostrar()
        

    def procesarInformacion(self, objetoXml):
        print('Procesando informacion...')

        numeroAtomico = objetoXml.getElementsByTagName('numeroAtomico')
        simbolos = objetoXml.getElementsByTagName('simbolo')
        nombreElemento = objetoXml.getElementsByTagName('nombreElemento')

        posicion=0
        for numeral in numeroAtomico:            
            numero = int(numeroAtomico[posicion].firstChild.data)
            simbolo = simbolos[posicion].firstChild.data
            nombre = nombreElemento[posicion].firstChild.data
            posicion=posicion+1
            nuevoElemento=Elemento(numero,simbolo,nombre)
            self.elementosIngresados.agregar(nuevoElemento)
            print('Elemento agregado: ',nuevoElemento.nombre)
            print('Numero atomico: ',nuevoElemento.numeroAtomico)
            print('Simbolo: ',nuevoElemento.simbolo)

        ordenar = input('Desea ordenar la lista? (s/n): ')
        if(ordenar=='s'):
            self.elementosIngresados.ordenar_por_numero_atomico()
            print('Lista ordenada')
            self.elementosIngresados.imprimirElementos()

        # for numero in numeroAtomico:
        #     bandera = False
        #     print('Numero atomico: ',numero.firstChild.data)
        #     for simbolo in simbolos:
        #         if bandera:
        #             continue
        #         print('Simbolo: ',simbolo.firstChild.data)                
        #         for nombre in nombreElemento:
        #             print('Nombre: ',nombre.firstChild.data)
        #             nuevoElemento=Elemento(numero.firstChild.data,simbolo.firstChild.data,nombre.firstChild.data)
        #             self.elementosIngresados.agregar(nuevoElemento)
        #             bandera=True
        #             continue
        
        
        