# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'liveVideo.ui',
# licensing of 'liveVideo.ui' applies.
#
# Created: Thu Dec  5 02:49:19 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wa_Button = QtWidgets.QPushButton(self.centralwidget)
        self.wa_Button.setGeometry(QtCore.QRect(60, 60, 91, 23))
        self.wa_Button.setObjectName("wa_Button")
        self.a_button = QtWidgets.QPushButton(self.centralwidget)
        self.a_button.setGeometry(QtCore.QRect(60, 120, 91, 23))
        self.a_button.setObjectName("a_button")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(70, 170, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.wa_Button.setText(QtWidgets.QApplication.translate("MainWindow", "Watch/Analyze", None, -1))
        self.a_button.setText(QtWidgets.QApplication.translate("MainWindow", "Analyze", None, -1))
        self.cancelButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))

