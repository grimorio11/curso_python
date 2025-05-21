saludo = "Hola Global"

def saludar():
    global saludo 
    print(saludo)  # Hola Local

def saludar_mundo():
    saludo = "Hola Mundo"
    
print(saludo)  # Hola Global
saludar()
saludar_mundo()