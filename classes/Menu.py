from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from ListaEnlazadaDoble import ListaEnlazadaDoble

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

        numeroPines = objetoXml.getElementsByTagName('numeroPines')
        numeroElementos = objetoXml.getElementsByTagName('numeroElementos')

        print('Numero de pines: ',numeroPines[0].firstChild.data)
        print('Numero de elementos: ',numeroElementos[0].firstChild.data)

        
        