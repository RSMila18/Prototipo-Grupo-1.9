import pickle

class Serializador:

    @staticmethod
    def guardar_datos(nombre_archivo, datos):
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(datos, archivo)

    @staticmethod
    def cargar_datos(nombre_archivo):
        try:
            with open(nombre_archivo, "rb") as archivo:
                return pickle.load(archivo)
        except FileNotFoundError:
            print(f"Archivo {nombre_archivo} no encontrado, creando nuevo archivo.")
            return []
        except (EOFError, pickle.UnpicklingError):
            print("Error al leer el archivo.")
            return []
