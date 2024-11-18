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
        self.btnMas.clicked.connect(lambda: self.agregarOperacion("+"))
        self.btnMenos.clicked.connect(lambda: self.agregarOperacion("-"))
        self.btnPor.clicked.connect(lambda: self.agregarOperacion("*"))
        self.btnDivi.clicked.connect(lambda: self.agregarOperacion("/"))
        self.btnIgual.clicked.connect(self.calcular)
        
        self.btnPunto.clicked.connect(self.setPunto)
        
        self.btnAC.clicked.connect(self.setCero)
        
    def keyPressEvent(self, key: QKeyEvent) -> None:
        super().keyPressEvent(key)
        if key.key() >= QtCore.Qt.Key.Key_0 and key.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(key.key() - QtCore.Qt.Key.Key_0)
        elif key.key() == QtCore.Qt.Key.Key_Period:
            self.setPunto()
        elif key.key() == QtCore.Qt.Key.Key_Plus:
            self.agregarOperacion("+")
        elif key.key() == QtCore.Qt.Key.Key_Minus:
            self.agregarOperacion("-")
        elif key.key() == QtCore.Qt.Key.Key_Asterisk:
            self.agregarOperacion("*")
        elif key.key() == QtCore.Qt.Key.Key_Slash:
            self.agregarOperacion("/")
        elif key.key() == QtCore.Qt.Key.Key_Return or key.key() == QtCore.Qt.Key.Key_Enter:
            self.calcular(self.etiqueta.text())

        
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
            if cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit()) or ("." in cadena and all(char.isdigit() or char == "." for char in cadena)):
                flotante = float(cadena)
                if flotante.is_integer():
                    entero = int(flotante)
                    cadena = str(entero)
                else:
                    cadena = str(flotante)
            self.etiqueta.setText(cadena)
    
    def calcular(self, operacion):
        
        operacion = self.etiqueta.text()
        if '+' in operacion:
            operandos = operacion.split('+')
            resultado = float(operandos[0])
            for op in operandos[1:]:
                resultado += float(op)
        elif '-' in operacion:
            operandos = operacion.split('-')
            resultado = float(operandos[0])
            for op in operandos[1:]:
                resultado -= float(op)
        elif '*' in operacion:
            operandos = operacion.split('*')
            resultado = float(operandos[0])
            for op in operandos[1:]:
                resultado *= float(op)
        elif '/' in operacion:
            operandos = operacion.split('/')
            resultado = float(operandos[0])
            for op in operandos[1:]:
                if float(op) != 0:
                    resultado /= float(op)
                else:
                    resultado = "Error"
                    break
        else:
            resultado = operacion

        self.etiqueta.setText(str(resultado))

    def agregarOperacion(self, operacion):
        cadena = self.etiqueta.text()
        if cadena == "0":
            self.etiqueta.setText(operacion)
        else:
            self.etiqueta.setText(cadena + operacion)
        
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    