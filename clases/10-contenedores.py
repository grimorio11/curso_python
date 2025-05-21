class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

class Categoria:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)
        #return f"Categoria: {self.nombre}, Productos: {self.productos}"

kayak = Producto("Kayak", 250)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Tabla de Surf", 500)
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()