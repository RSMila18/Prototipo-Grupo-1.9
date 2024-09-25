import tkinter as tk
from tkinter import ttk, messagebox
from gestorAplicacion.Evento import Evento

# Cargar eventos al iniciar
Evento.cargar_eventos()

class MonitoreoMateriales(tk.Frame):
    def __init__(self, master=None, regresar_callback=None):
        super().__init__(master)
        self.master = master
        self.regresar_callback = regresar_callback
        self.pack(pady=10, padx=10)
        self.create_widgets()

    def create_widgets(self):
        # Título
        self.label_titulo = tk.Label(self, text="Monitoreo de Materiales para Eventos", font=("Arial", 16, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=10, sticky="w")

        # Botón para regresar
        self.btn_salir = tk.Button(self, text="Regresar", command=self.regresar)
        self.btn_salir.grid(row=0, column=1, pady=10, sticky="e", padx=10)

        # Selección de evento
        self.label_eventos = tk.Label(self, text="Seleccione el evento para ver los materiales:")
        self.label_eventos.grid(row=1, column=0, padx=10, pady=10)

        self.combo_eventos = ttk.Combobox(self, values=[evento.nombre for evento in Evento.eventos_registrados], state="readonly")
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

    def mostrar_materiales(self, event):
        # Limpiar la tabla antes de agregar nuevos datos
        for item in self.tree_materiales.get_children():
            self.tree_materiales.delete(item)

        evento_seleccionado = self.combo_eventos.get()

        # Mostrar los materiales asignados al evento
        for evento in Evento.eventos_registrados:
            if evento.nombre == evento_seleccionado:
                for material in evento.materiales:
                    self.tree_materiales.insert("", "end", values=(material.nombre, material.cantidad, material.estado))
                break

    def mostrar_historial(self):
        selected_item = self.tree_materiales.selection()
        if selected_item:
            material_seleccionado = self.tree_materiales.item(selected_item, "values")[0]

            # Busca el material seleccionado en el evento actual
            evento_seleccionado = self.combo_eventos.get()
            for evento in Evento.eventos_registrados:
                if evento.nombre == evento_seleccionado:
                    for material in evento.materiales:
                        if material.nombre == material_seleccionado:
                            # Desbloquear el área de texto y mostrar el historial
                            self.historial_text.config(state=tk.NORMAL)
                            self.historial_text.delete(1.0, tk.END)  # Limpiar el área de texto
                            self.historial_text.insert(tk.END, material.obtener_historial())
                            self.historial_text.config(state=tk.DISABLED)  # Bloquear nuevamente el área de texto
                            return
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un material para ver su historial.")

    def regresar(self):
        if self.regresar_callback:
            self.regresar_callback()  # Llama al método que fue pasado como callback (en este caso, self.regresar_menu)
        else:
            self.master.destroy()  # En caso de que no haya callback, cierra la ventana (no necesario aquí)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monitoreo de Materiales para Eventos")
    root.geometry("750x550")

    def regresar_al_menu_principal():
        messagebox.showinfo("Regreso", "Volviendo al menú principal...")
        app.destroy()

    app = MonitoreoMateriales(master=root, regresar_callback=regresar_al_menu_principal)
    app.mainloop()
