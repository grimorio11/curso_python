# set conjunto o grupo
# no se repiten los elementos
# no tienen orden
# no son indexados

primer = {1, 1 ,2 ,2 ,3 ,4 ,5}
segundo = [3, 4, 5, 6, 7]
print(primer)
primer.add(6)
print(primer)
primer.remove(1)
print(primer)
primer.discard(2)
print(primer)

segundo = set(segundo)
print(segundo)

# print(primer | segundo) # union
# print(primer & segundo) # interseccion
print(primer - segundo) # diferencia
print(primer ^ segundo) # diferencia simetrica