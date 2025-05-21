# 1.- Eliminar los espacios en blanco de un string y devolver una lista con los elementos restantes
datos = "Este es un string con espacios en blanco"
datos = datos.lower()
datos = datos.replace(" ", "")
lista = []
for elemento in datos:
    lista.append(elemento)
    
print(lista)

# 2.- Contar en un diccionario cuanto se repiten los caracteres de un string
def contar_caracteres(string):
    """
    Esta función cuenta la cantidad de veces que se repite cada carácter en un string.
    """
    contador = {}
    for caracter in string:
        if caracter in contador:
            contador[caracter] += 1
        else:
            contador[caracter] = 1
    return contador

print(contar_caracteres(lista)) 

# 3.- Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contiene tuplas
#  [("a", 3), ("b", 2), ("c", 4), ("d", 5)]

def ordenar_diccionario_por_valor(diccionario):
    """
    Esta función ordena un diccionario por sus valores y devuelve una lista de tuplas.
    """
    return sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

lista_tuplas = (ordenar_diccionario_por_valor(contar_caracteres(lista)))

# 4.- De un listado de tuplas devolver las que tengan el mayor valor
def filtrar_tuplas_por_valor(tuplas):
    """
    Esta función filtra las tuplas que tienen el mayor valor.
    """
    maximo = max(tuplas, key=lambda x: x[1])[1]
    return [tupla for tupla in tuplas if tupla[1] == maximo]

maximos = dict(filtrar_tuplas_por_valor(lista_tuplas))
print(maximos)


# 5.- Crear un mensaje que diga:
# los caracteres que más se repiten con 4 repetciones son: C y D

def crear_mensaje(diccionario):
    """
    Esta función crea un mensaje con los caracteres que más se repiten.
    """
    # maximo = max(tuplas, key=lambda x: x[1])[1]
    # caracteres = [tupla[0] for tupla in tuplas if tupla[1] == maximo]
    # caracteres1 = [caracter.upper() for caracter in caracteres]
    #return f"Los caracteres que más se repiten con {maximo} repeticiones son: {", " .join(caracteres1)}"
    mensaje = "Los caracteres que más se repiten son: \n"
    for key, value in diccionario.items():
        mensaje += f"- {key} con {value} repeticiones \n"
    return mensaje

mensaje = crear_mensaje(maximos)
print(mensaje)


# 6.- Juntar la solución de los ejercicios anteriores para encontrar los caracteres que más se repiten de un string