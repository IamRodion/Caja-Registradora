from models import Product
from db.manage import db
from os import system

MENU1 = """\tCAJA REGISTRADORA\n
[1] Registrar Producto
[2] Ver Producto
[3] Modificar Producto
[4] Borrar Producto

[0] Cerrar Programa
\n>> """

MENU2 = """\tREGISTRAR PRODUCTO\n
[i] Indique los datos  del producto"""

def clear_screen():
    system('clear')

def create_product():
    obj = Product()
    obj.change_name(input("Nuevo nombre: "))
    obj.change_price(input("Nuevo precio: "))
    obj.change_code(input("Nuevo código: "))
    obj.change_amount(input("Nueva cantidad: "))
    return obj

def menu():
    pass


def app():
    while True:
        clear_screen()
        
        OPTION = input(MENU1)
        match OPTION:
            case '0':
                break
            case '1':
                product = create_product()
                product.insert()
            case '2':
                pass
            case '3':
                pass
            case '4':
                code_to_delete = input('[?] Indique el código del producto a borrar: ')
                product = Product(code=code_to_delete)
                product.delete()
            case _:
                input(f'[!] La opción "{OPTION}" no es correcta.')

    #db.connect()

    #product = create_product()

    #product.insert()
    #product.get()
    #product.update()
    #product.delete()

    #db.disconnect()

if __name__ == '__main__':
    db.connect()
    app()
    db.disconnect()