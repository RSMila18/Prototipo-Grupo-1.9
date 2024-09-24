import tkinter as tk
from tkinter import ttk, messagebox
import re


class ProveedoresGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Proveedores")

        # Datos de ejemplo más realistas
        self.proveedores = [
            {"nombre": "Sillas y Mesas ABC", "material": "Sillas y mesas", "ubicación": "Bogotá",
             "email": "ventas@smabc.com", "telefono": "3205551234"},
            {"nombre": "Sonido y Luces S.A.S", "material": "Equipos de sonido", "ubicación": "Cali",
             "email": "info@sonidoyluces.com", "telefono": "3109876543"},
            {"nombre": "Decoraciones del Valle", "material": "Decoraciones para eventos", "ubicación": "Cali",
             "email": "decoraciones@valle.com", "telefono": "3112345678"},
            {"nombre": "Catering Gourmet", "material": "Servicios de catering", "ubicación": "Medellín",
             "email": "catering@gourmet.com", "telefono": "3208765432"},
            {"nombre": "Alquiler de Carpas Colombia", "material": "Carpas y toldos", "ubicación": "Barranquilla",
             "email": "info@alquilercarpas.com", "telefono": "3154321098"},
            {"nombre": "Florería Arte Floral", "material": "Arreglos florales", "ubicación": "Bucaramanga",
             "email": "contacto@artefloral.com", "telefono": "3187654321"},
            {"nombre": "Equipos Audiovisuales S.A.", "material": "Proyectores y pantallas", "ubicación": "Cartagena",
             "email": "info@equiposaudio.com", "telefono": "3212345678"},
            {"nombre": "Transporte Eventos", "material": "Transporte de materiales", "ubicación": "Cali",
             "email": "transporte@eventos.com", "telefono": "3176543210"}
        ]

        self.detalles_visibles = False
        self.proveedor_seleccionado = None

        # --- Sección de Filtros y Búsquedas ---
        ttk.Label(self.master, text="Filtrar por tipo de material:").grid(column=0, row=0, padx=10, pady=5)
        self.material_combobox = ttk.Combobox(self.master,
                                              values=["Todos", "Concreto", "Madera", "Acero", "Plástico",
                                                      "Equipos de construcción", "Sistemas hidráulicos",
                                                      "Cemento", "Pinturas"])
        self.material_combobox.grid(column=1, row=0, padx=10, pady=5)
        self.material_combobox.set("Todos")

        filtrar_button = ttk.Button(self.master, text="Filtrar", command=self.filtrar_proveedores)
        filtrar_button.grid(column=2, row=0, padx=10, pady=5)

        ttk.Label(self.master, text="Buscar por nombre/material/ubicación:").grid(column=0, row=1, padx=10, pady=5)
        self.busqueda_entry = ttk.Entry(self.master)
        self.busqueda_entry.grid(column=1, row=1, padx=10, pady=5)

        buscar_button = ttk.Button(self.master, text="Buscar", command=self.buscar_proveedores)
        buscar_button.grid(column=2, row=1, padx=10, pady=5)

        # Lista de proveedores
        self.lista_proveedores = tk.Listbox(self.master, selectmode=tk.SINGLE, width=50)  # Ajusta el valor de width
        self.lista_proveedores.grid(column=0, row=2, columnspan=3, padx=10, pady=10)
        self.lista_proveedores.bind("<<ListboxSelect>>", self.seleccionar_proveedor)

        # Botón para mostrar detalles
        self.detalles_button = ttk.Button(self.master, text="Mostrar detalles", command=self.mostrar_detalles)
        self.detalles_button.grid(column=0, row=3, padx=10, pady=5)

        self.detalles_label = ttk.Label(self.master, text="Detalles del proveedor:")
        self.detalles_label.grid(column=0, row=4, columnspan=3, padx=10, pady=5)

        # Botón para agregar proveedor
        agregar_button = ttk.Button(self.master, text="Agregar Proveedor", command=self.abrir_ventana_agregar_proveedor)
        agregar_button.grid(column=0, row=5, padx=10, pady=5)

        # Botón para eliminar proveedor
        eliminar_button = ttk.Button(self.master, text="Eliminar Proveedor", command=self.eliminar_proveedor)
        eliminar_button.grid(column=2, row=5, padx=10, pady=5)

        # Cargar proveedores en la lista
        self.cargar_proveedores()

    def cargar_proveedores(self):
        self.lista_proveedores.delete(0, tk.END)
        for proveedor in self.proveedores:
            self.lista_proveedores.insert(tk.END, proveedor["nombre"])

    def filtrar_proveedores(self):
        tipo_material = self.material_combobox.get()
        self.lista_proveedores.delete(0, tk.END)

        for proveedor in self.proveedores:
            # Aseguramos que el combobox tenga los materiales correctos
            if tipo_material == "Todos" or proveedor["material"].lower() == tipo_material.lower():
                self.lista_proveedores.insert(tk.END, proveedor["nombre"])

        # Si no hay proveedores que coincidan, mostramos un mensaje
        if self.lista_proveedores.size() == 0:
            self.lista_proveedores.insert(tk.END, "No se encontraron proveedores.")

    def cargar_proveedores(self):
        self.lista_proveedores.delete(0, tk.END)
        materiales_existentes = set()

        for proveedor in self.proveedores:
            self.lista_proveedores.insert(tk.END, proveedor["nombre"])
            materiales_existentes.add(proveedor["material"])

        # Actualizar los valores del combobox con los materiales únicos
        self.material_combobox['values'] = ["Todos"] + list(materiales_existentes)

    def buscar_proveedores(self):
        criterio = self.busqueda_entry.get().lower()
        self.lista_proveedores.delete(0, tk.END)

        for proveedor in self.proveedores:
            if (criterio in proveedor["nombre"].lower() or
                    criterio in proveedor["material"].lower() or
                    criterio in proveedor["ubicación"].lower()):
                self.lista_proveedores.insert(tk.END, proveedor["nombre"])

    def seleccionar_proveedor(self, event):
        seleccion = self.lista_proveedores.curselection()
        if seleccion:
            indice = seleccion[0]
            self.proveedor_seleccionado = self.lista_proveedores.get(indice)
            if self.detalles_visibles:
                self.actualizar_detalles()

    def actualizar_detalles(self):
        if self.proveedor_seleccionado:
            for proveedor in self.proveedores:
                if proveedor["nombre"] == self.proveedor_seleccionado:
                    self.detalles_label.config(text=f"Nombre: {proveedor['nombre']}\n"
                                                    f"Material: {proveedor['material']}\n"
                                                    f"Ubicación: {proveedor['ubicación']}\n"
                                                    f"Correo: {proveedor.get('email', 'N/A')}\n"
                                                    f"Teléfono: {proveedor.get('telefono', 'N/A')}")
                    break

    def eliminar_proveedor(self):
        seleccion = self.lista_proveedores.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un proveedor para eliminar.")
            return

        indice = seleccion[0]
        proveedor_nombre = self.lista_proveedores.get(indice)

        # Confirmar eliminación
        confirmacion = messagebox.askyesno("Confirmar eliminación",
                                           f"¿Estás seguro de que deseas eliminar el proveedor '{proveedor_nombre}'?")
        if confirmacion:
            # Eliminar proveedor de la lista
            self.proveedores = [p for p in self.proveedores if p["nombre"] != proveedor_nombre]
            self.cargar_proveedores()  # Recargar la lista de proveedores
            self.detalles_label.config(text="Detalles del proveedor:")  # Limpiar detalles

            messagebox.showinfo("Éxito", "Proveedor eliminado exitosamente.")

    def mostrar_detalles(self):
        if not self.lista_proveedores.curselection():
            messagebox.showwarning("Advertencia", "Por favor, selecciona un proveedor.")
            return

        if self.detalles_visibles:
            self.detalles_label.config(text="Detalles del proveedor:")
            self.detalles_button.config(text="Mostrar detalles")
            self.detalles_visibles = False
        else:
            self.actualizar_detalles()
            self.detalles_button.config(text="Ocultar detalles")
            self.detalles_visibles = True

    def es_email_valido(self, email):
        patron_email = r"(^[\w\.-]+@[\w\.-]+\.\w+$)"
        return re.match(patron_email, email)

    def es_telefono_valido(self, telefono):
        patron_telefono = r"^\d{10}$"
        return re.match(patron_telefono, telefono)

    def agregar_proveedor_ventana(self, nombre, material, ubicacion, email, telefono, ventana):
        if not nombre or not material or not ubicacion or not email or not telefono:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        for proveedor in self.proveedores:
            if proveedor["nombre"].lower() == nombre.lower():
                messagebox.showerror("Error", "Ya existe un proveedor con este nombre")
                return

        if not self.es_email_valido(email):
            messagebox.showerror("Error", "El correo electrónico no es válido")
            return

        if not self.es_telefono_valido(telefono):
            messagebox.showerror("Error", "El número de teléfono debe ser de 10 dígitos")
            return

        nuevo_proveedor = {
            "nombre": nombre,
            "material": material,
            "ubicación": ubicacion,
            "email": email,
            "telefono": telefono
        }

        self.proveedores.append(nuevo_proveedor)
        self.lista_proveedores.insert(tk.END, nombre)

        # Actualizar la lista de materiales en el combobox de filtro
        if material not in self.material_combobox['values']:
            materiales_existentes = list(self.material_combobox['values'])
            materiales_existentes.append(material)
            self.material_combobox['values'] = materiales_existentes

        ventana.destroy()

    def abrir_ventana_agregar_proveedor(self):
        ventana_nueva = tk.Toplevel(self.master)
        ventana_nueva.title("Agregar Proveedor")
        ventana_nueva.geometry("400x350")

        ttk.Label(ventana_nueva, text="Nombre:").grid(column=0, row=0, padx=10, pady=5)
        nombre_entry = ttk.Entry(ventana_nueva)
        nombre_entry.grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(ventana_nueva, text="Material:").grid(column=0, row=1, padx=10, pady=5)
        material_entry = ttk.Entry(ventana_nueva)
        material_entry.grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(ventana_nueva, text="Ubicación:").grid(column=0, row=2, padx=10, pady=5)
        ubicacion_entry = ttk.Entry(ventana_nueva)
        ubicacion_entry.grid(column=1, row=2, padx=10, pady=5)

        ttk.Label(ventana_nueva, text="Correo:").grid(column=0, row=3, padx=10, pady=5)
        email_entry = ttk.Entry(ventana_nueva)
        email_entry.grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(ventana_nueva, text="Teléfono:").grid(column=0, row=4, padx=10, pady=5)
        telefono_entry = ttk.Entry(ventana_nueva)
        telefono_entry.grid(column=1, row=4, padx=10, pady=5)

        agregar_button = ttk.Button(ventana_nueva, text="Agregar Proveedor",
                                    command=lambda: self.agregar_proveedor_ventana(
                                        nombre_entry.get(),
                                        material_entry.get(),
                                        ubicacion_entry.get(),
                                        email_entry.get(),
                                        telefono_entry.get(),
                                        ventana_nueva))
        agregar_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = ProveedoresGUI(root)
    root.mainloop()
