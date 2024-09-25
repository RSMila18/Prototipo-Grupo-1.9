# archivo: gestorAplicacion/inventario.py
import pickle

class Material:
    def __init__(self, nombre, cantidad, estado):
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado

    def __str__(self):
        return f"Material: {self.nombre}, Cantidad: {self.cantidad}, Estado: {self.estado}"

class Inventario:
    def __init__(self):
        self.materiales = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open('inventario.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {}

    def guardar_inventario(self):
        with open('inventario.pkl', 'wb') as f:
            pickle.dump(self.materiales, f)

    def buscar_material(self, nombre):
        return self.materiales.get(nombre.lower())

    def agregar_material(self, nombre, cantidad, estado):
        nombre = nombre.lower()
        if nombre in self.materiales and self.materiales[nombre].estado != estado and self.materiales[nombre].cantidad > 0:
            self.materiales[nombre].cantidad += cantidad
        else:
            self.materiales[nombre] = Material(nombre, cantidad, estado)
        self.guardar_inventario()

    def retirar_material(self, nombre, cantidad, estado):
        nombre = nombre.lower()
        if nombre in self.materiales and self.materiales.cantidad - cantidad > 0:
            if self.materiales[nombre].cantidad >= cantidad:
                self.materiales[nombre].cantidad -= cantidad
                if self.materiales[nombre].cantidad == 0:
                    self.materiales[nombre].estado = "agotado"
                self.guardar_inventario()
                return True
        return False

    def listar_materiales(self):
        return list(self.materiales.values())

    def verificar_disponibilidad(self, nombre, cantidad_requerida):
        material = self.buscar_material(nombre)
        if material and material.cantidad < cantidad_requerida:
            return False
        return True


