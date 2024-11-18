from Ui_diseño import *
from clases_menu import*
from Ui_ingreso import*
from PyQt6.QtWidgets import QMainWindow,QDialog,QApplication,QMessageBox,QFileDialog
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QTimer
import sys

 
class MainWindow(QMainWindow, Ui_MainWindow,Ui_Dialog):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.inicio = self.findChild(QtWidgets.QWidget, 'inicio')
        self.set_background_image(self.inicio, 'fondo.jpg')
        self.ver_menu.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        #self.nombre=""
        self.pedido = Pedido(user_input)
        
        self.label_134.setText(self.pedido.nombre)
        self.agua_b.clicked.connect(self.agregar_agua_bo)
        self.lcdNumber.setDigitCount(8)
        self.agua_s.clicked.connect(self.agregar_agua_sabor)
        self.malteada.clicked.connect(self.agregar_malteada)
        self.soda.clicked.connect(self.agregar_soda_italiana)
        self.carlota.clicked.connect(self.agregar_carlota)
        self.arroz.clicked.connect(self.agregar_arroz)
        self.flan.clicked.connect(self.agregar_flan)
        self.hotcakes.clicked.connect(self.agregar_hotc)
        self.gelatina.clicked.connect(self.agregar_gelatina)
        self.wafles.clicked.connect(self.agregar_wafles)
        self.chila_s.clicked.connect(self.agregar_chil_s)
        self.chila_p.clicked.connect(self.agregar_chilaq_p)
        self.Molletes.clicked.connect(self.agregar_Molletes)
        self.sincronizada.clicked.connect(self.agregar_sincronizada)
        self.nachos.clicked.connect(self.agregar_Nachos)
        self.tac_aho.clicked.connect(self.agregar_tacos)
        self.fruta.clicked.connect(self.agregar_fruta)
        self.verdura.clicked.connect(self.agregar_verdura)
        self.cer_1.clicked.connect(self.agregar_cerals)
        self.cer_a.clicked.connect(self.agregar_cereala)
        self.chapata.clicked.connect(self.agregar_chapata)
        self.hojaldra.clicked.connect(self.agregar_Hojaldra)
        self.pizza.clicked.connect(self.agregar_pizza)
        self.hambu.clicked.connect(self.agregar_Hambur)
        self.sopa.clicked.connect(self.agregar_sopa)
        self.s_p.clicked.connect(self.agregar_SP)
        self.s_j.clicked.connect(self.agregar_SJ)
        self.s_h.clicked.connect(self.agregar_SH)
        self.s_o.clicked.connect(self.agregar_SO)
        #self.ui=MiDialogo()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.remaining_time = 0

        self.comprar.clicked.connect(self.comprar2)
        self.borrar.clicked.connect(self.limpiar)
        

    def limpiar(self):
        mensaje=f"¿Desea borrrar lo seleccionado?\n\n"
        QMessageBox.warning(self,'Borrar pedido', mensaje)
        if mensaje:
            self.lcdNumber.setDigitCount(8)
            self.ticket.setText("")
            self.total.setText("")
            self.lcdNumber.setDigitCount(8)
            self.timer.stop()
            self.lcdNumber.display("00:00:00")


    def comprar2(self):
        # Crear el mensaje de confirmación
        mensaje = f"¿Está seguro que desea confirmar el siguiente pedido?\n\n"
        mensaje += self.pedido.obtener_lista_productos()
        mensaje += f"\n\nTotal: {self.pedido.obtener_costo_total()}"
        ticket_venta=f"{user_input}\n\n\n{self.pedido.obtener_lista_productos()}\n\n\nTotal:-------{self.pedido.obtener_costo_total()}"
        confirmacion = QMessageBox.question(self, 'Confirmar Pedido', mensaje)
                                           
        
        if confirmacion:
            QMessageBox.information(self, 'Pedido Confirmado', 
                                    'Su pedido ha sido confirmado y será preparado en breve.')

            file_path, _ = QFileDialog.getSaveFileName(self, "Guardar Ticket de Venta", "", "Text Files (*.txt)")
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(ticket_venta)
                QMessageBox.information(self, "Guardado", f"El ticket de venta ha sido guardado en {file_path}")
                
        
        else:
            QMessageBox.information(self, 'Pedido Cancelado', 
                                    'Su pedido no ha sido confirmado.')



    def actualizar(self):
        self.ticket.setText(self.pedido.obtener_lista_productos())
        self.total.setText(self.pedido.obtener_costo_total())

        # Obtener el tiempo total en minutos
        tiempo_total_minutos = self.pedido.calcular_tiempo_total()

        # Convertir minutos a segundos
        self.remaining_time = tiempo_total_minutos * 60

        # Iniciar el temporizador
        self.timer.start(1000) 
    
    def update_time(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            horas = self.remaining_time // 3600
            minutos = (self.remaining_time % 3600) // 60
            segundos = self.remaining_time % 60
            tiempo_formateado = f"{horas:02}:{minutos:02}:{segundos:02}"
            self.lcdNumber.display(tiempo_formateado)
        else:
            self.timer.stop()

    def agregar_SO(self):
        producto =Sandich_O()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_SH(self):
        producto =Sandich_H()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_SJ(self):
        producto =Sandich_J()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_SP(self):
        producto =Sandich_P()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_sopa(self):
        producto =Sopa()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_Hambur(self):
        producto =Hamburgesa()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_pizza(self):
        producto =Pizza()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_Hojaldra(self):
        producto =Hojaldra()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_chapata(self):
        producto =Chapata()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_cereala(self):
        producto =Cereal_Acom()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_cerals(self):
        producto =Cereal_S()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_verdura(self):
        producto =Verdura()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_fruta(self):
        producto =Fruta()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_tacos(self):
        producto =Tacos_ahogados()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_Nachos(self):
        producto =Nachos()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_sincronizada(self):
        producto =Sincronizada()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_Molletes(self):
        producto =Molletes()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_chilaq_p(self):
        producto =Chilaquiles_p()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_chil_s(self):
        producto =Chilaquiles_()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_wafles(self):
        producto =Wafles()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_gelatina(self):
        producto =Gelatina()
        self.pedido.agregar_item(producto)
        self.actualizar()
    
    def agregar_hotc(self):
        producto =Hot_Cakes()
        self.pedido.agregar_item(producto)
        self.actualizar()

    def agregar_flan(self):
        producto =Flan()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_arroz(self):
        producto =Arroz()
        self.pedido.agregar_item(producto)
        self.actualizar()
    def agregar_carlota(self):
        producto =Carlota()
        self.pedido.agregar_item(producto)
        self.actualizar()

    def agregar_agua_bo(self):
        producto = AguaBo()
        self.pedido.agregar_item(producto)
        self.actualizar()

    def agregar_agua_sabor(self):
        producto = AguaSabor()
        self.pedido.agregar_item(producto)
        self.actualizar()
        

    def agregar_malteada(self):
        producto = Malteada()
        self.pedido.agregar_item(producto)
        self.actualizar()

    def agregar_soda_italiana(self):
        producto = SodaItaliana()
        self.pedido.agregar_item(producto)
        self.actualizar()
    

    def set_background_image(self, widget, image_path):
        palette = widget.palette()
        palette.setBrush(widget.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(image_path)))
        widget.setPalette(palette)
        widget.setAutoFillBackground(True)

    def iniciar_sesion(self):
        dialog = QDialog(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(dialog)
        dialog.setWindowTitle("Iniciar Sesión")
        if dialog.exec() == 1:
            self.nombre = self.ui.lineEdit.text()
            print(self.nombre)
            #self.initUI()
        



class MiDialogo(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    user_input=""
    dialog = MiDialogo()
    if dialog.exec() :
        user_input = dialog.lineEdit.text()
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()
