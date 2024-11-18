from PyQt6.QtGui import QKeyEvent
from Ui_ejemplo_calculadora import *
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        self.bt0.clicked.connect(self.setNumero)
        self.bt1.clicked.connect(self.setNumero)
        self.bt2.clicked.connect(self.setNumero)
        self.bt3.clicked.connect(self.setNumero)
        self.bt4.clicked.connect(self.setNumero)
        self.bt5.clicked.connect(self.setNumero)
        self.bt6.clicked.connect(self.setNumero)
        self.bt7.clicked.connect(self.setNumero)
        self.bt8.clicked.connect(self.setNumero)
        self.bt9.clicked.connect(self.setNumero)
        self.ac.clicked.connect(self.setCero)
        self.punto.clicked.connect(self.setPunto)
        self.suma.clicked.connect(self.Suma)
        self.igual.clicked.connect(self.Calcular)
        self.resta.clicked.connect(self.Resta)
        self.multi.clicked.connect(self.Multi)
        self.div.clicked.connect(self.Div)

        self.primer_numero=None
        self.operacion=None
    
    def Div(self):
        self.primer_numero = float(self.ventana.text())
        self.operacion_actual ="div"
        self.setCero()

    def Multi(self):
        self.primer_numero = float(self.ventana.text())
        self.operacion_actual ="multiplicacion"
        self.setCero()

    def Resta(self):
        self.primer_numero = float(self.ventana.text())
        self.operacion_actual ="resta"
        self.setCero()

    def Calcular(self):
        segundo=float(self.ventana.text())
        if self.operacion_actual=="suma":
            resultado=self.primer_numero+segundo
        elif self.operacion_actual=="resta":
            resultado=self.primer_numero-segundo
        
        elif self.operacion_actual=="multiplicacion":
            resultado=self.primer_numero*segundo
            
        elif self.operacion_actual=="div":
            try:
                resultado=self.primer_numero/segundo
            except ZeroDivisionError:
                self.ventana.setText("Error")

        self.ventana.setText(str(resultado)) 
    
            
    def Suma(self):
       self.primer_numero = float(self.ventana.text())
       self.operacion_actual ="suma"
       self.setCero()

    def keyPressEvent(self, key: QKeyEvent) -> None:
        super().keyPressEvent(key)
        if key.key()>= QtCore.Qt.Key.Key_0 and key.key()<= QtCore.Qt.Key.Key_9:
            self.setNumber(key.key()-QtCore.Qt.Key.Key_0)
        elif key.key()==QtCore.Qt.Key.Key_Period:
            self.setPunto()

    def setNumber(self,numero:int):
        cadena=self.ventana.text()+str(numero)
        flotante=float(cadena)
        if flotante.is_integer():
            entero=int(flotante)
            cadena=str(entero)
        else:
            cadena=str(flotante)
        self.ventana.setText(cadena)

    def setPunto(self):
        cadena=self.ventana.text()
        if cadena.find(".")==-1:
            cadena=cadena + "."
            self.ventana.setText(cadena)
        
    def setCero(self):
        self.ventana.setText("0")
    def setNumero(self):
        cadena=self.ventana.text()+self.sender().text()
        flotante=float(cadena)
        if flotante.is_integer():
            entero=int(flotante)
            cadena=str(entero)
        else:
            cadena=str(flotante)
        
        self.ventana.setText(cadena)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    