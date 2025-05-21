punto = { "x": 25, "y": 50 }
print(punto["x"])
print(punto["y"])

# Añadir un nuevo elemento
punto["z"] = 45
print(punto)

print(punto.get("x"))
print(punto.get("a", "No existe"))  # Si no existe devuelve el segundo argumento
del punto["x"]  # Eliminar un elemento
print(punto)
punto["x"] = 25

# Sacar los valores de un diccionario
for key in punto:
    print(key, ":", punto[key])

for key, value in punto.items():
    print(key, ":", value)

######################
usuarios = [{"id": 1, "nombre": "Juan", "edad": 25},
           {"id": 2, "nombre": "Pedro", "edad": 30},
           {"id": 3, "nombre": "Maria", "edad": 28},
           {"id": 4, "nombre": "Ana", "edad": 22}]

for usuario in usuarios:
    print( usuario["id"], usuario["nombre"])