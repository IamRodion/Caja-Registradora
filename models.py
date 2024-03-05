from db.manage import db

def convert(value, type, message): # Función para convertir un valor a un tipo dado
    try:
        return type(value) # Intenta convertir el valor al tipo
    except ValueError: # Si no se puede, maneja la excepción
        raise ValueError(message)
        #print(message) # Imprime el mensaje de error
        #return type() # Devuelve el valor por defecto del tipo

class Product(): # Clase para manejar los productos
    # def __init__(self, name = None, price = None, code = None, amount = None): # Constructor de la clase
    #     self.name = name
    #     self.price = price
    #     self.code = code
    #     self.amount = amount

    def __init__(self, name: str = '', price: float = 0.0, code: str = '', amount: int = 0): # Constructor de la clase
        self.name = convert(name, str, "El nombre debe ser una cadena") # Usa la función para convertir el nombre a cadena
        self.price = convert(price, float, "El precio debe ser un número decimal") # Usa la función para convertir el precio a entero
        self.code = convert(code, str, "El código debe ser una cadena") # Usa la función para convertir el código a cadena
        self.amount = convert(amount, int, "La cantidad debe ser un número entero") # Usa la función para convertir la cantidad a entero

    def __str__(self):
        return f'Product(Name: {self.name}, Price: {self.price}, Code: {self.code}, Amount: {self.amount})'

    def change_name(self, new_name: str):
        #self.name = new_name
        self.name = convert(new_name, str, "El nombre debe ser una cadena") # Usa la función para convertir el nombre a cadena

    def change_price(self, new_price: float):
        #self.price = new_price
        self.price = convert(new_price, float, "El precio debe ser un número decimal") # Usa la función para convertir el precio a entero

    def change_code(self, new_code: str):
        #self.code = new_code
        self.code = convert(new_code, str, "El código debe ser una cadena") # Usa la función para convertir el código a cadena

    def change_amount(self, new_amount: int):
        #self.amount = new_amount
        self.amount = convert(new_amount, int, "La cantidad debe ser un número entero") # Usa la función para convertir la cantidad a entero

    def insert(self): # Utiliza el método 'insert' de la base de datos para registrar el producto actual
        db.insert(self)
        
    def get(self): # Utiliza el método 'select' de la base de datos sobrescribir los datos del producto || para seleccionar el producto actual
        try:
            product = db.select(self)
            self.name, self.price, self.code, self.amount = product
        except Exception as e:
            self.name, self.price, self.code, self.amount = None, None, None, None
            print("Error al seleccionar el objeto:", e)

    def update(self): # Utiliza el método 'update' de la base de datos para actualizar el producto actual
        db.update(self)
        
    def delete(self): # Utiliza el método 'delete' de la base de datos para borrar el producto actual
        db.delete(self)