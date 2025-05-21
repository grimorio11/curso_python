import sqlite3

with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()
    # Insertar un producto
    productos = [
        (2, 'cargador', 25),
        (3, 'auriculares', 50),
        (4, 'ratón', 30),
        (5, 'teclado', 40),
        (6, 'monitor', 200),
        (7, 'pantalla', 150),
        (8, 'altavoces', 100)
    ]
    cursor.executemany(
        "INSERT INTO productos VALUES (?, ?, ?)",
        productos
    )
