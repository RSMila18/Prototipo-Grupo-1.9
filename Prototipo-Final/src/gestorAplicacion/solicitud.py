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
        if isinstance(datos, list):
            # Crear nuevas instancias de Solicitud
            cls.solicitudes_registradas = [Solicitud(**sol.__dict__) for sol in datos]
        else:
            cls.solicitudes_registradas = []
            print("No se pudieron cargar las solicitudes, se inicializa una lista vacía.")

    def mostrar_detalles(self):
        return (f"Detalles de la solicitud:\n- Responsable: {self.cliente.nombre}\n"
                f"- Número de documento: {self.cliente.documento}\n"
                f"- Nombre del evento: {self.nombre_evento}\n"
                f"- Fecha de realización: {self.fecha_evento}\n"
                f"- Descripción del evento: {self.descripcion_evento}\n"
                f"- Estado: {self.estado}")

    def obtener_descripcion(self):
        return self.descripcion_evento

# Cargar las solicitudes registradas al iniciar el programa
Solicitud.cargar_solicitudes()
