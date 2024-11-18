import requests
from bs4 import BeautifulSoup

def obtener_tablas(url):
    # Hacer la solicitud HTTP a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Analizar el contenido HTML de la página web
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las etiquetas <table> en la página
        tablas = soup.find_all('table')

        # Iterar sobre las tablas y procesar sus datos
        for i, tabla in enumerate(tablas):
            # Aquí puedes realizar operaciones específicas para cada tabla
            # Por ejemplo, imprimir las filas y columnas
            print(f"Tabla {i + 1}:")
            filas = tabla.find_all('tr')
            for fila in filas:
                columnas = fila.find_all(['th', 'td'])
                fila_datos = [col.text.strip() for col in columnas]
                print(fila_datos)
            print("\n" + "-" * 20 + "\n")

    else:
        print(f"Error al obtener la página. Código de estado: {response.status_code}")

# Reemplaza 'URL_DE_LA_PAGINA' con la URL de la página web que deseas analizar
url_pagina = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses'
obtener_tablas(url_pagina)
