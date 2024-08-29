from gestorAplicacion.Serializador import Serializador

class Cliente:
    usuarios_registrados = []  # Lista para almacenar instancias de Cliente
    archivo_usuarios = "usuarios.pkl"  # Nombre del archivo para guardar usuarios

    def __init__(self, nombre, tipo_documento, documento, representante_legal, correo, telefono, usuario, contrasena):
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.representante_legal = representante_legal
        self.correo = correo
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena
        self.verificado = False

    @classmethod
    def es_usuario_unico(cls, usuario):
        return all(cliente.usuario != usuario for cliente in cls.usuarios_registrados)

    def registrar(self):
        if Cliente.es_usuario_unico(self.usuario):
            Cliente.usuarios_registrados.append(self)
            print(f"Registrando cliente: {self.nombre}")
            self.enviar_verificacion()
            Cliente.guardar_usuarios()  # Guardar usuarios después de registrarse
        else:
            print(f"Error: El nombre de usuario '{self.usuario}' ya está en uso. Por favor, elija otro.")

    def enviar_verificacion(self):
        print(f"Su usuario fue registrado correctamente.")
        self.verificar()

    def verificar(self):
        self.verificado = True
        print(f"Cliente {self.nombre} verificado exitosamente.")

    def iniciar_sesion(self, usuario, contrasena):
        if self.usuario == usuario and self.contrasena == contrasena:
            if self.verificado:
                print(f"Bienvenido {self.nombre}, sesión iniciada.")
                return True
            else:
                print("La cuenta no ha sido verificada.")
                return False
        print("Usuario o contraseña incorrectos.")
        return False

    @classmethod
    def guardar_usuarios(cls):
        Serializador.guardar_datos(cls.archivo_usuarios, cls.usuarios_registrados)

    @classmethod
    def cargar_usuarios(cls):
        datos = Serializador.cargar_datos(cls.archivo_usuarios)
        if isinstance(datos, list) and all(isinstance(cliente, Cliente) for cliente in datos):
            cls.usuarios_registrados = datos
        else:
            cls.usuarios_registrados = []
            print(f"Datos cargados no válidos, se inicializa una lista vacía.")

# Cargar los usuarios registrados al iniciar el programa
Cliente.cargar_usuarios()
