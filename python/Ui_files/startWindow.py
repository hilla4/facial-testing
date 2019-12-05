# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Wed Dec  4 18:05:39 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_dataset = QtWidgets.QPushButton(self.centralwidget)
        self.add_dataset.setGeometry(QtCore.QRect(80, 70, 101, 31))
        self.add_dataset.setObjectName("add_dataset")
        self.live_video = QtWidgets.QPushButton(self.centralwidget)
        self.live_video.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.live_video.setObjectName("live_video")
        self.video_file = QtWidgets.QPushButton(self.centralwidget)
        self.video_file.setGeometry(QtCore.QRect(80, 210, 101, 31))
        self.video_file.setObjectName("video_file")
        self.setup_button = QtWidgets.QToolButton(self.centralwidget)
        self.setup_button.setGeometry(QtCore.QRect(360, 40, 25, 19))
        self.setup_button.setObjectName("setup_button")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(50, 10, 81, 31))
        self.name_label.setObjectName("name_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.add_dataset.setText(QtWidgets.QApplication.translate("MainWindow", "Add to Dataset", None, -1))
        self.live_video.setText(QtWidgets.QApplication.translate("MainWindow", "Live Video", None, -1))
        self.video_file.setText(QtWidgets.QApplication.translate("MainWindow", "Video File", None, -1))
        self.setup_button.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("MainWindow", "Hello, ", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

