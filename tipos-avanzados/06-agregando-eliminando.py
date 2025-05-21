mascotas = ['perro', 'gato', 'loro', 'pez', 'tortuga']

mascotas.insert(0, 'hamster')  # Agregar al inicio
print(mascotas)
mascotas.append('pato')  # Agregar al final
print(mascotas)
mascotas.insert(2, 'serpiente')  # Agregar en la posición 2     
print(mascotas)
mascotas.remove('pez')  # Eliminar por valor
print(mascotas)

mascotas.pop(1)  # Eliminar por índice
print(mascotas)