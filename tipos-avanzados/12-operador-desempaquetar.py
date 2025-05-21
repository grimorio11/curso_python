lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
#print(*lista)
# Desempaquetar una lista
combinada = [*lista1, *lista2]
print(combinada)

punto1 = {"x": 25, "z": 45}
punto2 = {"y": 50}

# Desempaquetar un diccionario
punto3 = {**punto1, **punto2, "n": "hola"}
print(punto3)