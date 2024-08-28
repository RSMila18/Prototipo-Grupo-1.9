from gestorAplicacion.cliente import Cliente



def main():
    print("¡Bienvenido!\nPor favor inicie sesión ó cree un nuevo usuario.\n1. Iniciar Sesión.\n2.Crear un nuevo usuario.")
    inicio = int(input("Elija una opción (1/2): "))

    if inicio == 1:
        print("Usted selecciono ** Inicio de Sesión **\nPor favor ingrese su nombre de usuario y contraseña")
        usuario_input = input("Nombre de usuario: ")
        contrasena_input = input("Contraseña: ")

        cliente.iniciar_sesion(usuario_input, contrasena_input)
    
    elif inicio == 2:

        while True:
            print("Usted selecciono ** Crear un nuevo usuario **\nPor favor diligencie sus datos")

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
                representante_legal = ("N/A")
            else:
                print("Opción no válida. Se asignará 'NIT' por defecto.")
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
            print("\n** Inicio de Sesión **")
            usuario_input = input("Nombre de usuario: ")
            contrasena_input = input("Contraseña: ")

            cliente.iniciar_sesion(usuario_input, contrasena_input)
        
            if Cliente.es_usuario_unico(usuario):
                break  # Sale del bucle si el registro fue exitoso (usuario único)

    
    else:
        print("Opción invalida")


if __name__ == "__main__":
    main()