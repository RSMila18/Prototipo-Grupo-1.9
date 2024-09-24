import tkinter as tk
from tkinter import messagebox
from funcionalidades.RegistroCliente import RegistroCliente
from funcionalidades.HistorialSolicitudes import HistorialSolicitudes
from funcionalidades.MonitoreoMateriales import MonitoreoMateriales  # Importar MonitoreoMateriales
from gestorAplicacion.cliente import Cliente
from gestorAplicacion.solicitud import Solicitud

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("650x400")
        self.usuario_actual = None  # Inicializa el usuario actual como None
        self.registro_cliente = RegistroCliente(self)  # Instancia la clase RegistroCliente y pasa self (MenuPrincipal)
        self.crear_menu()

    def crear_menu(self):
        self.limpiar_frame()
        self.label_opciones = tk.Label(self, text="Opciones", font=("Arial", 14))
        self.label_opciones.pack(pady=10)

        if self.usuario_actual is None:
            # Mostrar solo opciones de inicio de sesión y registro si no hay usuario actual
            tk.Button(self, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=5)
            tk.Button(self, text="Registrar Nuevo Usuario", command=self.mostrar_registro).pack(pady=5)
        else:
            if self.usuario_actual.usuario == "ADMIN":
                tk.Button(self, text="Ver Usuarios Registrados", command=self.ver_usuarios).pack(pady=5)
                tk.Button(self, text="Gestionar Solicitudes", command=self.gestionar_solicitudes).pack(pady=5)
                tk.Button(self, text="Monitoreo de Inventario", command=self.mostrar_monitoreo_inventario).pack(pady=5)  # Botón para el monitoreo de inventario
            else:  # Usuario regular
                tk.Button(self, text="Registrar Nueva Solicitud", command=self.mostrar_registro_solicitud).pack(pady=5)
                tk.Button(self, text="Ver Historial de Solicitudes", command=self.ver_historial).pack(pady=5)
            tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def mostrar_inicio_sesion(self):
        self.limpiar_frame()
        self.registro_cliente.mostrar_inicio_sesion()

    def mostrar_registro(self):
        self.limpiar_frame()
        self.registro_cliente.mostrar_registro()

    def mostrar_registro_solicitud(self):
        self.limpiar_frame()
        self.frame_solicitud = tk.Frame(self)
        self.frame_solicitud.pack()

        tk.Label(self.frame_solicitud, text="Registrar Solicitud", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_solicitud, text="Nombre del evento").grid(row=1, column=0)
        self.nombre_evento_entry = tk.Entry(self.frame_solicitud)
        self.nombre_evento_entry.grid(row=1, column=1)

        tk.Label(self.frame_solicitud, text="Fecha del evento (DD/MM/AAAA)").grid(row=2, column=0)
        self.fecha_evento_entry = tk.Entry(self.frame_solicitud)
        self.fecha_evento_entry.grid(row=2, column=1)

        tk.Label(self.frame_solicitud, text="Descripción del evento").grid(row=3, column=0)
        self.descripcion_evento_entry = tk.Entry(self.frame_solicitud)
        self.descripcion_evento_entry.grid(row=3, column=1)

        tk.Button(self.frame_solicitud, text="Enviar Solicitud", command=self.registrar_solicitud).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame_solicitud, text="Regresar", command=self.regresar_menu).grid(row=5, columnspan=2)

    def registrar_solicitud(self):
        nombre_evento = self.nombre_evento_entry.get()
        fecha_evento = self.fecha_evento_entry.get()
        descripcion_evento = self.descripcion_evento_entry.get()

        if nombre_evento and fecha_evento and descripcion_evento:
            cliente = self.usuario_actual  # Usuario actual logueado
            solicitud = Solicitud(cliente, nombre_evento, fecha_evento, descripcion_evento)
            solicitud.registrar_solicitud()

            messagebox.showinfo("Éxito", "Solicitud registrada con éxito.")
            self.regresar_menu()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def regresar_menu(self):
        self.crear_menu()

            
    def ver_historial(self):
        self.limpiar_frame()
        if self.usuario_actual:
            HistorialSolicitudes(self, self.usuario_actual)  # Llamada a la funcionalidad de historial
        else:
            messagebox.showerror("Error", "Debes iniciar sesión para ver el historial.")

    def ver_usuarios(self):
        self.limpiar_frame()
        # Aquí puedes agregar la lógica para ver los usuarios registrados

    def gestionar_solicitudes(self):
        self.limpiar_frame()
        # Aquí puedes agregar la lógica para gestionar solicitudes

    def mostrar_monitoreo_inventario(self):
        self.limpiar_frame()  # Limpiar cualquier otro frame visible
        monitoreo_frame = MonitoreoMateriales(self)  # Crear un frame con la interfaz de MonitoreoMateriales
        monitoreo_frame.pack()  # Empaquetar el frame dentro de la ventana principal

    def cerrar_sesion(self):
        self.usuario_actual = None
        messagebox.showinfo("Cierre de sesión", "Has cerrado sesión exitosamente.")
        self.regresar_menu()

    def regresar_menu(self):
        self.limpiar_frame()
        self.crear_menu()

    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
            
if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()
