class Material:
    def __init__(self, nombre, cantidad, estado):
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado
        self.historial = []  # Lista para guardar el historial del material

    def agregar_historial(self, descripcion):
        """Añade una descripción al historial del material."""
        self.historial.append(descripcion)

    def __str__(self):
        return f"Material: {self.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}"

    def obtener_historial(self):
        """Devuelve el historial como un string con cada evento en una nueva línea."""
        return "\n".join(self.historial)
