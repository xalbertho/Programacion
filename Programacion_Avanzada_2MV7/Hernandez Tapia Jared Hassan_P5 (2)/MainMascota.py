import sys
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import QtWidgets, QtCore
from PyQt6.uic import loadUi


class WelcomePet(QtWidgets.QMainWindow):

    def __init__(self,app):
        super().__init__()
        loadUi("menu.ui", self)
        
        self.app=app
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        self.arriba.mouseMoveEvent = self.mover_ventana
        self.btnMen.clicked.connect(self.abrir_menu)
        self.btnComp.hide()
        
        self.btnMin.clicked.connect(self.minimizar)
        self.btnComp.clicked.connect(self.comprimir)
        self.btnExpand.clicked.connect(self.expandir)
        self.btnCerrar.clicked.connect(lambda:self.close())
        
        self.bt_inv.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.invent))
        self.bt_admin.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.admin))
        self.bt_elim.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.eliminar))
        self.bt_vend.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.vender))
        self.bt_report.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.reporte))
        
        self.actualizar_inv.clicked.connect(self.actualizar_en_inventario)
        self.buscar_elim.clicked.connect(self.buscar_en_eliminar)
        self.eliminar_eliminar.clicked.connect(self.eliminar_en_eliminar)
        self.actuElim.clicked.connect(self.actualizar_en_eliminar)
        self.buscar_vend.clicked.connect(self.buscar_en_vender)
        self.vender_vend.clicked.connect(self.vender_en_vender)
        self.imprimir_inv.clicked.connect(self.reporte_inventario)
        self.imprimir_vent.clicked.connect(self.reporte_ventas)
        self.actualizar_admin.clicked.connect(self.actualizar_en_administrar)

        with open('inventario.txt', 'r') as archivo:
            animal = [line.strip().split(',') for line in archivo]
        
        self.tablaInventario.setRowCount(len(animal))
        for linea, linea_data in enumerate(animal):
            for columna, valor in enumerate(linea_data):
                item = QTableWidgetItem(valor)
                self.tablaInventario.setItem(linea, columna, item)
        for i in range(self.tablaInventario.columnCount()):
            self.tablaInventario.resizeColumnToContents(i)
                    
    def minimizar(self):
        self.showMinimized()

    def comprimir(self):
        self.showNormal()
        self.btnComp.hide()
        self.btnExpand.show()
        
    def expandir(self):
        self.showMaximized()
        self.btnExpand.hide()
        self.btnComp.show()
    
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
        if event.globalPosition().y() <= 10:
            self.showMaximized()
            self.btnExpand.hide()
            self.btnComp.show()
        else:
            self.showNormal()
            self.btnComp.hide()
            self.btnExpand.show()
            
    def abrir_menu(self):
        if True:
            width = self.frame_opciones.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_opciones, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
            self.animacion.start()
            
    def actualizar_en_inventario(self):
        with open('inventario.txt', 'r') as archivo:
            animal = [line.strip().split(',') for line in archivo]
        
        self.tablaInventario.setRowCount(len(animal))
        for linea, linea_data in enumerate(animal):
            for columna, valor in enumerate(linea_data):
                item = QTableWidgetItem(valor)
                self.tablaInventario.setItem(linea, columna, item)
        for i in range(self.tablaInventario.columnCount()):
            self.tablaInventario.resizeColumnToContents(i)
            
    def actualizar_en_eliminar(self):
        with open('inventario.txt', 'r') as archivo:
            animal = [line.strip().split(',') for line in archivo]
        
        self.tablaEliminar.setRowCount(len(animal))
        for linea, linea_data in enumerate(animal):
            for columna, valor in enumerate(linea_data):
                item = QTableWidgetItem(valor)
                self.tablaEliminar.setItem(linea, columna, item)
        for i in range(self.tablaEliminar.columnCount()):
            self.tablaEliminar.resizeColumnToContents(i)
        
    def actualizar_en_administrar(self): 
        if self.mascota_admin.text().upper() == "DOMESTICA" or "DOMESTICO": 
            factor_tp = f"TERNURA:{self.factor_admin.text()}"
        else:
            factor_tp = f"PELIGRO:{self.factor_admin.text()}"
        
        linea_nueva = f"{self.mascota_admin.text().upper()}, {self.tipo_admin.text().upper()}, {self.nombre_admin.text().upper()}, {self.edad_admin.text()}, {factor_tp}, EN VENTA" 

        with open("inventario.txt", "a") as archivo:
            archivo.write(linea_nueva + "\n")
        
        self.mascota_admin.clear()
        self.tipo_admin.clear()
        self.nombre_admin.clear()
        self.edad_admin.clear()
        self.factor_admin.clear()
    
    def buscar_en_eliminar(self):
        encontrado = False #SE PONE UNA BANDERO PQ SINO NO SIRVEEE
        with open("inventario.txt", "r") as archivo:
            lineas = archivo.readlines()
            
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[2].strip().upper() == self.nombre_eliminar.text().upper():
                self.mostrar.setText("Animal Seleccionado")
                encontrado = True
                
                self.tablaEliminar.setRowCount(0) 
                fila=0 #AGREGAMOS SOLO UNA FILA
                self.tablaEliminar.insertRow(0)
                
                
                for columna, valor in enumerate(datos):
                    item = QTableWidgetItem(valor)
                    self.tablaEliminar.setItem(fila, columna, item)
                for i in range(self.tablaEliminar.columnCount()):
                    self.tablaEliminar.resizeColumnToContents(i)
                break
            
        if not encontrado:
            self.mostrar.setText("Animal Inexistente")
            self.tablaEliminar.setRowCount(0)
            
    def eliminar_en_eliminar (self):
        encontrado = False #SE PONE UNA BANDERO PQ SINO NO SIRVEEE
        with open("inventario.txt", "r") as archivo:
            lineas = archivo.readlines()
            
        with open("inventario.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[2].strip().upper() == self.nombre_eliminar.text().strip().upper():
                    encontrado = True
                    continue  
                archivo.write(linea)
                
        if encontrado:
            self.mostrar.setText("Animal Eliminado")
        else:
            self.mostrar.setText("Animal Inexistente")
            
    def buscar_en_vender(self):
        encontrado = False 
        with open("inventario.txt", "r") as archivo:
            lineas = archivo.readlines()
            
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[2].strip().upper() == self.buscador_vend.text().upper():
                self.mostrar_v.setText("Animal Seleccionado")
                encontrado = True
                
                self.mascota_vend.setText(datos[0])
                self.tipo_vend.setText(datos[1])
                self.nombre_vend.setText(datos[2])
                self.edad_vend.setText(datos[3])
                self.factor_vend.setText(datos[4])
                break
            
        if not encontrado:
            self.mascota_vend.clear()
            self.tipo_vend.clear()
            self.nombre_vend.clear()
            self.edad_vend.clear()
            self.factor_vend.clear()
            self.mostrar_v.setText("Animal Inexistente")
            
    def vender_en_vender(self):
        encontrado = False 
        with open("inventario.txt", "r") as archivo:
            lineas = archivo.readlines()
            
        with open("inventario.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[2].strip().upper() == self.buscador_vend.text().strip().upper():
                    encontrado = True
                    continue 
                archivo.write(linea)
                
        if encontrado:
            if self.mascota_vend.text().upper() == "DOMESTICA" or "DOMESTICO": 
                factor_tpv = f"TERNURA:{self.factor_vend.text()}"
            else:
                factor_tpv = f"PELIGRO:{self.factor_vend.text()}"
            linea_nueva = f"{self.mascota_vend.text().upper()}, {self.tipo_vend.text().upper()}, {self.nombre_vend.text().upper()}, {self.edad_vend.text()}, {factor_tpv}, VENDIDO" 

            with open("ventas.txt", "a") as archivo:
                archivo.write(linea_nueva + "\n")
            
            self.mascota_vend.clear()
            self.tipo_vend.clear()
            self.nombre_vend.clear()
            self.edad_vend.clear()
            self.factor_vend.clear()
            self.mostrar_v.setText("Animal Vendido")
        else:
            self.mascota_vend.clear()
            self.tipo_vend.clear()
            self.nombre_vend.clear()
            self.edad_vend.clear()
            self.factor_vend.clear()
            self.mostrar_v.setText("Animal Inexistente")
            
    def reporte_inventario(self):
        with open("inventario.txt", "r") as archivo:
            contenido = archivo.read()
            self.cuadro_inv.setText(contenido)
            
    def reporte_inventario(self):
        with open("inventario.txt", "r") as archivo:
            contenido = archivo.readlines()
            #INTENTO DE ENUMERAR PERO NO SIRVE
            lista_numerada = [f" {i+1}. {linea}"for i, linea in enumerate(contenido)]
            lista_numerada_texto = "\n".join(lista_numerada) 
            self.cuadro_inv.setText(lista_numerada_texto)
        
    def reporte_ventas(self):
        with open("ventas.txt", "r") as archivo:
            contenido = archivo.readlines()
            lista_numerada = [f" {i+1}. {linea}"for i, linea in enumerate(contenido)]
            lista_numerada_texto = "\n".join(lista_numerada) 
            self.cuadro_vent.setText(lista_numerada_texto)
