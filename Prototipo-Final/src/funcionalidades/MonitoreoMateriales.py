import tkinter as tk
from tkinter import ttk, messagebox

# Simulación de la información de eventos y materiales
eventos_materiales = {
    "Evento A": [
        {"material": "Sillas", "cantidad": 50, "estado": "Adquirido"},
        {"material": "Mesas", "cantidad": 10, "estado": "En proceso"},
    ],
    "Evento B": [
        {"material": "Proyector", "cantidad": 2, "estado": "Adquirido"},
        {"material": "Micrófonos", "cantidad": 5, "estado": "Pendiente"},
    ]
}

# Simulación del historial de actualizaciones de materiales
historial_materiales = {
    "Sillas": [
        {"fecha": "21/09/2024", "accion": "Compra realizada", "cantidad": 50},
        {"fecha": "22/09/2024", "accion": "Entrega completada", "cantidad": 50},
    ],
    "Mesas": [
        {"fecha": "20/09/2024", "accion": "Orden de compra", "cantidad": 10},
    ]
}

class MonitoreoMateriales(tk.Frame):
    def __init__(self, master=None, regresar_callback=None):  # Se añade el callback de regresar
        super().__init__(master)
        self.master = master
        self.regresar_callback = regresar_callback  # Guardamos el callback
        self.pack(pady=10, padx=10)
        self.create_widgets()

    def create_widgets(self):
        
       
        # Título
        self.label_titulo = tk.Label(self, text="Monitoreo de Materiales para Eventos", font=("Arial", 16, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=10, sticky="w")  # Alineado a la izquierda

        # Botón para regresar
        self.btn_salir = tk.Button(self, text="Salir", command=self.regresar)
        self.btn_salir.grid(row=0, column=1, pady=10, sticky="e", padx=10)  # Alineado a la derecha

        # Selección de evento
        self.label_eventos = tk.Label(self, text="Seleccione el evento para ver los materiales:")
        self.label_eventos.grid(row=1, column=0, padx=10, pady=10)

        self.combo_eventos = ttk.Combobox(self, values=list(eventos_materiales.keys()), state="readonly")
        self.combo_eventos.grid(row=1, column=1, padx=10, pady=10)
        self.combo_eventos.bind("<<ComboboxSelected>>", self.mostrar_materiales)

        # Lista de materiales
        self.label_lista_materiales = tk.Label(self, text="Lista de materiales asignados:")
        self.label_lista_materiales.grid(row=2, column=0, padx=10, pady=10)

        self.tree_materiales = ttk.Treeview(self, columns=("Material", "Cantidad", "Estado"), show="headings")
        self.tree_materiales.heading("Material", text="Material")
        self.tree_materiales.heading("Cantidad", text="Cantidad")
        self.tree_materiales.heading("Estado", text="Estado")
        self.tree_materiales.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Botón para ver historial
        self.button_historial = tk.Button(self, text="Ver Historial de Material", command=self.mostrar_historial, width=30)
        self.button_historial.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Área de texto para mostrar el historial
        self.historial_text = tk.Text(self, width=60, height=10, state=tk.DISABLED)
        self.historial_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def regresar(self):
        # Aquí puedes elegir si deseas destruir la ventana actual o simplemente ocultarla.
        self.destroy()  # Esto cierra la ventana actual

        # Alternativa: Si deseas ocultarla, usa:
        #self.withdraw()

        # Asegúrate de que la ventana anterior se muestre. Esto depende de cómo gestionas las ventanas.
        self.parent_window.deiconify()  # Esto muestra la ventana anterior si fue ocultada.


    def mostrar_materiales(self, event):
        # Limpiar la tabla antes de agregar nuevos datos
        for item in self.tree_materiales.get_children():
            self.tree_materiales.delete(item)

        evento_seleccionado = self.combo_eventos.get()

        # Mostrar los materiales asignados al evento
        if evento_seleccionado in eventos_materiales:
            materiales = eventos_materiales[evento_seleccionado]
            for material in materiales:
                self.tree_materiales.insert("", "end", values=(material["material"], material["cantidad"], material["estado"]))

    def mostrar_historial(self):
        # Obtener el material seleccionado
        selected_item = self.tree_materiales.selection()
        if selected_item:
            material_seleccionado = self.tree_materiales.item(selected_item, "values")[0]

            # Limpiar el área de texto antes de mostrar el historial
            self.historial_text.config(state=tk.NORMAL)
            self.historial_text.delete(1.0, tk.END)

            # Mostrar el historial del material seleccionado
            if material_seleccionado in historial_materiales:
                self.historial_text.insert(tk.END, f"Historial de {material_seleccionado}:\n")
                for update in historial_materiales[material_seleccionado]:
                    self.historial_text.insert(tk.END, f"Fecha: {update['fecha']}, Acción: {update['accion']}, Cantidad: {update['cantidad']}\n")
            else:
                self.historial_text.insert(tk.END, "No hay historial disponible para este material.\n")
            
            self.historial_text.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un material para ver su historial.")

    def regresar(self):
        """Método para regresar a la ventana anterior."""
        if self.regresar_callback:
            self.regresar_callback()  # Llama al callback para regresar al menú anterior
        else:
            self.master.destroy()  # Si no hay callback, cierra la ventana actual


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monitoreo de Materiales para Eventos")
    root.geometry("750x550")
    
    def regresar_al_menu_principal():
        # Aquí iría la lógica para regresar al menú principal.
        # Por ejemplo, puedes destruir el Frame actual y mostrar otro frame.
        messagebox.showinfo("Regreso", "Volviendo al menú principal...")
        app.destroy()

    app = MonitoreoMateriales(master=root, regresar_callback=regresar_al_menu_principal)
    app.mainloop()
