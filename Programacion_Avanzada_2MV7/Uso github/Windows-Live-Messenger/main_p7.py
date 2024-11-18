from Ui_diseño import *
import sys, random,time, pyfirmata
from PyQt6.uic import loadUi
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,QMessageBox
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QThread, pyqtSignal

import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.perfilBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(0))
        self.contactosBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(1))
        self.mensajesBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(2))
        self.ajustesBtn.clicked.connect(lambda :self.mainmenu.setCurrentIndex(0))
        self.infoBtn.clicked.connect(lambda :self.mainmenu.setCurrentIndex(1))
        self.csesionBtn.clicked.connect(self.close)
        self.notificacionBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))
        self.masBtn.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(1))
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())