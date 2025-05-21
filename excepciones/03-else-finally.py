try:
    n1 = int(input("Introduce un número: "))
except Exception as e:
    print("Ocurrio un error!")
else:
    print("Todo correcto")
finally:
    print("Fin del programa")