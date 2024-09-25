from funcionalidades.RegistroCliente import registro_cliente_main
from funcionalidades.RegistroSolicitudes import registro_solicitudes_main
from funcionalidades.Calendario import calendariomain

from funcionalidades.MenuInventario import MenuInventario

def opciones_admin():
    print("\nBienvenido, ADMIN.")
    print("1. Gestion inventario.")
    print("2. Calendario de Eventos.")

def opciones_usuario_normal():
    print("\n¿Que desea realizar?")
    print("1. Crear una nueva Solicitud.")
    print("2. Ver mi historial de solicitudes.")


if __name__ == "__main__":
    usuario_actual = registro_cliente_main()
    
    if usuario_actual!= None:

        if usuario_actual == "ADMIN":
            opciones_admin()
            admin_input=int(input("Por favor, ingrese una opción (1/2): "))
            if admin_input == 1:
                print("\nGestion inventario") #Aqui enlaza tus funcionalidad JUAN MANUEL
                inventario = MenuInventario()
                inventario.mostrar_menu()

            if admin_input == 2:
                print("\nCalendario de Eventos")
                calendariomain()
        else:
            opciones_usuario_normal()
            usuario_normal_input= int(input("Por favor, ingrese una opción (1/2): "))
            if usuario_normal_input == 1:
                print("\n") #Aqui enlaza tus funcionalidad MANUEL FERNANDO
                registro_solicitudes_main()
            if usuario_normal_input == 2:
                print("\nHistorial de solicitudes") #Aqui enlaza tus funcionalidad ALEXANDER
