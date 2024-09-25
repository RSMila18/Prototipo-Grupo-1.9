import tkinter as tk
from tkinter import messagebox, ttk
from gestorAplicacion.solicitud import Solicitud
from datetime import datetime

class HistorialSolicitudes:
    def __init__(self, master, usuario_actual):
        self.master = master
        self.usuario_actual = usuario_actual
        self.master.title("Historial de Solicitudes")

        # Filtro frame
        self.filtro_frame = tk.Frame(self.master)
        self.filtro_frame.pack(pady=10)

        # Filtrar por estado
        self.label_filtro_estado = tk.Label(self.filtro_frame, text="Filtrar por estado:")
        self.label_filtro_estado.pack(side=tk.LEFT)

        self.combo_filtro_estado = ttk.Combobox(self.filtro_frame, values=["Todos", "Pendiente", "Aprobado", "Rechazado"])
        self.combo_filtro_estado.current(0)
        self.combo_filtro_estado.pack(side=tk.LEFT)

        # Filtrar por fecha
        self.label_filtro_fecha = tk.Label(self.filtro_frame, text="Filtrar por fecha (DD/MM/AAAA):")
        self.label_filtro_fecha.pack(side=tk.LEFT)

        self.fecha_filtro_entry = tk.Entry(self.filtro_frame)
        self.fecha_filtro_entry.pack(side=tk.LEFT)

        # Botones
        self.boton_filtrar = tk.Button(self.filtro_frame, text="Filtrar", command=self.filtrar_solicitudes)
        self.boton_filtrar.pack(side=tk.LEFT)

        self.boton_regresar = tk.Button(self.filtro_frame, text="Regresar", command=self.regresar)
        self.boton_regresar.pack(side=tk.LEFT)

        # Lista de solicitudes
        self.lista_solicitudes = tk.Listbox(self.master, width=80)
        self.lista_solicitudes.pack(pady=10)
        self.lista_solicitudes.bind('<<ListboxSelect>>', self.mostrar_detalle)

        # Cargar solicitudes al iniciar
        Solicitud.cargar_solicitudes()
        self.cargar_lista_solicitudes()

    def cargar_lista_solicitudes(self):
        """
        Carga y muestra solo las solicitudes del usuario actual.
        """
        self.lista_solicitudes.delete(0, tk.END)
        for solicitud in Solicitud.solicitudes_registradas:
            # Filtrar las solicitudes por el usuario actual
            if solicitud.cliente.usuario == self.usuario_actual.usuario:
                self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.fecha_evento} - {solicitud.estado}")

    def filtrar_solicitudes(self):
        """
        Aplica los filtros de estado y fecha sobre las solicitudes del usuario actual.
        """
        filtro_estado = self.combo_filtro_estado.get()
        fecha_filtro = self.fecha_filtro_entry.get()

        self.lista_solicitudes.delete(0, tk.END)
        for solicitud in Solicitud.solicitudes_registradas:
            if solicitud.cliente.usuario == self.usuario_actual.usuario:
                # Filtro por estado
                if filtro_estado == "Todos" or solicitud.estado == filtro_estado:
                    # Filtro por fecha
                    if fecha_filtro:
                        try:
                            fecha_input = datetime.strptime(fecha_filtro, "%d/%m/%Y")
                            if solicitud.fecha_evento != fecha_input.strftime("%d/%m/%Y"):
                                continue
                        except ValueError:
                            messagebox.showerror("Error", "Formato de fecha incorrecto. Use DD/MM/AAAA.")
                            return
                    # Agregar solicitud si pasa los filtros
                    self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.fecha_evento} - {solicitud.estado}")

    def mostrar_detalle(self, event):
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            # Obtener el índice correcto de la lista filtrada
            solicitudes_usuario = [s for s in Solicitud.solicitudes_registradas if s.cliente.usuario == self.usuario_actual.usuario]
            solicitud = solicitudes_usuario[index]
            descripcion = solicitud.descripcion_evento
            messagebox.showinfo("Detalles de la Solicitud", f"Descripción: {descripcion}")

    def regresar(self):
        self.master.limpiar_frame()
        self.master.crear_menu()

