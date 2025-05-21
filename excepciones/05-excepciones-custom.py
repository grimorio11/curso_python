class MiError(Exception):
    """Clase personalizada de error"""
    def __init__(self, mensaje, valor):
        self.mensaje = mensaje
        self.valor = valor

    def __str__(self):
        return f"{self.mensaje} - Error {self.valor}"

def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir entre cero", "805")
    return 5 / n

try:
    division()
except MiError as e:
    # print(e.valor)
    # print(e.mensaje)
    print(e)
