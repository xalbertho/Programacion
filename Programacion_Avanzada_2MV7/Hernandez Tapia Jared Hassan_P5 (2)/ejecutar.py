from MainMascota import WelcomePet
from PyQt6.QtWidgets import QApplication
import sys

class MainWindow(WelcomePet):
    def __init__(self,app):
        super().__init__(app)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_pet = MainWindow(app)
    welcome_pet.show()
    sys.exit(app.exec())
    
#INSTALAAAAR  pip install PyQt6 PyQt6-sip
