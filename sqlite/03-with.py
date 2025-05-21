import sqlite3

with sqlite3.connect('sqlite/app.db') as con:
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL
        )
    ''')

