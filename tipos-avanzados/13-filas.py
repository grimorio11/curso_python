from collections import deque

fila = deque([1, 2, 3, 4, 5])
print(fila)
fila.append(6)
print(fila)
fila.popleft()
print(fila) 