from zipfile import ZipFile

# Crear un archivo comprimido
with ZipFile('archivos/archivo.zip', 'w') as archivo_zip:
    archivo_zip.write('archivos/archivo.csv')
    archivo_zip.write('archivos/archivo.json')

# Leer un archivo comprimido
with ZipFile('archivos/archivo.zip', 'r') as archivo_zip:
    # Listar archivos
    print(archivo_zip.namelist())
    # Leer un archivo
    with archivo_zip.open('archivos/archivo.json') as archivo_json:
        print(archivo_json.read())