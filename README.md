# Caja Registradora 

## About: 
Este es mi primer proyecto desde que aprendí Python. Se trata de crear una caja registradora por consola **con muchas herramientas** y **muy intuitiva**.


Para ejecutarlo en **Linux**:
```
git clone https://github.com/RodionButEncapsulated/Caja-Registradora.git
python3 main.py
```

Para ejecutarlo en **Windows**:
```
git clone https://github.com/RodionButEncapsulated/Caja-Registradora.git
python main.py
```

## Requisitos:

Para que el programa funcione correctamente, será **necesario instalar** las siguientes **librerias**:

* [YAML](https://pypi.org/project/PyYAML/ "Ir a YAML en PyPI"): Para manejo de datos almacenados.
* [Colorama](https://pypi.org/project/colorama/ "Ir a YAML en PyPI"): Para colores en consola.

```
pip install -r requirements.txt
```

## Cambios:
* Se agrego el código del menú "historial".
* Ahora todas las compras se registran en un archivo .yaml llamado "Historial.yaml".
* Ahora cuando ocurre algún error muestra un mensaje en rojo y cuando se realiza algún proceso correctamente, un mensaje en verde.
* Se agregó un submenú en el menú de la caja registradora.
* Ahora se explica en el menú de caja que al ingresar "T" dará el total y "S" al subtotal.
* Se creó un archivo readme más "decente" y se agregó la descripción del código.

## Próximos Cambios:
* Se separarán las funciones y objetos en un archivo ".py" aparte del main.
* Los productos registrados se almacenarán en un archivo ".yaml" y ya no más en memoria.
* Crear una versión completamente en inglés.
* Se agregará la opción de crear una contraseña para acceder al historial de compras.
