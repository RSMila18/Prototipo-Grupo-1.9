from gestorAplicacion.cliente import Cliente

def main():
    print("---------------Bienvenido!---------------\nPor favor inicie sesión o cree un nuevo usuario.\n1. Iniciar Sesión.\n2. Crear un nuevo usuario.")
    inicio = int(input("\nElija una opción (1/2): "))

    if inicio == 1:
        print("------------** Iniciar Sesión **------------\nPor favor ingrese su nombre de usuario y contraseña\n")
        usuario_input = input("Nombre de usuario: ")
        contrasena_input = input("Contraseña: ")

        usuario_encontrado = False
        for user in Cliente.usuarios_registrados:
            if user.usuario == usuario_input:
                if user.iniciar_sesion(usuario_input, contrasena_input):
                    print("\nInicio de sesión exitoso.")
                    usuario_encontrado = True
                else:
                    print("\nContraseña incorrecta.")
                break

        if not usuario_encontrado:
            print("\nUsuario no encontrado.")

    elif inicio == 2:
        while True:
            print("---------** Crear un nuevo usuario **---------\nPor favor diligencie sus datos\n")

            nombre = ""
            documento = ""
            representante_legal = ""

            print("Tipo de documento:")
            print("1. NIT")
            print("2. Cédula")
            tipo_documento_opcion = int(input("Seleccione el tipo de documento (1/2): "))

            if tipo_documento_opcion == 1:
                tipo_documento = "NIT"
                documento = input(f"Ingrese el número del NIT: ")
                nombre = input("Nombre de la entidad: ")
                representante_legal = input("Representante legal: ")

            elif tipo_documento_opcion == 2:
                tipo_documento = "CC"
                documento = input(f"Ingrese el número de CC: ")
                nombre = input("Nombre: ")
                representante_legal = "N/A"
            else:
                print("\nOpción no válida. Se asignará 'NIT' por defecto.")
                tipo_documento = "NIT"
                documento = input(f"Ingrese el número del NIT: ")
                nombre = input("Nombre de la entidad: ")
                representante_legal = input("Representante legal: ")

            correo = input("Correo electrónico: ")
            telefono = input("Teléfono: ")

            usuario = input("Nombre de usuario: ")
            contrasena = input("Contraseña: ")

            cliente = Cliente(nombre, tipo_documento, documento, representante_legal, correo, telefono, usuario, contrasena)
            cliente.registrar()

            # Proceso de inicio de sesión
            print("\n------------** Iniciar Sesión **------------")
            usuario_input = input("Nombre de usuario: ")
            contrasena_input = input("Contraseña: ")

            if cliente.iniciar_sesion(usuario_input, contrasena_input):
                print("\nInicio de sesión exitoso.")
                break  # Sale del bucle si el registro e inicio de sesión fueron exitosos

    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()

