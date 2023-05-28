from clasePersona import Persona

class GestorPersona:
    __lista_persona: list
    __persona: object
    def __init__(self):
        self.__lista_persona = []
    def cargar_persona(self):
        '''Carga las personas inscriptas'''
        dni = input("DNI >> ")
        while dni != '0':
            nombre = input("Nombre >> ")
            direccion = input("Direccion >> ")
            self.__persona = Persona(nombre,direccion,dni)
            self.__lista_persona.append(self.__persona)
            dni = input("DNI >> ")
        return self.__lista_persona
    def enviar_dni(self,aux):
        for fila in self.__lista_persona:
            if fila.get_dni() == aux:
                return fila
            else:
                print("Error inesperado :/")