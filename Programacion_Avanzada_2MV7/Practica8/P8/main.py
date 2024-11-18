from Ui_gui import *
import numpy as np
import sys, random,time,cv2
import sys, random,time, pyfirmata,cv2
from PyQt6.uic import loadUi
from PyQt6.QtGui import QKeyEvent,QMouseEvent,QPixmap,QImage,QPainter,QPen, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem,QMessageBox,QDialog,QFileDialog,QWidget,QPlainTextEdit,QLineEdit,QListWidgetItem

from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QThread, Qt, pyqtSignal,QTimer, QPoint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.arriba.mouseMoveEvent = self.mover_ventana
        
        self.menuBtn_2.hide()
        self.tomarBtn.hide()
        self.minBtn.clicked.connect(self.minimizar)
        self.cerrarBtn.clicked.connect(lambda:self.close())
        self.menuBtn.clicked.connect(self.manipular_menu)
        self.menuBtn_2.clicked.connect(self.manipular_menu)
        self.desBTn.clicked.connect(self.desenfoque)
        self.nitidezBtn.clicked.connect(self.nitidez)
        self.aceptaBtn.clicked.connect(self.aceptar)
        self.cancelBtn.clicked.connect(self.cancelar)
        self.idBtn.clicked.connect(self.identificar_color) 
        self.regresarBTn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.opciones))


        
        self.menu_animacion = QPropertyAnimation(self.menu, b"maximumHeight")
        self.menu_animacion.setDuration(300)
        self.menu_animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)

        self.menu_max = 158
        self.menu_min = 100
        self.funcion = True
        
        self.cargarBtn.clicked.connect(self.cargar_imagen)
        self.guardarBTn.clicked.connect(self.guardar_imagen) 
        self.grisBtn.clicked.connect(self.escala_grises)
        self.resBTn.clicked.connect(self.color_original)
        self.derechaBtn.clicked.connect(self.rotar_derecha) 
        self.izquierdaBtn.clicked.connect(self.rotar_izquierda)
        self.negBtn.clicked.connect(self.conversion_negativo) 
        self.espejohBtn.clicked.connect(self.espejo_horizontal)
        self.espejovBtn.clicked.connect(self.espejo_vertical) 
        self.desBTn .clicked.connect(self.desenfoque)
        self.nitidezBtn.clicked.connect(self.nitidez)
        self.contornoBtn.clicked.connect(self.contornos)
        self.cannyBtn.clicked.connect(self.f_canny) 
        #self.cantidad.valueChanged.connect(self.desenfoque_imagen)
        #self.cantidad.valueChanged.connect(self.nitidez_imagen)
        
        self.fotoBtn.clicked.connect(self.toggle_camera)
        self.tomarBtn.clicked.connect(self.tomar_foto)

        self.tomarBtn_f = None
        self.foto_comparar=None
        self.camera_on = False
        self.contornos_activados = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.compararBtn.pressed.connect(self.mostrar_imagen_comparar)
        self.compararBtn.released.connect(self.volver_imagen)

        self.i=None


    def volver_imagen(self):
        self.imagen.setPixmap(self.i)

    def mostrar_imagen_comparar(self):
        if self.foto_comparar:
            self.imagen.setPixmap(self.foto_comparar)
        else:
            QMessageBox.warning(self, 'Advertencia', 'No se ha capturado ninguna imagen para comparar.')
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    
    def mousePressEvent(self, event):
        self.click_posicion = event.globalPosition()
        
    def mover_ventana(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move (self.pos() + event.globalPosition().toPoint() - self.click_posicion.toPoint())
                self.click_posicion = event.globalPosition()
                event.accept()
            
    def minimizar(self):
        self.showMinimized()  
        
    def manipular_menu(self):
        if self.funcion:
            inicio = self.menu_max
            fin = self.menu_min
            self.label_5.hide()
            self.label_13.hide()
            self.label_14.hide()
            self.label_15.hide()
            self.label_16.hide()
            self.label_17.hide()
            self.label_18.hide()
            self.label_19.hide()
            self.label_24.hide()
            self.menuBtn.hide()
            self.menuBtn_2.show()
        else:
            inicio = self.menu_min
            fin = self.menu_max
            self.label_5.show()
            self.label_13.show()
            self.label_14.show()
            self.label_15.show()
            self.label_16.show()
            self.label_17.show()
            self.label_18.show()
            self.label_19.show()
            self.label_24.show()
            self.menuBtn.show()
            self.menuBtn_2.hide()

        self.menu_animacion.setStartValue(inicio)
        self.menu_animacion.setEndValue(fin)
        self.menu_animacion.start()
        self.funcion = not self.funcion
        
    def cargar_imagen(self):
        imagen, _ = QFileDialog.getOpenFileName(self, 'Seleccionar Imagen', '', 'Imágenes (*.png *.xpm *.jpg *.jpeg *.svg)')
        if imagen:
            im_leida = cv2.imread(imagen)
            im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
            height, width, channel = im_leida.shape
            bytesPerLine = 3 * width
            qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)  
            self.imagen.setPixmap(pixmap)
            self.pixmap_original1 = pixmap
            self.foto_comparar=pixmap
    def guardar_imagen(self):
        pixmap = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or pixmap is None:
            QMessageBox.warning(self, 'Advertencia', 'No hay ninguna imagen para guardar.')
            return
        
        archivo, _ = QFileDialog.getSaveFileName(self, 'Guardar Imagen', '', 'Imágenes (*.png *.jpg *.jpeg)')
        if archivo:
            # Convertir el QPixmap a QImage
            qImg = pixmap.toImage()
            
            if not qImg.save(archivo):
                QMessageBox.warning(self, 'Error', 'No se pudo guardar la imagen.')
            else:
                QMessageBox.information(self, 'Información', 'Imagen guardada con éxito.')

            
    def toggle_camera(self):
        #NO SIRVE SI SE DESCOMENTA
        if self.camera_on:
            self.camera_on = False
            self.tomarBtn.hide()
            self.timer.stop()
            self.tomarBtn_f.release()
        else:
            self.camera_on = True
            self.tomarBtn_f = cv2.VideoCapture(0)
            self.tomarBtn.show()
            self.timer.start(30)

    def update_frame(self):
        if self.camera_on and self.tomarBtn_f.isOpened():
            ret, frame = self.tomarBtn_f.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(qImg)
                pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
                self.imagen.setPixmap(pixmap)
    
    def iniciar_camara(self):
        self.camera_on = True
        if not self.tomarBtn_f.isOpened():
            self.tomarBtn_f.open(0)
        QMessageBox.information(self, 'Información', 'La cámara está encendida.')

    def tomar_foto(self):
        if self.camera_on and self.tomarBtn_f.isOpened():
            ret, frame = self.tomarBtn_f.read()
            
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame.shape
                bytesPerLine = 3 * width
                qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(qImg)
                pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
                self.imagen.setPixmap(pixmap)
                self.pixmap_original1 = pixmap
                self.foto_comparar = pixmap
                self.camera_on = False  # Para detener la cámara después de capturar la imagen
                
                self.tomarBtn_f.release()  # Liberar la cámara
                self.tomarBtn.hide()
            else:
                QMessageBox.warning(self, 'Advertencia', 'No se pudo capturar la imagen desde la cámara.')
        else:
            QMessageBox.warning(self, 'Advertencia', 'La cámara no está encendida o no se puede acceder a ella.')

    def cerrar_camara(self):
        if self.tomarBtn_f.isOpened():
            self.tomarBtn_f.release()
            self.camera_on = False
            QMessageBox.information(self, 'Información', 'La cámara está cerrada.')

    def escala_grises(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return
        
        im_leida = self.generar_matriz (imagen)
        im_gris = cv2.cvtColor(im_leida, cv2.COLOR_BGR2GRAY)
        height, width= im_gris.shape
        bytesPerLine = width
        qImg = QImage(im_gris.data, width, height, bytesPerLine, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)  
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
        

    def generar_matriz(self, pixmap):
            qimg = pixmap.toImage()
            temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
            temp_shape += (4,)
            ptr = qimg.bits()
            ptr.setsize(qimg.sizeInBytes())
            arr = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
            arr = arr[:, :, :3]
            return arr
        
    def color_original(self):
        if hasattr(self, 'pixmap_original1'):
            pixmap = self.pixmap_original1.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.imagen.setPixmap(pixmap)
        else:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            
    def rotar_derecha(self):
            imagen = self.imagen.pixmap()
            texto = self.imagen.text()
            if texto == "Imagen" or imagen is None:
                QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
                return

            im_leida = self.generar_matriz(imagen)
            im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
            height, width, _ = im_leida.shape
            center = (width // 2, height // 2)
            angle = -90
            scale = 1.0
            M = cv2.getRotationMatrix2D(center, angle, scale)

            # Aplicar la rotación a la imagen
            rotated = cv2.warpAffine(im_leida, M, (width, height), flags = cv2.INTER_LANCZOS4)

            height, width, channels = rotated.shape
            bytesPerLine = channels * width
            qImg = QImage(rotated.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.imagen.setPixmap(pixmap)
            
    def rotar_izquierda(self):
            imagen = self.imagen.pixmap()
            texto = self.imagen.text()
            if texto == "Imagen" or imagen is None:
                QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
                return

            im_leida = self.generar_matriz(imagen)
            im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
            height, width, _ = im_leida.shape
            center = (width // 2, height // 2)
            angle = 90
            scale = 1.0
            M = cv2.getRotationMatrix2D(center, angle, scale)

            # Aplicar la rotación a la imagen
            rotated = cv2.warpAffine(im_leida, M, (width, height), flags = cv2.INTER_LANCZOS4)

            height, width, channels = rotated.shape
            bytesPerLine = channels * width
            qImg = QImage(rotated.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.imagen.setPixmap(pixmap)

    def desenfoque(self):
        #BORRAR EL OTRO CODIGO Y DESCOMENTAR EN CASO DE HACER CON SLIDER
        '''self.stackedWidget.setCurrentWidget(self.page_2)
        self.label_25.setText(f"Desenfoque") '''
        
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
       
        gaussian_blur_kernel = np.array([[1, 4, 6, 4, 1],
                                        [4, 16, 24, 16, 4],
                                        [6, 24, 36, 24, 6],
                                        [4, 16, 24, 16, 4],
                                        [1, 4, 6, 4, 1]]) / 256
      
        im_leida = cv2.filter2D(im_leida, -1, gaussian_blur_kernel)
            
        height, width, channels = im_leida.shape
        bytesPerLine = channels * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
    def nitidez(self):
        #BORRAR EL OTRO CODIGO Y DESCOMENTAR EN CASO DE HACER CON SLIDER
        '''self.stackedWidget.setCurrentWidget(self.page_2)
        self.label_25.setText(f"Nitidez")'''
        
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)

        unsharp_masking_kernel = np.array([[1, 4, 6, 4, 1],
                                        [4, 16, 24, 16, 4],
                                        [6, 24, -476, 24, 6],
                                        [4, 16, 24, 16, 4],
                                        [1, 4, 6, 4, 1]]) / -256

        im_leida = cv2.filter2D(im_leida, -1, unsharp_masking_kernel)

        height, width, channels = im_leida.shape
        bytesPerLine = channels * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
    def aceptar(self):
        self.stackedWidget.setCurrentWidget(self.opciones)
        
    def cancelar(self):
        self.stackedWidget.setCurrentWidget(self.opciones)
    
    def conversion_negativo(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_negativo = 255 - im_leida  # Conversión a negativo
        im_negativo = cv2.cvtColor(im_negativo, cv2.COLOR_BGR2RGB)  # Convertir de nuevo a RGB
        height, width, channel = im_negativo.shape
        bytesPerLine = 3 * width
        qImg = QImage(im_negativo.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
    def espejo_horizontal(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        eh = cv2.flip(im_leida, 1)  # Espejo horizontal
        eh = cv2.cvtColor(eh, cv2.COLOR_BGR2RGB)  # Convertir de nuevo a RGB
        height, width, channel = eh.shape
        bytesPerLine = 3 * width
        qImg = QImage(eh.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
    def espejo_vertical(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        ev = cv2.flip(im_leida, 0)  # Espejo vertical
        ev = cv2.cvtColor(ev, cv2.COLOR_BGR2RGB)  # Convertir de nuevo a RGB
        height, width, channel = ev.shape
        bytesPerLine = 3 * width
        qImg = QImage(ev.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap
    def identificar_color(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return
        self.stackedWidget.setCurrentWidget(self.id_color)
        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
        height, width, channels = im_leida.shape
        bytesPerLine = channels * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.imagen.setPixmap(pixmap)

        def coordenadas(event):
            if event.button() == Qt.MouseButton.LeftButton:
                x = event.position().x()
                y = event.position().y()
                r, g, b = 0, 0, 0
                if 0 <= x < width and 0 <= y < height:
                    pixel = qImg.pixelColor(int(x), int(y))
                    r, g, b = pixel.red(), pixel.green(), pixel.blue()

                    # Crear una nueva imagen con el punto marcado
                    img_marcada = pixmap.toImage()
                    pintor = QPainter(img_marcada)
                    pintor.setPen(QPen(Qt.GlobalColor.red, 3))
                    pintor.drawPoint(int(x), int(y))
                    pintor.end()

                    pixmap_marcada = QPixmap.fromImage(img_marcada)
                    self.imagen.setPixmap(pixmap_marcada)
                    self.i=pixmap
                self.rgb_2.setText(f"RGB\n{r}, {g}, {b}")
                color = QColor(r, g, b)
                self.color_2.setStyleSheet(f"background-color: {color.name()}")

        self.imagen.mousePressEvent = coordenadas  
        
    def contornos(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(im_leida, cv2.COLOR_RGB2GRAY)
        gauss = cv2.GaussianBlur(im_leida, (15, 15), 0)
        
        fcanny = cv2.Canny(gauss, 50, 150)
        (contornos, _) = cv2.findContours(fcanny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        

        cv2.drawContours(im_leida, contornos, -1, (0, 255, 0), 2) 

        height, width = im_leida.shape[:2]
        bytesPerLine = 3 * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)
        self.i=pixmap



    def f_canny(self):
            imagen = self.imagen.pixmap()
            texto = self.imagen.text()
            if texto == "Imagen" or imagen is None:
                QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
                return

            im_leida = self.generar_matriz(imagen)
            im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2GRAY)
        
            gx = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], dtype=np.float32) 
            
            gy = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]], dtype=np.float32)
             
            grad_x = cv2.filter2D(im_leida, cv2.CV_32F, gx)
            grad_y = cv2.filter2D(im_leida, cv2.CV_32F, gy)
            magnitud = cv2.magnitude(grad_x, grad_y)
            # Normaliza la magnitud para convertirla a una imagen de 8 bits
            magnitud = cv2.normalize(magnitud, None, 0, 255, cv2.NORM_MINMAX)
            magnitud = magnitud.astype(np.uint8)
                
        
            height, width= magnitud.shape
            bytesPerLine = width
            qImg = QImage(magnitud.data, width, height, bytesPerLine, QImage.Format.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qImg)
            pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)  
            self.imagen.setPixmap(pixmap)

            self.i=pixmap
    #INTENTO DE DESENFOQUE CON SLIDER 
    '''def desenfoque_imagen(self,value):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
        cantidad = value
        if cantidad == 0:
            cantidad = 1  # Establecer un valor pequeño si el slider es 0
        else:
            cantidad = cantidad / 10.0
        gaussian_blur_kernel = np.array([[1, 4, 6, 4, 1],
                                        [4, 16, 24, 16, 4],
                                        [6, 24, 36, 24, 6],
                                        [4, 16, 24, 16, 4],
                                        [1, 4, 6, 4, 1]]) / 256

        for _ in range(int(cantidad)):
            im_leida = cv2.filter2D(im_leida, -1, gaussian_blur_kernel)
            
        height, width, channels = im_leida.shape
        bytesPerLine = channels * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)'''
#INTENTO DE NITIDEZ CON SLIDER
    '''def nitidez_imagen(self, value):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
        
        cantidad = value
        if cantidad == 0:
            cantidad = 1  # Establecer un valor pequeño si el slider es 0
        else:
            cantidad = cantidad / 10.0

        unsharp_masking_kernel = np.array([[1, 4, 6, 4, 1],
                                        [4, 16, 24, 16, 4],
                                        [6, 24, -476, 24, 6],
                                        [4, 16, 24, 16, 4],
                                        [1, 4, 6, 4, 1]]) / -256

        for _ in range(int(cantidad)):
            im_leida = cv2.filter2D(im_leida, -1, unsharp_masking_kernel)

        height, width, channels = im_leida.shape
        bytesPerLine = channels * width
        qImg = QImage(im_leida.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        pixmap = pixmap.scaled(self.imagen.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.imagen.setPixmap(pixmap)'''


    '''def aceptar(self):
        if not hasattr(self, 'imagen_original'):
            self.imagen_original = self.imagen.pixmap()
        if self.label_25.text() == "Desenfoque":
            self.desenfoque_imagen()
        elif self.label_25.text() == "Nitidez":
            self.nitidez_imagen()
        self.stackedWidget.setCurrentWidget(self.opciones)
        
    def cancelar(self):
        if hasattr(self, 'imagen_original'):
            self.imagen.setPixmap(self.imagen_original)
        self.stackedWidget.setCurrentWidget(self.opciones)
            
    def contorno(self):
        imagen = self.imagen.pixmap()
        texto = self.imagen.text()
        if texto == "Imagen" or imagen is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar una imagen primero.')
            return

        im_leida = self.generar_matriz(imagen)
        im_leida = cv2.cvtColor(im_leida, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(im_leida, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(im_leida, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if not hasattr(self, 'contornos_activados') or not self.contornos_activados:
            im_contornos = im_leida.copy()
            cv2.drawContours(im_contornos, contours, -1, (255, 166, 0), 5)
            self.contornos_activados = True
            self.im_original = im_leida
        else:
            im_contornos = self.im_original.copy()
            self.contornos_activados = False
            
        height, width, channels = im_contornos.shape
        bytesPerLine = channels * width
        qImg = QImage(im_contornos.data, width, height, bytesPerLine, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)
        self.imagen.setPixmap(pixmap)
        
    def comparar_bordes(self):
        imagen2 = self.imagen2.pixmap()
        texto2 = self.imagen2.text()
        imagen3 = self.imagen3.pixmap()
        texto3 = self.imagen3.text()
    
        if texto2 == "Imagen 1" or imagen2 is None or texto3 == "Imagen 2" or imagen3 is None:
            QMessageBox.warning(self, 'Advertencia', 'Es necesario cargar ambas imágenes primero.')
            return

        im_leida2 = self.generar_matriz(imagen2)
        im_leida3 = self.generar_matriz(imagen3)
        contorno2 = self.obtener_contorno(im_leida2)
        contorno3 = self.obtener_contorno(im_leida3)

        # Comparar los contornos
        if contorno2 is None or contorno3 is None:
            self.res.setText("Las imágenes no tienen contornos definidos")
        elif len(contorno2) != len(contorno3):
            self.res.setText("Las imágenes son distintas")
        else:
            contorno2_aplanado = contorno2.reshape(1, -1)
            contorno3_aplanado = contorno3.reshape(1, -1)
            diff = cv2.subtract(contorno2_aplanado, contorno3_aplanado)
            if cv2.countNonZero(diff) == 0:
                self.res.setText("Las imágenes son iguales")
            else:
                self.res.setText("Las imágenes son distintas")

    def obtener_contorno(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            return max(contours, key=cv2.contourArea)
        return None'''
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())