import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication


class pantalla(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("diseño.ui", self)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    prueba = pantalla()
    prueba.show()
    sys.exit(app.exec())