class Perro:
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice Guau Guau")

    @classmethod
    def factory(cls):
        return cls("Pepe", 3)
        

perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())

print(perro1.__dict__)