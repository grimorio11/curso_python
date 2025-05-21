from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(days=1, hours=2, minutes=3)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)  # Devuelve un objeto timedelta
print(delta.days)  # Devuelve la diferencia en días
print(delta.seconds)  # Devuelve la diferencia en segundos
print(delta.total_seconds())  # Devuelve la diferencia total en segundos
print(delta.total_seconds() / 3600)  # Devuelve la diferencia total en horas