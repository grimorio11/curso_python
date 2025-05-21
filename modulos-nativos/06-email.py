from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib

mensaje = MIMEMultipart()
mensaje['From'] = 'tu_correo@example.com'
mensaje['To'] = 'destinatario@example.com'
mensaje['Subject'] = 'Asunto del correo'
cuerpo = """
Hola, este es un correo de prueba enviado desde Python.
Saludos,
Tu nombre
"""
mensaje.attach(MIMEText(cuerpo, 'plain'))

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # Inicia la conexión
    smtp.starttls()  # Inicia la conexión segura
    smtp.login('grimorio11@gmail.com', '3sp3r4nz4')
    smtp.send_message(mensaje)
print("Correo enviado con éxito.")