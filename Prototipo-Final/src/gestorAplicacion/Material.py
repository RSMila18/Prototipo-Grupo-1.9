class Material:
    def __init__(self, nombre, cantidad, estado, proveedor, historial):
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado
        self.proveedor = proveedor
        self.historial = historial

    def __str__(self):
        return f"Material: {self.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}, Proveedor: {self.proveedor}\nHistorial: {self.historial}"