mascotas = [['perro', 4],
            [ 'gato', 5],
            ['loro', 1],
            ['pez', 8],
            ['tortuga', 3]]

# map
animales = [animal[0] for animal in mascotas]
print(animales)

#filter
#animales = [animal for animal in mascotas if animal[1] > 3]

# filtrar y transformar
animales = [animal[0] for animal in mascotas if animal[1] > 3]
print(animales)

#MAP
animales = list(map(lambda animal: animal[0], mascotas))
print(animales)

# FILTER
animales = list(filter(lambda animal: animal[1] > 3, mascotas))
print(animales)