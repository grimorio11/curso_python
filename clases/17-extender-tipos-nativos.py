class List(list):
    def prepend(self, item):
        self.insert(0, item)
        

lista = List([1, 2, 3])
lista.append(4)
lista.prepend(0)
print(lista)    