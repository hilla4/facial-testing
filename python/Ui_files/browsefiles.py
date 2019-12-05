# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browsefiles.ui',
# licensing of 'browsefiles.ui' applies.
#
# Created: Wed Dec  4 19:57:47 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(211, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_file = QtWidgets.QPushButton(self.centralwidget)
        self.add_file.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.add_file.setObjectName("add_file")
        self.finished_button = QtWidgets.QPushButton(self.centralwidget)
        self.finished_button.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.finished_button.setObjectName("finished_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 211, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.add_file.setText(QtWidgets.QApplication.translate("MainWindow", "Add File", None, -1))
        self.finished_button.setText(QtWidgets.QApplication.translate("MainWindow", "Finished", None, -1))

