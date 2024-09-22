from gestorAplicacion.cliente import Cliente
from gestorAplicacion.Serializador import Serializador

class Solicitud:
    solicitudes_registradas = []
    archivo_solicitudes = "solicitudes.pkl"

    def __init__(self, cliente, nombre_evento, fecha_evento, descripcion_evento, estado="Pendiente"):
        self.cliente = cliente
        self.nombre_evento = nombre_evento
        self.fecha_evento = fecha_evento
        self.descripcion_evento = descripcion_evento
        self.estado = estado

    def registrar_solicitud(self):
        Solicitud.solicitudes_registradas.append(self)
        Solicitud.guardar_solicitudes()

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

    def mostrar_detalles(self):
        print(f"Detalles de la solicitud:\n- Responsable: {self.cliente.nombre}\n- Numero de documento: {self.cliente.documento}\n- Nombre del evento: {self.nombre_evento}\n- Fecha de realización: {self.fecha_evento}\n- Descripción del evento: {self.descripcion_evento}\n- Estado: {self.estado}")

# Cargar las solicitudes registradas al iniciar el programa
Solicitud.cargar_solicitudes()
