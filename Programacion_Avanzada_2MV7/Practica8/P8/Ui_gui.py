# Form implementation generated from reading ui file 'e:\Programacion\Programacion_Avanzada_2MV7\Practica8\P8\gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        MainWindow.setMaximumSize(QtCore.QSize(800, 550))
        MainWindow.setStyleSheet("*{\n"
"    font: 11pt \"Tempus Sans ITC\";\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(46, 46, 46);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-radius:15px;\n"
"    background-color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"#principal QLabel{\n"
"    border-radius:15px;\n"
"    background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 550))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 550))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(800, 550))
        self.widget.setMaximumSize(QtCore.QSize(800, 550))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(9, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arriba = QtWidgets.QWidget(parent=self.widget)
        self.arriba.setObjectName("arriba")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.arriba)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(parent=self.arriba)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.fotoBtn = QtWidgets.QPushButton(parent=self.frame)
        self.fotoBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.fotoBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.fotoBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/add_a_photo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fotoBtn.setIcon(icon)
        self.fotoBtn.setIconSize(QtCore.QSize(20, 20))
        self.fotoBtn.setObjectName("fotoBtn")
        self.verticalLayout_24.addWidget(self.fotoBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_23 = QtWidgets.QLabel(parent=self.frame)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_24.addWidget(self.label_23, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_24)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cargarBtn = QtWidgets.QPushButton(parent=self.frame)
        self.cargarBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.cargarBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.cargarBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/add_photo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cargarBtn.setIcon(icon1)
        self.cargarBtn.setIconSize(QtCore.QSize(20, 20))
        self.cargarBtn.setObjectName("cargarBtn")
        self.verticalLayout_4.addWidget(self.cargarBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.resBTn = QtWidgets.QPushButton(parent=self.frame)
        self.resBTn.setMinimumSize(QtCore.QSize(30, 30))
        self.resBTn.setMaximumSize(QtCore.QSize(30, 30))
        self.resBTn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/restart_alt.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.resBTn.setIcon(icon2)
        self.resBTn.setIconSize(QtCore.QSize(20, 20))
        self.resBTn.setObjectName("resBTn")
        self.verticalLayout_23.addWidget(self.resBTn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_23.addWidget(self.label_4, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_23)
        self.horizontalLayout_5.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(507, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(parent=self.arriba)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minBtn = QtWidgets.QPushButton(parent=self.frame_2)
        self.minBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.minBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.minBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/remove.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minBtn.setIcon(icon3)
        self.minBtn.setIconSize(QtCore.QSize(20, 20))
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_3.addWidget(self.minBtn)
        self.cerrarBtn = QtWidgets.QPushButton(parent=self.frame_2)
        self.cerrarBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.cerrarBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.cerrarBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cerrarBtn.setIcon(icon4)
        self.cerrarBtn.setIconSize(QtCore.QSize(20, 20))
        self.cerrarBtn.setObjectName("cerrarBtn")
        self.horizontalLayout_3.addWidget(self.cerrarBtn)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.arriba)
        self.principal = QtWidgets.QWidget(parent=self.widget)
        self.principal.setObjectName("principal")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.principal)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem1 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_21.addItem(spacerItem1)
        self.compararBtn = QtWidgets.QPushButton(parent=self.principal)
        self.compararBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.compararBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.compararBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/compare.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.compararBtn.setIcon(icon5)
        self.compararBtn.setIconSize(QtCore.QSize(20, 20))
        self.compararBtn.setObjectName("compararBtn")
        self.verticalLayout_21.addWidget(self.compararBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_21 = QtWidgets.QLabel(parent=self.principal)
        self.label_21.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_21.addWidget(self.label_21, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout_21)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.imagen = QtWidgets.QLabel(parent=self.principal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagen.sizePolicy().hasHeightForWidth())
        self.imagen.setSizePolicy(sizePolicy)
        self.imagen.setMinimumSize(QtCore.QSize(350, 300))
        self.imagen.setMaximumSize(QtCore.QSize(350, 300))
        self.imagen.setStyleSheet("color: tranparent;")
        self.imagen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imagen.setObjectName("imagen")
        self.horizontalLayout.addWidget(self.imagen)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        spacerItem4 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_20.addItem(spacerItem4)
        self.cannyBtn = QtWidgets.QPushButton(parent=self.principal)
        self.cannyBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.cannyBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.cannyBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/spa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cannyBtn.setIcon(icon6)
        self.cannyBtn.setIconSize(QtCore.QSize(20, 20))
        self.cannyBtn.setObjectName("cannyBtn")
        self.verticalLayout_20.addWidget(self.cannyBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(parent=self.principal)
        self.label_22.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_20.addWidget(self.label_22)
        self.contornoBtn = QtWidgets.QPushButton(parent=self.principal)
        self.contornoBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.contornoBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.contornoBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/filter_vintage.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.contornoBtn.setIcon(icon7)
        self.contornoBtn.setIconSize(QtCore.QSize(20, 20))
        self.contornoBtn.setObjectName("contornoBtn")
        self.verticalLayout_20.addWidget(self.contornoBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_20 = QtWidgets.QLabel(parent=self.principal)
        self.label_20.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_20.addWidget(self.label_20, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout.addLayout(self.verticalLayout_20)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.tomarBtn = QtWidgets.QPushButton(parent=self.principal)
        self.tomarBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.tomarBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.tomarBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/radio_button.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tomarBtn.setIcon(icon8)
        self.tomarBtn.setIconSize(QtCore.QSize(20, 20))
        self.tomarBtn.setObjectName("tomarBtn")
        self.horizontalLayout_10.addWidget(self.tomarBtn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addWidget(self.principal)
        self.menu = QtWidgets.QWidget(parent=self.widget)
        self.menu.setObjectName("menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_3.setContentsMargins(10, 0, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menuBtn = QtWidgets.QPushButton(parent=self.menu)
        self.menuBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.menuBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.menuBtn.setStyleSheet("background-color: transparent;")
        self.menuBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/stat_minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon9)
        self.menuBtn.setIconSize(QtCore.QSize(20, 20))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_9.addWidget(self.menuBtn)
        self.menuBtn_2 = QtWidgets.QPushButton(parent=self.menu)
        self.menuBtn_2.setMinimumSize(QtCore.QSize(30, 30))
        self.menuBtn_2.setMaximumSize(QtCore.QSize(30, 30))
        self.menuBtn_2.setStyleSheet("background-color: transparent;")
        self.menuBtn_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/keyboard_control.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn_2.setIcon(icon10)
        self.menuBtn_2.setIconSize(QtCore.QSize(20, 20))
        self.menuBtn_2.setObjectName("menuBtn_2")
        self.horizontalLayout_9.addWidget(self.menuBtn_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.menu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.opciones = QtWidgets.QWidget()
        self.opciones.setObjectName("opciones")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.opciones)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.grisBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.grisBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.grisBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.grisBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/escala_grises.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.grisBtn.setIcon(icon11)
        self.grisBtn.setIconSize(QtCore.QSize(20, 20))
        self.grisBtn.setObjectName("grisBtn")
        self.verticalLayout_5.addWidget(self.grisBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(parent=self.opciones)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.negBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.negBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.negBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.negBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/negativos.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.negBtn.setIcon(icon12)
        self.negBtn.setIconSize(QtCore.QSize(20, 20))
        self.negBtn.setObjectName("negBtn")
        self.verticalLayout_13.addWidget(self.negBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(parent=self.opciones)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_13.addWidget(self.label_13, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.izquierdaBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.izquierdaBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.izquierdaBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.izquierdaBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/rotar_izquierda.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.izquierdaBtn.setIcon(icon13)
        self.izquierdaBtn.setIconSize(QtCore.QSize(20, 20))
        self.izquierdaBtn.setObjectName("izquierdaBtn")
        self.verticalLayout_14.addWidget(self.izquierdaBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_14 = QtWidgets.QLabel(parent=self.opciones)
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_14.addWidget(self.label_14, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.derechaBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.derechaBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.derechaBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.derechaBtn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/rotar_derecha.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.derechaBtn.setIcon(icon14)
        self.derechaBtn.setIconSize(QtCore.QSize(20, 20))
        self.derechaBtn.setObjectName("derechaBtn")
        self.verticalLayout_15.addWidget(self.derechaBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(parent=self.opciones)
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_15.addWidget(self.label_15, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.espejovBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.espejovBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.espejovBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.espejovBtn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/espejo_vertical.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.espejovBtn.setIcon(icon15)
        self.espejovBtn.setIconSize(QtCore.QSize(20, 20))
        self.espejovBtn.setObjectName("espejovBtn")
        self.verticalLayout_16.addWidget(self.espejovBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(parent=self.opciones)
        self.label_16.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_16.addWidget(self.label_16, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.espejohBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.espejohBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.espejohBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.espejohBtn.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/espejo_horizontal.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.espejohBtn.setIcon(icon16)
        self.espejohBtn.setIconSize(QtCore.QSize(20, 20))
        self.espejohBtn.setObjectName("espejohBtn")
        self.verticalLayout_17.addWidget(self.espejohBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_17 = QtWidgets.QLabel(parent=self.opciones)
        self.label_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_17.addWidget(self.label_17, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.desBTn = QtWidgets.QPushButton(parent=self.opciones)
        self.desBTn.setMinimumSize(QtCore.QSize(30, 30))
        self.desBTn.setMaximumSize(QtCore.QSize(30, 30))
        self.desBTn.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/borroso.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.desBTn.setIcon(icon17)
        self.desBTn.setIconSize(QtCore.QSize(20, 20))
        self.desBTn.setObjectName("desBTn")
        self.verticalLayout_18.addWidget(self.desBTn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_18 = QtWidgets.QLabel(parent=self.opciones)
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.nitidezBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.nitidezBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.nitidezBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.nitidezBtn.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/nitidez.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.nitidezBtn.setIcon(icon18)
        self.nitidezBtn.setIconSize(QtCore.QSize(20, 20))
        self.nitidezBtn.setObjectName("nitidezBtn")
        self.verticalLayout_19.addWidget(self.nitidezBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(parent=self.opciones)
        self.label_19.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_19.addWidget(self.label_19)
        self.horizontalLayout_6.addLayout(self.verticalLayout_19)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.idBtn = QtWidgets.QPushButton(parent=self.opciones)
        self.idBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.idBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.idBtn.setText("")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/colorize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.idBtn.setIcon(icon19)
        self.idBtn.setIconSize(QtCore.QSize(20, 20))
        self.idBtn.setObjectName("idBtn")
        self.verticalLayout_28.addWidget(self.idBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_27 = QtWidgets.QLabel(parent=self.opciones)
        self.label_27.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_28.addWidget(self.label_27)
        self.horizontalLayout_6.addLayout(self.verticalLayout_28)
        spacerItem9 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setContentsMargins(-1, -1, 9, -1)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.guardarBTn = QtWidgets.QPushButton(parent=self.opciones)
        self.guardarBTn.setMinimumSize(QtCore.QSize(30, 30))
        self.guardarBTn.setMaximumSize(QtCore.QSize(30, 30))
        self.guardarBTn.setText("")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.guardarBTn.setIcon(icon20)
        self.guardarBTn.setIconSize(QtCore.QSize(20, 20))
        self.guardarBTn.setObjectName("guardarBTn")
        self.verticalLayout_25.addWidget(self.guardarBTn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_24 = QtWidgets.QLabel(parent=self.opciones)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_25.addWidget(self.label_24, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_6.addLayout(self.verticalLayout_25)
        self.stackedWidget.addWidget(self.opciones)
        self.id_color = QtWidgets.QWidget()
        self.id_color.setObjectName("id_color")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.id_color)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem10 = QtWidgets.QSpacerItem(271, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.color_2 = QtWidgets.QLabel(parent=self.id_color)
        self.color_2.setMinimumSize(QtCore.QSize(40, 40))
        self.color_2.setMaximumSize(QtCore.QSize(40, 40))
        self.color_2.setStyleSheet("border-radius:10px;\n"
"border: 1px solid rgba(255, 255, 255, 150);")
        self.color_2.setText("")
        self.color_2.setObjectName("color_2")
        self.horizontalLayout_12.addWidget(self.color_2)
        self.rgb_2 = QtWidgets.QLabel(parent=self.id_color)
        self.rgb_2.setMinimumSize(QtCore.QSize(100, 40))
        self.rgb_2.setMaximumSize(QtCore.QSize(100, 40))
        self.rgb_2.setStyleSheet("border-radius:10px;\n"
"border: 1px solid rgba(255, 255, 255, 150);")
        self.rgb_2.setText("")
        self.rgb_2.setObjectName("rgb_2")
        self.horizontalLayout_12.addWidget(self.rgb_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)
        spacerItem11 = QtWidgets.QSpacerItem(271, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
        self.regresarBTn = QtWidgets.QPushButton(parent=self.id_color)
        self.regresarBTn.setMinimumSize(QtCore.QSize(30, 30))
        self.regresarBTn.setMaximumSize(QtCore.QSize(30, 30))
        self.regresarBTn.setText("")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.regresarBTn.setIcon(icon21)
        self.regresarBTn.setIconSize(QtCore.QSize(20, 20))
        self.regresarBTn.setObjectName("regresarBTn")
        self.horizontalLayout_13.addWidget(self.regresarBTn)
        self.stackedWidget.addWidget(self.id_color)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_25 = QtWidgets.QLabel(parent=self.page_2)
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.verticalLayout_26.addWidget(self.label_25)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.cantidad = QtWidgets.QSlider(parent=self.page_2)
        self.cantidad.setStyleSheet("QSlider::groove:horizontal {\n"
"    background: rgba(255, 255, 255, 180);\n"
"    margin: 7px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgba(180, 226, 255, 200);\n"
"    width: 15px;\n"
"    margin: -5px 0; \n"
"    border-radius: 3px;\n"
"}")
        self.cantidad.setMinimum(0)
        self.cantidad.setMaximum(100)
        self.cantidad.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.cantidad.setObjectName("cantidad")
        self.horizontalLayout_8.addWidget(self.cantidad)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.verticalLayout_26.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.aceptaBtn = QtWidgets.QPushButton(parent=self.page_2)
        self.aceptaBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.aceptaBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.aceptaBtn.setText("")
        self.aceptaBtn.setIcon(icon21)
        self.aceptaBtn.setIconSize(QtCore.QSize(20, 20))
        self.aceptaBtn.setObjectName("aceptaBtn")
        self.horizontalLayout_7.addWidget(self.aceptaBtn)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.cancelBtn = QtWidgets.QPushButton(parent=self.page_2)
        self.cancelBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.cancelBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.cancelBtn.setText("")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\iconos/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cancelBtn.setIcon(icon22)
        self.cancelBtn.setIconSize(QtCore.QSize(20, 20))
        self.cancelBtn.setObjectName("cancelBtn")
        self.horizontalLayout_7.addWidget(self.cancelBtn)
        self.verticalLayout_26.addLayout(self.horizontalLayout_7)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.menu)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 550))
        self.label.setMinimumSize(QtCore.QSize(800, 550))
        self.label.setMaximumSize(QtCore.QSize(800, 550))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Practica8\\P8\\fondos.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_23.setText(_translate("MainWindow", "Foto"))
        self.label_3.setText(_translate("MainWindow", "Subir"))
        self.label_4.setText(_translate("MainWindow", "Reestablecer"))
        self.label_21.setText(_translate("MainWindow", "Comparar"))
        self.imagen.setText(_translate("MainWindow", "Imagen"))
        self.label_22.setText(_translate("MainWindow", "Canny"))
        self.label_20.setText(_translate("MainWindow", "Contorno"))
        self.label_5.setText(_translate("MainWindow", "Escala de\n"
"grises"))
        self.label_13.setText(_translate("MainWindow", "Conversión a\n"
"negativo"))
        self.label_14.setText(_translate("MainWindow", "Rotar a la\n"
"izquierda"))
        self.label_15.setText(_translate("MainWindow", "Rotar a la\n"
"derecha"))
        self.label_16.setText(_translate("MainWindow", "Espejo\n"
"vertical"))
        self.label_17.setText(_translate("MainWindow", "Espejo\n"
"horizontal"))
        self.label_18.setText(_translate("MainWindow", "Desenfoque"))
        self.label_19.setText(_translate("MainWindow", "Nitidez"))
        self.label_27.setText(_translate("MainWindow", "Color"))
        self.label_24.setText(_translate("MainWindow", "Guardar"))