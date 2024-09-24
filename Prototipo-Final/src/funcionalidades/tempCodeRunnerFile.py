import tkinter as tk
from tkinter import ttk, messagebox
from gestorAplicacion.cliente import Cliente

class RegistroCliente:
    def __init__(self, master):
        self.master = master
        self.usuario_actual_var = None  # Cambié para usar una variable de instancia

        self.master.title("Bienvenido al Portal")
        self.frame_bienvenida = tk.Frame(self.master)
        self.frame_bienvenida.pack()

        tk.Button(self.frame_bienvenida, text="Iniciar Sesión", command=self.mostrar_inicio_sesion).pack(pady=5)
        tk.Button(self.frame_bienvenida, text="Registrar Nuevo Usuario", command=self.mostrar_registro).pack(pady=5)

    # Este método ya devuelve la variable de instancia correctamente
    def obtener_usuario_actual(self):
        return self.usuario_actual_var

    def mostrar_inicio_sesion(self):
        self.master.limpiar_frame()

        self.frame_inicio_sesion = tk.Frame(self.master)
        self.frame_inicio_sesion.pack(pady=10)
        
        tk.Label(self.frame_inicio_sesion, text="Inicio de Sesión", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)

        tk.Label(self.frame_inicio_sesion, text="Usuario").grid(row=1, column=0)
        self.usuario_entry = tk.Entry(self.frame_inicio_sesion)
        self.usuario_entry.grid(row=1, column=1)

        tk.Label(self.frame_inicio_sesion, text="Contraseña").grid(row=2, column=0)
        self.contrasena_entry = tk.Entry(self.frame_inicio_sesion, show='*')
        self.contrasena_entry.grid(row=2, column=1)

        tk.Button(self.frame_inicio_sesion, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame_inicio_sesion, text="Regresar", command=self.mostrar_bienvenida).grid(row=4, columnspan=2)

    def mostrar_bienvenida(self):
        self.master.limpiar_frame()
        self.frame_bienvenida.pack()  # Volver a mostrar el marco de bienvenida

    def mostrar_registro(self):
        self.master.limpiar_frame()
    
        self.frame_registro = tk.Frame(self.master)
        self.frame_registro.pack(pady=10)

        tk.Label(self.frame_registro, text="Registro de Usuario", font=("Arial", 14)).grid(row=0, columnspan=2, pady=10)
        tk.Label(self.frame_registro, text="Nombre").grid(row=1, column=0)
        self.nombre_entry = tk.Entry(self.frame_registro)
        self.nombre_entry.grid(row=1, column=1)

        tk.Label(self.frame_registro, text="Tipo de Documento").grid(row=2, column=0)
        self.tipo_documento_var = tk.StringVar()
        self.tipo_documento_combo = ttk.Combobox(self.frame_registro, textvariable=self.tipo_documento_var)
        self.tipo_documento_combo['values'] = ["Cédula de Ciudadanía", "NIT"]
        self.tipo_documento_combo.grid(row=2, column=1)
        self.tipo_documento_combo.bind("<<ComboboxSelected>>", self.cambiar_tipo_documento)

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
        tk.Button(self.frame_registro, text="Regresar", command=self.regresar).grid(row=10, columnspan=2)

        self.ocultar_representante()

    def cambiar_tipo_documento(self, event):
        tipo_documento = self.tipo_documento_var.get()
        if tipo_documento == "NIT":
            self.mostrar_representante()
        else:
            self.ocultar_representante()

    def mostrar_representante(self):
        self.representante_label.grid()
        self.representante_entry.grid()

    def ocultar_representante(self):
        self.representante_label.grid_remove()
        self.representante_entry.grid_remove()
        self.representante_entry.delete(0, tk.END)
        self.representante_entry.insert(0, "N/A")

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

        cliente = Cliente(nombre, documento, tipo_documento, representante, correo, telefono, usuario, contrasena)
        Cliente.registrar_cliente(cliente)

        # Almacenar el usuario actual después de registrarlo
        self.usuario_actual_var = cliente
        messagebox.showinfo("Éxito", "Usuario registrado con éxito.")

    def iniciar_sesion(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()

        for cliente in Cliente.clientes_registrados:
            if cliente.iniciar_sesion(usuario, contrasena):
                self.usuario_actual_var = cliente  # Almacenar el usuario actual
                messagebox.showinfo("Éxito", f"Bienvenido {cliente.nombre}")
                
                # En lugar de destruir la ventana, limpiamos el frame actual
                self.master.limpiar_frame()
                self.mostrar_menu_principal()  # Llamar al menú principal después de iniciar sesión
                return cliente  # Devolver el usuario actual

        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
        return None


    def regresar(self):
        self.master.limpiar_frame()
        self.master.crear_menu()