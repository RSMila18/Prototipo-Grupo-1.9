import ManejoInventario

class MenuInventario:
    def __init__(self):
        self.inventario = ManejoInventario.Inventario()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú de Gestión de Inventario ---")
            print("1. Ver inventario completo")
            print("2. Buscar material en el inventario")
            print("3. Ingresar material desde consola")
            print("4. Guardar inventario actualizado")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.ver_inventario_completo()
            elif opcion == '2':
                self.buscar_material()
            elif opcion == '3':
                self.ingresar_material_consola()
            elif opcion == '4':
                self.guardar_inventario()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida, por favor intente de nuevo.")

    def ver_inventario_completo(self):
        if not self.inventario.materiales:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for material in self.inventario.materiales:
                print(material)

    def buscar_material(self):
        nombre = input("Ingrese el nombre del material a buscar: ")
        material = self.inventario.buscar_material(nombre)
        if material:
            print(f"Material encontrado:\n{material}")
        else:
            print("Material no encontrado.")

    def ingresar_material_consola(self):
        self.inventario.ingresar_material_consola()

    def guardar_inventario(self):
        self.inventario.guardar_inventario_en_archivo()
        print("Inventario guardado exitosamente.")

