def mostrar_menu():
    print("----- Bienvenido a la solicitud de eventos -----")
    print("1. Enviar una nueva solicitud")
    print("2. Historial de solicitudes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion
    

def enviar_solicitud():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    carnet = input("Ingrese su numero de identificación")
    nombre_evento = input("Ingrese el nombre del evento: ")
    fecha_evento = input("Ingrese la fecha del evento (DD/MM/AAAA): ")
    descripcion_evento = input("Ingrese una breve descripción del evento: ")

    # Aquí podrías agregar lógica para almacenar la información en una base de datos o archivo
    print("\nSolicitud enviada con éxito.")
    print(f"Detalles de la solicitud:\n- Responsable: {nombre, apellido}\n- Numero de documento: {carnet}\n- Nombre del evento: {nombre_evento}\n- Fechad de realización: {fecha_evento}\n- Descripción del evento: {descripcion_evento}")




def main():
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            enviar_solicitud()

        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == '__main__':
    main()
