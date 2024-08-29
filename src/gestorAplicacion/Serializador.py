import pickle
import os

class Serializador:

    @staticmethod
    def guardar_datos(ruta_archivo, datos):
        with open(ruta_archivo, "wb") as archivo:
            pickle.dump(datos, archivo)
            print(f"++++++++++++++++++++++++++++++++++++++++++++++++") #Datos guardados correctamente

    @staticmethod
    def cargar_datos(ruta_archivo):
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "rb") as archivo:
                datos = pickle.load(archivo)
                print(f"++++++++++++++++++++++++++++++++++++++++++++++++") #Datos cargados correctamente
                return datos
        else:
            print(f"------------------------------------------------") #No se encontró el archivo, Se devolverá una lista vacía.
            return []