from claseInscripcion import Inscripcion
from gestor_persona import GestorPersona
from claseTallerCapacitacion import TallerCapacitacion
class GestorInscripcion:
    __lista_inscriptos: list
    __inscripto: object
    __gestor_persona: object
    __talleres: object
    def __init__(self):
        self.__lista_inscriptos = []
    def cargar_inscriptos(self):
        '''Carga los inscriptos'''
        self.__gestor_persona = GestorPersona()
        self.__talleres = TallerCapacitacion()
        fecha_inscripto = str(input("Fecha de inscripcion > >"))
        while fecha_inscripto != '0':
            pago = False
            listado = self.__gestor_persona.cargar_persona()
            self.__inscripto = Inscripcion(fecha_inscripto,pago)
            self.__lista_inscriptos.append(self.__inscripto)
            self.__lista_inscriptos.append(listado)
            fecha_inscripto = str(input("Fecha de inscripcion > >"))
        return self.__lista_inscriptos
    def mostrar_lista_inscriptos(self):
        '''Muestra la lista de inscriptos'''
        dni = input("Ingrese el DNI de la persona > > ")
        for fila in self.__lista_inscriptos:
            if fila.enviar_dni(dni):
                print(f"{fila.get_nombre()}  | Pago inscripcion > >{fila.get_monto_inscripciones()}")
            else:
                print("DNI no encontrado")
    def lista_inscriptos(self):
        '''Muestra la lista de inscriptos'''
        id_ = int(input("ID del taller > > "))
        for fila in self.__lista_inscriptos:
            if fila.get_idtaller == id_:
                print(f"{fila.get_nombre()}  | Pago inscripcion > >{fila.get_monto_inscripciones()}")
            else:
                print("Taller no encontrado")
    def registrar_pago(self):
        for fila in self.__lista_inscriptos:
            print(f"Pago a abonar >> {fila.get_monto_inscripciones()} |")
            monto = int(input("Ingrese monto >> "))
            if monto > 0:
                return True
    def guardar_inscripcion(self):
        valor_str = input("Guardar datos registrados 1 >> si | 0 >> no --> ")
        if valor_str == '1':
            print("Datos guardados")
        else:
            print("Ups Intente nuevamente")
