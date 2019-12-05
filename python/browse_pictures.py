import argparse
import shutil
from PySide2 import QtWidgets
import os
from tkinter.filedialog import askopenfilename
from python.Ui_files import browsefiles


class BrowseWindowApp(browsefiles.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(BrowseWindowApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Browse Files')
        self.add_file.clicked.connect(lambda: self.browse_files_button())
        self.finished_button.clicked.connect(lambda: self.finished_press())

    def browse_files_button(self):
        filename = askopenfilename()
        shutil.copy(filename, dest)

    def finished_press(self):
        os.system("python encode_faces.py")
        self.close()


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", type=str,
    help="Name to add to dataset")
args = vars(ap.parse_args())
name = args["name"]

app = QtWidgets.QApplication()
browsewin = BrowseWindowApp()
browsewin.show()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__), "dataset"))
path = os.path.join(__location__, name)

if not os.path.exists(path):
    os.mkdir(path)

dest = os.path.join('dataset', name)
app.exec_()
