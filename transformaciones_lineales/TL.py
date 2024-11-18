import cv2
import os
import glob

def crear_stop_motion(entrada_carpeta, salida_video, fps=2.3):
    imagenes = sorted(glob.glob(os.path.join(entrada_carpeta, '*.jpg')))  # podemos ajustar dependiendo del formato
    size = (0, 0)
    
    # Obtiene el tamaño de l aprimera imagen para usar en el video
    if imagenes:
        img = cv2.imread(imagenes[0])
        height, width, layers = img.shape
        size = (width, height)

    # Configuramos el videowriter y creamos el viddeo con un for
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Ajusta el codec según tus necesidades
    video = cv2.VideoWriter(salida_video, fourcc, fps, size)

    for imagen in imagenes:
        img = cv2.imread(imagen)
        video.write(img)

    # Libera los recursos
    video.release()

if __name__ == "__main__":
    # Especificamo s la ruta de las ftos y el nombre del video
    carpeta_entrada = "E:\MATLAB_PRACTICA_MECATRONICA\TL\Transformaciones lineales"
    archivo_salida = "stop_motion.mp4"

    # Crea el stop motion
    crear_stop_motion(carpeta_entrada, archivo_salida)

    print("¡Stop motion creado con éxito!")
