from Ui_diseño import *
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap, QImage, QPalette, QBrush, QColor
import sys, socket,cv2
import numpy as np
from PyQt6.QtCore import QThread, pyqtSignal,QTimer, Qt, QTimer, QThread, pyqtSignal, QTime, QElapsedTimer

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

class ThreadSocket(QThread):
    global connected
    signal_message = pyqtSignal(str)

    def __init__(self, host, port):
        global connected
        super().__init__()
        self.host = host
        self.port = port

    def run(self):
        global connected
        try:
            server.connect((self.host, self.port))
            connected = True

            while connected:
                message = server.recv(BUFFER_SIZE)
                if message:
                    self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconnected!!>")
                    break
                
        except Exception as e:
            self.signal_message.emit(f"<!!error!!> {str(e)}")
        finally:
            server.close()
            connected = False
        
    def stop(self):
        global connected
        connected = False
        self.wait()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        server = '3.136.134.23'
        port = 5000
        self.coneccion = ThreadSocket(server, int(port))
        self.coneccion.signal_message.connect(self.mensage_entrante)
        self.coneccion.start()
        self.pushButton_3.clicked.connect(self.iniciar_camara)
        self.elapsed_timer = QElapsedTimer()

        self.perillas.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.diales = [self.dial_1, self.dial_2, self.dial_3, self.dial_4, self.dial_5, self.dial_6]
        self.servos = []


        self.thread = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.time = QTime(0, 0)
        self.start_delay_timer = QTimer(self)
        self.start_delay_timer.timeout.connect(self.start_counter)
        self.elapsed_timer = QElapsedTimer()
        self.is_first_start = True
        self.paused_time = QTime(0, 0)
        
        for i, dial in enumerate(self.diales):
            dial.valueChanged.connect(lambda value, index=i: self.mueveServo(value, index))


    def start_counter(self):
        self.start_delay_timer.stop()
        if self.is_first_start:
            self.time = QTime(0, 0)
            self.is_first_start = False
        else:
            self.time = self.paused_time
        self.timer.start(1000)  # Actualizar cada segundo
        self.update_time()
    def iniciar_camara(self):
        if self.thread is None:
            self.thread = VideoThread()
            self.thread.change_pixmap_signal.connect(self.mostrar_frame)
        self.thread.running = True
        self.thread.start()
        
        self.start_delay_timer.start(15000)  # 15 segundos
        self.elapsed_timer.start()
        
    def update_time(self):
        if self.start_delay_timer.isActive():
            elapsed = self.elapsed_timer.elapsed()
            if elapsed >= 15000:  # Si han pasado 15 segundos o más
                self.start_counter()
            else:
                remaining = 15 - (elapsed // 1000)
                
        else:
            self.time = self.time.addSecs(1)
            #self.label_tiempo.setText(self.time.toString("      mm:ss      "))
    def mensage_entrante(self, mensaje):
        print(f"Mensaje recibido: {mensaje}")
        if mensaje.startswith("SERVO:"):
            partes = mensaje.split(":")
            if len(partes) == 3:
                servo_num = int(partes[1])
                valor = int(partes[2])
                if 1 <= servo_num <= len(self.diales):
                    # Desconectamos temporalmente la señal para evitar recursión
                    self.diales[servo_num - 1].valueChanged.disconnect()
                    self.diales[servo_num - 1].setValue(valor)
                    self.mueveServo(valor, servo_num - 1)
                    # Reconectamos la señal
                    self.diales[servo_num - 1].valueChanged.connect(
                        lambda value, index=servo_num-1: self.mueveServo(value, index))
                    print(f"Servo {servo_num} actualizado a: {valor}")

    def mueveServo(self, value, index):
        print(f"Moviendo Servo {index + 1}: {value}")
        if self.servos:
            self.servos[index].write(value)


    def move_to_position(self, target_positions):
        for index, target in enumerate(target_positions):
            current_value = self.diales[index].value()
            step = 1 if target > current_value else -1
            timer = QTimer(self)
            timer.setInterval(50)  # Adjust the interval for smooth movement
            timer.timeout.connect(lambda index=index, current_value=current_value, target=target, step=step, timer=timer: self.move_servo_step(index, current_value, target, step, timer))
            timer.start()
    def move_servo_step(self, index, current_value, target, step, timer):
            if (step > 0 and current_value < target) or (step < 0 and current_value > target):
                current_value += step
                self.diales[index].setValue(current_value)
                self.mueveServo(current_value, index)
            else:
                timer.stop()
   
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
            
            resultado = f"{color}"
            print(resultado)
            #self.label_id.setStyleSheet(f"color: {color_rgb};")

            # Convertir imagen para mostrar en QLabel
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            p = convert_to_Qt_format.scaled(self.label_2.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.label_2.setPixmap(QPixmap.fromImage(p))
if __name__ == "__main__":
    BUFFER_SIZE = 1024  
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    app = QApplication(sys.argv)
    
    import pyfirmata
    board = pyfirmata.Arduino('COM7')
    it = pyfirmata.util.Iterator(board)
    it.start()
    servo_pins = ['d:2:s', 'd:3:s', 'd:4:s', 'd:5:s', 'd:6:s', 'd:7:s']
    window = MainWindow()
    
   
    for pin in servo_pins:
        window.servos.append(board.get_pin(pin))
    
    window.show()
    sys.exit(app.exec())