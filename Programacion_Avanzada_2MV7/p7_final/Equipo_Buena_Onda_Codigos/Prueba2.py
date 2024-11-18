from Ui_diseño import *
from Ui_ingreso import*
from Ui_buscar_usuario import*
import sys, random,time, pyfirmata,cv2
from PyQt6.uic import loadUi
from PyQt6.QtGui import QKeyEvent,QMouseEvent,QPixmap,QImage
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,QMessageBox,QDialog,QFileDialog,QWidget,QPlainTextEdit,QLineEdit,QListWidgetItem

from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QThread, Qt, pyqtSignal,QTimer, QPoint
import socket

import sys


class ThreadSocket(QThread):
    global connected
    signal_message = pyqtSignal(str)

    def __init__(self, host, port, username):
        global connected
        super().__init__()
        self.host = host
        self.port = port
        self.username = username
        server.connect((self.host, self.port))
        connected = True

    def run(self):
        global connected
        try:
            # Enviar el nombre de usuario inmediatamente después de conectar
            server.send(bytes(f"<name>{self.username}", 'utf-8'))

            while connected:
                message = server.recv(BUFFER_SIZE)
                if message:
                    self.signal_message.emit(message.decode("utf-8"))
                else:
                    self.signal_message.emit("<!!disconnected!!>")
                    break
                
        except Exception as e:
            self.signal_message.emit(f"<!!error!!> {str(e)}")
        finally:
            server.close()
            connected = False
        
    def stop(self):
        global connected
        connected = False
        self.wait()

        
