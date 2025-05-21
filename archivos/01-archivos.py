from pathlib import Path
from time import ctime

archivo = Path('archivos/archivo-prueba.txt')

#print(archivo.stat())
print("acceso", ctime(archivo.stat().st_atime))
print("acceso", ctime(archivo.stat().st_mtime))
print("acceso", ctime(archivo.stat().st_ctime))
