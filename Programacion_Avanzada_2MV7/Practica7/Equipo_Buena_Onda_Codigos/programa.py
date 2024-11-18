import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMainWindow, QApplication


nombre=""
contraseña=""

class Ingreso(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ingreso.ui', self)
        self.setup_ui()
        
    def setup_ui(self):
        self.iniciar.clicked.connect(self.iniciar_usuario)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(10, 10)
        self.arriba.mouseMoveEvent = self.mover_ventana
        self.minBtn.clicked.connect(self.showMinimized)
        self.cerrarBtn.clicked.connect(self.close)
        self.registrate.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.registrarse))
        self.regresar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inicio))
        self.registrar.clicked.connect(self.iniciar_usuario)
        

    def iniciar_usuario(self):
        self.diseño = Usuario()
        self.diseño.show()
        self.close()
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()
        
    def mover_ventana(self, event):
        if not self.isMaximized() and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
            self.click_posicion = event.globalPosition()
            event.accept()
            

class Usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('diseño.ui', self)
        self.setup_ui()

    def setup_ui(self):
        self.csesionBtn.clicked.connect(self.inicio_sesion)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(10, 10)
        self.arriba.mouseMoveEvent = self.mover_ventana
        self.init_menu()
        self.minBtn.clicked.connect(self.showMinimized)
        self.cerrarBtn.clicked.connect(self.close)
        self.perfilBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.perfil))
        self.contactosBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.contactos))
        self.mensajesBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.mensajes))
        self.editar.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editar_perfil))
        self.listo.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.perfil))

    
    def init_menu(self):
        self.menu_animacion = QPropertyAnimation(self.menu, b"maximumWidth")
        self.menu_animacion.setDuration(300)
        self.menu_animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.menu_max, self.menu_min = 150, 50
        self.funcion = True
        self.menuBtn.clicked.connect(self.manipular_menu)
        self.ajustesBtn.clicked.connect(lambda: self.toggle_menu(self.mainmenu, self.ajustes, "Ajustes"))
        self.infoBtn.clicked.connect(lambda: self.toggle_menu(self.mainmenu, self.informacion, "Información"))
        self.notificacionBtn.clicked.connect(lambda: self.toggle_menu(self.stackedWidget, self.notificaciones, "Notificaciones", True))
        self.masBtn.clicked.connect(lambda: self.toggle_menu(self.stackedWidget, self.mas, "Más...", True))
        self.reducirBtn.hide()
        self.menucentral.hide()
        self.rightmenu.hide()
        self.reducirBtn.clicked.connect(self.showNormal)
        self.maxBtn.clicked.connect(self.showMaximized)
    
    def inicio_sesion(self):
        self.ingreso = Ingreso()
        self.ingreso.show()
        self.close()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - 10, rect.bottom() - 10)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()
        
    def mover_ventana(self, event):
        if not self.isMaximized() and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
            self.click_posicion = event.globalPosition()
            event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
        else:
            self.showNormal()
    
    def manipular_menu(self):
        inicio, fin = (self.menu_max, self.menu_min) if self.funcion else (self.menu_min, self.menu_max)
        self.menu_animacion.setStartValue(inicio)
        self.menu_animacion.setEndValue(fin)
        self.menu_animacion.start()
        self.funcion = not self.funcion
        
    def toggle_menu(self, widget, page, text, is_right=False):
        menu = self.rightmenu if is_right else self.menucentral
        menu.setVisible(not menu.isVisible())
        if menu.isVisible():
            widget.setCurrentWidget(page)
            label = self.menusuperior if is_right else self.menuinferior
            label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pantalla_ingreso = Ingreso()
    pantalla_ingreso.show()
    sys.exit(app.exec())
