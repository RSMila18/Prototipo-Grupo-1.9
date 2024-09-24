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
        self.lista_solicitudes.bind('<<ListboxSelect>>', self.mostrar_detalle_solicitud)

        self.boton_regresar = tk.Button(self.master, text="Regresar", command=self.regresar_menu)
        self.boton_regresar.pack(pady=10)

        self.cargar_solicitudes()  # Cargar las solicitudes al iniciar

    def cargar_solicitudes(self):
        self.lista_solicitudes.delete(0, tk.END)
        solicitudes = Solicitud.solicitudes_registradas  # Obtener todas las solicitudes

        for solicitud in solicitudes:
            if solicitud.cliente == self.usuario_actual or self.usuario_actual.usuario == "ADMIN":
                self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.estado}")

    def filtrar_solicitudes(self):
        filtro = self.combo_filtro.get()
        self.lista_solicitudes.delete(0, tk.END)
        solicitudes = Solicitud.solicitudes_registradas  # Obtener todas las solicitudes

        for solicitud in solicitudes:
            if (solicitud.cliente == self.usuario_actual or self.usuario_actual.usuario == "ADMIN") and (filtro == "Todos" or solicitud.estado == filtro):
                self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.estado}")

    def mostrar_detalle_solicitud(self, event):
        try:
            seleccion = self.lista_solicitudes.curselection()[0]
            solicitud = Solicitud.solicitudes_registradas[seleccion]
            messagebox.showinfo("Detalles de Solicitud", f"Evento: {solicitud.nombre_evento}\nFecha: {solicitud.fecha_evento}\nDescripción: {solicitud.descripcion_evento}\nEstado: {solicitud.estado}")
        except IndexError:
            pass  # No se seleccionó nada

    def regresar_menu(self):
        self.master.limpiar_frame()  # Limpiar la ventana
        self.master.crear_menu()  # Regresar al menú principal


