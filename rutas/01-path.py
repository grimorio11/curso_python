from pathlib import Path

path = Path("Hola-mundo/mi-archivo.py")
path.is_file()  # True
path.is_dir()  # False
path.exists()  # True

print(path.name,
      path.stem,
      path.suffix,
      path.parent,
      path.absolute()
      )  # mi-archivo.py

p = path.with_name("nuevo-archivo.py")
print(p.name,
      p.stem,
      p.suffix,
      p.parent,
      p.absolute()
      )  # nuevo-archivo.py
