import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, timedelta


class CalendarioInteractivo:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendario Interactivo")

        # Obtener la fecha actual
        today = datetime.now()

        # Inicializar el calendario con la fecha actual
        self.cal = Calendar(master, selectmode='day', year=today.year, month=today.month, day=today.day, font=('Arial', 14), width=20, height=8)
        self.cal.pack(pady=20)

        self.event_dates = {}
        self.create_event_button = tk.Button(master, text="Agregar Evento", command=self.show_event_form)
        self.create_event_button.pack(pady=10)

        self.events = {}  # Diccionario para almacenar eventos
        self.cal.bind("<<CalendarSelected>>", self.show_event_details)  # Vincular clic en calendario

        # Para almacenar el frame desplegable del calendario
        self.calendar_popup = None

        # Añadir eventos de ejemplo
        self.add_example_events()

    def add_example_events(self):
        example_events = [
            {
                'name': 'Reunión de Proyecto',
                'requester': 'Juan Pérez',
                'location': 'Sala de Conferencias',
                'start_date': '2024-09-25',
                'end_date': '2024-09-25',
                'materials': {'Proyector': {'required': 1, 'missing': 1}, 'Sillas': {'required': 10, 'missing': 10}}
            },
            {
                'name': 'Taller de Capacitación',
                'requester': 'María Gómez',
                'location': 'Aula 101',
                'start_date': '2024-09-26',
                'end_date': '2024-09-27',
                'materials': {'Computadoras': {'required': 5, 'missing': 5}, 'Mesas': {'required': 5, 'missing': 5}}
            }
        ]

        for event in example_events:
            start_date_obj = datetime.strptime(event['start_date'], '%Y-%m-%d').date()
            end_date_obj = datetime.strptime(event['end_date'], '%Y-%m-%d').date()

            current_date = start_date_obj
            while current_date <= end_date_obj:
                date_str = current_date.strftime('%Y-%m-%d')
                self.events[date_str] = event
                current_date += timedelta(days=1)

        self.update_calendar_events()

    def show_event_form(self):
        event_form = tk.Toplevel(self.master)
        event_form.title("Agregar Evento")

        tk.Label(event_form, text="Nombre del Evento:").grid(row=0, column=0)
        self.event_name_entry = tk.Entry(event_form)
        self.event_name_entry.grid(row=0, column=1)

        tk.Label(event_form, text="Solicitante:").grid(row=1, column=0)
        self.requester_entry = tk.Entry(event_form)
        self.requester_entry.grid(row=1, column=1)

        tk.Label(event_form, text="Lugar:").grid(row=2, column=0)
        self.location_entry = tk.Entry(event_form)
        self.location_entry.grid(row=2, column=1)

        tk.Label(event_form, text="Fecha de Inicio:").grid(row=3, column=0)
        self.start_date_entry = tk.Entry(event_form)
        self.start_date_entry.grid(row=3, column=1)
        self.start_date_button = tk.Button(event_form, text="Seleccionar", command=lambda: self.show_calendar(event_form, "start", self.start_date_entry))
        self.start_date_button.grid(row=3, column=2)

        tk.Label(event_form, text="Fecha de Fin:").grid(row=4, column=0)
        self.end_date_entry = tk.Entry(event_form)
        self.end_date_entry.grid(row=4, column=1)
        self.end_date_button = tk.Button(event_form, text="Seleccionar", command=lambda: self.show_calendar(event_form, "end", self.end_date_entry))
        self.end_date_button.grid(row=4, column=2)

        # Sección para agregar materiales
        tk.Label(event_form, text="Tipo de Material:").grid(row=5, column=0)
        self.material_entry = tk.Entry(event_form)
        self.material_entry.grid(row=5, column=1)

        tk.Label(event_form, text="Cantidad:").grid(row=5, column=2)
        self.quantity_entry = tk.Entry(event_form)
        self.quantity_entry.grid(row=5, column=3)

        self.material_listbox = tk.Listbox(event_form, width=50)
        self.material_listbox.grid(row=6, column=0, columnspan=4)

        self.add_material_button = tk.Button(event_form, text="Agregar Material", command=self.add_material)
        self.add_material_button.grid(row=7, column=0, columnspan=4)

        # Botón para guardar el evento
        self.save_event_button = tk.Button(event_form, text="Guardar Evento", command=lambda: self.save_event(event_form))
        self.save_event_button.grid(row=8, column=0, columnspan=4)

    def show_calendar(self, parent, date_type, entry_widget):
        # Si ya hay un calendario desplegado, lo destruye
        if self.calendar_popup:
            self.calendar_popup.destroy()

        # Crear un Frame que actúe como menú desplegable
        self.calendar_popup = tk.Frame(parent, borderwidth=1, relief="solid")
        self.calendar_popup.place(x=entry_widget.winfo_x(), y=entry_widget.winfo_y() + entry_widget.winfo_height())

        # Crear un calendario dentro del frame desplegable
        calendar = Calendar(self.calendar_popup, selectmode='day')
        calendar.pack(pady=5)

        # Función para seleccionar la fecha
        def select_date():
            selected_date = calendar.selection_get()
            today = datetime.now().date()

            if selected_date < today:
                messagebox.showwarning("Advertencia", "No se puede seleccionar una fecha pasada.")
                return

            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, selected_date.strftime('%Y-%m-%d'))

            # Verificar si es la fecha de fin y comparar con la fecha de inicio
            if date_type == "end":
                start_date_str = self.start_date_entry.get()
                if start_date_str:
                    start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    if selected_date < start_date_obj:
                        messagebox.showwarning("Advertencia",
                                               "La fecha de fin no puede ser anterior a la fecha de inicio. Por favor elija una fecha correcta.")
                        entry_widget.delete(0, tk.END)  # Limpiar el campo de fecha de fin
                        return

            # Verificar si la fecha ya tiene un evento programado
            if selected_date.strftime('%Y-%m-%d') in self.events:
                messagebox.showwarning("Advertencia",
                                       "Ya hay un evento programado para esta fecha. Por favor elija otra.")
                entry_widget.delete(0, tk.END)  # Limpiar el campo de fecha
                return

            self.calendar_popup.destroy()  # Cerrar el "desplegable" al seleccionar la fecha
            self.calendar_popup = None

        # Botón para cerrar el calendario sin seleccionar una fecha
        def close_calendar():
            self.calendar_popup.destroy()
            self.calendar_popup = None

        # Botón para seleccionar la fecha
        select_button = tk.Button(self.calendar_popup, text="Seleccionar Fecha", command=select_date)
        select_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Botón para cerrar el calendario
        close_button = tk.Button(self.calendar_popup, text="Cerrar", command=close_calendar, bg="red", fg="white")
        close_button.pack(side=tk.LEFT, padx=5, pady=5)

    def add_material(self):
        material_name = self.material_entry.get()
        quantity = self.quantity_entry.get()

        if material_name and quantity.isdigit():
            self.material_listbox.insert(tk.END, f"{material_name}: {quantity}")
            self.material_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa un nombre de material válido y una cantidad.")

    def save_event(self, event_form):
        event_name = self.event_name_entry.get()
        requester = self.requester_entry.get()
        location = self.location_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        if not all([event_name, requester, location, start_date, end_date]):
            messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            return

        # Convertir las fechas
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.strptime(end_date, '%Y-%m-%d').date()

        # Verificación de solapamiento
        for key, details in self.events.items():
            existing_start_date = datetime.strptime(details['start_date'], '%Y-%m-%d').date()
            existing_end_date = datetime.strptime(details['end_date'], '%Y-%m-%d').date()
            if (start_date_obj <= existing_end_date and end_date_obj >= existing_start_date):
                messagebox.showwarning("Advertencia",
                                       "Las fechas se solapan con un evento ya programado. Por favor elige otras fechas.")
                return

        # Guardar los materiales
        materials = {}
        for item in self.material_listbox.get(0, tk.END):
            material_name, quantity = item.split(": ")
            materials[material_name] = {'required': int(quantity), 'missing': int(quantity)}

        # Guardar el evento
        self.events[start_date] = {
            'name': event_name,
            'requester': requester,
            'location': location,
            'start_date': start_date,
            'end_date': end_date,
            'materials': materials
        }

        # Marcar todas las fechas ocupadas
        current_date = start_date_obj
        while current_date <= end_date_obj:
            self.events[current_date.strftime('%Y-%m-%d')] = {
                'name': event_name,
                'requester': requester,
                'location': location,
                'start_date': start_date,
                'end_date': end_date,
                'materials': materials
            }
            current_date += timedelta(days=1)

        # Actualizar el calendario
        self.update_calendar_events()

        event_form.destroy()  # Cerrar la ventana de agregar evento

    def update_calendar_events(self):
        for key, details in self.events.items():
            start_date = datetime.strptime(details['start_date'], '%Y-%m-%d').date()
            end_date = datetime.strptime(details['end_date'], '%Y-%m-%d').date()
            current_date = start_date
            while current_date <= end_date:
                date_str = current_date.strftime('%Y-%m-%d')
                self.event_dates[date_str] = details
                self.cal.calevent_create(current_date, details['name'], 'event')
                current_date += timedelta(days=1)
        self.cal.tag_config('event', background='yellow', foreground='black')

    def show_event_details(self, event):
        selected_date = self.cal.selection_get().strftime('%Y-%m-%d')
        event_found = False

        # Revisar todos los eventos en event_dates
        for key, details in self.event_dates.items():
            if key == selected_date or (details['start_date'] <= selected_date <= details['end_date']):
                event_found = True
                details_message = (
                    f"Evento: {details['name']}\n"
                    f"Solicitante: {details['requester']}\n"
                    f"Lugar: {details['location']}\n"
                    f"Fecha de Inicio: {details['start_date']}\n"
                    f"Fecha de Fin: {details['end_date']}\n"
                    "Materiales:\n"
                )
                for material, info in details['materials'].items():
                    details_message += f" - {material}: {info['required']} (Faltante: {info['missing']})\n"

                messagebox.showinfo("Detalles del Evento", details_message)
                break

        if not event_found:
            messagebox.showinfo("Detalles del Evento", "No hay eventos programados para esta fecha.")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarioInteractivo(root)
    root.mainloop()
