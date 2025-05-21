import json
from pathlib import Path
import os

# escribir json
productos = [
    {
        "id": 1,
        "nombre": "surfboard",
        "precio": 10.0
    },
    {
        "id": 2,
        "nombre": "bicicleta",
        "precio": 20.0
    },
    {
        "id": 3,
        "nombre": "skate",
        "precio": 30.0
    }    
]

data = json.dumps(productos)
print(data)

Path('archivos/archivo.json').write_text(data)

# leer json
data = Path('archivos/archivo.json').read_text()
product = json.loads(data)
print(product)

# modificar json
with open('archivos/archivo.json', 'r') as r, open('archivos/archivo_tmp.json', 'w') as w:
    data = json.load(r)
    for product in data:
        if product['id'] == 2:
            product['precio'] = 25.0
    json.dumps(data, w)

os.remove('archivos/archivo.json')
os.rename('archivos/archivo_tmp.json', 'archivos/archivo.json')
