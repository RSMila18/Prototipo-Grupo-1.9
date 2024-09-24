from gestorAplicacion.Serializador import Serializador

class Cliente:
    clientes_registrados = []
    archivo_usuarios = "clientes.pkl"

    def __init__(self, nombre, documento, tipo_documento, representante_legal="N/A", correo="", telefono="", usuario="", contrasena=""):
        self.nombre = nombre
        self.documento = documento
        self.tipo_documento = tipo_documento
        self.representante_legal = representante_legal
        self.correo = correo
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena

    @classmethod
    def registrar_cliente(cls, cliente):
        cls.clientes_registrados.append(cliente)
        cls.guardar_usuarios()

    @classmethod
    def guardar_usuarios(cls):
        Serializador.guardar_datos(cls.archivo_usuarios, cls.clientes_registrados)

    @classmethod
    def cargar_usuarios(cls):
        datos = Serializador.cargar_datos(cls.archivo_usuarios)
        if isinstance(datos, list) and all(isinstance(cliente, Cliente) for cliente in datos):
            cls.clientes_registrados = datos
        else:
            cls.clientes_registrados = []
            print("Datos de clientes cargados no válidos, se inicializa una lista vacía.")

    @classmethod
    def obtener_cliente(cls, documento):
        for cliente in cls.clientes_registrados:
            if cliente.documento == documento:
                return cliente
        return None

    def iniciar_sesion(self, usuario, contrasena):
        return self.usuario == usuario and self.contrasena == contrasena

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}\nDocumento: {self.documento}\nTipo de Documento: {self.tipo_documento}")
        if self.tipo_documento == "NIT":
            print(f"Representante Legal: {self.representante_legal}")
        print(f"Correo: {self.correo}\nTeléfono: {self.telefono}\nUsuario: {self.usuario}")

# Cargar usuarios al inicio
Cliente.cargar_usuarios()

