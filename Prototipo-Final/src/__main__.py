import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from funcionalidades.RegistroCliente import RegistroCliente
from funcionalidades.HistorialSolicitudes import HistorialSolicitudes
from funcionalidades.MonitoreoMateriales import MonitoreoMateriales  
from funcionalidades.GestionSolicitudes import GestionSolicitudes
from funcionalidades.ProveedoresGUI import ProveedoresGUI
from gestorAplicacion.cliente import Cliente
from gestorAplicacion.solicitud import Solicitud

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("650x400")
        self.usuario_actual = None  
        self.registro_cliente = RegistroCliente(self)  
        self.crear_menu()

    def crear_menu(self):
        self.limpiar_frame()
        self.label_opciones = tk.Label(self, text="Opciones", font=("Arial", 14))
        self.label_opciones.pack(pady=10)

        if self.usuario_actual is None:
            tk.Button(self, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=5)
            tk.Button(self, text="Registrar Nuevo Usuario", command=self.mostrar_registro).pack(pady=5)
        else:
            if self.usuario_actual.usuario == "ADMIN":
                tk.Button(self, text="Gestionar Solicitudes", command=self.gestionar_solicitudes).pack(pady=5)
                tk.Button(self, text="Ver Calendario de Eventos", command=self.ver_calendario).pack(pady=5)
                tk.Button(self, text="Gestionar Inventario", command=self.gestionar_inventario).pack(pady=5)
                tk.Button(self, text="Monitoreo de Inventario", command=self.mostrar_monitoreo_inventario).pack(pady=5)  
                tk.Button(self, text="Buscar Proveedores", command=self.busqueda_proveedores).pack(pady=5)
                tk.Button(self, text="Reportes de Estado", command=self.reportes_estado).pack(pady=5)
            else:  # Usuario estándar
                tk.Button(self, text="Registrar Nueva Solicitud", command=self.mostrar_registro_solicitud).pack(pady=5)
                tk.Button(self, text="Ver Historial de Solicitudes", command=self.ver_historial).pack(pady=5)
            tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def gestionar_solicitudes(self):
        self.limpiar_frame()
        GestionSolicitudes(self, self.usuario_actual, self.regresar_menu)  # Pasamos el callback

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
            # Validación de la fecha en formato DD/MM/AAAA
            try:
                # Intentamos convertir la fecha ingresada
                datetime.strptime(fecha_evento, "%d/%m/%Y")
            except ValueError:
                # Si la fecha es inválida, mostramos el error y permitimos corregir
                messagebox.showerror("Error", "Formato de la fecha incorrecto. Por favor, use DD/MM/AAAA.")
                return  # Salimos de la función para corregir

            # Si la fecha es válida, continuamos con el registro de la solicitud
            cliente = self.usuario_actual  # Usuario actual logueado
            solicitud = Solicitud(cliente, nombre_evento, fecha_evento, descripcion_evento)
            solicitud.registrar_solicitud()

            messagebox.showinfo("Éxito", "Solicitud registrada con éxito.")
            self.regresar_menu()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def ver_historial(self):
        self.limpiar_frame()
        if self.usuario_actual:
            HistorialSolicitudes(self, self.usuario_actual)
        else:
            messagebox.showerror("Error", "Debes iniciar sesión para ver el historial.")
    
    def ver_calendario(self):
        calendario_window = tk.Toplevel(self.master)
        calendario = CalendarioInteractivo(calendario_window)
        pass

    def gestionar_inventario(self):
        gestion_inventario = GestionInventario(self)
        gestion_inventario.mostrar_interfaz()
        pass

    def mostrar_monitoreo_inventario(self):
        self.limpiar_frame()  # Limpiar cualquier otro frame visible
        monitoreo_frame = MonitoreoMateriales(self, regresar_callback=self.regresar_menu)  # Pasamos el callback regresar_menu
        monitoreo_frame.pack()  # Empaquetar el frame dentro de la ventana principal

    def busqueda_proveedores(self):
        nueva_ventana = tk.Toplevel(self)
        ProveedoresGUI(nueva_ventana)
        pass

    def reportes_estado(self):
        # Implementar funcionalidad para generar reportes de estado
        pass

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.crear_menu()

    def regresar_menu(self):
        self.limpiar_frame()
        self.crear_menu()

    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MenuPrincipal()
    app.mainloop()

