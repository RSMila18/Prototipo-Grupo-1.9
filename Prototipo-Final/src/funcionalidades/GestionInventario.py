# archivo: interfazGrafica/gestionInventario.py

import tkinter as tk
from tkinter import ttk, messagebox
from gestorAplicacion.Inventario import Inventario
from gestorAplicacion.Evento import Evento  # Add this line to import the Evento class

class GestionInventario:
    def __init__(self, parent):
        self.parent = parent
        self.inventario = Inventario()

    def mostrar_interfaz(self):
        self.ventana = tk.Toplevel(self.parent)
        self.ventana.title("Gestión de Inventario")
        
        # Frame para búsqueda
        frame_busqueda = ttk.Frame(self.ventana, padding="10")
        frame_busqueda.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame_busqueda, text="Buscar Material:").grid(column=0, row=0, sticky=tk.W)
        self.entrada_busqueda = ttk.Entry(frame_busqueda)
        self.entrada_busqueda.grid(column=1, row=0, sticky=(tk.W, tk.E))
        ttk.Button(frame_busqueda, text="Buscar", command=self.realizar_busqueda).grid(column=2, row=0)
        
        # Frame para agregar/retirar material
        frame_modificar = ttk.Frame(self.ventana, padding="10")
        frame_modificar.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(frame_modificar, text="Nombre:").grid(column=0, row=0, sticky=tk.W)
        self.entrada_nombre = ttk.Entry(frame_modificar)
        self.entrada_nombre.grid(column=1, row=0, sticky=(tk.W, tk.E))
        
        ttk.Label(frame_modificar, text="Cantidad:").grid(column=0, row=1, sticky=tk.W)
        self.entrada_cantidad = ttk.Entry(frame_modificar)
        self.entrada_cantidad.grid(column=1, row=1, sticky=(tk.W, tk.E))
        
        ttk.Label(frame_modificar, text="Estado:").grid(column=0, row=2, sticky=tk.W)
        self.entrada_estado = ttk.Entry(frame_modificar)
        self.entrada_estado.grid(column=1, row=2, sticky=(tk.W, tk.E))
        
        ttk.Button(frame_modificar, text="Agregar", command=self.agregar).grid(column=0, row=3)
        ttk.Button(frame_modificar, text="Retirar", command=self.retirar).grid(column=1, row=3)
        
        # Lista de materiales
        self.tree = ttk.Treeview(self.ventana, columns=('Nombre', 'Cantidad', 'Estado'), show='headings')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Cantidad', text='Cantidad')
        self.tree.heading('Estado', text='Estado')
        self.tree.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.actualizar_lista()

    def realizar_busqueda(self):
        nombre = self.entrada_busqueda.get()
        material = self.inventario.buscar_material(nombre)
        if material:
            messagebox.showinfo("Resultado", str(material))
        else:
            messagebox.showinfo("Resultado", "Material no encontrado")

    def agregar(self):
        nombre = self.entrada_nombre.get()
        estado = self.entrada_estado.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            self.inventario.agregar_material(nombre, cantidad, estado)
            self.actualizar_lista()
            messagebox.showinfo("Éxito", "Material agregado correctamente")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")

    def retirar(self):
        nombre = self.entrada_nombre.get()
        try:
            cantidad = int(self.entrada_cantidad.get())
            if self.inventario.retirar_material(nombre, cantidad):
                self.actualizar_lista()
                messagebox.showinfo("Éxito", "Material retirado correctamente")
            else:
                messagebox.showerror("Error", "No hay suficiente cantidad de este material")
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero")

    def actualizar_lista(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for material in self.inventario.listar_materiales():
            self.tree.insert('', 'end', values=(material.nombre, material.cantidad, material.estado))

    def verificar_disponibilidad(self, nombre, cantidad_requerida):
        if not self.inventario.verificar_disponibilidad(nombre, cantidad_requerida):
            messagebox.showwarning("Advertencia", f"El material '{nombre}' tiene una cantidad insuficiente. Disponible: {self.inventario.buscar_material(nombre).cantidad}, Requerido: {cantidad_requerida}")
            return False
        return True
    
    def asignar_material_evento(self):
    # Obtiene los valores del formulario
        nombre_material = self.entrada_nombre.get()
        cantidad = int(self.entrada_cantidad.get())
        estado = self.entrada_estado.get()
        
        # Buscar el evento seleccionado
        evento_seleccionado = self.combo_eventos.get()
        if not evento_seleccionado:
            messagebox.showerror("Error", "Seleccione un evento.")
            return

        # Verificar si el material está disponible en el inventario
        if not self.inventario.verificar_disponibilidad(nombre_material, cantidad):
            messagebox.showerror("Error", "Cantidad insuficiente de material en el inventario.")
            return

        # Asignar el material al evento
        for evento in Evento.eventos_registrados:
            if evento.nombre == evento_seleccionado:
                evento.agregar_material(nombre_material, cantidad, estado)
                self.inventario.retirar_material(nombre_material, cantidad)
                messagebox.showinfo("Éxito", f"Material {nombre_material} asignado al evento {evento_seleccionado}.")
                self.actualizar_lista()
                return
