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
        """Registra una nueva solicitud y la guarda."""
        Solicitud.solicitudes_registradas.append(self)
        Solicitud.guardar_solicitudes()

    @classmethod
    def guardar_solicitudes(cls):
        """Guarda todas las solicitudes registradas en un archivo."""
        Serializador.guardar_datos(cls.archivo_solicitudes, cls.solicitudes_registradas)

    @classmethod
    def cargar_solicitudes(cls):
        """Carga todas las solicitudes desde el archivo de serialización."""
        datos = Serializador.cargar_datos(cls.archivo_solicitudes)
        if isinstance(datos, list):
            cls.solicitudes_registradas = datos
            print(f"Se cargaron {len(cls.solicitudes_registradas)} solicitudes.")
        else:
            cls.solicitudes_registradas = []
            print("No se pudieron cargar las solicitudes, se inicializa una lista vacía.")

    def mostrar_detalles(self):
        """Devuelve los detalles de la solicitud en formato de texto."""
        return (f"Detalles de la solicitud:\n"
                f"- Responsable: {self.cliente.nombre}\n"
                f"- Número de documento: {self.cliente.documento}\n"
                f"- Nombre del evento: {self.nombre_evento}\n"
                f"- Fecha de realización: {self.fecha_evento}\n"
                f"- Descripción del evento: {self.descripcion_evento}\n"
                f"- Estado: {self.estado}")

# Ejemplo de cómo agregar una solicitud
if __name__ == "__main__":
    cliente_prueba = Cliente("NombreCliente", "123456789", "Cédula de Ciudadanía", "n/a", "cliente@correo.com", "123456789", "usuario", "password")
    solicitud_prueba = Solicitud(cliente_prueba, "Evento de Prueba", "2024-10-10", "Descripción del evento de prueba")
    solicitud_prueba.registrar_solicitud()
    Solicitud.cargar_solicitudes()
    for solicitud in Solicitud.solicitudes_registradas:
        print(solicitud.mostrar_detalles())

