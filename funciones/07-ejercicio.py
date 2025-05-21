def es_palindromo(texto):
    """
    Esta función verifica si una palabra es un palíndromo.
    Un palíndromo es una palabra que se lee igual de izquierda a derecha que de derecha a izquierda.
    """
    # Convertir la palabra a minúsculas para evitar problemas de mayúsculas
    texto = texto.lower()
    texto = texto.replace(" ", "")  # Eliminar espacios en blanco
    
    inverso = ""
    for letra in texto:
        inverso = letra + inverso
    # Comparar la palabra con su reverso
    #return texto == texto[::-1]
    return texto == inverso


print("Anita lava la tina", "=>", es_palindromo("Anita lava la tina"))
print("Hola mundo", "=>", es_palindromo("Hola mundo"))
print("Reconocer", "=>", es_palindromo("Reconocer"))