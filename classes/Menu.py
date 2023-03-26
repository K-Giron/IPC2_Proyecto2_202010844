from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom

class Menu:

    def __init__(self) -> None:
        self.opciones=[
            ' Abrir muestra',
            ' Cargar un archivo XML',
            ' Generar archivo XML',
            ' Gestión de elementos químicos',
            ' Acerca de',
            ' Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('         __________________________           ')
        print('        |        Proyecto 1        |          ')
        print('        |        Muestras          |          ')
        print('        |--------------------------|          \n')

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
        elif(opcion=='5'):
            espera = input('\n\tUSAC - S1\n\tProyecto 1\n\tDesarrollado por Kevin Girón-202010844...')
            self.pausa()  
        elif(opcion=='6'):
            quit()
        else:
            self.mostrar()
        