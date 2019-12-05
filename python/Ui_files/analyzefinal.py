# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analyzefinal.ui',
# licensing of 'analyzefinal.ui' applies.
#
# Created: Wed Dec  4 19:19:05 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(173, 173)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.end_analyze_button = QtWidgets.QPushButton(self.centralwidget)
        self.end_analyze_button.setGeometry(QtCore.QRect(40, 80, 75, 23))
        self.end_analyze_button.setObjectName("end_analyze_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 173, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.end_analyze_button.setText(QtWidgets.QApplication.translate("MainWindow", "End Analyze", None, -1))

