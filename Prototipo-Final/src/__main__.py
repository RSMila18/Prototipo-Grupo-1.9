import tkinter as tk
from tkinter import messagebox
from funcionalidades.RegistroCliente import RegistroCliente
from funcionalidades.HistorialSolicitudes import HistorialSolicitudes

class MenuPrincipal(tk.Tk):
    def __init__(self, usuario_actual):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("800x600")  # Ventana más grande

        self.usuario_actual = usuario_actual
        self.frame_principal = tk.Frame(self)
        self.frame_principal.pack(fill="both", expand=True)

        # Crear la barra de menú
        self.crear_menu()

        # Mostrar bienvenida
        self.mostrar_bienvenida()

    def crear_menu(self):
        self.menu_bar = tk.Menu(self)

        # Opciones para ADMIN
        if self.usuario_actual.usuario == "ADMIN":
            admin_menu = tk.Menu(self.menu_bar, tearoff=0)
            admin_menu.add_command(label="Gestión de Inventario", command=self.gestion_inventario)
            admin_menu.add_command(label="Calendario de Eventos", command=self.calendario_eventos)
            self.menu_bar.add_cascade(label="Administración", menu=admin_menu)
        else:
            cliente_menu = tk.Menu(self.menu_bar, tearoff=0)
            cliente_menu.add_command(label="Crear Nueva Solicitud", command=self.crear_solicitud)
            cliente_menu.add_command(label="Ver Historial de Solicitudes", command=self.ver_historial)
            self.menu_bar.add_cascade(label="Opciones", menu=cliente_menu)

        self.config(menu=self.menu_bar)

    def mostrar_bienvenida(self):
        welcome_label = tk.Label(self.frame_principal, text=f"Bienvenido {self.usuario_actual.nombre}", font=("Arial", 16))
        welcome_label.pack(pady=10)

    def gestion_inventario(self):
        messagebox.showinfo("Inventario", "Funcionalidad de gestión de inventario aún no implementada.")

    def calendario_eventos(self):
        messagebox.showinfo("Calendario", "Funcionalidad de calendario de eventos aún no implementada.")

    def crear_solicitud(self):
        messagebox.showinfo("Crear Solicitud", "Funcionalidad de creación de solicitudes aún no implementada.")

    def ver_historial(self):
        # Limpiar el contenido del frame principal y mostrar el historial
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
        
        # Crear el historial de solicitudes
        HistorialSolicitudes(self.frame_principal, self.usuario_actual)

def iniciar_aplicacion():
    # Iniciar el registro/login
    app_login = RegistroCliente()

    # Recuperar usuario logueado después de que la ventana se cierra
    usuario_actual = app_login.usuario_actual
    if usuario_actual is not None:
        # Lanzar el menú principal
        app_menu = MenuPrincipal(usuario_actual)
        app_menu.mainloop()
    else:
        messagebox.showerror("Error", "No se pudo iniciar sesión.")

if __name__ == "__main__":
    iniciar_aplicacion()
