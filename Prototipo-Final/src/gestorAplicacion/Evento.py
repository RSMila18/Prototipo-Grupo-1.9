from Material import Material

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales = []

    def agregar_material(self, material):
        if isinstance(material, Material):
            self.materiales.append(material)
        else:
            raise TypeError("El elemento a agregar debe ser un objeto de tipo Material")

    def listar_materiales(self):
        for material in self.materiales:
            print(material)

    def monitorear_material(self, nombre_material):
        for material in self.materiales:
            if material.nombre == nombre_material:
                return material
        return None  # Si no se encuentra el material