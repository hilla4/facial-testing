from PySide2 import QtWidgets
import os
from tkinter.filedialog import askopenfilename
from python import database_creator as dbc

from python.Ui_files import startWindow, setupwindow, liveVideo, videofile, analyzefinal, databaseadd, \
    browsefiles, takepic


class BrowseWindowApp(browsefiles.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(BrowseWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Browse Files')
        self.add_file.clicked.connect(lambda: self.browse_files_button())
        self.finished_button.clicked.connect(lambda: self.finished_press())

    def browse_files_button(self):
        self.analyzewin = AnalyzeWindowApp()
        self.analyzewin.show()

    def finished_press(self):
        self.adddatabasewin = AddDatabaseWindowApp()
        self.adddatabasewin.show()
        self.close()


class TakePicWindowApp(takepic.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(TakePicWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Take Pic')
        self.take_pic.clicked.connect(lambda: self.take_pic_button())
        self.finished_button.clicked.connect(lambda: self.finished_press())

    def take_pic_button(self):
        self.analyzewin = AnalyzeWindowApp()
        self.analyzewin.show()

    def finished_press(self):
        self.analyzewin = AnalyzeWindowApp()
        self.analyzewin.show()


class AddDatabaseWindowApp(databaseadd.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(AddDatabaseWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Add To Database')
        self.take_pic.clicked.connect(lambda: self.t_pic())
        self.browse_files.clicked.connect(lambda: self.b_files())
        self.cancelButton.clicked.connect(lambda: self.cancel())

    def t_pic(self):
        name = self.enter_name.text()
        os.system("python add_pictures.py --name " + name)
        os.system("python encode_faces.py")

    def b_files(self):
        name = self.enter_name.text()
        os.system("python browse_pictures.py --name " + name)

    def cancel(self):
        startwin.show()
        self.close()


class AnalyzeWindowApp(analyzefinal.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(AnalyzeWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Analyze')


class FileWindowApp(videofile.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(FileWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Video File')
        self.a_button.clicked.connect(lambda: self.anaylze_button())
        self.wa_button.clicked.connect(lambda: self.watch_anaylze_button())
        self.cancelButton.clicked.connect(lambda: self.cancel())

    def anaylze_button(self):
        val = '0'
        filename = askopenfilename()
        os.system("python recognize_faces_video_file.py --input " + filename + " --display " + val)
        startwin.show()
        self.close()

    def watch_anaylze_button(self):
        val = '1'
        filename = askopenfilename()
        os.system("python recognize_faces_video_file.py --input " + filename + " --display " + val)
        startwin.show()
        self.close()

    def cancel(self):
        startwin.show()
        self.close()


class LiveWindowApp(liveVideo.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(LiveWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Live Video')
        self.a_button.clicked.connect(lambda: self.anaylze_button())
        self.wa_Button.clicked.connect(lambda: self.watch_anaylze_button())
        self.cancelButton.clicked.connect(lambda: self.cancel())

    def anaylze_button(self):
        val = '0'
        os.system("python recognize_faces_video.py --display " + val)
        startwin.show()
        self.close()

    def watch_anaylze_button(self):
        val = '1'
        os.system("python recognize_faces_video.py --display " + val)
        startwin.show()
        self.close()

    def cancel(self):
        startwin.show()
        self.close()


class SetupWindowApp(setupwindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(SetupWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Setup')
        self.okButton.clicked.connect(lambda: self.fill_form())
        self.cancelButton.clicked.connect(lambda: self.cancel())

    def fill_form(self):
        name = self.enterName.text()
        phone = self.enterPhone.text()
        email = self.enterEmail.text()
        conn = dbc.return_conn()
        dbc.delete_all_tasks(conn)
        user = (name, email, phone)
        dbc.insert_test(conn, user)
        dbc.select_all_users(conn)
        startwin.show()
        self.close()

    def cancel(self):
        startwin.show()
        self.close()


class MainWindowApp(startWindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindowApp, self).__init__()
        self.setupUi(self)
        self.setup_button.clicked.connect(lambda: self.launch_setup())
        self.live_video.clicked.connect(lambda: self.launch_live_video())
        self.video_file.clicked.connect(lambda: self.launch_video_file())
        self.add_dataset.clicked.connect(lambda: self.launch_database_add())

    def launch_setup(self):
        setupwin = SetupWindowApp()
        setupwin.show()
        self.close()

    def launch_live_video(self):
        self.livewin = LiveWindowApp()
        self.livewin.show()
        self.close()

    def launch_video_file(self):
        self.filewin = FileWindowApp()
        self.filewin.show()
        self.close()

    def launch_database_add(self):
        self.adddatabasewin = AddDatabaseWindowApp()
        self.adddatabasewin.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    startwin = MainWindowApp()
    startwin.show()
    app.exec_()
