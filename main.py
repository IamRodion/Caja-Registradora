import os, yaml, time
from colorama import Style, Back, init
#import Funciones

init(autoreset=True)
COLOR_ROJO = Back.RED+Style.BRIGHT
COLOR_VERDE = Back.GREEN+Style.BRIGHT

LOGO = """
     $$$$$$\                          
    $$  __$$\                         
    $$ /  \__| $$$$$$\  $$\  $$$$$$\  
    $$ |       \____$$\ \__| \____$$\ 
    $$ |       $$$$$$$ |$$\  $$$$$$$ |
    $$ |  $$\ $$  __$$ |$$ |$$  __$$ |
    \$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$ |
     \______/  \_______|$$ | \_______|
                  $$\   $$ |          
                  \$$$$$$  |          
                   \______/           """
SALUDO = "Software de caja v0.13 -Creado por __Rodion__"

total = 0
cart = {}
reg_products = []

#-------------------------------------------------------------------------------------------------

#Creando textos de los menús
menu1 = """\t MENÚ PRINCIPAL

1) Administrar Productos
2) Abrir Caja
3) Historial de Productos
4) Cerrar Programa
"""

menu2 = """\t MENÚ DE ADMINISTRACIÓN DE PRODUCTOS

1) Mostrar Productos Registrados
2) Editar Producto Registrado
3) Eliminar Producto Registrado
4) Agregar Nuevo Producto
5) Volver al Menú Anterior
"""

menu3 = """\t CAJA REGISTRADORA
1) Registrar Nueva Compra
2) Volver al Menú Anterior
"""
#-------------------------------------------------------------------------------------------------

#Creando la clase para los produtos
class Product():

    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code
    
    def buy(self):
        if self.name in cart:
            a = cart[self.name]
            b = [1, self.price]
            cart[self.name] = [a[0] + b[0], round(a[1] + b[1], 2)]
        else:
            cart[self.name] = [1, self.price]
        global total
        total += self.price
        total = round(total, 2)
        print(f'{COLOR_VERDE}El producto "{self.name}" ha sido comprado')

    def change_price(self, new_price):
        self.price = new_price
        print(f'{COLOR_VERDE}El precio del producto "{self.name}" ha sido cambiado a $"{self.price}"')

    def change_name(self, new_name):
        self.name = new_name
        print(f'{COLOR_VERDE}El nombre del producto se cambió a "{self.name}"')

# #-------------------------------------------------------------------------------------------------

#Creando funciones
def clean_screen():
    os.system("clear || cls")

def converter(func, choice):
    try:
        converter = func(choice)
        return converter
    except:
        clean_screen()
        print(f'{COLOR_ROJO}ERROR: La opción "{choice}" no está disponible')

def create_product(name, price, code):
    new_product = Product(name, price, code)
    reg_products.append(new_product)
    return new_product

def add_product():
    print("Ingrese los datos del nuevo producto")
    name = input("Nombre: ")
    clean_screen()

    while True:
        print("Ingrese los datos del nuevo producto")
        code = input("Código: ")
        if code.isnumeric():
            codes = []
            for i in reg_products:
                codes.append(i.code)
            if code not in codes:
                clean_screen()
                break
            else:
                clean_screen()
                print(f'{COLOR_ROJO}ERROR: El código "{code}" ya está registrado')
        else:
            clean_screen()
            print(f"{COLOR_ROJO}ERROR: El valor del código debe ser numérico")

    while True:
        print("Ingrese los datos del nuevo producto")
        price = input("Precio: ")
        price = converter(float, price)
        if type(price) == float:
            break 

    create_product(name, price, code)
    clean_screen()
    print(f'{COLOR_VERDE}El producto "{name}" fue creado y guardado correctamente en el registo')

def show_products():
    print("CÓDIGO\tPRECIO\tNOMBRE")
    for i in reg_products:
        print(f"{i.code}\t${i.price}\t{i.name}")

def del_product():
    while True:
        code = input("¿Código del producto que desea eliminar?: ")
        if code.isnumeric():
            codes = []
            for i in reg_products:
                codes.append(i.code)
            if code in codes:
                clean_screen()
                for i in reg_products:
                    if i.code == code:
                        reg_products.remove(i)
                        clean_screen()
                        print(f'{COLOR_VERDE}El producto "{i.name}" fue eliminado del registro')
                    else:
                        continue
                break
            else:
                clean_screen()
                print(f'{COLOR_ROJO}ERROR: El código "{code}" no está registrado')
        else:
            clean_screen()
            print(f"{COLOR_ROJO}ERROR: El valor del código debe ser numérico")

