import sqlite3

with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute("SELECT * FROM productos")
    print(cursor.fetchall())
