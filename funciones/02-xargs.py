def suma(*numeros):
    """
    Suma dos números.
    """
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)



suma(1, 2)
suma(4, 67, 23, 45, 67, 89)