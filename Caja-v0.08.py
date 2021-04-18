import time
import os
history = []
simbolos = ["/", "-", "|"]

os.system("clear")

print('Bienvenido al sorfware de caja v0.08 \n------Creado por RodionDoma------')

products = {
	1:[3.15, 'Arroz'],
	2:[4.35, 'Frijol'],
	3:[4.75, 'Pasta'],
	4:[5.25, 'Atún'],
	5:[2.15, 'Banana']
}


#Aqui se declaran los productos registrados

def check(choice):
	try:
		choice = int(choice)
		return choice
	except ValueError:
		os.system("clear")
		print('***Error: Ingrese sólo números por favor***')
		return 'Error'
		
def check_float(choice):
	try:
		choice = float(choice)
		return choice
	except ValueError:
		print('***Error: Ingrese sólo números por favor***')
		return 'Error'
		
#Esta función revisa un input, genera un error sí el input es texto y sí no lo es, lo convierte a int o float.
		
while True:
	print('')
	print('	Menu Principal'.upper())
	print('')
	print('1) Administración de productos','2) Abrir Caja','3) Historial de registros','4) Cerrar programa',sep='\n')
	
	print('')
	choice = input('>>>Elija su opción: ')
	choice = check(choice)
	#Aqui se establece el menú principal. Apartir de abajo se declarará que hace cada menú.
	
	if choice == 'Error':
		#os.system("clear")
		continue
	elif choice == 4:
		break
	elif choice <= 0 or choice >= 5:
		os.system("clear")
		print(f'***Error: La opción {choice} no está disponible***')
		continue
	#Aqui se generan los errores de opciones que no están incluidas

	elif choice == 1:
		os.system("clear")
		while True:
			print('')
			print('	Menú de administración de productos'.upper())
			print('')
			print('1) Agregar productos','2) Mostrar productos','3) Eliminar productos','4) Volver al menú anterior',sep='\n')
			
			print('')
			choice = input('>>>Elija su opción: ')
			choice = check(choice)
			#Aqui se establecen las opciones disponibles en el menú 1
			
			if choice == 'Error':
				continue
			elif choice == 4:
				os.system("clear")
				break
			elif choice <= 0 or choice >= 5:
				os.system("clear")
				print(f'***Error: La opción {choice} no está disponible***')
				continue				
			#Aqui se generan los errores de las opciones que no estan disponibles

			elif choice == 1:
				os.system("clear")
				while True:
					print('')
					while True:
						code = input('>>>Código: ')
						code = check(code)
						if code == 'Error':
							print('')
							continue
						elif code in products:
							print('')
							os.system("clear")
							print(f'***Error: El código {code} ya está registrado***')
							print('')
						else:
							break
					name = input('>>>Nombre: ')
					while True:
						price = input('>>>Precio: ')
						price = check_float(price)
						if price == 'Error':
							print('')
							continue
						else:
							break
					new_product={code:[price,name]}
					print('')
					#Establece los valores para un nuevo producto
					products.update(new_product)
					os.system("clear")
					print(f'El producto {name} ha sido registrado')
					#Agrega el nuevo producto al registro
					break
					
			elif choice == 2:
				os.system("clear")
				print('Código | Precio | Nombre')
				print('')
				for i in sorted(products):
					print(f"{i}	${products[i][0]}	{products[i][1]}")
			#Aqui se muestra el contenido de products
			
			elif choice == 3:
				os.system("clear")
				while True:
				 	if products == {}:
				 		print('')
				 		print('No hay más productos registrados')
				 		break
				 	index = input('>>>Indique el código del producto que desea eliminar: ')
				 	os.system("clear")
				 	index = check(index)
				 	if index == 'Error':
				 		continue
				 	elif index not in products:
				 		print(f'El código {index} no está registrado')
				 		continue
				 	elif index in products:
				 		del_item = products[index]
				 		print(f'El producto {products[index][1]} ha sido eliminado')
				 		products.pop(index)
				 	break
				 	
			elif choice == 4:
				 break

	elif choice == 2:
		os.system("clear")
		cart = []
		Total = 0
		print('\n	Caja de Registros'.upper())
		print('\n(Para ver el Total escriba "T" o "S" para el Subtotal")')
		
		while True:
			choice = input('\n>>>Ingrese el código del producto: ')
			
			if choice == 't' or choice == 'T':
				print('')
				print('Precio | Producto | Cantidad')
				for i in cart:
					if cart.count(i) == 1:
						print(f'${i[0]}	{i[1]}	{cart.count(i)}')
						time.sleep(0.5)
					else:
						print(f'${round(i[0]*cart.count(i),3)}	{i[1]}	{cart.count(i)}')
						time.sleep(0.5)
						x = 1
						while x < cart.count(i):
							cart.remove(i)
				print('----------------------------')
				print(f'${round(Total,2)}..........Total')
				break
				
			elif choice == 's' or choice == 'S':
				print('')
				print(f'El Subtotal es ${round(Total,2)}')
				
			else:
				choice = check(choice)
				if choice == 'Error':
					continue
				else:
					print('')
					if choice in products:
						cart.append(products[choice])
						Total += round(products[choice][0],2)
						print(f'El producto {products[choice][1]} fue agregado')
					else:
						print('El código no está registrado')
						
	#elif choice == 3:
