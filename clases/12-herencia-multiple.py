class Animal:
    def comer(self):
        print("comiendo")

class Perro:
    def pasear(self):
        print("paseando")

# herencia multiple
class Cerdo(Perro, Animal):
    def programar(self):
        print("programando")

cerdito = Cerdo()
cerdito.comer()