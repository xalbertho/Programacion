from PyQt6.QtGui import QKeyEvent
from Ui_calculadora import *
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.btn0.clicked.connect(self.setNumero)
        self.btn1.clicked.connect(self.setNumero)
        self.btn2.clicked.connect(self.setNumero)
        self.btn3.clicked.connect(self.setNumero)
        self.btn4.clicked.connect(self.setNumero)
        self.btn5.clicked.connect(self.setNumero)
        self.btn6.clicked.connect(self.setNumero)
        self.btn7.clicked.connect(self.setNumero)
        self.btn8.clicked.connect(self.setNumero)
        self.btn9.clicked.connect(self.setNumero)
        
        self.btnPunto.clicked.connect(self.setPunto)
        
        self.btnAC.clicked.connect(self.setCero)
        
    def keyPressEvent(self, key: QKeyEvent) -> None:
        super().keyPressEvent(key)
        if key.key() >= QtCore.Qt.Key.Key_0 and key.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(key.key()-QtCore.Qt.Key.Key_0)
        elif key.key() == QtCore.Qt.Key.Key_Period:
            self.setPunto()

        
    def setCero(self):
        self.etiqueta.setText("0")
        
    def setPunto(self):
        cadena = self.etiqueta.text()
        if cadena.find(".") == -1:
            cadena = cadena + "."
            self.etiqueta.setText(cadena)  
    
    def setNumber(self, numero:int):
        cadena = self.etiqueta.text() + str(numero)
        flotante = float(cadena)
        if flotante.is_integer():
            entero = int(flotante)
            cadena = str(entero)
        else:
            cadena = str(flotante)
            
        self.etiqueta.setText(cadena)
    
    def setNumero(self):
        cadena = self.etiqueta.text() + self.sender().text()
        flotante = float(cadena)
        if flotante.is_integer():
            entero = int(flotante)
            cadena = str(entero)
        else:
            cadena = str(flotante)
            
        self.etiqueta.setText(cadena)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    