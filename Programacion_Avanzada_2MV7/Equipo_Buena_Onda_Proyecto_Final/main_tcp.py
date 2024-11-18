from Ui_diseño import *
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys, pyfirmata, socket
from PyQt6.QtCore import QThread, pyqtSignal, QTimer

class ThreadSocket(QThread):
    signal_message = pyqtSignal(str)

    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.connected = False
        self.server = None

    def run(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.connect((self.host, self.port))
            self.connected = True
            self.signal_message.emit("<!!connected!!>")

            while self.connected:
                try:
                    message = self.server.recv(BUFFER_SIZE)
                    if message:
                        self.signal_message.emit(message.decode("utf-8"))
                    else:
                        self.signal_message.emit("<!!disconnected!!>")
                        break
                except Exception as e:
                    self.signal_message.emit(f"<!!error receiving!!> {str(e)}")
                    break
                
        except Exception as e:
            self.signal_message.emit(f"<!!error connecting!!> {str(e)}")
        finally:
            if self.server:
                self.server.close()
            self.connected = False
        
    def stop(self):
        self.connected = False
        if self.server:
            self.server.close()
        self.wait()

    def send_message(self, message):
        if self.connected:
            try:
                self.server.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error al enviar mensaje: {str(e)}")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        server = '3.136.134.23'
        port = 5000
        self.coneccion = ThreadSocket(server, int(port))
        self.coneccion.signal_message.connect(self.mensaje_entrante)
        self.coneccion.start()

        self.perillas.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
        self.diales = [self.dial_1, self.dial_2, self.dial_3, self.dial_4, self.dial_5, self.dial_6]
        self.servos = []
        for i, dial in enumerate(self.diales):
            dial.valueChanged.connect(lambda value, index=i: self.mueveServo(value, index))
        
        # Timer para enviar pings
        self.ping_timer = QTimer(self)
        self.ping_timer.timeout.connect(self.send_ping)
        self.ping_timer.start(5000)  # Enviar ping cada 5 segundos

    def mensaje_entrante(self, message):
        print(f"Mensaje recibido: {message}")
        if message == "<!!disconnected!!>":
            self.coneccion.stop()

    def enviar_valores_servos(self):
        if hasattr(self, 'coneccion') and self.coneccion.isRunning():
            for i, dial in enumerate(self.diales):
                servo_num = i + 1
                valor = dial.value()
                mensaje = f"SERVO:{servo_num}:{valor}"
                self.coneccion.send_message(mensaje)

    def mueveServo(self, value, index):
        print(f"Servo {index + 1}: {value}")
        if hasattr(self, 'coneccion') and self.coneccion.isRunning():
            mensaje = f"SERVO:{index + 1}:{value}"
            self.coneccion.send_message(mensaje)

    def send_ping(self):
        if hasattr(self, 'coneccion') and self.coneccion.isRunning():
            self.coneccion.send_message("PING")

if __name__ == "__main__":
    BUFFER_SIZE = 1024
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
