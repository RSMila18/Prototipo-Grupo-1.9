from gestorAplicacion.Material import Material
from gestorAplicacion.Serializador import Serializador

class Evento:
    eventos_registrados = []
    archivo_eventos = "eventos.pkl"

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
        """Registra el evento y lo guarda en el archivo."""
        Evento.eventos_registrados.append(self)
        Evento.guardar_eventos()
        print(f"Evento '{self.nombre}' creado con fecha '{self.fecha}' y {len(self.materiales)} materiales.")

    @classmethod
    def guardar_eventos(cls):
        """Guarda todos los eventos registrados en un archivo."""
        Serializador.guardar_datos(cls.archivo_eventos, cls.eventos_registrados)

    @classmethod
    def cargar_eventos(cls):
        """Carga todos los eventos desde el archivo de serialización."""
        datos = Serializador.cargar_datos(cls.archivo_eventos)
        if isinstance(datos, list):
            cls.eventos_registrados = datos
            print(f"Se cargaron {len(cls.eventos_registrados)} eventos.")
        else:
            cls.eventos_registrados = []
            print("No se pudieron cargar los eventos, se inicializa una lista vacía.")

