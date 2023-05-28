class Persona:
    __nombre: str
    __direccion: str
    __dni: str
    def __init__(self,nombre,direccion,dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni
    def get_nombre(self):
        '''Retorna nombre'''
        return self.__nombre
    def get_direccion(self):
        '''Retorna direccion'''
        return self.__direccion
    def get_dni(self):
        '''Retorna dni'''
        return self.__dni