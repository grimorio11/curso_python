import csv
import os

# escribir un archivo CSV
# with open('archivos/archivo.csv', 'w') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(['twit_id', 'user_id', 'text'])
#     writer.writerow(['1', '1', 'Hola'])
#     writer.writerow(['2', '2', 'Adios'])

# leer un archivo CSV
# with open('archivos/archivo.csv', 'r') as archivo:
#     reader = csv.reader(archivo)
#     #print(list(reader))
#     archivo.seek(0)     # Regresar al inicio del archivo
#     for fila in reader:
#         print(fila)

# modificar un archivo CSV
with open('archivos/archivo.csv', 'r') as r, open('archivos/archivo_tmp.csv', 'w') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for fila in reader:
        if fila[0] == '2':
            writer.writerow([2,2,"hola de nuevo"])
        else:
            writer.writerow(fila)
    
os.remove('archivos/archivo.csv')
os.rename('archivos/archivo_tmp.csv', 'archivos/archivo.csv')