import curses

def main(stdscr):
    # Configurar la pantalla
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Obtener el tamaño de la pantalla
    sh, sw = stdscr.getmaxyx()

    # Crear los campos a llenar
    fields = [
        {"name": "Nombre", "value": "", "type": str},
        {"name": "Precio", "value": None, "type": float},
        {"name": "Código", "value": "", "type": str},
        {"name": "Cantidad", "value": None, "type": int}
    ]

    # Índice del campo actualmente seleccionado
    current_field = 0

    while True:
        stdscr.clear()

        # Mostrar el título del menú
        title = "REGISTRAR PRODUCTO"
        stdscr.addstr(0, (sw - len(title)) // 2, title)

        # Mostrar los campos a llenar
        for i, field in enumerate(fields):
            name = field["name"]
            value = field["value"]
            field_type = field["type"]

            # Determinar el color del campo
            if value is None:
                color = curses.color_pair(1)  # Campo vacío
            else:
                color = curses.color_pair(2)  # Campo lleno

            # Mostrar el nombre del campo
            stdscr.addstr(i + 2, 2, name)

            # Mostrar el valor del campo
            if value is None:
                stdscr.addstr(i + 2, 20, "")
            else:
                stdscr.addstr(i + 2, 20, str(value))

            # Resaltar el campo actualmente seleccionado
            if i == current_field:
                stdscr.addstr(i + 2, 2, name, curses.A_REVERSE)

        # Mostrar la opción "guardar"
        if all(field["value"] is not None for field in fields):
            save_option = "[GUARDAR]"
            stdscr.addstr(sh - 2, (sw - len(save_option)) // 2, save_option, curses.A_REVERSE)
        else:
            save_option = "[GUARDAR]"
            stdscr.addstr(sh - 2, (sw - len(save_option)) // 2, save_option)

        # Obtener la tecla presionada por el usuario
        key = stdscr.getch()

        # Navegar entre los campos utilizando las flechas del teclado
        if key == curses.KEY_UP:
            current_field = max(current_field - 1, 0)
        elif key == curses.KEY_DOWN:
            current_field = min(current_field + 1, len(fields) - 1)
        # Escribir en el campo actualmente seleccionado
        elif key != -1:
            field = fields[current_field]
            value = field["value"]
            field_type = field["type"]

            if value is None:
                if field_type == str:
                    field["value"] = chr(key)
                elif field_type == int:
                    try:
                        field["value"] = int(chr(key))
                    except ValueError:
                        pass
                elif field_type == float:
                    try:
                        field["value"] = float(chr(key))
                    except ValueError:
                        pass
            else:
                if field_type == str:
                    field["value"] += chr(key)

    stdscr.refresh()

# Inicializar curses y ejecutar el menú
curses.wrapper(main)