class MainWindow(QMainWindow, Ui_MainWindow,Ui_Widget1):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)

        self.ui2=Dialogo()
        self.perfilBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(0))
        self.contactosBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(2))
        self.mensajesBtn.clicked.connect(lambda :self.stackedWidget_2.setCurrentIndex(5))
    
        self.infoBtn.clicked.connect(lambda: self.toggle_menu(self.mainmenu, self.informacion, "Información"))
        self.ajustesBtn.clicked.connect(lambda: self.toggle_menu(self.mainmenu, self.ajustes, "Ajustes"))
        self.csesionBtn.clicked.connect(self.close)
        self.menu_animacion = QPropertyAnimation(self.menu, b"maximumWidth")
        self.menu_animacion.setDuration(300)
        self.menu_animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.menu_max, self.menu_min = 150, 50
        self.funcion = True
        self.menuBtn.clicked.connect(self.manipular_menu)
        self.notificacionBtn.clicked.connect(lambda: self.toggle_menu(self.stackedWidget, self.notificaciones, "Notificaciones", True))
        self.masBtn.clicked.connect(lambda: self.toggle_menu(self.stackedWidget, self.mas, "Más...", True))
        self.reducirBtn.hide()
        self.menucentral.hide()
        self.rightmenu.hide()
        self.reducirBtn.clicked.connect(self.showNormal)
        self.maxBtn.clicked.connect(self.showMaximized)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(10, 10)
        self.arriba.mouseMoveEvent = self.mover_ventana
        self.minBtn.clicked.connect(self.showMinimized)
        self.cerrarBtn.clicked.connect(self.close)
        self.editar.clicked.connect(self.cambiar_foto_perfil)
        self.listo.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        #self.lista_contactos.itemClicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(2))
        self.agregar.clicked.connect(self.agregar_contacto)
        self.enviar_mensajes.clicked.connect(self.send_private_message)
        self.enviar_mensajes_2.clicked.connect(self.mensaje_saliente)
        self.chat_personal.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(3))
        self.lista_contactos.itemClicked.connect(self.chat_privado)
        self.enviar_mensajes_5.clicked.connect(self.send_private_message)
        self.enviar_mensajes_6.clicked.connect(self.send_private_message)
        self.enviar_mensajes_7.clicked.connect(self.send_private_message)
        self.enviar_mensajes_8.clicked.connect(self.send_private_message)
        self.enviar_mensajes_9.clicked.connect(self.send_private_message)
        self.lista_mensajes_recibidos.itemClicked.connect(self.activar_ventana_chat_desde_mensaje)

        self.contact_to_page = {}
        
        self.available_chat_pages = set()
        for i in range(11):  # Supongamos un total de 15 páginas
            page = QWidget()
            self.stackedWidget_2.addWidget(page)
            if i in {4, 6, 7, 8, 9,10}:  # Solo estas páginas son para chats
                self.available_chat_pages.add(i)

    def shake_window(self):
        # Configura cuánto debería "vibrar" la ventana y cuántas veces
        amplitude = 10  # Píxeles de desplazamiento
        duration = 100  # Milisegundos totales para la vibración
        shakes = 6  # Número de movimientos

        original_pos = self.pos()
        offsets = [QPoint(amplitude, 0), QPoint(-amplitude, amplitude), QPoint(0, -amplitude), QPoint(-amplitude, 0)]


        def do_shake(step):
            if step == shakes * len(offsets):
                self.move(original_pos)
                return
            offset = offsets[step % len(offsets)]
            new_pos = original_pos + offset
            self.move(new_pos)
            QTimer.singleShot(int(duration / (shakes * len(offsets))), lambda: do_shake(step + 1))

        do_shake(0)

        
    def chat_privado(self,item):
        contact_name = item.text()
        if contact_name not in self.contact_to_page:
            for i  in self.available_chat_pages:
                if i not in self.contact_to_page.values():
                    self.contact_to_page[contact_name]=i
                    break
        
        if contact_name in self.contact_to_page:
            self.prepare_private_chat_interface(contact_name)
            self.stackedWidget_2.setCurrentIndex(self.contact_to_page[contact_name])

        #self.prepare_private_chat_interface(contact_name)
        #self.stackedWidget_2.setCurrentIndex(4)

    def prepare_private_chat_interface(self, contact_name):
        self.current_chat_user = contact_name  # Almacena el nombre del contacto actual
        #self.chat_label.setText(f"Chat con {contact_name}")  # Suponiendo que hay una etiqueta para mostrar el nombre
        pagina=self.contact_to_page[contact_name]

    def send_private_message(self):
        boton = self.sender()
        parent_widget = boton.parentWidget()
        index = self.stackedWidget_2.indexOf(parent_widget)
        page_widget = self.stackedWidget_2.widget(index)  # Obtener el widget de la página
        nombre_plain = find_plain_text_edit(page_widget) 
        nombre_line_edit = find_line_edit(page_widget)  # Buscar el QPlainTextEdit correcto
        
        if nombre_line_edit:
            #print("QPlainTextEdit encontrado")
            #print(nombre_plain)
            texto_mensaje = nombre_line_edit.text()
            #print(f"Texto obtenido de QLineEdit: {texto_mensaje}")  # Debe obtener el texto de nombre_plain
            print(texto_mensaje)
            if texto_mensaje:
                mensaje_completo = f"<private>:{self.current_chat_user}:{texto_mensaje}"
                server.send(bytes(mensaje_completo, 'utf-8'))  # Asumiendo que 'server' es tu socket conectado
                nombre_line_edit.clear()  # Limpiar el QPlainTextEdit después de enviar el mensaje
                self.update_chat_display(f"Tú: {texto_mensaje}\n", nombre_plain)

    def update_chat_display(self, message, plain):
        # Agrega el mensaje al área de texto de la conversación correcta
        plain.setPlainText(plain.toPlainText() + message)

        
    def update_chat_display(self, message,plain):
        # Agrega el mensaje al área de texto de la conversación
        plain.setPlainText(plain.toPlainText() + message)
        

    
    def trigger_search(self):
        user_text = self.ui2.buscar_usuario.text()
        if user_text:
            self.search_user(user_text)

    def search_user(self, name):
        global server, connected  # Asegúrate de que estas variables estén definidas correctamente
        if connected:
            try:
                server.send(bytes(f"<search>{name}", 'utf-8'))
            except Exception as e:
                QMessageBox.critical(self, "Error", "Failed to send message due to: " + str(e))

    def agregar_contacto(self):
        self.ui2.boton_buscar.clicked.connect(self.trigger_search)  # Conecta la señal aquí
        resp = self.ui2.exec()  # Ejecuta el diálogo
        if resp == 1:
            print("Dialog accepted")

    def process_search_result(self, message):
        #print(message)
        if message.startswith("search_result:"):
            users = message.split("search_result:")[1]
            print(users)     
            if users !='No results\n':
                found_users = users.split(',')
                current_users = [self.lista_contactos.item(i).text() for i in range(self.lista_contactos.count())]
                new_users = [user for user in found_users if user not in current_users]
                self.lista_contactos.addItems(new_users)
            else:
                QMessageBox.information(self, "Busqueda", "Usuario no localizado:((")
 


    def iniciar_sesion(self):
        dialog = QDialog(self)
        self.ui = Ui_Widget1()
        self.ui.setupUi(dialog)
        dialog.setWindowTitle("Iniciar Sesión")
        self.ui.iniciar.clicked.connect(lambda: self.conectar( dialog))
        dialog.exec()

    def conectar(self, dialog):
        server = '3.136.134.23'
        port = 5000
        usuario=self.ui.usuario.text()
        self.coneccion = ThreadSocket(server, int(port),usuario)
        self.coneccion.signal_message.connect(self.mensage_entrante)
        self.coneccion.start()
        dialog.accept()

    def cambiar_foto_perfil(self):
        self.stackedWidget_2.setCurrentIndex(1)
        imagen, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Imagen', '', 'Imágenes (*.png *.xpm *.jpg *.jpeg)')
        if imagen:
            im_leida = cv2.imread(imagen)
            im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
            height, width, channel = im_leida.shape
            bytesPerLine = 3 * width
            qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            self.poner_imagen(pixmap)
            lambda: self.label_8.setPixmap(pixmap)
            lambda: self.label.setPixmap(pixmap)

    def poner_imagen(self, pixmap):
        self.label_8.setPixmap(pixmap)
        self.label.setPixmap(pixmap)
        

    def mensaje_saliente(self):
        str=self.escribir_mensaje_2.text()

        if str!="" and connected:
            server.send(bytes(str,'utf-8'))
            self.escribir_mensaje_2.clear()
            self.mensage_entrante("<Tú> " + str + '\n')

    def agregar_mensaje_a_lista_mensajes(self, mensaje, remitente):
        # Asume que mensaje es el contenido del mensaje y remitente es quien lo envía
        item_text = f"{remitente}: {mensaje}"  # Formato del mensaje en la lista
        item = QListWidgetItem(item_text)
        self.lista_mensajes_recibidos.addItem(item)


    def mensage_entrante(self, mensaje):
        print(mensaje)
        if mensaje.startswith("<privado>"):
            # Suponiendo que el formato del mensaje es "<privado>:nombre_remitente:contenido_mensaje"
            _, remitente, contenido = mensaje.split(':', 2)

            remitente = remitente.strip().removeprefix("De ")
            self.agregar_mensaje_a_lista_mensajes(contenido, remitente)
            if remitente in self.contact_to_page:
                index = self.contact_to_page[remitente]
                pagina_widget = self.stackedWidget_2.widget(index)
                text_edit = find_plain_text_edit(pagina_widget)
                if text_edit:
                    text_edit.setPlainText(text_edit.toPlainText() + remitente + contenido + "\n")
            else:
                print("Remitente no reconocido o chat no iniciado.")
        elif mensaje.startswith("Nuevo Mensaje de\n"):
            # Actualiza la lista de notificaciones con el mensaje
            self.lista_notifiaciones.addItem(mensaje)
        else:
            # Mensajes no privados, manejo normal
            self.mensajes_recibidos_2.setPlainText(self.mensajes_recibidos_2.toPlainText() + mensaje + "\n")
            self.process_search_result(mensaje)

    def activar_ventana_chat_desde_mensaje(self, item):
        mensaje = item.text()
        remitente = mensaje.split(':', 1)[0]  # Extraer el nombre del remitente del mensaje
        if remitente in self.contact_to_page:
            self.stackedWidget_2.setCurrentIndex(self.contact_to_page[remitente])
        else:
            QMessageBox.warning(self, "Contacto no encontrado", f"Primero debe agregar a {remitente} como contacto para iniciar un chat.")
    ''''' 
    def mensage_entrante(self, mensaje):
        if mensaje.startswith("<privado>") :
            self.mensajes_recibidos.setPlainText(self.mensajes_recibidos.toPlainText() + mensaje + "\n")
        elif mensaje.startswith("Nuveo Mensaje de\n"):
            self.lista_notifiaciones.addItem(mensaje)
        else:
            # Mensajes no privados, manejo normal
            self.mensajes_recibidos_2.setPlainText(self.mensajes_recibidos_2.toPlainText() + mensaje + "\n")
            self.process_search_result(mensaje)
    '''
    #def mensage_entrante(self, mensaje):
    #    self.mensajes_recibidos_2.setPlainText(self.mensajes_recibidos_2.toPlainText() + mensaje)
     #   self.process_search_result(mensaje)

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
    def mover_ventana(self, event):
        if not self.isMaximized() and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
            self.click_posicion = event.globalPosition()
            event.accept()
        if event.globalPosition().y() <= 10:
            self.showMaximized()
        else:
            self.showNormal()
        
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - 10, rect.bottom() - 10)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()

    def manipular_menu(self):

        inicio, fin = (self.menu_max, self.menu_min) if self.funcion else (self.menu_min, self.menu_max)
        self.menu_animacion.setStartValue(inicio)
        self.menu_animacion.setEndValue(fin)
        self.menu_animacion.start()
        self.funcion = not self.funcion
    
def find_plain_text_edit(widget):
  
    if isinstance(widget, QPlainTextEdit):
        return widget
    elif hasattr(widget, 'children'):
        for child in widget.children():
            result = find_plain_text_edit(child)
            if result:
                return result
    return None

def find_line_edit(widget):
    """
    Busca recursivamente un QLineEdit dentro de un widget.
    Retorna el primer QLineEdit encontrado o None si no hay ninguno.
    """
    if isinstance(widget, QLineEdit):
        return widget
    elif hasattr(widget, 'children'):
        for child in widget.children():
            result = find_line_edit(child)
            if result:
                return result
    return None

class Dialogo(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    BUFFER_SIZE = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False
    window = MainWindow()
    window.iniciar_sesion()  # Llamar a iniciar sesión antes de mostrar la ventana principal.
    window.show()
    sys.exit(app.exec())