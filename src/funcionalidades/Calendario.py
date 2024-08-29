from datetime import datetime, timedelta

# Diccionario para almacenar eventos (Ejemplos)
events = {
    '2024-08-28': {
        'name': 'Limpieza de Playa',
        'requester': 'Fundación Ambiental',
        'location': 'Playa del Sol',
        'start_date': '2024-08-28',
        'end_date': '2024-08-28',
        'materials': {
            'Bolsas de Basura': {'required': 100, 'inventory': 80, 'missing': 20},
            'Guantes': {'required': 50, 'inventory': 40, 'missing': 10},
            'Pala': {'required': 10, 'inventory': 8, 'missing': 2}
        }
    },
    '2024-09-01': {
        'name': 'Jornada de Salud',
        'requester': 'Cruz Roja',
        'location': 'Centro Comunitario',
        'start_date': '2024-09-01',
        'end_date': '2024-09-02',
        'materials': {
            'Mascarillas': {'required': 200, 'inventory': 150, 'missing': 50},
            'Guantes': {'required': 100, 'inventory': 80, 'missing': 20},
            'Termómetros': {'required': 20, 'inventory': 15, 'missing': 5}
        }
    },
    '2024-09-10': {
        'name': 'Taller de Reciclaje',
        'requester': 'EcoAmigos',
        'location': 'Escuela Primaria',
        'start_date': '2024-09-10',
        'end_date': '2024-09-11',
        'materials': {
            'Papel': {'required': 100, 'inventory': 80, 'missing': 20},
            'Tijeras': {'required': 50, 'inventory': 40, 'missing': 10},
            'Pegamento': {'required': 30, 'inventory': 25, 'missing': 5}
        }
    },
    '2024-09-15': {
        'name': 'Foro de Políticas Públicas',
        'requester': 'Gobierno Local',
        'location': 'Auditorio Municipal',
        'start_date': '2024-09-15',
        'end_date': '2024-09-17',
        'materials': {
            'Sillas': {'required': 200, 'inventory': 180, 'missing': 20},
            'Mesas': {'required': 20, 'inventory': 18, 'missing': 2},
            'Proyector': {'required': 2, 'inventory': 2, 'missing': 0},
            'Micrófono': {'required': 5, 'inventory': 4, 'missing': 1}
        }
    },
    '2024-09-20': {
        'name': 'Feria de Emprendimiento',
        'requester': 'Cámara de Comercio',
        'location': 'Plaza Mayor',
        'start_date': '2024-09-20',
        'end_date': '2024-09-21',
        'materials': {
            'Stands': {'required': 100, 'inventory': 90, 'missing': 10},
            'Sillas': {'required': 200, 'inventory': 180, 'missing': 20},
            'Mesas': {'required': 50, 'inventory': 45, 'missing': 5}
        }
    },
    '2024-10-05': {
        'name': 'Festival de Música',
        'requester': 'Asociación Cultural',
        'location': 'Parque Central',
        'start_date': '2024-10-05',
        'end_date': '2024-10-07',
        'materials': {
            'Escenario': {'required': 1, 'inventory': 1, 'missing': 0},
            'Sillas': {'required': 300, 'inventory': 250, 'missing': 50},
            'Micrófono': {'required': 10, 'inventory': 8, 'missing': 2}
        }
    },
    '2024-10-15': {
        'name': 'Conferencia de Tecnología',
        'requester': 'Universidad Local',
        'location': 'Centro de Convenciones',
        'start_date': '2024-10-15',
        'end_date': '2024-10-16',
        'materials': {
            'Proyector': {'required': 5, 'inventory': 4, 'missing': 1},
            'Sillas': {'required': 500, 'inventory': 450, 'missing': 50},
            'Mesas': {'required': 50, 'inventory': 45, 'missing': 5}
        }
    },
    '2024-10-25': {
        'name': 'Día de la Comunidad',
        'requester': 'Asociación Vecinal',
        'location': 'Parque del Barrio',
        'start_date': '2024-10-25',
        'end_date': '2024-10-25',
        'materials': {
            'Mesas': {'required': 20, 'inventory': 18, 'missing': 2},
            'Sillas': {'required': 100, 'inventory': 90, 'missing': 10},
            'Carpas': {'required': 5, 'inventory': 4, 'missing': 1}
        }
    }
}


# Función para mostrar el calendario en consola
def print_calendar(year, month):
    print(f"Calendario de {year}-{month:02d}")
    print("Lu Ma Mi Ju Vi Sá Do")

    # Obtener el primer día del mes
    first_day = datetime(year, month, 1)
    start_day = first_day.weekday()  # 0 = Lunes, 6 = Domingo

    # Imprimir espacios en blanco para los días antes del primer día del mes
    print("   " * start_day, end="")

    # Imprimir los días del mes
    current_date = first_day
    while current_date.month == month:
        day_str = f"{current_date.day:02d}"
        if any(event['start_date'] <= current_date.strftime('%Y-%m-%d') <= event['end_date'] for event in
               events.values()):
            day_str = f"\033[1m{day_str}\033[0m"  # Negrita
        print(day_str, end=" ")
        if current_date.weekday() == 6:  # Domingo
            print()
        current_date += timedelta(days=1)
    print()


# Función para mostrar detalles del evento en consola
def show_event_details(date):
    found = False
    for event in events.values():
        start_date = datetime.strptime(event['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(event['end_date'], '%Y-%m-%d')
        current_date = datetime.strptime(date, '%Y-%m-%d')

        # Verifica si la fecha ingresada está dentro del rango del evento
        if start_date <= current_date <= end_date:
            print(f"Evento: {event['name']}")
            print(f"Solicitante: {event['requester']}")
            print(f"Lugar: {event['location']}")
            print(f"Fecha de Inicio: {event['start_date']}")
            print(f"Fecha de Fin: {event['end_date']}")
            print("Materiales:")
            for item, quantity in event['materials'].items():
                print(
                    f"  {item}: Requeridos: {quantity['required']}, En Inventario: {quantity['inventory']}, Faltante: {quantity['missing']}")
            print()  # Salto de línea entre eventos
            found = True

    if not found:
        print("No hay eventos en esta fecha.")


# Función principal para navegar entre meses y consultar eventos
def main():
    year = 2024
    month = 8

    while True:
        print_calendar(year, month)

        print("1. Mes siguiente")
        print("2. Mes anterior")
        print("3. Consultar detalles de un evento")
        print("4. Salir")

        action = input("Seleccione una opción: ").strip()

        if action == '1':
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        elif action == '2':
            if month == 1:
                month = 12
                year -= 1
            else:
                month -= 1
        elif action == '3':
            day_input = input("Ingrese el día del mes para consultar detalles del evento (DD): ").strip()
            date_input = f"{year}-{month:02d}-{int(day_input):02d}"
            show_event_details(date_input)
        elif action == '4':
            break
        else:
            print("Acción no válida. Intente de nuevo.")


# Ejecutar la función principal
main()
