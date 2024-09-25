from gestorAplicacion.Material import Material

class Evento:
    def __init__(self, nombre, fecha=None, materiales=None):
        self.nombre = nombre
        self.fecha = fecha if fecha is not None else "Sin fecha"
        self.materiales = materiales if materiales is not None else []

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

    def crear_evento(self):
        # Aquí puedes definir lo que quieras que el método haga cuando se cree el evento.
        print(f"Evento '{self.nombre}' creado con fecha '{self.fecha}' y {len(self.materiales)} materiales.")
        # Si necesitas serializarlo o realizar otras acciones, lo puedes hacer aquí.
