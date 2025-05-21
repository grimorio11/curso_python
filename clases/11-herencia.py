class Animal:
    def comer(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("paseando")

class Cerdo(Perro):
    def programar(self):
        print("programando")

cerdito = Cerdo()
cerdito.pasear()    