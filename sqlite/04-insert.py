import sqlite3

with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()
    # Insertar un producto
    cursor.execute(
        "INSERT INTO productos VALUES (?, ?, ?)",
        (1, 'batería', 75),
    )
    

