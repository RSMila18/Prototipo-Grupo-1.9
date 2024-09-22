import tkinter as tk
from tkinter import ttk, messagebox
from gestorAplicacion.cliente import Cliente

class RegistroCliente:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Portal de Inicio")

        # Pantalla de bienvenida
        self.frame_bienvenida = tk.Frame(self.root)
        self.frame_bienvenida.pack()

        tk.Label(self.frame_bienvenida, text="Bienvenido al Portal", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_bienvenida, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=5)
        tk.Button(self.frame_bienvenida, text="Registrar Nuevo Usuario", command=self.mostrar_registro).pack(pady=5)

        self.root.mainloop()

    def mostrar_inicio_sesion(self):
        self.limpiar_frame()
        self.frame_inicio_sesion = tk.Frame(self.root)
        self.frame_inicio_sesion.pack()

        tk.Label(self.frame_inicio_sesion, text="Inicio de Sesión", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_inicio_sesion, text="Usuario").grid(row=1, column=0)
        self.usuario_entry = tk.Entry(self.frame_inicio_sesion)
        self.usuario_entry.grid(row=1, column=1)

        tk.Label(self.frame_inicio_sesion, text="Contraseña").grid(row=2, column=0)
        self.contrasena_entry = tk.Entry(self.frame_inicio_sesion, show='*')
        self.contrasena_entry.grid(row=2, column=1)

        tk.Button(self.frame_inicio_sesion, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame_inicio_sesion, text="Regresar", command=self.mostrar_bienvenida).grid(row=4, columnspan=2)

    def mostrar_registro(self):
        self.limpiar_frame()
        self.frame_registro = tk.Frame(self.root)
        self.frame_registro.pack()

        tk.Label(self.frame_registro, text="Registro de Usuario", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_registro, text="Nombre").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(self.frame_registro)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(self.frame_registro, text="Tipo de Documento").grid(row=2, column=0)
        self.tipo_documento_var = tk.StringVar()
        self.tipo_documento_combo = ttk.Combobox(self.frame_registro, textvariable=self.tipo_documento_var)
        self.tipo_documento_combo['values'] = ["Cédula de Ciudadanía", "NIT"]  # Opciones restringidas
        self.tipo_documento_combo.grid(row=2, column=1)
        self.tipo_documento_combo.bind("<<ComboboxSelected>>", self.cambiar_tipo_documento)  # Evento para manejar cambio

        tk.Label(self.frame_registro, text="Documento").grid(row=3, column=0)
        self.documento_entry = tk.Entry(self.frame_registro)
        self.documento_entry.grid(row=3, column=1)

        tk.Label(self.frame_registro, text="Representante Legal").grid(row=4, column=0)
        self.representante_entry = tk.Entry(self.frame_registro)
        self.representante_label = tk.Label(self.frame_registro, text="Representante Legal")
        self.representante_label.grid(row=4, column=0)
        self.representante_entry.grid(row=4, column=1)

        tk.Label(self.frame_registro, text="Correo Electrónico").grid(row=5, column=0)
        self.correo_entry = tk.Entry(self.frame_registro)
        self.correo_entry.grid(row=5, column=1)

        tk.Label(self.frame_registro, text="Teléfono").grid(row=6, column=0)
        self.telefono_entry = tk.Entry(self.frame_registro)
        self.telefono_entry.grid(row=6, column=1)

        tk.Label(self.frame_registro, text="Usuario").grid(row=7, column=0)
        self.usuario_entry = tk.Entry(self.frame_registro)
        self.usuario_entry.grid(row=7, column=1)

        tk.Label(self.frame_registro, text="Contraseña").grid(row=8, column=0)
        self.contrasena_entry = tk.Entry(self.frame_registro, show='*')
        self.contrasena_entry.grid(row=8, column=1)

        tk.Button(self.frame_registro, text="Registrar", command=self.registrar_usuario).grid(row=9, columnspan=2, pady=10)
        tk.Button(self.frame_registro, text="Regresar", command=self.mostrar_bienvenida).grid(row=10, columnspan=2)

        self.ocultar_representante()  # Inicialmente ocultar la entrada de representante legal

    def cambiar_tipo_documento(self, event):
        tipo_documento = self.tipo_documento_var.get()
        if tipo_documento == "NIT":
            self.mostrar_representante()
        else:
            self.ocultar_representante()

    def mostrar_representante(self):
        self.representante_label.grid()  # Mostrar el label
        self.representante_entry.grid()  # Mostrar el campo de entrada

    def ocultar_representante(self):
        self.representante_label.grid_remove()  # Ocultar el label
        self.representante_entry.grid_remove()  # Ocultar el campo de entrada
        self.representante_entry.delete(0, tk.END)  # Asegurar que esté vacío
        self.representante_entry.insert(0, "N/A")  # Insertar "N/A" si no es NIT

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        tipo_documento = self.tipo_documento_var.get()
        documento = self.documento_entry.get()
        representante = self.representante_entry.get() if tipo_documento == "NIT" else "N/A"
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "El correo electrónico no es válido.")
            return

        cliente = Cliente(nombre, tipo_documento, documento, representante, correo, telefono, usuario, contrasena)
        cliente.registrar()

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        for cliente in Cliente.usuarios_registrados:
            if cliente.iniciar_sesion(usuario, contrasena):
                messagebox.showinfo("Éxito", f"Bienvenido {cliente.nombre}")
                return

        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def limpiar_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_bienvenida(self):
        self.limpiar_frame()
        self.__init__()

if __name__ == "__main__":
    RegistroCliente()



