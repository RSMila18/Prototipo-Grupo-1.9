import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.solicitud import Solicitud  # Asegúrate de que esta importación sea correcta

class HistorialSolicitudes:
    def __init__(self, master, cliente):
        self.master = master  # Guardamos la referencia de la ventana principal
        self.cliente = cliente  # Guardamos el cliente actual
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.cargar_historial()
        self.boton_regresar = tk.Button(self.frame, text="Regresar", command=self.regresar)
        self.boton_regresar.pack(pady=10)

    def cargar_historial(self):
        solicitudes = [solicitud for solicitud in Solicitud.solicitudes_registradas if solicitud.cliente.documento == self.cliente.documento]
        
        if not solicitudes:
            messagebox.showinfo("Historial de Solicitudes", "No hay solicitudes registradas para este cliente.")
            return
        
        tk.Label(self.frame, text="Historial de Solicitudes", font=("Arial", 14)).pack(pady=10)

        for solicitud in solicitudes:
            tk.Label(self.frame, text=f"{solicitud.nombre_evento} - {solicitud.estado}").pack()

    def regresar(self):
        self.frame.destroy()  # Destruir el frame actual
        self.master.crear_menu()  # Regresar al menú principal


