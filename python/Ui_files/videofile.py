# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videofile.ui',
# licensing of 'videofile.ui' applies.
#
# Created: Sun Dec  8 21:13:48 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 257)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wa_button = QtWidgets.QPushButton(self.centralwidget)
        self.wa_button.setGeometry(QtCore.QRect(40, 70, 91, 23))
        self.wa_button.setObjectName("wa_button")
        self.a_button = QtWidgets.QPushButton(self.centralwidget)
        self.a_button.setGeometry(QtCore.QRect(140, 70, 91, 23))
        self.a_button.setObjectName("a_button")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(100, 140, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.wa_button.setText(QtWidgets.QApplication.translate("MainWindow", "watch/analyze", None, -1))
        self.a_button.setText(QtWidgets.QApplication.translate("MainWindow", "analyze", None, -1))
        self.cancelButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))

