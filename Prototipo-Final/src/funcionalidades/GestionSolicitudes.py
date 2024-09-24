import tkinter as tk
from tkinter import messagebox
from gestorAplicacion.solicitud import Solicitud
from gestorAplicacion.Evento import Evento  # Asegúrate de tener esta clase implementada
from datetime import datetime

class GestionSolicitudes:
    def __init__(self, master, usuario_actual, regresar_callback):
        self.master = master
        self.usuario_actual = usuario_actual
        self.regresar_callback = regresar_callback  # Guardamos el callback para regresar
        self.master.title("Gestión de Solicitudes")

        self.lista_solicitudes = tk.Listbox(self.master, width=80)
        self.lista_solicitudes.pack(pady=10)
        self.lista_solicitudes.bind('<<ListboxSelect>>', self.mostrar_detalle)

        self.boton_aprobar = tk.Button(self.master, text="Aprobar Solicitud", command=self.aprobar_solicitud)
        self.boton_aprobar.pack(pady=5)

        self.boton_rechazar = tk.Button(self.master, text="Rechazar Solicitud", command=self.rechazar_solicitud)
        self.boton_rechazar.pack(pady=5)

        self.boton_crear_evento = tk.Button(self.master, text="Crear Evento", command=self.crear_evento)
        self.boton_crear_evento.pack(pady=5)

        # Botón de regresar
        self.boton_regresar = tk.Button(self.master, text="Regresar", command=self.regresar_callback)
        self.boton_regresar.pack(pady=5)

        self.cargar_lista_solicitudes()

    def cargar_lista_solicitudes(self):
        """Carga y muestra todas las solicitudes."""
        self.lista_solicitudes.delete(0, tk.END)
        for solicitud in Solicitud.solicitudes_registradas:
            self.lista_solicitudes.insert(tk.END, f"{solicitud.nombre_evento} - {solicitud.fecha_evento} - {solicitud.estado}")

    def mostrar_detalle(self, event):
        """Muestra los detalles de la solicitud seleccionada."""
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            solicitud = Solicitud.solicitudes_registradas[index]
            descripcion = solicitud.descripcion_evento
            messagebox.showinfo("Detalles de la Solicitud", f"Descripción: {descripcion}")

    def aprobar_solicitud(self):
        """Cambia el estado de la solicitud seleccionada a 'Aprobado'."""
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            solicitud = Solicitud.solicitudes_registradas[index]
            solicitud.estado = "Aprobado"
            messagebox.showinfo("Éxito", "Solicitud aprobada.")
            self.cargar_lista_solicitudes()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una solicitud.")

    def rechazar_solicitud(self):
        """Cambia el estado de la solicitud seleccionada a 'Rechazado'."""
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            solicitud = Solicitud.solicitudes_registradas[index]
            solicitud.estado = "Rechazado"
            messagebox.showinfo("Éxito", "Solicitud rechazada.")
            self.cargar_lista_solicitudes()
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una solicitud.")

    def crear_evento(self):
        """Permite crear un evento asociado a la solicitud seleccionada."""
        seleccion = self.lista_solicitudes.curselection()
        if seleccion:
            index = seleccion[0]
            solicitud = Solicitud.solicitudes_registradas[index]
            # Aquí pides los materiales y la fecha del evento
            nombre_evento = solicitud.nombre_evento
            fecha_evento = solicitud.fecha_evento
            materiales = []  # Puedes solicitar al usuario que ingrese materiales

            # Por simplicidad, vamos a simular la entrada de materiales
            materiales.append("Sillas")  # Esto sería reemplazado por entradas de usuario
            materiales.append("Mesas")

            evento = Evento(nombre_evento, fecha_evento, materiales)
            evento.crear_evento()  # Asegúrate de tener esta funcionalidad en la clase Evento

            messagebox.showinfo("Éxito", "Evento creado con éxito.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una solicitud.")



