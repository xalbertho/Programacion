# Form implementation generated from reading ui file 'c:\Repos\2024-2\PAM\P9\calculadora.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 262)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 3, 1, 1, 1)
        self.btn4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 3, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.btn9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btnMenos = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMenos.setObjectName("btnMenos")
        self.gridLayout.addWidget(self.btnMenos, 3, 3, 1, 1)
        self.btn6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 3, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.btn1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 5, 0, 1, 1)
        self.btnIgual = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnIgual.setObjectName("btnIgual")
        self.gridLayout.addWidget(self.btnIgual, 6, 3, 1, 1)
        self.btnAC = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnAC.setObjectName("btnAC")
        self.gridLayout.addWidget(self.btnAC, 1, 0, 1, 1)
        self.btnMas = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMas.setObjectName("btnMas")
        self.gridLayout.addWidget(self.btnMas, 5, 3, 1, 1)
        self.btn3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 5, 2, 1, 1)
        self.etiqueta = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(48)
        font.setBold(True)
        self.etiqueta.setFont(font)
        self.etiqueta.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.etiqueta.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.etiqueta.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.etiqueta.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.etiqueta.setObjectName("etiqueta")
        self.gridLayout.addWidget(self.etiqueta, 0, 0, 1, 4)
        self.btnPunto = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnPunto.setObjectName("btnPunto")
        self.gridLayout.addWidget(self.btnPunto, 6, 2, 1, 1)
        self.btnDivi = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDivi.setObjectName("btnDivi")
        self.gridLayout.addWidget(self.btnDivi, 1, 3, 1, 1)
        self.btn7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btnPor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnPor.setObjectName("btnPor")
        self.gridLayout.addWidget(self.btnPor, 2, 3, 1, 1)
        self.btn2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 5, 1, 1, 1)
        self.btn0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "+/-"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnMenos.setText(_translate("MainWindow", "-"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.pushButton_3.setText(_translate("MainWindow", "%"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btnIgual.setText(_translate("MainWindow", "="))
        self.btnAC.setText(_translate("MainWindow", "AC"))
        self.btnMas.setText(_translate("MainWindow", "+"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.etiqueta.setText(_translate("MainWindow", "0"))
        self.btnPunto.setText(_translate("MainWindow", "."))
        self.btnDivi.setText(_translate("MainWindow", "/"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnPor.setText(_translate("MainWindow", "x"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn0.setText(_translate("MainWindow", "0"))