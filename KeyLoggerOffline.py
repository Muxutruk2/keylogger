import requests

def get_public_ip():
    """
    Obtiene la dirección IP pública del equipo utilizando httpbin.org.
    """
    try:
        response = requests.get('https://httpbin.org/ip')
        ip_data = response.json()
        public_ip = ip_data.get('origin')
        return public_ip
    except Exception as e:
        print(f"Error al obtener la IP pública: {e}")
        return None

def save_ip_to_file(ip):
    """
    Guarda la dirección IP pública en un archivo de texto.
    """
    try:
        with open("public_ip.txt", "w") as file:
            file.write(ip)
        print(f"La IP pública ({ip}) se ha guardado en public_ip.txt")
    except Exception as e:
        print(f"Error al guardar la IP pública: {e}")

def main():
    # Obtiene la dirección IP pública
    public_ip = get_public_ip()

    if public_ip:
        # Guarda la dirección IP pública en un archivo de texto
        save_ip_to_file(public_ip)
    else:
        print("No se pudo obtener la IP pública.")

if __name__ == "__main__":
    main()
