import curses
from curses import wrapper
from curses.textpad import Textbox

def main(stdscr):
    curses.init_pair(1, 46, curses.COLOR_BLACK)
    
    #stdscr.nodelay(True)
    #curses.echo(True)
    stdscr.keypad(1)
    curses.curs_set(False)
    sh, sw = stdscr.getmaxyx()

    TITLE = curses.color_pair(1) | curses.A_BOLD
    TEXT = curses.color_pair(1)
    SELECT = curses.color_pair(1) | curses.A_REVERSE

    position = 5
    while True:
        stdscr.clear()

        stdscr.addstr(0, (sw - len("MENÚ PRINCIPAL")) // 2, "MENÚ PRINCIPAL", TITLE)
        stdscr.addstr(2, 1, "[1] Registrar Producto", SELECT if position == 1 else TEXT)
        stdscr.addstr(3, 1, "[2] Ver Producto", SELECT if position == 2 else TEXT)
        stdscr.addstr(4, 1, "[3] Modificar Producto", SELECT if position == 3 else TEXT)
        stdscr.addstr(5, 1, "[4] Borrar Producto", SELECT if position == 4 else TEXT)
        stdscr.addstr(7, 1, "[0] Cerrar Programa", SELECT if position == 5 else TEXT)

        key = stdscr.getkey()

        if key == '0' or key == '\n' and position == 5:
            break
        elif key == '1' or key == '\n' and position == 1:
            # Registrar Producto
            stdscr.clear()
            curses.curs_set(True)
            #curses.KEY_
            

            stdscr.addstr(0, (sw - len("REGISTRAR PRODUCTO")) // 2, "REGISTRAR PRODUCTO", TITLE)
            stdscr.addstr(2, 1, "[Nombre] ", TEXT)
            stdscr.addstr(3, 1, "[Precio] ", TEXT)
            stdscr.addstr(4, 1, "[Código] ", TEXT)
            stdscr.addstr(5, 1, "[Cantidad] ", TEXT)
            stdscr.addstr(7, 1, "GUARDAR", SELECT)
            #rectangle(stdscr, 1, 0, 8, 40)

            stdscr.refresh()

            win_name = curses.newwin(1, 20, 2, 14)
            win_name.attron(curses.color_pair(1))
            box_name = Textbox(win_name)

            win_price = curses.newwin(1, 20, 3, 14)
            win_price.attron(curses.color_pair(1))
            box_price = Textbox(win_price)

            win_code = curses.newwin(1, 20, 4, 14)
            win_code.attron(curses.color_pair(1))
            box_code = Textbox(win_code)

            win_amount = curses.newwin(1, 20, 5, 14)
            win_amount.attron(curses.color_pair(1))
            box_amount = Textbox(win_amount)

            box_name.edit()
            box_price.edit()
            box_code.edit()
            box_amount.edit()

            # stdscr.move(2, 14)
            # stdscr.move(3, 14)
            # stdscr.move(4, 14)
            # stdscr.move(5, 14)
            
            curses.curs_set(False)

        elif key == '2' or key == '\n' and position == 2:
            # Ver Producto
            pass
        elif key == '3' or key == '\n' and position == 3:
            # Modificar Producto'
            pass
        elif key == '4' or key == '\n' and position == 4:
            # Borrar Producto
            stdscr.clear()
            curses.curs_set(True)
            
            stdscr.addstr(0, (sw - len("BORRAR PRODUCTO")) // 2, "BORRAR PRODUCTO", TITLE)
            stdscr.addstr(2, 1, "[?] Indique el código del producto a borrar: ", TEXT)

            stdscr.refresh()

            win_code_delete = curses.newwin(1, 20, 2, 46)
            win_code_delete.attron(curses.color_pair(1))
            box_code_delete = Textbox(win_code_delete)

            box_code_delete.edit()

            curses.curs_set(False)

        elif key in ('KEY_DOWN', 'KEY_RIGHT'):
            position = 1 if position >= 5 else position + 1
        elif key in ('KEY_UP', 'KEY_LEFT'):
            position = 5 if position <= 1 else position - 1
        else:
            #continue
            stdscr.addstr(9, 1, f"[Error] No existe opción {key}", TEXT)
            stdscr.getch()

        #stdscr.addstr(9, 1, str(position), TEXT)
        stdscr.refresh()
        #stdscr.getch()

    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
        
if __name__ == '__main__':
    try:
        wrapper(main)
    except:
        pass