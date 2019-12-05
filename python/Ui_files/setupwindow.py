# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setupwindow.ui',
# licensing of 'setupwindow.ui' applies.
#
# Created: Wed Dec  4 23:52:47 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(247, 261)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enterName = QtWidgets.QLineEdit(self.centralwidget)
        self.enterName.setGeometry(QtCore.QRect(100, 70, 113, 20))
        self.enterName.setText("")
        self.enterName.setObjectName("enterName")
        self.enterEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.enterEmail.setGeometry(QtCore.QRect(100, 130, 113, 20))
        self.enterEmail.setText("")
        self.enterEmail.setObjectName("enterEmail")
        self.enterPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.enterPhone.setGeometry(QtCore.QRect(100, 100, 113, 20))
        self.enterPhone.setText("")
        self.enterPhone.setObjectName("enterPhone")
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.okButton.setObjectName("okButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 70, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 71, 20))
        self.label_3.setObjectName("label_3")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(150, 180, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 247, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.okButton.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Enter Name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Enter Phone:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Enter Email:", None, -1))
        self.cancelButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))

