# Form implementation generated from reading ui file 'e:\Programacion\Programacion_Avanzada_2MV7\Uso github\Windows-Live-Messenger\ingreso.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 620)
        MainWindow.setMaximumSize(QtCore.QSize(740, 620))
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
"QStackedWidget{\n"
"    background-color: rgba(0, 0, 0, 80); \n"
"    border-radius:20px;\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"border: 2px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(23,139,216);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255,255,255);\n"
"border: 2px solid rgb(91,220,252);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator { \n"
"    width: 18px; \n"
"    height:18px;\n"
"}\n"
"\n"
"\n"
"#inicial QPushButton{\n"
"border-radius:10px;\n"
"border: 2px solid #ffffff;\n"
"}\n"
"\n"
"#inicial  QPushButton:hover{\n"
"border-radius:10px;\n"
"border: 2px solid rgb(41, 178, 202);\n"
"background-color: rgb(23,139,216);\n"
"}\n"
"\n"
"\n"
"#arriba QPushButton:hover{\n"
"border-radius:24px;\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0852273 rgba(176, 235, 255, 167), stop:0.1 rgba(255, 255, 255, 255), stop:0.204545 rgba(151, 242, 255, 92), stop:0.426136 rgba(85, 170, 255, 255), stop:0.454545 rgba(125, 222, 255, 51), stop:0.596591 rgba(0, 158, 226, 228), stop:0.738636 rgba(180, 233, 255, 84), stop:0.818182 rgba(0, 85, 138, 205), stop:0.982955 rgba(255, 255, 255, 0))\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(740, 620))
        self.centralwidget.setMaximumSize(QtCore.QSize(740, 620))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 740, 620))
        self.widget.setMinimumSize(QtCore.QSize(740, 620))
        self.widget.setMaximumSize(QtCore.QSize(740, 620))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arriba = QtWidgets.QFrame(parent=self.widget)
        self.arriba.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.arriba.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.arriba.setObjectName("arriba")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.arriba)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.arriba)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/minus.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(parent=self.arriba)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\feather/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.arriba, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop)
        self.inicial = QtWidgets.QFrame(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inicial.sizePolicy().hasHeightForWidth())
        self.inicial.setSizePolicy(sizePolicy)
        self.inicial.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.inicial.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.inicial.setObjectName("inicial")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.inicial)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.inicial)
        self.stackedWidget.setObjectName("stackedWidget")
        self.inicio = QtWidgets.QWidget()
        self.inicio.setObjectName("inicio")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.inicio)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(parent=self.inicio)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 18pt \"Tempus Sans ITC\";")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(parent=self.inicio)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.usuario = QtWidgets.QLineEdit(parent=self.inicio)
        self.usuario.setMinimumSize(QtCore.QSize(0, 35))
        self.usuario.setText("")
        self.usuario.setObjectName("usuario")
        self.verticalLayout_2.addWidget(self.usuario)
        spacerItem3 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(parent=self.inicio)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.contra = QtWidgets.QLineEdit(parent=self.inicio)
        self.contra.setMinimumSize(QtCore.QSize(0, 35))
        self.contra.setText("")
        self.contra.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra.setObjectName("contra")
        self.verticalLayout_2.addWidget(self.contra)
        self.recordar = QtWidgets.QCheckBox(parent=self.inicio)
        self.recordar.setObjectName("recordar")
        self.verticalLayout_2.addWidget(self.recordar)
        spacerItem4 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.advertencia = QtWidgets.QLabel(parent=self.inicio)
        self.advertencia.setStyleSheet("color: rgb(255, 160, 162);")
        self.advertencia.setText("")
        self.advertencia.setObjectName("advertencia")
        self.verticalLayout_2.addWidget(self.advertencia)
        self.iniciar = QtWidgets.QPushButton(parent=self.inicio)
        self.iniciar.setMinimumSize(QtCore.QSize(0, 35))
        self.iniciar.setObjectName("iniciar")
        self.verticalLayout_2.addWidget(self.iniciar)
        spacerItem5 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.face = QtWidgets.QPushButton(parent=self.inicio)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\../P7 (1)/P7/Face.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.face.setIcon(icon2)
        self.face.setIconSize(QtCore.QSize(30, 35))
        self.face.setObjectName("face")
        self.horizontalLayout_3.addWidget(self.face)
        self.google = QtWidgets.QPushButton(parent=self.inicio)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\../P7 (1)/P7/google.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.google.setIcon(icon3)
        self.google.setIconSize(QtCore.QSize(30, 35))
        self.google.setObjectName("google")
        self.horizontalLayout_3.addWidget(self.google)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.inicio)
        self.label_6.setStyleSheet("font: 11pt \"Tempus Sans ITC\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.registrate = QtWidgets.QPushButton(parent=self.inicio)
        self.registrate.setMinimumSize(QtCore.QSize(0, 0))
        self.registrate.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"font: 11pt \"Tempus Sans ITC\";\n"
"color:rgb(255,255,254);\n"
"border: None;\n"
"background-color: None;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"font: 11pt \"Tempus Sans ITC\";\n"
"    color: rgb(41, 178, 202);\n"
"border: None;\n"
"background-color: None;\n"
"}")
        self.registrate.setObjectName("registrate")
        self.horizontalLayout_4.addWidget(self.registrate, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.inicio)
        self.registrarse = QtWidgets.QWidget()
        self.registrarse.setObjectName("registrarse")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.registrarse)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_3.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(parent=self.registrarse)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 18pt \"Tempus Sans ITC\";")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.label_4 = QtWidgets.QLabel(parent=self.registrarse)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.nombres = QtWidgets.QLineEdit(parent=self.registrarse)
        self.nombres.setMinimumSize(QtCore.QSize(0, 35))
        self.nombres.setText("")
        self.nombres.setObjectName("nombres")
        self.verticalLayout_3.addWidget(self.nombres)
        spacerItem9 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.label_8 = QtWidgets.QLabel(parent=self.registrarse)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.apellidos = QtWidgets.QLineEdit(parent=self.registrarse)
        self.apellidos.setMinimumSize(QtCore.QSize(0, 35))
        self.apellidos.setText("")
        self.apellidos.setObjectName("apellidos")
        self.verticalLayout_3.addWidget(self.apellidos)
        spacerItem10 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.label_9 = QtWidgets.QLabel(parent=self.registrarse)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.contra_2 = QtWidgets.QLineEdit(parent=self.registrarse)
        self.contra_2.setMinimumSize(QtCore.QSize(0, 35))
        self.contra_2.setText("")
        self.contra_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra_2.setObjectName("contra_2")
        self.verticalLayout_3.addWidget(self.contra_2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.label_10 = QtWidgets.QLabel(parent=self.registrarse)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.contra_3 = QtWidgets.QLineEdit(parent=self.registrarse)
        self.contra_3.setMinimumSize(QtCore.QSize(0, 35))
        self.contra_3.setText("")
        self.contra_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.contra_3.setObjectName("contra_3")
        self.verticalLayout_3.addWidget(self.contra_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 23, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.advertencia_2 = QtWidgets.QLabel(parent=self.registrarse)
        self.advertencia_2.setStyleSheet("color: rgb(255, 160, 162);")
        self.advertencia_2.setText("")
        self.advertencia_2.setObjectName("advertencia_2")
        self.verticalLayout_3.addWidget(self.advertencia_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.regresar = QtWidgets.QPushButton(parent=self.registrarse)
        self.regresar.setMinimumSize(QtCore.QSize(0, 35))
        self.regresar.setObjectName("regresar")
        self.horizontalLayout_5.addWidget(self.regresar)
        self.registrar = QtWidgets.QPushButton(parent=self.registrarse)
        self.registrar.setMinimumSize(QtCore.QSize(0, 35))
        self.registrar.setObjectName("registrar")
        self.horizontalLayout_5.addWidget(self.registrar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.registrarse)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        spacerItem13 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.verticalLayout.addWidget(self.inicial)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 740, 620))
        self.label.setMinimumSize(QtCore.QSize(740, 620))
        self.label.setMaximumSize(QtCore.QSize(740, 620))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\Programacion\\Programacion_Avanzada_2MV7\\Uso github\\Windows-Live-Messenger\\fondo.jpg"))
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
        self.label_5.setText(_translate("MainWindow", "Python Live Messenger"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.label_3.setText(_translate("MainWindow", "Contraseña"))
        self.recordar.setText(_translate("MainWindow", "Recordar contraseña"))
        self.iniciar.setText(_translate("MainWindow", "Iniciar Sesión"))
        self.face.setText(_translate("MainWindow", "Facebook"))
        self.google.setText(_translate("MainWindow", "Google"))
        self.label_6.setText(_translate("MainWindow", "¿No tienes una cuenta?"))
        self.registrate.setText(_translate("MainWindow", "Regístrate"))
        self.label_7.setText(_translate("MainWindow", "Registrarse"))
        self.label_4.setText(_translate("MainWindow", "Nombre ( s )"))
        self.label_8.setText(_translate("MainWindow", "Apellidos"))
        self.label_9.setText(_translate("MainWindow", "Contraseña"))
        self.label_10.setText(_translate("MainWindow", "Confirmar contraseña"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.registrar.setText(_translate("MainWindow", "Registrar"))
