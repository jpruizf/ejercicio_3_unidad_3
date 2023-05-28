from gestor_Incripcion import GestorInscripcion
from lista_talleres import Arreglo_Talleres
#from gestor_persona import GestorPersona

def menu():
    gestor_inscripcion = GestorInscripcion()
    arreglo_talleres = Arreglo_Talleres()
    #gestor_persona = GestorPersona()
    print("1 > > Cargar talleres")
    print("2 > > Inscribir a una persona en algun taller")
    print("3 > > Consultar inscripcion")
    print("4 > > Consultar inscriptos")
    print("5 > > Registrar pago")
    print("6 > > Guardar incripciones")
    print("7 > > Finalizar operacion")
    opcion = input("Seleccion una de las opciones dadas >>> ")
    while opcion != 0:
        if opcion == '1':
            arreglo_talleres.cargar_talleres()
            arreglo_talleres.mostrar_talleres()
        elif opcion == '2':
            gestor_inscripcion.cargar_inscriptos()
        elif opcion == '3':
            gestor_inscripcion.mostrar_lista_inscriptos()
        elif opcion == '4':
            gestor_inscripcion.lista_inscriptos()
        elif opcion == '5':
            if gestor_inscripcion.registrar_pago():
                print("<< Pago Registrado >>")
        elif opcion == '6':
            gestor_inscripcion.guardar_inscripcion()
        elif opcion == '7':
            return 0
        print("1 > > Cargar talleres")
        print("2 > > Inscribir a una persona en algun taller")
        print("3 > > Consultar inscripcion")
        print("4 > > Consultar inscriptos")
        print("5 > > Registrar pago")
        print("6 > > Guardar incripciones")
        print("7 > > Finalizar operacion")
        opcion = input("Seleccion una de las opciones dadas >>> ")





if __name__ == '__main__':
    menu()
