import os

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
SALUDO = "Software de caja v0.11 -Creado por __Rodion__"

total = []
cart = []
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
#-------------------------------------------------------------------------------------------------

#Creando la clase para los produtos
class Product():

    def __init__(self, name, price, code):
        self.name = name
        self.price = price
        self.code = code
    
    def buy(self):
        cart.append(self.name)
        total.append(self.price)
        print(f'El producto "{self.name}" ha sido comprado')

    def change_price(self, new_price):
        self.price = new_price
        print(f'El precio del producto "{self.name}" ha sido cambiado a "{self.price}"')

    def change_name(self, new_name):
        self.name = new_name
        print(f'El nombre del producto se cambió a "{self.name}"')

#-------------------------------------------------------------------------------------------------

#Creando funciones
def clean_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "java" or os.name == "nt":
        os.system("cls")

def converter(func, choice):
    try:
        converter = func(choice)
        return converter
    except:
        clean_screen()
        print(f'La opción "{choice}" no está disponible')

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
        code = converter(int, code)
        if type(code) == int:
            codes = []
            for i in reg_products:
                codes.append(i.code)
            if code not in codes:
                clean_screen()
                break
            else:
                clean_screen()
                print(f'El código "{code}" ya está registrado')

    while True:
        print("Ingrese los datos del nuevo producto")
        price = input("Precio: ")
        price = converter(float, price)
        if type(price) == float:
            break 

    create_product(name, price, code)
    clean_screen()
    print(f'El producto "{name}" fue creado y guardado correctamente en el registo')

def show_products():
    print("CÓDIGO\tNOMBRE\tPRECIO")
    for i in reg_products:
        print(f"{i.code}\t{i.name}\t${i.price}")

def del_product(code):
    for i in reg_products:
        if i.code == code:
            reg_products.remove(i)
            clean_screen()
            print(f'El producto "{i.name}" fue eliminado del registro')
        else:
            continue

def edit_product(code):
    for i in reg_products:
        if i.code == code:
            clean_screen()
            i.change_name(name)
            i.change_price(price)
        else:
            continue

#-------------------------------------------------------------------------------------------------

#Creando productos pre-Registrados
create_product("Papa", 1.13, 0)
create_product("Arroz", 1.35, 1)
create_product("Pasta", 1.10, 2)
create_product("Avena", 1.54, 3)

#-------------------------------------------------------------------------------------------------

#Loop principal
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
                show_products()
                print("")

            elif choice == "2":
                clean_screen()
                while True:
                    while True:
                        code = input("¿Cual es el código del producto que desea editar?: ")
                        code = converter(int, code)
                        if type(code) == int:
                            codes = []
                            for i in reg_products:
                                codes.append(i.code)
                            if code in codes:
                                clean_screen()
                                break
                            else:
                                clean_screen()
                                print(f'El código "{code}" no está registrado')

                    while True:
                        price = input("¿Que precio desea establecer?: ")
                        price = converter(float, price)
                        if type(price) == float:
                            clean_screen()
                            break

                    name = input("¿Que nombre desea establecer?: ")
                    edit_product(code)
                    break

            elif choice == "3":
                clean_screen()
                while True:
                    code = input("¿Código del producto que desea eliminar?: ")
                    code = converter(int, code)
                    if type(code) == int:
                        codes = []
                        for i in reg_products:
                            codes.append(i.code)
                        if code in codes:
                            clean_screen()
                            del_product(code)
                            break
                        else:
                            clean_screen()
                            print(f'El código "{code}" no está registrado')

            elif choice == "4":
                clean_screen()
                add_product()

            else:
                clean_screen()
                print("ERROR: La opción indicada no existe")

    elif choice == "2":
        clean_screen()
        print("Aqui va el código de la caja (Próximamente)")

    elif choice == "3":
        clean_screen()
        print("Aqui va el código del historial (Próximamente)")

    else:
        clean_screen()
        print("ERROR: La opción indicada no existe")

