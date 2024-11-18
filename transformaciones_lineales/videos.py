from pytube import YouTube

def descargar_video(url, ruta_guardado='~/Videos'):
    try:
        # Crear un objeto YouTube
        video = YouTube(url)

        # Obtener la mejor calidad disponible
        stream = video.streams.get_highest_resolution()

        # Descargar el video en la ruta especificada
        print(f'Descargando video: {video.title}')
        stream.download(ruta_guardado)
        print('Descarga completa!')

    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Ejemplo de uso
url_del_video = 'https://youtu.be/B0hj_qK2oXw?si=Fuc9Iyj4lyqEYmYY'
ruta_de_guardado = 'D:\cs5h'

descargar_video(url_del_video, ruta_de_guardado)
