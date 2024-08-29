import os

class Material:
    def __init__(self, nombre, cantidad, fecha_uso):
        self.nombre = nombre
        self.cantidad = cantidad
        self.fecha_uso = fecha_uso

    def __str__(self):
        return f"{self.nombre}: {self.cantidad} unidades, fecha de uso: {self.fecha_uso}"

    def formatear_material(self):
        """Devuelve el material formateado para guardarlo en un archivo txt"""
        return f"{self.nombre}|{self.cantidad}|{self.fecha_uso}"

    @staticmethod
    def desde_formato(txt_linea):
        """Crea un objeto Material a partir de una línea de texto formateada"""
        nombre, cantidad, fecha_uso = txt_linea.strip().split('|')
        return Material(nombre, int(cantidad), fecha_uso)


class Inventario:
    def __init__(self):
        self.materiales = self.cargar_materiales_desde_archivo()

    def buscar_material(self, nombre):
        for material in self.materiales:
            if material.nombre == nombre:
                return material
        return None

    def ingresar_material(self, nombre, cantidad, fecha_uso):
        material = self.buscar_material(nombre)

        #Verifica si el material existe en la lista para modificarlos, si no, crea un nuevo material
        if material:
            material.cantidad += cantidad
            material.fecha_uso = fecha_uso
        else:
            nuevo_material = Material(nombre, cantidad, fecha_uso)
            self.materiales.append(nuevo_material)
        self.actualizar_estado()

    def ingresar_material_consola(self):
        nombre = input("Ingrese el nombre del material: ")
        cantidad = int(input("Ingrese la cantidad: "))
        fecha_uso = input("Ingrese la fecha de uso (YYYY-MM-DD): ")
        self.ingresar_material(nombre, cantidad, fecha_uso)

    def actualizar_estado(self):
        print("Estado del inventario actualizado.")
        self.guardar_inventario_en_archivo()
        self.notificar_cambio()

    def notificar_cambio(self):
        for material in self.materiales:
            if material.cantidad < 1:  # Umbral mínimo de ejemplo
                print(f"Notificación: {material.nombre} está por debajo del umbral mínimo ({material.cantidad} unidades disponibles).")

    def cargar_materiales_desde_archivo(self):
        ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'basesDatos', 'INVENTARIO.txt')
        materiales = []
        try:
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    material = Material.desde_formato(linea)
                    materiales.append(material)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Iniciando con un inventario vacío.")
        return materiales

    def guardar_inventario_en_archivo(self):
        ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'basesDatos', 'INVENTARIO.txt')
        with open(ruta_archivo, 'w') as archivo:
            for material in self.materiales:
                archivo.write(material.formatear_material() + '\n')

class MenuInventario:
    def __init__(self):
        self.inventario = Inventario()

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
