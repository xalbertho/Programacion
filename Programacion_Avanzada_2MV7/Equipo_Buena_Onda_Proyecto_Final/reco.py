import cv2
import numpy as np

def detectar_forma_y_color(frame):
    # Invertir la imagen horizontalmente para eliminar efecto espejo
    frame = cv2.flip(frame, 1)

    # Detección de color
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx, cy = int(width / 2), int(height / 2)
    pixel_central = hsv_frame[cy, cx]
    hue_value = pixel_central[0]
    saturation = pixel_central[1]
    value = pixel_central[2]

    color = "Desconocido"
    color_rgb = (128, 128, 128)  # Gray
    if saturation > 50 and value > 50:
        if (hue_value < 10) or (hue_value > 170):
            color = "Rojo"
            color_rgb = (0, 0, 255)  # Red
        elif 25 <= hue_value < 35:
            color = "Amarillo"
            color_rgb = (0, 255, 255)  # Yellow
        elif 35 <= hue_value < 85:
            color = "Verde"
            color_rgb = (0, 255, 0)  # Green
        elif 85 <= hue_value < 130:
            color = "Azul"
            color_rgb = (255, 0, 0)  # Blue

    # Detección de forma
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 10, 150)
    canny = cv2.dilate(canny, None, iterations=1)
    canny = cv2.erode(canny, None, iterations=1)
    cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    forma = "Desconocida"
    for c in cnts:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)

        if len(approx) == 3:
            forma = "Triángulo"
        elif len(approx) == 4:
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                forma = "Cuadrado"
            else:
                forma = "Rectángulo"
        elif len(approx) == 12:
            forma = "Cruz"
        elif len(approx) > 12:
            forma = "Círculo"

        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)

    resultado = f"{forma} {color}"
    cv2.putText(frame, resultado, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color_rgb, 2, cv2.LINE_AA)
    return frame

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = detectar_forma_y_color(frame)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
