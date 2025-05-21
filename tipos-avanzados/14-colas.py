pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimo_elemento = pila.pop()
print(ultimo_elemento)
print(pila)

if not pila:
    print("La pila está vacía")