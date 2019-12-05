# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'takepic.ui',
# licensing of 'takepic.ui' applies.
#
# Created: Wed Dec  4 19:57:42 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(226, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.take_pic = QtWidgets.QPushButton(self.centralwidget)
        self.take_pic.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.take_pic.setObjectName("take_pic")
        self.finished_button = QtWidgets.QPushButton(self.centralwidget)
        self.finished_button.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.finished_button.setObjectName("finished_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 226, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.take_pic.setText(QtWidgets.QApplication.translate("MainWindow", "Take Picture", None, -1))
        self.finished_button.setText(QtWidgets.QApplication.translate("MainWindow", "Finished", None, -1))

