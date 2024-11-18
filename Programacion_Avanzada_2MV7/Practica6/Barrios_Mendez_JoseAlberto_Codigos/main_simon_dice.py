import sys, random,time, pyfirmata
from PyQt6.uic import loadUi
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,QMessageBox
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QThread, pyqtSignal

from Ui_diseño import *
from PyQt6.QtWidgets import QMainWindow

class JuegoThread(QThread):
    exito =  pyqtSignal(bool)
    def __init__(self, main_window, parent=None):
        super(JuegoThread, self).__init__(parent)
        self.main_window = main_window
        self.main_window.secuencia = []
    
    def run(self):
        while True:
            
            self.exit.emit(False)
            time.sleep(1)
            #self.main_window.jugar_varios_integrantes()
            #if self.main_window.secuencia != self.main_window.respuesta:
            #    break
        
  
class JuegoThread2(QThread):
    def __init__(self,main_window, parent=None):
        super(JuegoThread2,self).__init__(parent)
        self.main_window=main_window
        
    def run(self):
        while True:
            self.main_window.un_solo_jugador()
            if self.main_window.secuencia!=self.main_window.respuesta:
                break
            
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        
    
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
            
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
        self.reducir.clicked.connect(self.reducirr)
        self.expandir.clicked.connect(self.expandirr)
        self.minimizar.clicked.connect(self.minimizarr)
        self.exit.clicked.connect(self.close)
        self.cerrar.clicked.connect(self.close)

        self.extremo.clicked.connect(self.ir_nombres)
        self.extremo.clicked.connect(self.ir_extremo)
        self.play_5.clicked.connect(self.ventana_1jugador)
        self.play_1.clicked.connect(self.ventana_iniciar)
        self.play_2.clicked.connect(self.ventana_iniciar)
        self.play_3.clicked.connect(self.ventana_iniciar)
        self.play_4.clicked.connect(self.ventana_iniciar)
        self.lento.clicked.connect(self. velocidad)
        self.lento_2.clicked.connect(self. velocidad)
        self.rapido.clicked.connect(self. velocidad)
        self.rapido_2.clicked.connect(self. velocidad)
        self.medio.clicked.connect(self. velocidad)
        self.medio_2.clicked.connect(self. velocidad)
 
        self.actualizar.clicked.connect(self.act_ranking)
        self.reducir.hide()
             
        self.nombre1=""
        self.nombre2=""
        self.nombre3=""
        self.nombre4=""
        self.nombre5=""
        self.puntaje1=0
        self.puntaje2=0
        self.puntaje3=0
        self.puntaje4=0
        self.puntaje5=0
        self.velocidad=0

        self.iniciar_multijugador.clicked.connect(self.iniciar_juego)
        self.iniciar_1jugador.clicked.connect(self.iniciar_para_1_jugador)
        self.arduino=pyfirmata.Arduino('COM3')
        
        self.arriba.mouseMoveEvent = self.mover_ventana
        
        it = pyfirmata.util.Iterator(self.arduino)
        it.start()
        self.servo=self.arduino.get_pin('d:7:s')
        self.servo.write(94)

        self.buttons_pins = [self.arduino.get_pin(f'd:{pin}:i') for pin in [9, 10, 11, 12]]
        self.led_pins = [self.arduino.get_pin(f'd:{pin}:o') for pin in [2, 3, 4, 5]]

        self.juego_thread = JuegoThread(self)
        self.juego2_thread=JuegoThread2(self)

        self.juego_thread.exito.connect(self.mensaje)
        self.juego_thread.start()
    
    def mensaje(self, bandera):
        print(bandera)
    
    def minimizarr(self):
        self.showMinimized()

    def reducirr(self):
        self.showNormal()
        self.reducir.hide()
        self.expandir.show()
        
    def expandirr(self):
        self.showMaximized()
        self.expandir.hide()
        self.reducir.show()
        
    def act_ranking(self):
        nombre = self.in_nombre1.toPlainText()
        puntaje = str(self.agregar_puntaje_unjugador())  
        
        with open('scores.txt', 'a') as archivo:
            archivo.write(f"{nombre},{puntaje}\n")

        with open('scores.txt', 'r') as archivo:
            record = [line.strip().split(',') for line in archivo]

        self.tableWidget.setRowCount(len(record))
        for linea, linea_data in enumerate(record):
            for columna, valor in enumerate(linea_data):
                item = (QTableWidgetItem(valor))
                self.tableWidget.setItem(linea, columna, item)
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.resizeColumnToContents(i)
        nombre = ""
        puntaje = "" 

    
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()
        
    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move (self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.expandir.hide()
            self.reducir.show()
        else:
            self.showNormal()
            self.reducir.hide()
            self.expandir.show()
       
    def reiniciar_juego(self):
        self.secuencia = []
        self.respuesta = []
        self.puntaje1 = 0
        self.puntaje2 = 0
        self.puntaje3 = 0
        self.puntaje4 = 0
        self.puntaje5 = 0
        self.nombre1=""
        self.nombre2=""
        self.nombre3=""
        self.nombre4=""
        self.nombre5=""

        num_filas=self.tableWidget.rowCount()
        num_columnas = self.tableWidget.columnCount()

        for fila in range(num_filas):
            for columna in range(num_columnas):
        
                nuevo_elemento = QTableWidgetItem("")

                self.tableWidget.setItem(fila, columna, nuevo_elemento)
        
    def iniciar_para_1_jugador(self):
        if not self.juego2_thread.isRunning():
            self.juego2_thread.start()

    def un_solo_jugador(self):
        self.secuencia=[]
        if self.velocidad is None:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una velocidad antes de iniciar.')

        while True:
        
            time.sleep(1)
            self.secuencia= self.agregar_secuencia()
            print(self.secuencia)
            self.enviar_secuencia()
            self.recibe_respuesta(len(self.secuencia))
            self.agregar_puntaje_unjugador()
            #para deputracion unicamente:

            if self.secuencia==self.respuesta:
                print("Respuesta correcta, continua.")
            else:
                print("game over.")
                break
        self.reiniciar_juego()
        time.sleep(1)

    def iniciar_juego(self):
        if not self.juego_thread.isRunning():
            self.juego_thread.start()
            

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
            self.agregar_puntaje()
            #para deputracion unicamente:

            if self.secuencia==self.respuesta:
                print("Respuesta correcta, continue.")
            else:
                print("game over.")
                break            
        time.sleep(1)

    def agregar_puntaje(self):
            puntaje=len(self.respuesta)*2
            if self.jug_elegido==1:
                self.puntaje1=puntaje
            elif self.jug_elegido==2:
                self.puntaje2=puntaje
            elif self.jug_elegido==3:
                self.puntaje3=puntaje
            elif self.jug_elegido==4:
                self.puntaje4=puntaje
            elif self.jug_elegido==5:
                self.puntaje5=puntaje
            self.puntaje_actual.setText(str(puntaje))

    def agregar_puntaje_unjugador(self):
            puntaje=len(self.respuesta)*2
            self.label_6.setText(str(puntaje))
          
            
    def elegir_jugador(self):

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

        
    def velocidad(self):
        opcion=self.sender()
        #Vel lenta=0.5
        if opcion == self.lento or opcion==self.lento_2:
            self.velocidad = .5  # Velocidad lenta
        elif opcion == self.rapido or opcion==self.rapido_2:#.1
            self.velocidad = .25  # Velocidad rápida
        elif opcion == self.medio or opcion==self.medio_2:#.25
            self.velocidad = .1  # Velocidad media

    def enviar_secuencia(self):
        for i in self.secuencia:
            self.led_pins[i].write(1)

            time.sleep(self.velocidad)
            self.led_pins[i].write(0)
            time.sleep(self.velocidad)
  
    def agregar_secuencia(self):
        self.secuencia.append(random.randint(0,3))
        return self.secuencia
    
    def ventana_1jugador(self):
        self.nombre1 = self.in_nombre1.toPlainText()
        if self.nombre1:  # Verifica si nombre1 no está vacío
            self.stackedWidget.setCurrentIndex(3)
        else:
        # Muestra un mensaje de advertencia
            QMessageBox.warning(self, "Advertencia", "El nombre del jugador no puede estar vacío.")
        
    def ventana_iniciar(self):
        sender=self.sender()
   
        if self.numero_jugadores == 2:
            self.nombre1 = self.in_nombre.toPlainText()
            self.nombre2 = self.in_nombre_2.toPlainText()
            if not self.nombre1 or not self.nombre2:
                QMessageBox.warning(self, "Advertencia", "El nombre del jugador no puede estar vacío.")
            else:

                self.stackedWidget.setCurrentIndex(8)

        elif self.numero_jugadores == 3:
            self.nombre1 = self.in_nombre_3.toPlainText()
            self.nombre2 = self.in_nombre_4.toPlainText()
            self.nombre3 = self.in_nombre_5.toPlainText()
            if not self.nombre1 or not self.nombre2 or not self.nombre3:
                QMessageBox.warning(self, "Advertencia", "El nombre del jugador no puede estar vacío.")
            else:

                self.stackedWidget.setCurrentIndex(8)

        elif self.numero_jugadores == 4:
            self.nombre1 = self.in_nombre_6.toPlainText()
            self.nombre2 = self.in_nombre_7.toPlainText()
            self.nombre3 = self.in_nombre_8.toPlainText()
            self.nombre4 = self.in_nombre_9.toPlainText()
            if not self.nombre1 or not self.nombre2 or not self.nombre3 or not self.nombre4:
                QMessageBox.warning(self, "Advertencia", "El nombre del jugador no puede estar vacío.")
            else:
      
                self.stackedWidget.setCurrentIndex(8)

        elif self.numero_jugadores == 5:
            self.nombre1 = self.in_nombre_10.toPlainText()
            self.nombre2 = self.in_nombre_11.toPlainText()
            self.nombre3 = self.in_nombre_12.toPlainText()
            self.nombre4 = self.in_nombre_13.toPlainText()
            self.nombre5 = self.in_nombre_14.toPlainText()
            if not self.nombre1 or not self.nombre2 or not self.nombre3 or not self.nombre4 or not self.nombre5:
                QMessageBox.warning(self, "Advertencia", "El nombre del jugador no puede estar vacío.")
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