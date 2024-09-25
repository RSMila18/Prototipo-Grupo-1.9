class Material:
    def __init__(self, nombre, cantidad, estado):
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado

    def __str__(self):
        return f"Material: {self.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}"
