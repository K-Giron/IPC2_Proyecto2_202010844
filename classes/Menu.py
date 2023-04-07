from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from classes.ListaEnlazadaDoble import ListaEnlazadaDoble
from classes.Elemento import Elemento
from classes.Compuesto import Compuesto
from classes.Maquinas import Maquinas
from classes.Pin import Pin

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
            print('En construcción ...')
            self.pausa()
        elif(opcion=='3'):
            self.gestionElementos()
            self.pausa()
        elif(opcion=='4'):
            self.gestionCompuestos()
            self.pausa()
        elif(opcion=='5'):
            self.gestionMaquinas()
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
        #elementos
        posicion=0
        for numeral in numeroAtomico:
            
            numero = int(numeroAtomico[posicion].firstChild.data)
            simbolo = simbolos[posicion].firstChild.data
            nombre = nombreElemento[posicion].firstChild.data
            posicion=posicion+1


            # Verificar si el elemento ya está presente en la lista
            nodo_actual = self.elementosIngresados.primero
            encontrado = False

            while nodo_actual is not None:
                if nodo_actual.valor.numeroAtomico ==  numero or nodo_actual.valor.simbolo == simbolo or nodo_actual.valor.nombre == nombre:
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
            
            if not encontrado:
                nuevoElemento = Elemento(numero, simbolo, nombre)
                self.elementosIngresados.agregar(nuevoElemento)
                print('Elemento agregado: ', nuevoElemento.nombre)


            self.elementosIngresados.ordenar_por_numero_atomico()
        print('----------------------------------------------')

        compuestos = objetoXml.getElementsByTagName('compuesto')
        for compuesto in compuestos:
            nombreCompuesto = compuesto.getElementsByTagName('nombre')[0].firstChild.data
            print('Nombre compuesto: ',nombreCompuesto)

            # Verificar si el nombre del compuesto ya existe en la lista de compuestos ingresados
            nombreDiferente = True
            actual = self.compuestosIngresados.primero

            while actual != None:
                if actual.valor.nombre == nombreCompuesto:
                    nombreDiferente = False
                    break
                actual = actual.siguiente

            if nombreDiferente:
                elementos = compuesto.getElementsByTagName('elemento')
                compuestoss=Compuesto(nombreCompuesto)
                for elemento in elementos:
                    nuevosElementos = elemento.firstChild.data
                    print('Elemento: ',nuevosElementos)
                    compuestoss.listaElementos.agregar(nuevosElementos)
                print('-----------------------------------')
                self.compuestosIngresados.agregar(compuestoss)
            else:
                print('El compuesto ya existe en la lista de compuestos ingresados.')

        maquinas = objetoXml.getElementsByTagName('Maquina')

        for maquina in maquinas:
            nombreMaquina = maquina.getElementsByTagName('nombre')[0].firstChild.data
            print('Nombre maquina: ',nombreMaquina)
            # Verificar si el nombre de la maquina ya existe en la lista de compuestos ingresados
            nombreDiferente = True
            actual = self.maquinasIngresadas.primero

            while actual != None:
                if actual.valor.nombre == nombreMaquina:
                    nombreDiferente = False
                    break
                actual = actual.siguiente

            if nombreDiferente:
                numeroPines = int(maquina.getElementsByTagName('numeroPines')[0].firstChild.data)
                numeroElementos = int(maquina.getElementsByTagName('numeroElementos')[0].firstChild.data)
                nuevaMaquina=Maquinas(nombreMaquina,numeroPines,numeroElementos)
                pines=maquina.getElementsByTagName('pin')
                idPin=0
                for pin in pines:
                    elementos = pin.getElementsByTagName('elemento')
                    nuevoPin = Pin(idPin)
                    idPin=idPin+1
                    for elemento in elementos:
                        nuevoElemento = elemento.firstChild.data
                        nuevoPin.listaElementos.agregar(nuevoElemento)
                    nuevaMaquina.listaPines.agregar(nuevoPin)
                self.maquinasIngresadas.agregar(nuevaMaquina)
                print('-----------------------------------')
            else:
                print('La maquina ya existe en la lista de maquinas ingresadas.')
            
#-------------------------------------Gestion de elementos--------------------------------------------
    def gestionElementos(self):
        print('--------Gestion de elementos----------')

        print('1 - Ver listado de elementos')
        print('2 - Agregar elemento')
        opcion = input('Escribe tu opcion: ')
        print('--------------------------------------')

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
#-------------------------------------Gestion de compuestos--------------------------------------------
    def gestionCompuestos(self):
        print('--------Gestion de compuestos----------')

        print('1 - Ver listado de compuestos')
        print('2 - Analizar compuesto')
        print('3 - Regresar')
        opcion = input('Escribe tu opcion: ')
        print('--------------------------------------')

        if(opcion=='1'):
            self.compuestosIngresados.imprimirCompuestos()
        elif(opcion=='2'):
            print('En construcción karnal...')
        elif(opcion=='3'):
            self.mostrar(False)
        else:
            print('Opcion incorrecta!!')
            self.mostrar(False)
#-------------------------------------Gestion de maquinas--------------------------------------------
    def gestionMaquinas(self):
        print('--------Gestion de maquinas----------')

        print('1 - Ver listado de maquinas')
        print('2 - Regresar')
        opcion = input('Escribe tu opcion: ')
        print('--------------------------------------')

        if(opcion=='1'):
            self.maquinasIngresadas.imprimirMaquinas()
        elif(opcion=='2'):
            self.mostrar()
        else:
            print('Opcion incorrecta!!')
            self.mostrar(False)
