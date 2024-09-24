import tkinter as tk
from tkinter import messagebox
from funcionalidades.RegistroCliente import RegistroCliente
from funcionalidades.HistorialSolicitudes import HistorialSolicitudes
from gestorAplicacion.cliente import Cliente
from gestorAplicacion.solicitud import Solicitud

class MenuPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú Principal")
        self.geometry("600x400")
        self.usuario_actual = None  # Variable para almacenar el usuario actual
        self.crear_menu()

    def crear_menu(self):
        self.label_opciones = tk.Label(self, text="Opciones", font=("Arial", 14))
        self.label_opciones.pack(pady=10)

        if self.usuario_actual is None:
            tk.Button(self, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=5)
            tk.Button(self, text="Registrar Nuevo Usuario", command=self.mostrar_registro).pack(pady=5)

        elif self.usuario_actual.usuario == "ADMIN":
            tk.Button(self, text="Ver Usuarios Registrados", command=self.ver_usuarios).pack(pady=5) #Son botones temporales, cambienlos con lo que necesesiten
            tk.Button(self, text="Gestionar Solicitudes", command=self.gestionar_solicitudes).pack(pady=5)
            tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)
            
        else:  # Usuario regular
            tk.Button(self, text="Registrar Nueva Solicitud", command=self.mostrar_registro_solicitud).pack(pady=5)
            tk.Button(self, text="Ver Historial de Solicitudes", command=self.ver_historial).pack(pady=5)
            tk.Button(self, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=5)

    def mostrar_inicio_sesion(self):
        self.limpiar_frame()
        self.frame_inicio_sesion = tk.Frame(self)
        self.frame_inicio_sesion.pack()

        tk.Label(self.frame_inicio_sesion, text="Inicio de Sesión", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_inicio_sesion, text="Usuario").grid(row=1, column=0)
        self.usuario_entry = tk.Entry(self.frame_inicio_sesion)
        self.usuario_entry.grid(row=1, column=1)

        tk.Label(self.frame_inicio_sesion, text="Contraseña").grid(row=2, column=0)
        self.contrasena_entry = tk.Entry(self.frame_inicio_sesion, show='*')
        self.contrasena_entry.grid(row=2, column=1)

        tk.Button(self.frame_inicio_sesion, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame_inicio_sesion, text="Regresar", command=self.regresar_menu).grid(row=4, columnspan=2)

    def mostrar_registro(self):
        self.limpiar_frame()
        self.frame_registro = tk.Frame(self)
        self.frame_registro.pack()

        tk.Label(self.frame_registro, text="Registro de Usuario", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_registro, text="Usuario").grid(row=1, column=0)
        self.registro_usuario_entry = tk.Entry(self.frame_registro)
        self.registro_usuario_entry.grid(row=1, column=1)

        tk.Label(self.frame_registro, text="Contraseña").grid(row=2, column=0)
        self.registro_contrasena_entry = tk.Entry(self.frame_registro, show='*')
        self.registro_contrasena_entry.grid(row=2, column=1)

        tk.Button(self.frame_registro, text="Registrar", command=self.registrar_usuario).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame_registro, text="Regresar", command=self.regresar_menu).grid(row=4, columnspan=2)

    def registrar_usuario(self):
        usuario = self.registro_usuario_entry.get()
        contrasena = self.registro_contrasena_entry.get()
        registro = RegistroCliente()

        if registro.registrar(usuario, contrasena):  # Método de registro
            messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            self.regresar_menu()
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        for cliente in Cliente.clientes_registrados:
            if cliente.iniciar_sesion(usuario, contrasena):
                messagebox.showinfo("Éxito", f"Bienvenido {cliente.nombre}")
                self.usuario_actual = cliente  # Guardar el usuario actual
                self.limpiar_frame()
                self.crear_menu()  # Regresar al menú después de iniciar sesión
                return

        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

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
        self.limpiar_frame()
        self.crear_menu()

    def ver_historial(self):
        self.limpiar_frame()
        if self.usuario_actual:
            HistorialSolicitudes(self, self.usuario_actual)  # Pasar el usuario actual
        else:
            messagebox.showerror("Error", "No hay un usuario actual.")

    def ver_usuarios(self):
        pass  # Implementa la funcionalidad para ver los usuarios registrados

    def gestionar_solicitudes(self):
        pass  # Implementa la funcionalidad para gestionar solicitudes

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.regresar_menu()

    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

def iniciar_aplicacion():
    app_menu = MenuPrincipal()
    app_menu.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
