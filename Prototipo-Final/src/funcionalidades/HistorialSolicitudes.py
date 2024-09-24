import tkinter as tk
from tkinter import messagebox, ttk
from gestorAplicacion.solicitud import Solicitud

class HistorialSolicitudes:
    def __init__(self, master, usuario_actual):
        self.master = master
        self.usuario_actual = usuario_actual  # Guardar el usuario actual
        self.master.title("Historial de Solicitudes")

        self.filtro_frame = tk.Frame(self.master)
        self.filtro_frame.pack(pady=10)

        self.label_filtro = tk.Label(self.filtro_frame, text="Filtrar por:")
        self.label_filtro.pack(side=tk.LEFT)

        self.combo_filtro = ttk.Combobox(self.filtro_frame, values=["Todos", "Pendiente", "Aprobado", "Rechazado"])
        self.combo_filtro.current(0)
        self.combo_filtro.pack(side=tk.LEFT)

        self.boton_filtrar = tk.Button(self.filtro_frame, text="Filtrar", command=self.filtrar_solicitudes)
        self.boton_filtrar.pack(side=tk.LEFT)

        self.lista_solicitudes = tk.Listbox(self.master, width=50)
        self.lista_solicitudes.pack(pady=10)
        self.lista_solicitudes.bind('<<ListboxSelect>>', self.mostrar_detalle)

        self.cargar_lista_solicitudes()

    def cargar_lista_solicitudes(self):
        self.lista_solicitudes.delete(0, tk.END)
        for solicitud in Solicitud.solicitudes_registradas:
            self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.fecha_evento} - {solicitud.estado}")

    def filtrar_solicitudes(self):
        filtro = self.combo_filtro.get()
        self.lista_solicitudes.delete(0, tk.END)
        for solicitud in Solicitud.solicitudes_registradas:
            if filtro == "Todos" or solicitud.estado == filtro:
                self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.fecha_evento} - {solicitud.estado}")

    def mostrar_detalle(self, event):
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            solicitud = Solicitud.solicitudes_registradas[index]
            descripcion = solicitud.obtener_descripcion()
            messagebox.showinfo("Detalles de la Solicitud", f"Descripción: {descripcion}")

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = HistorialSolicitudes(root, "Usuario Actual")  # Cambia "Usuario Actual" por un usuario real si es necesario
    root.mainloop()


