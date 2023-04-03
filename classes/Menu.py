from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from classes.ListaEnlazadaDoble import ListaEnlazadaDoble
from classes.Elemento import Elemento
from classes.Compuesto import Compuesto

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
            print('En construcción karnal...')
            self.pausa()
        elif(opcion=='3'):
            self.gestionElementos()
            self.pausa()
        elif(opcion=='4'):
            print('En construcción karnal...')
            self.pausa()
        elif(opcion=='5'):
            print('En construcción karnal...')
            self.pausa()
        elif(opcion=='6'):
            espera = input('\n\tUSAC - S1\n\tProyecto 2\n\tDesarrollado por Kevin Girón-202010844...')
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
            self.elementosIngresados.ordenar_por_numero_atomico()
            print('----------------------------------------------')

        compuestos = objetoXml.getElementsByTagName('compuesto')
        for compuesto in compuestos:
            nombreCompuesto = compuesto.getElementsByTagName('nombre')[0].firstChild.data
            print('Nombre compuesto: ',nombreCompuesto)
            elementos = compuesto.getElementsByTagName('elemento')
            compuestoss=Compuesto(nombreCompuesto)
            for elemento in elementos:
                nuevosElementos = elemento.firstChild.data
                print('Elemento: ',nuevosElementos)
                compuestoss.listaElementos.agregar(nuevosElementos)
            print('-----------------------------------')
            


    def gestionElementos(self):
        print('--------Gestion de elementos----------')

        print('1 - Ver listado de elementos')
        print('2 - Agregar elemento')
        opcion = input('Escribe tu opcion: ')

        if(opcion=='1'):
            self.elementosIngresados.imprimirElementos()
        elif(opcion=='2'):
            print('En construcción karnal...')
            self.agregarElemento()
        else:
            print('Opcion incorrecta!!')
        
        
    def agregarElemento(self):
        system("cls")
        ingresoNumeroAtomico = int(input('Ingrese el numero atomico: '))
        ingresoSimbolo = input('Ingrese el simbolo: ')
        ingresoNombre = input('Ingrese el nombre: ')

        actual = self.elementosIngresados.primero
        while actual != None:
            if(actual.valor.numeroAtomico==ingresoNumeroAtomico or actual.valor.simbolo==ingresoSimbolo or actual.valor.nombre==ingresoNombre):
                print('-------Ya existe un elemento con ese numero atomico, simbolo o nombre-------')
                return
            actual = actual.siguiente
        nuevoElemento=Elemento(ingresoNumeroAtomico,ingresoSimbolo,ingresoNombre)
        self.elementosIngresados.agregar_elemento_por_numero_atomico(nuevoElemento)
        print('Elemento agregado: ',nuevoElemento.nombre)
        print('Numero atomico: ',nuevoElemento.numeroAtomico)
        print('Simbolo: ',nuevoElemento.simbolo)
        self.elementosIngresados.imprimirElementos()
