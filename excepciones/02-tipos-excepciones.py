# Todas las excepciones
# try:
#     n1 = int(input("Introduce un número: "))
#     uhsdfusdh
# except Exception as e:
#     #print("Error, no es un número")
#     print(type(e))
# else:
#     print("Todo correcto")

# ValueError:
try:
    n1 = int(input("Introduce un número: "))
    uhsdfusdh
except ValueError as e:
    #print("Error, no es un número")
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error")