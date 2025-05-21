class Perro:
    patas = 4  # Propiedad de clase
    cola = 1   # Propiedad de clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau Guau")

    @classmethod
    def factory(cls):
        return cls("Pepe", 3)
        

Perro.habla() 
perro = Perro.factory()
print(perro.nombre)
print(perro.edad, perro.nombre)