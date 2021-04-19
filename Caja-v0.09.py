import os

saludo = "Bienvenido al software de caja v0.09. -Creado por __Rodion__"

total = []
cart = []
reg_products = []

#Creando menús
menu1 = """\t Menú Principal
1) Administrar Productos
2) Abrir Caja
3) Historial de Registros
4) Cerrar Programa
"""

menu2 = """\t Menú de Administración de Productos
1) Mostrar Productos Registrados
2) Editar Producto Registrado
3) Eliminar Producto Registrado
4) Agregar Nuevo Producto
5) Volver al menú anterior
"""

menu3 = """--"""

#Creando la clase para los productos
class Product():
	
	def __init__(self, name, price, code):
		self.name = name
		self.price = price
		self.code = code

	def buy(self):
		cart.append(self.name)
		total.append(self.price)
		return print(f'El producto {self.name} ha sido comprado')
		
	def change_price(self, new_price):
		self.price = new_price
		return print(f'El precio del producto {self.name} se cambió a "{self.price}"')
		
	def change_name(self, new_name):
		self.name = new_name
		return print(f'El nombre del producto se cambió a "{self.name}"')


#Creando funciones
def create_product(name, price, code):
	new_product = Product(name, price, code)
	reg_products.append(new_product)
	return new_product
	
def add_product():
	name = input("Nombre: ")
	price = float(input("Precio: "))
	code = len(reg_products) + 1
	create_product(name, price, code)
	os.system("clear")
	return print(f"El producto {name} fue creado y guardado correctamente")
	
def show_products():
	print("NOMBRE\tPRECIO\tCÓDIGO")
	for i in reg_products:
		print(f"{i.name}\t{i.price}\t{i.code}")
	
def converter(func, choice):
    try:
    	return func(choice)
    except:
    	return "La opción ingresada no existe"

#Creando Productos Pre-Registrados
create_product("Papa", 1.50, 0)
create_product("Arroz", 1.70, 1)
create_product("Pasta", 1.25, 2)

#Loop Principal
while True:
	print(menu1)
	choice = input("Elija una opción: ")
	
	if choice == "4":
		break
		
	elif choice == "1":
		os.system("clear")
		
		while True:
			print(menu2)
			choice = input("Elija una opción: ")
			
			if choice == "5":
				os.system("clear")
				break
			
			elif choice == "1":
				os.system("clear")
				show_products()
				print("")
				
			elif choice == "2":
				os.system("clear")
				code = int(input("¿Cual es el código del producto que desea editar?: "))
				name = input("¿Que nombre desea poner?: ")
				for i in reg_products:
					if i.code == code:
						i.change_name(name)
					else:
						print("El código indicado no existe")
						
	else:
		os.system("clear")
		print("La opción seleccionada no existe")
