from abc import ABC, abstractmethod

class Model(ABC):
    #tabla = False
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    @property        
    @abstractmethod
    def tabla(self):
        pass
 
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando {self.tabla} por id {_id} en BBDD")
        return self

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()
Usuario.buscar_por_id(123)