def edit_product():
    while True:
        while True:
            code = input("¿Cual es el código del producto que desea editar?: ")
            if code.isnumeric():
                codes = []
                for i in reg_products:
                    codes.append(i.code)
                if code in codes:
                    clean_screen()
                    break
                else:
                    clean_screen()
                    print(f'{COLOR_ROJO}ERROR: El código "{code}" no está registrado')
            else:
                clean_screen()
                print(f"{COLOR_ROJO}ERROR: El valor del código debe ser numérico")

        while True:
            price = input("¿Que precio desea establecer?: ")
            price = converter(float, price)
            if type(price) == float:
                clean_screen()
                break

        name = input("¿Que nombre desea establecer?: ")

        for i in reg_products:
            if i.code == code:
                clean_screen()
                i.change_name(name)
                i.change_price(price)
            else:
                continue
        break

def caja():
    while True:
        code_to_buy = input('·Código del producto a comprar ("S" para subtotal o "T" para total): ')

        if code_to_buy.isnumeric():
            codes = []
            for i in reg_products:
                codes.append(i.code)
            if code_to_buy in codes:
                clean_screen()
                for i in reg_products:
                    if code_to_buy == i.code:
                        clean_screen
                        i.buy()
                    else:
                        continue
            else:
                clean_screen()
                print(f'{COLOR_ROJO}ERROR: El código "{code_to_buy}" no está registrado')

        elif code_to_buy == "t" or code_to_buy == "T":
            clean_screen()
            print("CANTIDAD\tPRECIO\tNOMBRE")
            for i in cart:
                print(f"\t{cart[i][0]}\t${cart[i][1]}\t{i}")
            print("--------------------------------")
            print(f"Total-------------------${total}")
            print()

            fecha = time.strftime("%d-%m-%Y %H:%M:%S")
            registro_clave = {fecha:{}}

            for i in cart:
                registro_clave[fecha].update({i:{"Cantidad":cart[i][0], "Precio":cart[i][1]}})
                registro_clave[fecha].update({f"Total":total})
            
            with open('Historial.yaml', 'a') as file:
                yaml.dump(registro_clave, file)
            break

        elif code_to_buy == "s" or code_to_buy == "S":
            clean_screen()
            print("CANTIDAD\tPRECIO\tNOMBRE")
            for i in cart:
                print(f"\t{cart[i][0]}\t${cart[i][1]}\t{i}")
            print("--------------------------------")
            print(f"Total-------------------${total}")
            print()

        else:
            clean_screen()
            print(f"{COLOR_ROJO}ERROR: El valor del código debe ser numérico")


def history():
    if os.name == "posix":
        os.system("nano -v Historial.yaml")
    elif os.name == "nt" or os.name == "java":
        os.system("Historial.yaml")
    else:
        print(f"{COLOR_ROJO}ERROR: No se puede abrir el archivo")

#-------------------------------------------------------------------------------------------------

#Creando productos pre-Registrados
create_product("Papa", 1.13, "0")
create_product("Arroz", 1.35, "1")
create_product("Pasta", 1.10, "2")
create_product("Avena", 1.54, "3")

#-------------------------------------------------------------------------------------------------
#Loop principal
def app():
    clean_screen()

    while True:
        print(SALUDO)
        print(LOGO)
        print("")
        print(menu1)
        choice = input("Elija una opción: ")

        if choice == "4":
            break

        elif choice == "1":
            clean_screen()
            
            while True:
                print(menu2)
                choice = input("Elija una opción: ")

                if choice == "5":
                    clean_screen()
                    break

                elif choice == "1":
                    clean_screen()
                    if len(reg_products) == 0:
                        print(f"{COLOR_ROJO}ERROR: No hay productos registrados")
                    else:
                        show_products()
                        print("")

                elif choice == "2":
                    clean_screen()
                    if len(reg_products) == 0:
                        print(f"{COLOR_ROJO}ERROR: No hay productos registrados")
                    else:
                        edit_product()
                    
                elif choice == "3":
                    clean_screen()
                    if len(reg_products) == 0:
                        print(f"{COLOR_ROJO}ERROR: No hay productos registrados")
                    else:
                        del_product()

                elif choice == "4":
                    clean_screen()
                    add_product()

                else:
                    clean_screen()
                    print(f"{COLOR_ROJO}ERROR: La opción indicada no existe")

        elif choice == "2":
            clean_screen()
            while True:
                print(menu3)
                choice = input("Elija una opción: ")
                if choice == "1":
                    clean_screen()
                    caja()
                    global cart 
                    cart = {}
                    global total
                    total = 0
                elif choice == "2":
                    clean_screen()
                    break
                else:
                    clean_screen()
                    print(f"{COLOR_ROJO}ERROR: La opción indicada no existe")


        elif choice == "3":
            clean_screen()
            history()

        else:
            clean_screen()
            print(f"{COLOR_ROJO}ERROR: La opción indicada no existe")   

if __name__ == "__main__":
    app()
