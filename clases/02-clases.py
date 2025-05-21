class Perro:
    # Metodos
    def habla(self):
        print("Guau Guau")

mi_perro = Perro()
print(type(mi_perro))

mi_perro.habla()

print(isinstance(mi_perro, Perro))
