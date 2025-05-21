import sys
from pathlib import Path
import os

def cli(args):
    if len(args) == 1:
        print("No arguments provided.")
        return
    if len(args) != 3:
        print("se necesitan dos argumentos")
        return
    
    origen = args[1]
    o = Path(origen) 
    if not o.exists():
        print(f"El archivo {origen} no existe")
        return
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print(f"El {destino} ya existe")
        return
    
    os.rename(str(origen), str(destino))
    print(f"El archivo {origen} ha sido renombrado a {destino}")

cli(sys.argv)
