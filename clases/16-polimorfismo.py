# from abc import ABC, abstractmethod

# class Model(ABC):
    
#     @abstractmethod
#     def tabla(self):
#         pass

# class Usuario(Model):
#     def guardar(self):
#         print("Guardando en BBDD")

# class Sesion(Model):
#     def guardar(self):
#         print("Guardando Sesion en archivo")

# def guardar(entidades):
#     for entidad in entidades:
#         entidad.guardar()

# usuario = Usuario()
# sesion = Sesion()
# guardar([sesion, usuario])

class Usuario():
    def guardar(self):
        print("Guardando en BBDD")

class Sesion():
    def guardar(self):
        print("Guardando Sesion en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])

