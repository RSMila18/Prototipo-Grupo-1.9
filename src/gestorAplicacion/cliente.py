class Cliente:
    usuarios_registrados = set()  # Conjunto para almacenar nombres de usuario únicos

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
        return usuario not in cls.usuarios_registrados

    def registrar(self):
        if Cliente.es_usuario_unico(self.usuario):
            Cliente.usuarios_registrados.add(self.usuario)
            print(f"Registrando cliente: {self.nombre}")
            self.enviar_verificacion()
        else:
            print(f"Error: El nombre de usuario '{self.usuario}' ya está en uso. Por favor, elija otro.")

    def enviar_verificacion(self):
        # Simulación de envío de verificación
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