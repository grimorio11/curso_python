from io import open

# escritura
# texto = "Hola mundo! \n"
# archivo = open('archivos/hola-mundo.txt', 'w', encoding='utf-8')
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open('archivos/hola-mundo.txt', 'r', encoding='utf-8')
# texto = archivo.read()
# print(texto)
# archivo.close()

# lectura como lista
# archivo = open('archivos/hola-mundo.txt', 'r', encoding='utf-8')
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# with y seek
# with open('archivos/hola-mundo.txt', 'r', encoding='utf-8') as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar texto
# archivo = open('archivos/hola-mundo.txt', 'a', encoding='utf-8')
# archivo.write('Otro mundo!\n')
# archivo.close()

# lectura y escritura
with open('archivos/hola-mundo.txt', 'r+', encoding='utf-8') as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Otros Aires"
    print(texto)
    archivo.writelines(texto)