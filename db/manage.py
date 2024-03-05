import sqlite3
import os

class Database:
    def __init__(self, db_name):
        self.db_name = db_name # El nombre de la base de datos
        self.conn = None # La conexión a la base de datos
        self.cursor = None # El cursor para ejecutar consultas

    def connect(self):
        # Este método se conecta a la base de datos si existe, o la crea si no existe
        try:
            self.conn = sqlite3.connect(os.path.join("db", self.db_name))
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos")
        except sqlite3.Error as e:
            print("Error al conectar a la base de datos:", e)

    def disconnect(self):
        # Este método cierra la conexión a la base de datos
        if self.conn:
            self.conn.close()
            print("Conexión cerrada")

    def create_tables(self):
        # Este método crea las tablas que tendrá la base de datos
        # En este caso, solo habrá una tabla llamada "products" que almacenará los productos de la caja registradora
        try:
            self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                code TEXT UNIQUE,
                amount INTEGER NOT NULL);""")
            self.conn.commit()
            print("Tablas creadas")
        except sqlite3.Error as e:
            print("Error al crear las tablas:", e)

    def insert(self, obj):
        # Este método inserta un objeto en la tabla "products"
        # El objeto debe tener los atributos name, price, code y amount
        try:
            self.cursor.execute("""INSERT INTO products (name, price, code, amount) VALUES (?,?,?,?)""", (obj.name, obj.price, obj.code, obj.amount))
            self.conn.commit()
            #print(f"Objeto {obj.name} insertado")
            input(f"Objeto {obj.name} insertado correctamente")
        except sqlite3.Error as e:
            #print(f"Error al insertar el objeto {obj.name}: {e}")
            input(f"Error al insertar el objeto {obj.name}: {e}")

    def select(self, obj):
        # Este método selecciona un objeto de la tabla "products" cuyo código sea el mismo del objeto pasado como argumento
        try:
            self.cursor.execute("""SELECT name, price, code, amount FROM products WHERE code = ?""", (obj.code,))
            result = self.cursor.fetchone()
            # print(f"Objeto {result[0]} seleccionado")
            return result
        except sqlite3.Error as e:
            print("Error al seleccionar el objeto:", e)

    def select_all(self):
        # Este método selecciona todos los objetos de la tabla "products" y los devuelve como una lista de tuplas
        try:
            self.cursor.execute("""SELECT * FROM products""")
            result = self.cursor.fetchall()
            print("Objetos seleccionados")
            return result
        except sqlite3.Error as e:
            print("Error al seleccionar todos los objetos:", e)

    def update(self, obj):
        # Este método actualiza un objeto en la tabla "products"
        # El objeto debe tener los atributos name, price, code y amount
        try:
            self.cursor.execute("""UPDATE products SET name = ?, price = ?, amount = ? WHERE code = ?""", (obj.name, obj.price, obj.amount, obj.code))
            self.conn.commit()
            print(f"Objeto {obj.name} actualizado")
        except sqlite3.Error as e:
            print(f"Error al actualizar el objeto {obj.name}: {e}")

    def delete(self, obj):
        # Este método elimina un objeto de la tabla "products"
        # El objeto debe tener el atributo code
        try:
            self.cursor.execute("""DELETE FROM products WHERE code = ?""", (obj.code,))
            self.conn.commit()
            #print(f"Objeto {obj.name} eliminado")
            input(f"Objeto {obj.name} eliminado")
        except sqlite3.Error as e:
            #print(f"Error al eliminar el objeto {obj.name}: {e}")
            input(f"Error al eliminar el objeto {obj.name}: {e}")

db = Database("Caja.sqlite3")