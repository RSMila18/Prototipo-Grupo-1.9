import pickle
import os

class Serializador:
    @staticmethod
    def guardar_datos(archivo, datos):
        try:
            with open(archivo, 'wb') as f:
                pickle.dump(datos, f)
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    @staticmethod
    def cargar_datos(archivo):
        if not os.path.exists(archivo):
            return []

        try:
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            print("Error al cargar datos: archivo vacío o datos corruptos.")
            return []
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            return []