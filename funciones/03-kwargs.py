def get_product(**datos):
    """
    This function takes keyword arguments and returns the product of all the values.
    """
    print(datos["id"], datos["nombre"])
 



get_product(id="i23", nombre="nombre", precio=10, cantidad=5)