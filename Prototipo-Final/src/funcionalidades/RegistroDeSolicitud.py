import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.cliente import Cliente
from gestorAplicacion.solicitud import Solicitud


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Solicitud de Eventos")
        self.geometry("400x300")

        # Crear los widgets
        self.label_bienvenida = tk.Label(self, text="Bienvenido a la solicitud de eventos", font=("Arial", 14))
        self.label_bienvenida.pack(pady=20)

        self.btn_solicitud = tk.Button(self, text="Enviar nueva solicitud", command=self.enviar_solicitud)
        self.btn_solicitud.pack(pady=10)

        self.btn_salir = tk.Button(self, text="Salir", command=self.quit)
        self.btn_salir.pack(pady=10)

    def enviar_solicitud(self):
        # Ventana de entrada para los datos de la solicitud
        self.solicitud_window = SolicitudWindow(self)

class SolicitudWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Nueva Solicitud")
        self.geometry("400x400")

        # Campos de entrada para los datos del evento
        self.label_nombre_evento = tk.Label(self, text="Nombre del evento:")
        self.label_nombre_evento.pack(pady=5)
        self.entry_nombre_evento = tk.Entry(self)
        self.entry_nombre_evento.pack(pady=5)

        self.label_fecha_evento = tk.Label(self, text="Fecha del evento (DD/MM/AAAA):")
        self.label_fecha_evento.pack(pady=5)
        self.entry_fecha_evento = tk.Entry(self)
        self.entry_fecha_evento.pack(pady=5)

        self.label_descripcion_evento = tk.Label(self, text="Descripción del evento:")
        self.label_descripcion_evento.pack(pady=5)
        self.entry_descripcion_evento = tk.Entry(self)
        self.entry_descripcion_evento.pack(pady=5)

        self.btn_enviar = tk.Button(self, text="Enviar Solicitud", command=self.registrar_solicitud)
        self.btn_enviar.pack(pady=20)

    def registrar_solicitud(self):
        # Obtener los datos de entrada
        nombre_evento = self.entry_nombre_evento.get()
        fecha_evento = self.entry_fecha_evento.get()
        descripcion_evento = self.entry_descripcion_evento.get()

        if nombre_evento and fecha_evento and descripcion_evento:
            # Asumir que el primer cliente está logueado
            cliente = Cliente.usuarios_registrados[0]
            solicitud = Solicitud(cliente, nombre_evento, fecha_evento, descripcion_evento)
            solicitud.registrar_solicitud()

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Solicitud enviada con éxito.")
            solicitud.mostrar_detalles()
            self.destroy()  # Cerrar ventana de solicitud
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
