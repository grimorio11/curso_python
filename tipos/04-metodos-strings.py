animal = "  cacho perro  "
print(animal.upper())  # Convierte a mayúsculas
print(animal.lower())  # Convierte a minúsculas
print(animal.title())  # Convierte la primera letra de cada palabra a mayúscula
print(animal.capitalize())  # Convierte la primera letra de la cadena a mayúscula
print(animal.strip())  # Elimina los espacios en blanco al principio y al final de la cadena
print(animal.lstrip())  # Elimina los espacios en blanco al principio de la cadena
print(animal.rstrip())  # Elimina los espacios en blanco al final de la cadena
print(animal.strip().capitalize())  # Elimina los espacios en blanco al principio y al final de la cadena y convierte la primera letra a mayúscula
print(animal.find("ch"))  # Busca la posición de la subcadena "cacho" en la cadena
print(animal.replace("cacho", "pedazo"))  # Reemplaza "cacho" por "perro" en la cadena
print(animal.split())  # Divide la cadena en una lista de palabras