import requests
from bs4 import BeautifulSoup
import pandas as pd

# Función para obtener cuotas de una casa de apuestas (ejemplo genérico)
def obtener_cuotas(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extraer datos relevantes de la página web
    # Nota: Esto varía según la estructura de cada sitio web
    eventos = soup.find_all('div', class_='evento')
    datos_cuotas = []
    
    for evento in eventos:
        nombre_evento = evento.find('h2').text
        cuotas = [float(cuota.text) for cuota in evento.find_all('span', class_='cuota')]
        datos_cuotas.append([nombre_evento] + cuotas)
    
    return datos_cuotas

# URLs de ejemplo de diferentes casas de apuestas
urls_casas_de_apuestas = [
    'https://www.bet365.mx/?_h=jYiG_6T5kFJPW9GaDxpqWg%3D%3D&btsffd=1#/AC/B1/C1/D8/E158404516/F3/I^17/',
    'https://www.playdoit.mx/#page=prelive'
]

# Recopilar datos de todas las casas de apuestas
datos_todos_eventos = []

for url in urls_casas_de_apuestas:
    datos_todos_eventos.extend(obtener_cuotas(url))

# Crear DataFrame de pandas para el análisis
columnas = ['Evento', 'Cuota1_Casa1', 'Cuota2_Casa1', 'Cuota1_Casa2', 'Cuota2_Casa2']
df = pd.DataFrame(datos_todos_eventos, columns=columnas)

# Análisis de datos: Identificación de mejores cuotas
df['Mejor_Cuota1'] = df[['Cuota1_Casa1', 'Cuota1_Casa2']].max(axis=1)
df['Mejor_Cuota2'] = df[['Cuota2_Casa1', 'Cuota2_Casa2']].max(axis=1)

# Visualización de datos
print(df)

# Ejemplo de visualización básica
df.plot(kind='bar', x='Evento', y=['Mejor_Cuota1', 'Mejor_Cuota2'])
