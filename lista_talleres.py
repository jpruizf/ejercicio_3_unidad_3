from claseTallerCapacitacion import TallerCapacitacion
#import csv
class Arreglo_Talleres:
    __arre: list
    __talleres: object
    __sum:int
    def __init__(self):
        self.__arre = []
        self.__sum = 0
    def cargar_talleres(self):
        '''Carga de talleres'''
        #with open('talleres.csv','w',encoding='UTF-8') as archivo:
        #escritor = csv.writer(archivo, delimiter=';')
        #for fila in escritor:
        idtaller = int(input("Ingrese ID del taller >>"))
        while idtaller != 0:
            nombre = input("Ingrese el nombre del taller >>")
            vacantes = int(input("Ingrese las vacantes del taller ingresado >>"))
            montoincripcion = int(input("Ingrese el valor de la inscripcion del taller >>"))
            self.__sum += 1
            self.__talleres = TallerCapacitacion()
            
            self.__arre.append(self.new_method(idtaller, nombre, vacantes, montoincripcion))
            idtaller = int(input("Ingrese ID del taller >>"))
    def new_method(self, idtaller, nombre, vacantes, montoincripcion):
        return self.__talleres.guardar_talleres(idtaller,nombre,vacantes,montoincripcion)
            #archivo.write()
    def mostrar_talleres(self):
        '''Muestro tallers cargados'''
        self.__talleres = TallerCapacitacion()
        for fila in self.__arre:
            print(f"{fila.get_idtaller()} | {fila.get_nombre()} | {fila.get_vacante()} | {fila.get_monto_inscripciones()}")
        print(f"Total talleres > > {self.__sum}")