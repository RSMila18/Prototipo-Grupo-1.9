# Clase para representar una solicitud
class Solicitud:
    def __init__(self, nombre_evento, fecha, estado):
        self.nombre_evento = nombre_evento
        self.fecha = fecha
        self.estado = estado

    def __str__(self):
        return f"Evento: {self.nombre_evento}, Fecha: {self.fecha}, Estado: {self.estado}"

# Clase para representar al cliente y su historial de solicitudes
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial_solicitudes = []

    def agregar_solicitud(self, solicitud):
        self.historial_solicitudes.append(solicitud)

    def ver_historial(self):
        if not self.historial_solicitudes:
            print("No hay solicitudes en el historial.")
        else:
            for idx, solicitud in enumerate(self.historial_solicitudes):
                print(f"{idx+1}. {solicitud}")

    def ver_solicitud_detalle(self, indice):
        if 0 <= indice < len(self.historial_solicitudes):
            print(self.historial_solicitudes[indice])
        else:
            print("Índice de solicitud inválido.")

    def filtrar_solicitudes(self, fecha=None, estado=None):
        solicitudes_filtradas = [
            solicitud for solicitud in self.historial_solicitudes
            if (fecha is None or solicitud.fecha == fecha) and
               (estado is None or solicitud.estado == estado)
        ]

        if solicitudes_filtradas:
            for solicitud in solicitudes_filtradas:
                print(solicitud)
        else:
            print("No se encontraron solicitudes con los filtros aplicados.")

# Ejemplo de uso
cliente1 = Cliente("Juan Pérez")
cliente2 = Cliente("Juan Marcos")

# Agregar solicitudes al historial
cliente1.agregar_solicitud(Solicitud("Evento A", "2024-01-15", "Aprobada"))
cliente1.agregar_solicitud(Solicitud("Evento B", "2024-02-20", "Rechazada"))
cliente1.agregar_solicitud(Solicitud("Evento C", "2024-03-10", "Pendiente"))
cliente1.agregar_solicitud(Solicitud("Evento d", "2021-03-10", "Aprobada"))

# Ver historial de solicitudes
print("Historial de solicitudes:")
cliente1.ver_historial()

# Filtrar solicitudes por fecha
print("\nFiltrar solicitudes por fecha:")
cliente1.filtrar_solicitudes(fecha="2021-03-10")

# Filtrar solicitudes por estado
print("\nFiltrar solicitudes por estado:")
cliente1.filtrar_solicitudes(estado="Aprobada")
