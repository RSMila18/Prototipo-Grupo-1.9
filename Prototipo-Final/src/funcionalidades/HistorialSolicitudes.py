import tkinter as tk
from tkinter import ttk, messagebox
from gestorAplicacion.solicitud import Solicitud
from gestorAplicacion.cliente import Cliente

class HistorialSolicitudes:
    def __init__(self, cliente):
        self.cliente = cliente
        self.root = tk.Tk()
        self.root.title("Historial de Solicitudes")

        # Tabla para mostrar solicitudes
        self.tree = ttk.Treeview(self.root, columns=("Evento", "Fecha", "Estado", "Descripción"), show="headings")
        self.tree.heading("Evento", text="Evento")
        self.tree.heading("Fecha", text="Fecha de Creación")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Evento", width=150)
        self.tree.column("Fecha", width=100)
        self.tree.column("Estado", width=100)
        self.tree.column("Descripción", width=250)

        self.tree.pack(fill="both", expand=True)

        # Cargar las solicitudes basadas en el tipo de cliente
        self.cargar_solicitudes()

        self.root.mainloop()

    def cargar_solicitudes(self):
        # Limpiar la tabla antes de cargar nuevas solicitudes
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Mostrar solicitudes basadas en el tipo de cliente
        if self.cliente.nombre == "ADMIN":
            # Si es ADMIN, muestra todas las solicitudes
            for solicitud in Solicitud.solicitudes_registradas:
                self.tree.insert("", "end", values=(
                    solicitud.nombre_evento,
                    solicitud.fecha_evento,
                    solicitud.estado,
                    solicitud.descripcion_evento
                ))
        else:
            # Si no es ADMIN, solo muestra las solicitudes del cliente
            for solicitud in Solicitud.solicitudes_registradas:
                if solicitud.cliente == self.cliente:
                    self.tree.insert("", "end", values=(
                        solicitud.nombre_evento,
                        solicitud.fecha_evento,
                        solicitud.estado,
                        solicitud.descripcion_evento
                    ))

# Prueba de la funcionalidad
if __name__ == "__main__":
    # Simulación de un cliente para probar la funcionalidad
    cliente_prueba = Cliente("Juan", "Cédula de Ciudadanía", "12345678", "N/A", "juan@correo.com", "5551234", "juan123", "contraseña123")
    HistorialSolicitudes(cliente_prueba)
