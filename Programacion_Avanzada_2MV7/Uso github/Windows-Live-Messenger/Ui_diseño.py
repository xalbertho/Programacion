# Form implementation generated from reading ui file 'e:\Programacion\Programacion_Avanzada_2MV7\Uso github\Windows-Live-Messenger\diseño.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 418)
        MainWindow.setStyleSheet("*{\n"
"    font: 11pt \"Tempus Sans ITC\";\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#submenu{\n"
"    background-color: #16191d;\n"
"}\n"
"\n"
"#submenu QPushButton{\n"
"text-align: left;\n"
"padding: 5px 10px;\n"
"border-radius:10px;\n"
"font: 11pt \"Tempus Sans ITC\";\n"
"color: rgb(255,255,255 ); \n"
"}\n"
"\n"
"#submenu QPushButton:hover{\n"
"text-align: left;\n"
"padding: 5px 10px;\n"
"border-radius:10px;\n"
"font: 11pt \"Tempus Sans ITC\";\n"
"color:rbg(255,255,255);\n"
"background-color: rgb(23,139,216);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#submenucentral, #rightsubmenu{\n"
"    background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4, #frame_8{\n"
"    background-color: #16191d;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#arriba{\n"
"    background-color: #2c313c;\n"
"}\n"
"\n"
"#arriba QPushButton{\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"#arriba QPushButton:hover{\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0852273 rgba(176, 235, 255, 167), stop:0.1 rgba(255, 255, 255, 255), stop:0.204545 rgba(151, 242, 255, 92), stop:0.426136 rgba(85, 170, 255, 255), stop:0.454545 rgba(125, 222, 255, 51), stop:0.596591 rgba(0, 158, 226, 228), stop:0.738636 rgba(180, 233, 255, 84), stop:0.818182 rgba(0, 85, 138, 205), stop:0.982955 rgba(255, 255, 255, 0))\n"
"}\n"
"\n"
"arriba QFrame{\n"
"    background-color: rgb(138, 138, 138,180);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu = QtWidgets.QWidget(parent=self.centralwidget)
        self.menu.setObjectName("menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.submenu = QtWidgets.QWidget(parent=self.menu)
        self.submenu.setObjectName("submenu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.submenu)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.submenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(parent=self.frame)
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/align-justify.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(24, 24))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_2 = QtWidgets.QFrame(parent=self.submenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.perfilBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.perfilBtn.setIcon(icon1)
        self.perfilBtn.setIconSize(QtCore.QSize(24, 24))
        self.perfilBtn.setObjectName("perfilBtn")
        self.verticalLayout_3.addWidget(self.perfilBtn)
        self.contactosBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/grid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.contactosBtn.setIcon(icon2)
        self.contactosBtn.setIconSize(QtCore.QSize(24, 24))
        self.contactosBtn.setObjectName("contactosBtn")
        self.verticalLayout_3.addWidget(self.contactosBtn)
        self.mensajesBtn = QtWidgets.QPushButton(parent=self.frame_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/message-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.mensajesBtn.setIcon(icon3)
        self.mensajesBtn.setIconSize(QtCore.QSize(24, 24))
        self.mensajesBtn.setObjectName("mensajesBtn")
        self.verticalLayout_3.addWidget(self.mensajesBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(parent=self.submenu)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ajustesBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ajustesBtn.setIcon(icon4)
        self.ajustesBtn.setIconSize(QtCore.QSize(24, 24))
        self.ajustesBtn.setObjectName("ajustesBtn")
        self.verticalLayout_4.addWidget(self.ajustesBtn)
        self.infoBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/info.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(24, 24))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.csesionBtn = QtWidgets.QPushButton(parent=self.frame_3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.csesionBtn.setIcon(icon6)
        self.csesionBtn.setIconSize(QtCore.QSize(24, 24))
        self.csesionBtn.setObjectName("csesionBtn")
        self.verticalLayout_4.addWidget(self.csesionBtn)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(self.submenu, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.menu)
        self.menucentral = QtWidgets.QWidget(parent=self.centralwidget)
        self.menucentral.setMinimumSize(QtCore.QSize(0, 0))
        self.menucentral.setObjectName("menucentral")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menucentral)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.submenucentral = QtWidgets.QWidget(parent=self.menucentral)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submenucentral.sizePolicy().hasHeightForWidth())
        self.submenucentral.setSizePolicy(sizePolicy)
        self.submenucentral.setMinimumSize(QtCore.QSize(200, 0))
        self.submenucentral.setObjectName("submenucentral")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.submenucentral)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.submenucentral)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuinferior = QtWidgets.QLabel(parent=self.frame_4)
        self.menuinferior.setText("")
        self.menuinferior.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.menuinferior.setObjectName("menuinferior")
        self.horizontalLayout_3.addWidget(self.menuinferior)
        self.cerrarBtn1 = QtWidgets.QPushButton(parent=self.frame_4)
        self.cerrarBtn1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/x-circle.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cerrarBtn1.setIcon(icon7)
        self.cerrarBtn1.setIconSize(QtCore.QSize(24, 24))
        self.cerrarBtn1.setObjectName("cerrarBtn1")
        self.horizontalLayout_3.addWidget(self.cerrarBtn1, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.mainmenu = QtWidgets.QStackedWidget(parent=self.submenucentral)
        self.mainmenu.setStyleSheet("")
        self.mainmenu.setObjectName("mainmenu")
        self.ajustes = QtWidgets.QWidget()
        self.ajustes.setObjectName("ajustes")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ajustes)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.mainmenu.addWidget(self.ajustes)
        self.informacion = QtWidgets.QWidget()
        self.informacion.setObjectName("informacion")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.informacion)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.mainmenu.addWidget(self.informacion)
        self.cerrar_sesion = QtWidgets.QWidget()
        self.cerrar_sesion.setObjectName("cerrar_sesion")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.cerrar_sesion)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mainmenu.addWidget(self.cerrar_sesion)
        self.verticalLayout_6.addWidget(self.mainmenu)
        self.verticalLayout_5.addWidget(self.submenucentral, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.horizontalLayout.addWidget(self.menucentral)
        self.inicio = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inicio.sizePolicy().hasHeightForWidth())
        self.inicio.setSizePolicy(sizePolicy)
        self.inicio.setStyleSheet("")
        self.inicio.setObjectName("inicio")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.inicio)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.arriba = QtWidgets.QWidget(parent=self.inicio)
        self.arriba.setObjectName("arriba")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.arriba)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(parent=self.arriba)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.notificacionBtn = QtWidgets.QPushButton(parent=self.frame_5)
        self.notificacionBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/bell.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.notificacionBtn.setIcon(icon8)
        self.notificacionBtn.setIconSize(QtCore.QSize(24, 24))
        self.notificacionBtn.setObjectName("notificacionBtn")
        self.horizontalLayout_7.addWidget(self.notificacionBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.arriba)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.masBtn = QtWidgets.QPushButton(parent=self.frame_6)
        self.masBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/more-horizontal.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.masBtn.setIcon(icon9)
        self.masBtn.setIconSize(QtCore.QSize(24, 24))
        self.masBtn.setObjectName("masBtn")
        self.horizontalLayout_6.addWidget(self.masBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(parent=self.arriba)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.minBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minBtn.setIcon(icon10)
        self.minBtn.setIconSize(QtCore.QSize(24, 24))
        self.minBtn.setObjectName("minBtn")
        self.horizontalLayout_4.addWidget(self.minBtn)
        self.reducirBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.reducirBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/minimize.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.reducirBtn.setIcon(icon11)
        self.reducirBtn.setIconSize(QtCore.QSize(24, 24))
        self.reducirBtn.setObjectName("reducirBtn")
        self.horizontalLayout_4.addWidget(self.reducirBtn)
        self.maxBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.maxBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/maximize.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.maxBtn.setIcon(icon12)
        self.maxBtn.setIconSize(QtCore.QSize(24, 24))
        self.maxBtn.setObjectName("maxBtn")
        self.horizontalLayout_4.addWidget(self.maxBtn)
        self.cerrarBtn = QtWidgets.QPushButton(parent=self.frame_7)
        self.cerrarBtn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.cerrarBtn.setIcon(icon13)
        self.cerrarBtn.setIconSize(QtCore.QSize(24, 24))
        self.cerrarBtn.setObjectName("cerrarBtn")
        self.horizontalLayout_4.addWidget(self.cerrarBtn)
        self.horizontalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_10.addWidget(self.arriba, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.maininicio = QtWidgets.QWidget(parent=self.inicio)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maininicio.sizePolicy().hasHeightForWidth())
        self.maininicio.setSizePolicy(sizePolicy)
        self.maininicio.setObjectName("maininicio")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.maininicio)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.maincontenido = QtWidgets.QWidget(parent=self.maininicio)
        self.maincontenido.setObjectName("maincontenido")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.maincontenido)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(parent=self.maincontenido)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.perfil = QtWidgets.QWidget()
        self.perfil.setObjectName("perfil")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.perfil)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_10 = QtWidgets.QFrame(parent=self.perfil)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.frame_10)
        self.label.setMinimumSize(QtCore.QSize(120, 120))
        self.label.setMaximumSize(QtCore.QSize(120, 120))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\usuario.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_10)
        self.pushButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/edit.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_16.addWidget(self.frame_10, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_9 = QtWidgets.QFrame(parent=self.perfil)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_19.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_3.setStyleSheet("border-bottom: 1px solid white;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_19.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_19.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_5.setStyleSheet("border-bottom: 1px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_19.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_19.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_9)
        self.label_7.setStyleSheet("border-bottom: 1px solid white;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_19.addWidget(self.label_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_19.addItem(spacerItem4)
        self.verticalLayout_16.addWidget(self.frame_9)
        self.stackedWidget_2.addWidget(self.perfil)
        self.contactos = QtWidgets.QWidget()
        self.contactos.setObjectName("contactos")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.contactos)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.stackedWidget_2.addWidget(self.contactos)
        self.mensajes = QtWidgets.QWidget()
        self.mensajes.setObjectName("mensajes")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.mensajes)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.stackedWidget_2.addWidget(self.mensajes)
        self.verticalLayout_15.addWidget(self.stackedWidget_2)
        self.horizontalLayout_8.addWidget(self.maincontenido)
        self.rightmenu = QtWidgets.QWidget(parent=self.maininicio)
        self.rightmenu.setMinimumSize(QtCore.QSize(200, 0))
        self.rightmenu.setObjectName("rightmenu")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.rightmenu)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rightsubmenu = QtWidgets.QWidget(parent=self.rightmenu)
        self.rightsubmenu.setMinimumSize(QtCore.QSize(200, 0))
        self.rightsubmenu.setObjectName("rightsubmenu")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.rightsubmenu)
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_8 = QtWidgets.QFrame(parent=self.rightsubmenu)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.menusuperior = QtWidgets.QLabel(parent=self.frame_8)
        self.menusuperior.setText("")
        self.menusuperior.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.menusuperior.setObjectName("menusuperior")
        self.horizontalLayout_9.addWidget(self.menusuperior)
        self.cerrarBtn2 = QtWidgets.QPushButton(parent=self.frame_8)
        self.cerrarBtn2.setText("")
        self.cerrarBtn2.setIcon(icon7)
        self.cerrarBtn2.setIconSize(QtCore.QSize(24, 24))
        self.cerrarBtn2.setObjectName("cerrarBtn2")
        self.horizontalLayout_9.addWidget(self.cerrarBtn2, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.rightsubmenu)
        self.stackedWidget.setObjectName("stackedWidget")
        self.notificaciones = QtWidgets.QWidget()
        self.notificaciones.setObjectName("notificaciones")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.notificaciones)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.stackedWidget.addWidget(self.notificaciones)
        self.mas = QtWidgets.QWidget()
        self.mas.setObjectName("mas")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.mas)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.stackedWidget.addWidget(self.mas)
        self.verticalLayout_12.addWidget(self.stackedWidget)
        self.verticalLayout_11.addWidget(self.rightsubmenu)
        self.horizontalLayout_8.addWidget(self.rightmenu, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_10.addWidget(self.maininicio)
        self.horizontalLayout.addWidget(self.inicio)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainmenu.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.perfilBtn.setText(_translate("MainWindow", "Perfil"))
        self.contactosBtn.setText(_translate("MainWindow", " Contactos"))
        self.mensajesBtn.setText(_translate("MainWindow", " Mensajes"))
        self.ajustesBtn.setText(_translate("MainWindow", " Ajustes"))
        self.infoBtn.setText(_translate("MainWindow", "Información"))
        self.csesionBtn.setText(_translate("MainWindow", " Cerrar sesión"))
        self.cerrarBtn1.setToolTip(_translate("MainWindow", "Close Window"))
        self.label_2.setText(_translate("MainWindow", "Nombre"))
        self.label_4.setText(_translate("MainWindow", "Correo"))
        self.label_6.setText(_translate("MainWindow", "Info."))
        self.label_7.setText(_translate("MainWindow", "Disponible"))
