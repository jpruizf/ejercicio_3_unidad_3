class TallerCapacitacion:
    '''Clase taller'''
    __id_taller: int
    __nombre: str
    __vacantes: int
    __monto_inscripcion: int
    def __init__(self):
        self.__id_taller = 0
        self.__nombre = ""
        self.__vacantes = 0
        self.__monto_inscripcion =0
    def guardar_talleres(self,id_taller,nombre,vacante,monto_inscripcion):
        self.__id_taller = id_taller
        self.__nombre = nombre
        self.__vacantes = vacante
        self.__monto_inscripcion = monto_inscripcion
    def get_idtaller(self):
        '''Retorna el id taller'''
        return self.__id_taller
    def get_nombre(self):
        '''Retorna el nombre del taller'''
        return self.__nombre
    def get_vacante(self):
        '''Retorna los puestos vacantes en el taller'''
        return self.__vacantes
    def get_monto_inscripciones(self):
        '''Retorna el monto correspondiete del taller'''
        return self.__monto_inscripcion