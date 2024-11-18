import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit


class PetStoreApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pet Store')
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Crear acciones para el menú
        self.create_actions()

        # Crear menú
        self.create_menu()

    def create_actions(self):
        self.inventory_action = QAction('Administrar Inventario', self)
        self.inventory_action.triggered.connect(self.show_inventory)

        self.sell_action = QAction('Vender Mascotas', self)
        self.sell_action.triggered.connect(self.sell_pets)

        self.report_action = QAction('Imprimir Reportes', self)
        self.report_action.triggered.connect(self.print_reports)

        self.exit_action = QAction('Salir', self)
        self.exit_action.triggered.connect(self.close)

    def create_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('Opciones')

        file_menu.addAction(self.inventory_action)
        file_menu.addAction(self.sell_action)
        file_menu.addAction(self.report_action)
        file_menu.addAction(self.exit_action)

    def show_inventory(self):
        # Lógica para mostrar el inventario
        self.text_edit.clear()
        self.text_edit.append('Aquí se mostrará el inventario.')

    def sell_pets(self):
        # Lógica para vender mascotas
        self.text_edit.clear()
        self.text_edit.append('Aquí se mostrará la interfaz para vender mascotas.')

    def print_reports(self):
        # Lógica para imprimir reportes
        self.text_edit.clear()
        self.text_edit.append('Aquí se mostrará la interfaz para imprimir reportes.')


def main():
    app = QApplication(sys.argv)
    window = PetStoreApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
