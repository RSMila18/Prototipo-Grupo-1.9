import tkinter as tk
from tkinter import messagebox
from funcionalidades.RegistroCliente import RegistroCliente
#from funcionalidades.RegistroSolicitudes import registro_solicitudes_main
#from funcionalidades.Calendario import calendariomain
#from funcionalidades.MenuInventario import MenuInventario

class MenuPrincipal(tk.Tk):
    def __init__(self, usuario_actual):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("300x200")

        self.usuario_actual = usuario_actual
        self.crear_menu()

    def crear_menu(self):
        if self.usuario_actual == "ADMIN":
            tk.Label(self, text="Bienvenido ADMIN", font=("Arial", 14)).pack(pady=10)
            tk.Button(self, text="Gestión de Inventario", command=self.gestion_inventario).pack(pady=5)
            tk.Button(self, text="Calendario de Eventos", command=self.calendario_eventos).pack(pady=5)
        else:
            tk.Label(self, text=f"Bienvenido {self.usuario_actual.nombre}", font=("Arial", 14)).pack(pady=10)
            tk.Button(self, text="Crear Nueva Solicitud", command=self.crear_solicitud).pack(pady=5)
            tk.Button(self, text="Ver Historial de Solicitudes", command=self.ver_historial).pack(pady=5)

    #def gestion_inventario(self):
        #inventario = MenuInventario()
        #inventario.mostrar_menu()

    #def calendario_eventos(self):
        #calendariomain()

    #def crear_solicitud(self):
        #registro_solicitudes_main()

    def ver_historial(self):
        messagebox.showinfo("Historial de Solicitudes", "Funcionalidad de historial de solicitudes aún no implementada.")

def iniciar_aplicacion():
    # Iniciar el registro/login
    app_login = RegistroCliente()
    app_login.mainloop()

    # Recuperar usuario logueado
    usuario_actual = app_login.iniciar_sesion()
    if usuario_actual is not None:
        # Lanzar el menú principal
        app_menu = MenuPrincipal(usuario_actual)
        app_menu.mainloop()
    else:
        messagebox.showerror("Error", "No se pudo iniciar sesión.")

if __name__ == "__main__":
    iniciar_aplicacion()

