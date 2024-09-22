import tkinter as tk
from tkinter import messagebox
from funcionalidades.RegistroCliente import RegistroCliente
from funcionalidades.HistorialSolicitudes import HistorialSolicitudes

class MenuPrincipal(tk.Tk):
    def __init__(self, usuario_actual):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("300x200")

        self.usuario_actual = usuario_actual
        self.crear_menu()

    def crear_menu(self):
        # Si el usuario es ADMIN, mostrar las opciones de administración
        if self.usuario_actual.usuario == "ADMIN":
            tk.Label(self, text="Bienvenido ADMIN", font=("Arial", 14)).pack(pady=10)
            tk.Button(self, text="Gestión de Inventario", command=self.gestion_inventario).pack(pady=5)
            tk.Button(self, text="Calendario de Eventos", command=self.calendario_eventos).pack(pady=5)
        # Si es un usuario regular, mostrar las opciones de cliente
        else:
            tk.Label(self, text=f"Bienvenido {self.usuario_actual.nombre}", font=("Arial", 14)).pack(pady=10)
            tk.Button(self, text="Crear Nueva Solicitud", command=self.crear_solicitud).pack(pady=5)
            tk.Button(self, text="Ver Historial de Solicitudes", command=self.ver_historial).pack(pady=5)

    def gestion_inventario(self):
        messagebox.showinfo("Inventario", "Funcionalidad de gestión de inventario aún no implementada.")

    def calendario_eventos(self):
        messagebox.showinfo("Calendario", "Funcionalidad de calendario de eventos aún no implementada.")

    def crear_solicitud(self):
        messagebox.showinfo("Crear Solicitud", "Funcionalidad de creación de solicitudes aún no implementada.")

    def ver_historial(self):
        self.destroy()  # Cierra la ventana actual del menú principal
        HistorialSolicitudes(self.usuario_actual)  # Lanza la ventana del historial de solicitudes

def iniciar_aplicacion():
    # Iniciar el registro/login
    app_login = RegistroCliente()

    # Recuperar usuario logueado después de que la ventana se cierra
    usuario_actual = app_login.usuario_actual  # Cambiar a la propiedad
    if usuario_actual is not None:
        # Lanzar el menú principal
        app_menu = MenuPrincipal(usuario_actual)
        app_menu.mainloop()
    else:
        messagebox.showerror("Error", "No se pudo iniciar sesión.")

if __name__ == "__main__":
    iniciar_aplicacion()
