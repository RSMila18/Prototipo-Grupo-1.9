class Cliente:
    def __init__(self, nombre, nit, representante_legal, correo, telefono, usuario, contrasena):
        self.nombre = nombre
        self.nit = nit
        self.representante_legal = representante_legal
        self.correo = correo
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena
        self.verificado = False

    def registrar(self):
        print(f"Registrando cliente: {self.nombre}")
        # Aquí podrías agregar más lógica para almacenar o procesar los datos del cliente
        self.enviar_verificacion()

    def enviar_verificacion(self):
        # Simulación de envío de verificación
        print(f"Enviando verificación al correo: {self.correo}")
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
