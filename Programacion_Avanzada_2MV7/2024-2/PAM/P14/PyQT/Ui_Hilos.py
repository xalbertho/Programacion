# Form implementation generated from reading ui file '/Users/j0z3ph/Repos/Vision/Python/Threads/PyQT/Hilos.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(258, 149)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 10, 81, 41))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 70, 64, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 221, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Threads"))
        self.pushButton.setText(_translate("MainWindow", "Contar"))