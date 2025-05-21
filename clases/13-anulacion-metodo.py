class Ave:
    def __init__(self):
        self.volador = True
    
    def vuela(self):
        print("vuela ave")

class Pato(Ave):
    def vuela(self):
        # llamada al constructor de la clase padre
        super().__init__()
        print("vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador)