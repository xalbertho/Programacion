import sys
import cv2
import numpy as np
from PyQt6.QtGui import QPixmap, QImage, QPalette, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QWidget, QSizeGrip
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal, QTime, QElapsedTimer
from PyQt6 import QtWidgets, uic, QtCore

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 350)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 350)
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.change_pixmap_signal.emit(frame)

    def stop(self):
        self.running = False
        self.wait()
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        window = uic.loadUi("diseño.ui", self)
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.gripSize = 10
        self.grip = QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.arriba.mouseMoveEvent = self.mover_ventana
        self.arriba2.mouseMoveEvent = self.mover_ventana2
        self.comprimirbtn1.hide()
        self.comprimirbtn2.hide()
        
        self.minimizarbtn1.clicked.connect(self.minimizar1)
        self.comprimirbtn1.clicked.connect(self.comprimir1)
        self.expandirbtn1.clicked.connect(self.expandir1)
        self.cerrarbtn1.clicked.connect(self.detener_camara)
        self.cerrarbtn1.clicked.connect(lambda: self.close())
        
        self.minimizarbtn2.clicked.connect(self.minimizar2)
        self.comprimirbtn2.clicked.connect(self.comprimir2)
        self.expandirbtn2.clicked.connect(self.expandir2)
        self.cerrarbtn2.clicked.connect(self.detener_camara)
        self.cerrarbtn2.clicked.connect(lambda: self.close())
        
        self.iniciar1.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.menu))        
        self.iniciar2.clicked.connect(self.iniciar_camara)
        self.regresarbtn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.inicio))
        self.regresarbtn.clicked.connect(self.detener_camara)
        self.pause2.clicked.connect(self.pausar_camara)
        self.repetir2.clicked.connect(self.reiniciar_tiempo)
        self.inicio = self.findChild(QtWidgets.QWidget, 'inicio')
        self.menu = self.findChild(QtWidgets.QWidget, 'menu')
        
        self.background_pixmaps = {}

        # Establece la imagen de fondo para los widgets 
        self.set_background_image(self.inicio, 'fondo.jpg')
        self.set_background_image(self.menu, 'fondo2.jpg')
        
        self.inicio.resizeEvent = self.on_resize_inicio
        self.menu.resizeEvent = self.on_resize_menu

        # Configurar QLabel para mostrar el video
        self.label_foto = self.findChild(QLabel, 'foto')
        self.label_id = self.findChild(QLabel, 'id')
        self.label_tiempo = self.findChild(QLabel, 'tiempo')

        # Crear un hilo para la captura de video
        self.thread = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time = QTime(0, 0)
        self.start_delay_timer = QTimer(self)
        self.start_delay_timer.timeout.connect(self.start_counter)
        self.elapsed_timer = QElapsedTimer()
        self.is_first_start = True
        self.paused_time = QTime(0, 0)

        
    def set_background_image(self, widget, image_path):
        self.background_pixmaps[widget] = QPixmap(image_path)
        self.update_background(widget)

    def update_background(self, widget):
        palette = QPalette()
        scaled_pixmap = self.background_pixmaps[widget].scaled(widget.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
        widget.setAutoFillBackground(True)
        widget.setPalette(palette)

    def on_resize_inicio(self, event):
        self.update_background(self.inicio)
        QWidget.resizeEvent(self.inicio, event)
    
    def on_resize_menu(self, event):
        self.update_background(self.menu)
        QWidget.resizeEvent(self.menu, event)
        
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()
        
    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.expandirbtn1.hide()
            self.comprimirbtn1.show()
        else:
            self.showNormal()
            self.comprimirbtn1.hide()
            self.expandirbtn1.show()
            
    def mover_ventana2(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.expandirbtn2.hide()
            self.comprimirbtn2.show()
        else:
            self.showNormal()
            self.comprimirbtn2.hide()
            self.expandirbtn2.show()
            
    def minimizar1(self):
        self.showMinimized()
        
    def minimizar2(self):
        self.showMinimized()

    def comprimir1(self):
        self.showNormal()
        self.comprimirbtn1.hide()
        self.expandirbtn1.show()
        
    def comprimir2(self):
        self.showNormal()
        self.comprimirbtn2.hide()
        self.expandirbtn2.show()
        
    def expandir1(self):
        self.showMaximized()
        self.expandirbtn1.hide()
        self.comprimirbtn1.show()
    
    def expandir2(self):
        self.showMaximized()
        self.expandirbtn2.hide()
        self.comprimirbtn2.show()

    def iniciar_camara(self):
        if self.thread is None:
            self.thread = VideoThread()
            self.thread.change_pixmap_signal.connect(self.mostrar_frame)
        self.thread.running = True
        self.thread.start()
        
        self.start_delay_timer.start(15000)  # 15 segundos
        self.elapsed_timer.start()
        self.label_tiempo.setText("      Iniciando...      ")
        
    def pausar_camara(self):
        if self.thread is not None:
            self.thread.stop()
        self.timer.stop()
        self.start_delay_timer.stop()
        self.paused_time = self.time

    def detener_camara(self):
        if self.thread is not None:
            self.thread.stop()
            self.thread = None
        self.timer.stop()
        self.start_delay_timer.stop()
        self.label_foto.clear()
        self.label_id.setText("")
        self.label_tiempo.setText("      00:00      ")
        self.is_first_start = True
        self.paused_time = QTime(0, 0)
        
    def reiniciar_tiempo(self):
        self.time = QTime(0, 0)
        self.label_tiempo.setText("      00:00      ")
        self.timer.stop()
        self.start_delay_timer.stop()
        self.is_first_start = True
        self.paused_time = QTime(0, 0)

    def start_counter(self):
        self.start_delay_timer.stop()
        if self.is_first_start:
            self.time = QTime(0, 0)
            self.is_first_start = False
        else:
            self.time = self.paused_time
        self.timer.start(1000)  # Actualizar cada segundo
        self.update_time()

    def start_counter(self):
        self.start_delay_timer.stop()
        if self.is_first_start:
            self.time = QTime(0, 0)
            self.is_first_start = False
        else:
            self.time = self.paused_time
        self.timer.start(1000)  # Actualizar cada segundo
        self.update_time()
        
    def update_time(self):
        if self.start_delay_timer.isActive():
            elapsed = self.elapsed_timer.elapsed()
            if elapsed >= 15000:  # Si han pasado 15 segundos o más
                self.start_counter()
            else:
                remaining = 15 - (elapsed // 1000)
                self.label_tiempo.setText(f"      Iniciando en {remaining}...      ")
        else:
            self.time = self.time.addSecs(1)
            self.label_tiempo.setText(self.time.toString("      mm:ss      "))
            
    def mostrar_frame(self, frame):
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
        color_rgb = "gray"
        if saturation > 50 and value > 50:
            if (hue_value < 10) or (hue_value > 170):
                color = "Rojo"
                color_rgb = "red"
            elif 25 <= hue_value < 35:
                color = "Amarillo"
                color_rgb = "yellow"
            elif 35 <= hue_value < 85:
                color = "Verde"
                color_rgb = "green"
            elif 85 <= hue_value < 130:
                color = "Azul"
                color_rgb = "blue"

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

        # Actualizar el label con la forma y color detectados
        resultado = f"{forma} {color}"
        self.label_id.setText(resultado)
        self.label_id.setStyleSheet(f"color: {color_rgb};")

        # Convertir imagen para mostrar en QLabel
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.label_foto.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.label_foto.setPixmap(QPixmap.fromImage(p))

    def closeEvent(self, event):
        self.detener_camara()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
