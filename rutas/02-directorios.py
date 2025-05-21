from pathlib import Path

path = Path("rutas")
# path.exists()  # True
# path.mkdir()
# path.rename("nuevo-directorio")


for p in path.iterdir():
    print(p.name,
          p.stem,
          p.suffix,
          p.parent,
          p.absolute()
          )  # nuevo-archivo.py
 
archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py")]
archivos = [p for p in path.glob("**/*.py")]
archivos = [p for p in path.rglob("*.py")]
print(archivos)

