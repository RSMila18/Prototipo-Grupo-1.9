from gestorAplicacion.cliente import Cliente
from gestorAplicacion.solicitud import Solicitud


def mostrar_menu():
    print("--------------- Bienvenido a la solicitud de eventos ---------------")
    print("1. Enviar una nueva solicitud")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
    

def enviar_solicitud():
   
    nombre_evento = input("Ingrese el nombre del evento: ")
    fecha_evento = input("Ingrese la fecha del evento (DD/MM/AAAA): ")
    descripcion_evento = input("Ingrese una breve descripción del evento: ")

    cliente = Cliente.usuarios_registrados[0]  # Aquí se asume que el primer cliente está logueado
    solicitud = Solicitud(cliente, nombre_evento, fecha_evento, descripcion_evento)
    solicitud.registrar_solicitud()

    print("\nSolicitud enviada con éxito.")
    solicitud.mostrar_detalles()



def registro_solicitudes_main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            enviar_solicitud()

        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == '__main__':
    registro_solicitudes_main()
