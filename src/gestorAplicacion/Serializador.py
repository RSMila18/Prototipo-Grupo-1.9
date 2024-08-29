import pickle
import os

class Serializador:

    @staticmethod
    def guardar_datos(ruta_archivo, datos):
        with open(ruta_archivo, "wb") as archivo:
            pickle.dump(datos, archivo)
            print(f"Datos guardados correctamente en {ruta_archivo}.")

    @staticmethod
    def cargar_datos(ruta_archivo):
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "rb") as archivo:
                datos = pickle.load(archivo)
                print(f"Datos cargados correctamente desde {ruta_archivo}.")
                return datos
        else:
            print(f"No se encontró el archivo {ruta_archivo}. Se devolverá una lista vacía.")
            return []