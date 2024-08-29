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
        fecha_uso = input("Ingrese la fecha de uso (DD/MM/YYYY): ")
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
        ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'basesDatos', 'INVENTARIO.TXT')
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
        ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'basesDatos', 'INVENTARIO.TXT')
        with open(ruta_archivo, 'w') as archivo:
            for material in self.materiales:
                archivo.write(material.formatear_material() + '\n')
