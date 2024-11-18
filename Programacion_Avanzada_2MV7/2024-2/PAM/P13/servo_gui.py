from Ui_servo_gui import *
from PyQt6.QtWidgets import QMainWindow
import sys
import pyfirmata
import time
import inspect

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.dial.valueChanged.connect(self.mueveServo)
        
    def mueveServo(self, value):
        print(value)
        pin2.write(value)
        
if __name__ == "__main__":
  
    board=pyfirmata.Arduino('COM6')

    it = pyfirmata.util.Iterator(board)
    it.start()

    pin2 = board.get_pin('d:7:s') # s para servo
    
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    