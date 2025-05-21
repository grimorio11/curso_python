import time
import datetime

print(time.time())  # Devuelve el tiempo en segundos desde el 1 de enero de 1970

from datetime import datetime
print(datetime.now())  # Devuelve la fecha y hora actual

fechaStr = datetime.strptime("2023-10-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(fechaStr)  # Convierte una cadena a un objeto datetime

