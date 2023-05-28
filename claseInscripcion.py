
class Inscripcion:
    __fecha_inscripcion: str
    __pago: bool
    def __init__(self,fecha_inscripcion,pago):
        self.__fecha_inscripcion = fecha_inscripcion
        self.__pago = pago
    def get_fecha_inscripcion(self):
        ''''Retorna fecha de inscripcion'''
        return self.__fecha_inscripcion
    def get_pago(self):
        '''Retorna el pago'''
        return self.__pago