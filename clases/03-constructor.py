class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años")

    # Metodos
    def habla(self):
        print("Guau Guau")

mi_perro = Perro("Pepe",3)
print(mi_perro.nombre)
print(mi_perro.edad)
print(mi_perro.info())