from Ui_ventana import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.btnAceptar.clicked.connect(self.test)
        
    def test(self):
        QMessageBox.information(self, "Hola", "Texto", QMessageBox.StandardButton.Ok)
        # msg = QMessageBox(self)
        # msg.setWindowTitle("Saludo")
        # msg.setIcon(QMessageBox.Icon.Critical)
        # msg.setText("Hola " + self.editNombre.text())
        # msg.setInformativeText(f"Hola {self.editNombre.text()}")
        # msg.setDetailedText("Saluditos")
        # msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        # msg.exec()
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    