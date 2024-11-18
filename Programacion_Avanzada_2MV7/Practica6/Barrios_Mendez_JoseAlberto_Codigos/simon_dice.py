import sys, random,time, pyfirmata
from PyQt6.uic import loadUi
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,QMessageBox
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QThread

from Ui_diseño import *
from PyQt6.QtWidgets import QMainWindow

class JuegoThread(QThread):
    actualizar_ui = QtCore.pyqtSignal(str)
    juego_terminado = QtCore.pyqtSignal(str)

    def __init__(self, main_window, parent=None):
        super(JuegoThread, self).__init__(parent)
        self.main_window = main_window
        self.secuencia = []

    def run(self):
        while True:
            self.main_window.elegir_jugador()
            time.sleep(1)
            self.main_window.servo.write(94)
            self.secuencia = self.main_window.agregar_secuencia()
            print(self.secuencia)
            self.main_window.enviar_secuencia()
            respuesta_correcta = self.main_window.recibe_respuesta(len(self.secuencia))

            if respuesta_correcta:
                self.actualizar_ui.emit("Respuesta correcta, continúe.")
            else:
                self.actualizar_ui.emit("Game Over: Respuesta incorrecta.")
                self.juego_terminado.emit("Game Over")
                break
            time.sleep(1)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.jugadores1.clicked.connect(self.ir_nombres)
        self.jugadores2.clicked.connect(self.ir_nombres)
        self.jugadores3.clicked.connect(self.ir_nombres)
        self.jugadores4.clicked.connect(self.ir_nombres)
        self.jugadores5.clicked.connect(self.ir_nombres)
        self.numero_jugadores=0
        self.menu.clicked.connect(self.ir_a_menu_principal)
        self.menu_multi.clicked.connect(self.ir_a_menu_principal)
        self.menu_puntaje.clicked.connect(self.ir_a_menu_principal)
        self.menu_2p.clicked.connect(self.ir_a_menu_principal)
        self.menu_3p.clicked.connect(self.ir_a_menu_principal)
        self.menu_4p.clicked.connect(self.ir_a_menu_principal)
        self.menu_5p.clicked.connect(self.ir_a_menu_principal)
        self.menu_r.clicked.connect(self.ir_a_menu_principal)
        self.menu_s.clicked.connect(self.ir_a_menu_principal)
        self.menu_puntaje.clicked.connect(self.ir_a_menu_principal)
        self.exit.clicked.connect(self.close)
        self.cerrar.clicked.connect(self.close)
        self.scores.clicked.connect(self.ir_rank)
        self.scores_2.clicked.connect(self.ir_rank)
        self.scores_5.clicked.connect(self.ir_rank)
        self.scores_6.clicked.connect(self.ir_rank)
        self.scores_4.clicked.connect(self.ir_rank)
        self.extremo.clicked.connect(self.ir_nombres)
        self.extremo.clicked.connect(self.ir_extremo)
        self.play_5.clicked.connect(self.ventana_iniciar)
        self.play_1.clicked.connect(self.ventana_iniciar)
        self.play_2.clicked.connect(self.ventana_iniciar)
        self.play_3.clicked.connect(self.ventana_iniciar)
        self.play_4.clicked.connect(self.ventana_iniciar)
        #self.iniciar_1jugador.clicked.connect(self.jugar_1_integrante)
        #self.iniciar_multijugador.clicked.connect(self.jugar_varios_integrantes)
        
        
        self.arduino=pyfirmata.Arduino('COM3')
        
        it = pyfirmata.util.Iterator(self.arduino)
        it.start()
        self.servo=self.arduino.get_pin('d:7:s')
        self.servo.write(94)

        self.buttons_pins = [self.arduino.get_pin(f'd:{pin}:i') for pin in [9, 10, 11, 12]]
        self.led_pins = [self.arduino.get_pin(f'd:{pin}:o') for pin in [2, 3, 4, 5]]

        self.juego_thread = JuegoThread(self)
        self.juego_thread.actualizar_ui.connect(self.actualizar_ui)
        
        self.iniciar_multijugador.clicked.connect(self.iniciar_juego)

    def iniciar_juego(self):
        if not self.juego_thread.isRunning():
            self.juego_thread.start()

    def actualizar_ui(self, mensaje):
        # Actualiza la interfaz de usuario basándote en el mensaje del hilo
        QMessageBox.information(self, "Estado del Juego", mensaje)

    def jugar_varios_integrantes(self):
        self.secuencia=[]
        while True:
            self.elegir_jugador()
            
            time.sleep(1)
            self.servo.write(94)
            self.secuencia= self.agregar_secuencia()
            print(self.secuencia)
            self.enviar_secuencia()
            self.recibe_respuesta(len(self.secuencia))
            #para deputracion unicamente:
            if self.secuencia==self.respuesta:
                print("Respuesta correcta, continue.")
            else:
                print("game over.")
                break
        time.sleep(1)

    def elegir_jugador(self):
        
        if self.numero_jugadores==2:
            self.nombre1=self.in_nombre.toPlainText()
            self.nombre2=self.in_nombre_2.toPlainText()
        elif self.numero_jugadores==3:
            self.nombre1=self.in_nombre_3.toPlainText()
            self.nombre2=self.in_nombre_4.toPlainText()
            self.nombre3=self.in_nombre_5.toPlainText()
        elif self.numero_jugadores==4:
            self.nombre1=self.in_nombre_6.toPlainText()
            self.nombre2=self.in_nombre_7.toPlainText()
            self.nombre3=self.in_nombre_8.toPlainText()
            self.nombre4=self.in_nombre_9.toPlainText()
        elif self.numero_jugadores==5:
            self.nombre1=self.in_nombre_10.toPlainText()
            self.nombre2=self.in_nombre_11.toPlainText()
            self.nombre3=self.in_nombre_12.toPlainText()
            self.nombre4=self.in_nombre_13.toPlainText()
            self.nombre5=self.in_nombre_14.toPlainText()
        self.jug_elegido=random.randint(1,self.numero_jugadores)
        if self.jug_elegido==1:
            self.label_nombre_jugador.setText(self.nombre1)

            self.servo.write(60)
        elif self.jug_elegido==2:
            self.label_nombre_jugador.setText(self.nombre2)
            time.sleep(.5)
            self.servo.write(120)
        elif self.jug_elegido==3:
            self.label_nombre_jugador.setText(self.nombre3)
            time.sleep(.5)
            self.servo.write(180)
        elif self.jug_elegido==4:
            self.label_nombre_jugador.setText(self.nombre4)
            time.sleep(.5)
            self.servo.write(240)
        elif self.jug_elegido==5:
            self.label_nombre_jugador.setText(self.nombre4)
            time.sleep(.5)
            self.servo.write(320)

       



    def recibe_respuesta(self,longitud) :
        self.respuesta=[]
        for _ in range(longitud):
            respuesta=self.espera_presion_boton()
            self.respuesta.append(respuesta)
            print(f"Respuesta recibida{respuesta}")

    def espera_presion_boton(self):
        while True:
            for i,j in enumerate(self.buttons_pins):
                if j.read():
                    self.led_pins[i].write(1)
                    while j.read():
                        pass
                    self.led_pins[i].write(0)
                    return i


    def enviar_secuencia(self):
        for i in self.secuencia:
            self.led_pins[i].write(1)
            time.sleep(.5)
            self.led_pins[i].write(0)
            time.sleep(.5)
  
    def agregar_secuencia(self):
        self.secuencia.append(random.randint(0,3))
        return self.secuencia

        
        
    def ventana_iniciar(self):
        sender=self.sender()
        if sender==self.play_5:
            self.stackedWidget.setCurrentIndex(3)
        else:
            self.stackedWidget.setCurrentIndex(8)
    def ir_extremo(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def ir_rank(self):
        self.stackedWidget.setCurrentIndex(9)
    def ir_a_menu_principal(self):
        self.stackedWidget.setCurrentIndex(0)

    def ir_nombres(self):
        sender=self.sender()
        
        if sender==self.jugadores1:
            self.numero_jugadores=1
            self.stackedWidget.setCurrentIndex(1)
        elif sender==self.jugadores2:
            self.numero_jugadores=2
            self.stackedWidget.setCurrentIndex(4)
        elif sender==self.jugadores3:
            self.numero_jugadores=3
            self.stackedWidget.setCurrentIndex(5)
        elif sender==self.jugadores4:
            self.numero_jugadores=4
            self.stackedWidget.setCurrentIndex(6)
        elif sender==self.jugadores5:
            self.numero_jugadores=5
            self.stackedWidget.setCurrentIndex(7)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())