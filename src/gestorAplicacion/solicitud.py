from gestorAplicacion.cliente import Cliente
from gestorAplicacion.Serializador import Serializador

class Solicitud:
    solicitudes_registradas = []
    archivo_solicitudes = "solicitudes.pkl"

    def __init__(self, cliente, nombre_evento, fecha_evento, descripcion_evento):
        self.cliente = cliente
        self.nombre_evento = nombre_evento
        self.fecha_evento = fecha_evento
        self.descripcion_evento = descripcion_evento

    def registrar_solicitud(self):
        Solicitud.solicitudes_registradas.append(self)
        Solicitud.guardar_solicitudes()
        print(f"Solicitud para el evento '{self.nombre_evento}' registrada correctamente.")

    @classmethod
    def guardar_solicitudes(cls):
        Serializador.guardar_datos(cls.archivo_solicitudes, cls.solicitudes_registradas)

    @classmethod
    def cargar_solicitudes(cls):
        datos = Serializador.cargar_datos(cls.archivo_solicitudes)
        if isinstance(datos, list) and all(isinstance(solicitud, Solicitud) for solicitud in datos):
            cls.solicitudes_registradas = datos
        else:
            cls.solicitudes_registradas = []
            print("Datos de solicitudes cargados no válidos, se inicializa una lista vacía.")

    def mostrar_detalles(self):
        print(f"Detalles de la solicitud:\n- Responsable: {self.cliente.nombre}\n- Numero de documento: {self.cliente.documento}\n- Nombre del evento: {self.nombre_evento}\n- Fecha de realización: {self.fecha_evento}\n- Descripción del evento: {self.descripcion_evento}")

# Cargar las solicitudes registradas al iniciar el programa
Solicitud.cargar_solicitudes()
