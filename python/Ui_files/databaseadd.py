# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databaseadd.ui',
# licensing of 'databaseadd.ui' applies.
#
# Created: Thu Dec  5 02:49:36 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_name = QtWidgets.QLineEdit(self.centralwidget)
        self.enter_name.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.enter_name.setObjectName("enter_name")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label.setObjectName("label")
        self.take_pic = QtWidgets.QPushButton(self.centralwidget)
        self.take_pic.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.take_pic.setObjectName("take_pic")
        self.browse_files = QtWidgets.QPushButton(self.centralwidget)
        self.browse_files.setGeometry(QtCore.QRect(90, 130, 75, 23))
        self.browse_files.setObjectName("browse_files")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(90, 170, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 330, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Name:", None, -1))
        self.take_pic.setText(QtWidgets.QApplication.translate("MainWindow", "Take Picture", None, -1))
        self.browse_files.setText(QtWidgets.QApplication.translate("MainWindow", "Browse Files", None, -1))
        self.cancelButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))

