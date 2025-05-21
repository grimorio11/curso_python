numeros = [56, 12, 43, 90, 1, 7, 13, 8, 2, 3]
# Ordenar de menor a mayor
numeros.sort()
print(numeros)
# Ordenar de mayor a menor
numeros.sort(reverse=True)
print(numeros)

numeros2 = [56, 12, 43, 90, 1, 7, 13, 8, 2, 3]

sorted_numeros = sorted(numeros2, reverse=True)
print(sorted_numeros)
# sorted() devuelve una nueva lista ordenada, pero no modifica la lista original
print(numeros2)

mascotas = [['perro', 4],
            [ 'gato', 5],
            ['loro', 1],
            ['pez', 8],
            ['tortuga', 3]]
# Ordenar alfabéticamente
mascotas.sort(key=lambda x: x[0])
print(mascotas)
# Ordenar por el segundo elemento de cada sublista
mascotas.sort(key=lambda x: x[1], reverse=True)    
print(mascotas)