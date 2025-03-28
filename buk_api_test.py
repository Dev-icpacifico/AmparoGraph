import requests
import numpy
# URL de la API
url = "https://desarrollohumano.buk.cl/api/v1/chile/employees/996/statements/2025-1.pdf"

# Encabezados de la solicitud
headers = {
    "Accept": "application/pdf",
    "auth_token": "xxxx"  # Reemplaza con tu token real
}

# Realizar la solicitud GET
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    with open("estado_cuenta_2025-1.pdf", "wb") as file:
        file.write(response.content)
    print("PDF descargado exitosamente.")
else:
    print(f"Error al descargar el PDF: {response.status_code} - {response.text}")
