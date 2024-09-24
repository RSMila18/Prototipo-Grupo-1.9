import tkinter as tk
from tkinter import ttk
from gestorAplicacion.solicitud import Solicitud

class HistorialSolicitudes:
    def __init__(self, master, cliente):
        self.cliente = cliente
        self.frame = tk.Frame(master)
        self.frame.pack(fill="both", expand=True)

        # Tabla para mostrar solicitudes
        self.tree = ttk.Treeview(self.frame, columns=("Evento", "Fecha", "Estado", "Descripción"), show="headings")
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

    def cargar_solicitudes(self):
        # Limpiar la tabla antes de cargar nuevas solicitudes
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Mostrar solicitudes basadas en el tipo cliente
        if self.cliente.nombre == "ADMIN":
            for solicitud in Solicitud.solicitudes_registradas:
                self.tree.insert("", "end", values=(
                    solicitud.nombre_evento,
                    solicitud.fecha_evento,
                    solicitud.estado,
                    solicitud.descripcion_evento
                ))
        else:
            for solicitud in Solicitud.solicitudes_registradas:
                if solicitud.cliente == self.cliente:
                    self.tree.insert("", "end", values=(
                        solicitud.nombre_evento,
                        solicitud.fecha_evento,
                        solicitud.estado,
                        solicitud.descripcion_evento
                    ))

