numeros = (56, 12, 43, 90, 1) + (7, 13, 8, 2, 3)
print(numeros)

#Crear una tupla desde una lista
punto = tuple([1, 2])
print(punto)

primero, segundo, *resto = numeros
print(primero, segundo, resto)

for n in numeros:
    print(n)

# Crear lista a partir de una tupla
lista = list(numeros)
print(lista)