import random
import string

lista = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
random.shuffle(lista)
print(lista)

lista2 = ["rojo", "verde", "azul", "negro", "blanco", "rosa"]

print(random.random(),
      random.randint(1, 10),
      random.choice(["rojo", "verde", "azul", "negro", "blanco", "rosa"]),
      random.choices(lista2, k=2),
      "".join(random.choices("qwertyuiopñlkjhgfdsamnbvcxz1234567890!·$%&/()=¿", k=5)),
        )

chars = string.ascii_letters
digitos = string.digits
puntos = string.punctuation

seleccion = random.choices(chars + digitos + puntos, k=16)
print(seleccion)
contrasena = "".join(seleccion)
print(contrasena)





