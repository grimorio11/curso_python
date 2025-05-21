import sqlite3

con = sqlite3.connect('sqlite/app.db')
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
''')
con.commit()    # Guardar cambios
con.close()

