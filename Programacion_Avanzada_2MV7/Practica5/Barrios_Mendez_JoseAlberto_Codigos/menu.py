from PyQt6.QtGui import QKeyEvent
from Ui_menu import *
import re
from PyQt6.QtWidgets import QMainWindow,QMessageBox,QFileDialog
from PyQt6.QtCore import Qt,QSize,QEvent
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QPixmap,QFont
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        
        self.inicio1.clicked.connect(self.activar_inicio1)
        self.inicio2.toggled.connect(self.activar_inicio1)
        self.inventario1.clicked.connect(self.activar_inventario1)
        self.inventario2.toggled.connect(self.activar_inventario1)
        self.comprar1.clicked.connect(self.activar_comprar1)
        self.comprar2.clicked.connect(self.activar_comprar1)
        self.acpetar_cambios.clicked.connect(self.activar_cambios)
        self.reporte1.toggled.connect(self.activar_reporte1)
        self.reporte2.toggled.connect(self.activar_reporte1)
        self.salir1.clicked.connect(self.close)
        self.totala=0

        self.gato_venta.clicked.connect(self.venta_gato)
        self.perro_venta.clicked.connect(self.venta_perro)
        self.tigre_venta.clicked.connect(self.venta_tigre)
        self.bronto_venta.clicked.connect(self.venta_bronto)
        self.vivora_venta.clicked.connect(self.venta_vivora)
        self.raptor_venta.clicked.connect(self.venta_raptor)
        self.rex_venta.clicked.connect(self.venta_rex)

        self.vender_todo.clicked.connect(self.vender)
        self.vaciar.clicked.connect(self.vaciar_carrito)
        

        
        # Conectar la función de validación a los campos de texto
        self.validar_campos_texto()

    def vaciar_carrito(self):
        self.ticket_mascota.setText('')
        self.ticket_precio.setText('')
        self.total.setText('0')

    def vender(self):
        # Obtener información del ticket
        nombre_cliente = self.nom_cliente.toPlainText()
        if nombre_cliente == '':
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese el nombre del cliente.")
            return  # Salir de la función si no se ha ingresado el nombre del cliente

        mascota = self.ticket_mascota.text()
        precio = self.ticket_precio.text()
        total = self.total.text()

# Formatear el ticket de venta
        ticket_venta = f"""
         --- Ticket de Venta ---
            Cliente: {nombre_cliente}
            Mascota:        {mascota}
            Precio:         {precio}
            Total:          {total}
        """

# Mostrar el ticket de venta
        QMessageBox.information(self, "Ticket de Venta", ticket_venta)

# Guardar el ticket en un archivo .txt
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Ticket de Venta", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(ticket_venta)
            QMessageBox.information(self, "Guardado", f"El ticket de venta ha sido guardado en {file_path}")

        
        

    def venta_rex(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.rex_precio.text())
        self.total.setText(str(self.totala+float(self.rex_precio.text())))
        self.agregar_text_al_ticket(self.rex_venta.text())

    def venta_raptor(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.raptor_precio.text())
        self.total.setText(str(self.totala+float(self.raptor_precio.text())))
        self.agregar_text_al_ticket(self.raptor_venta.text())
    

    def venta_vivora(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.vivora_presio.text())
        self.total.setText(str(self.totala+float(self.vivora_presio.text())))
        self.agregar_text_al_ticket(self.vivora_venta.text())
                                    
    def venta_bronto(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.bronto_precio.text())
        self.total.setText(str(self.totala+float(self.bronto_precio.text())))
        self.agregar_text_al_ticket(self.bronto_venta.text())

    def venta_tigre(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.tigre_precio.text())
        self.total.setText(str(self.totala+float(self.tigre_precio.text())))
        self.agregar_text_al_ticket(self.tigre_venta.text())
    
    
    def venta_perro(self):
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.perro_precio.text())
        self.total.setText(str(self.totala+float(self.perro_precio.text())))
        self.agregar_text_al_ticket(self.perro_venta.text())
    
    def venta_gato(self):
        
        self.totala=float(self.total.text())
        self.agregar_mascota_al_ticket(self.gato_precio.text())
        self.agregar_text_al_ticket(self.gato_venta.text())
        self.total.setText(str(self.totala+float(self.gato_precio.text())))
    
    def agregar_text_al_ticket(self,nueva_mascota):
        cadena=self.ticket_mascota.text()
        nueva_cadena=f"{cadena}\n{nueva_mascota}"
        self.ticket_mascota.setText(nueva_cadena)
       
    def agregar_mascota_al_ticket(self,precio_mascota):
        texto_actual_precio = self.ticket_precio.text()
        nuevo_texto_precio = f"{texto_actual_precio}\n{precio_mascota}"
        self.ticket_precio.setText(nuevo_texto_precio)


    def validar_campos_texto(self):
        self.num_gatos.installEventFilter(self)
        self.num_perros.installEventFilter(self)
        self.num_tigres.installEventFilter(self)
        self.num_rex.installEventFilter(self)
        self.num_bronto.installEventFilter(self)
        self.num_vivoras.installEventFilter(self)
        self.num_raptor.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.KeyPress:
            key = event.key()
            if key < Qt.Key.Key_0 or key > Qt.Key.Key_9:
                QMessageBox.warning(self, "Advertencia", "Por favor, ingrese solo números.")
                return True  
        return super().eventFilter(obj, event)


    def activar_cambios(self):
        self.total_perros.setText(self.num_perros.toPlainText())
        self.total_gatos.setText(self.num_gatos.toPlainText())
        self.total_tigres.setText(self.num_tigres.toPlainText())
        self.total_vivoras.setText(self.num_vivoras.toPlainText())
        self.total_bronto.setText(self.num_bronto.toPlainText())
        self.total_raptor.setText(self.num_raptor.toPlainText())
        self.total_rex.setText(self.num_rex.toPlainText())


    def activar_inicio1(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(0)

    def activar_inventario1(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(1)

    def activar_comprar1(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(2)

    def activar_reporte1(self, checked):
        if checked:
            self.stackedWidget.setCurrentIndex(3)
       
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    