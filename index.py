import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtCore import QFile, QFileSelector
from PySide2.QtGui import QFileOpenEvent


UI_file = "ui.ui"


class PhotoUploader:
    def __init__(self, ui_file):
        ui = QFile(ui_file)
        ui.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui)
        ui.close()
        self.window.setFixedSize(self.window.size())

        self.browse_btn = self.window.findChild(QPushButton, "BrowseButton")
        self.list_view = self.window.findChild(QTextEdit, "textEdit_3")

        self.browse_btn.clicked.connect(self.file_browse_evevt)
        self.window.show()


    def file_browse_evevt(self):
        print("button pressed")
        files = QFileDialog.getOpenFileNames()

        print(files[0])

        file_list = ""
        index = 1
        for file in files[0]:
            f = file.split("/")[-1]
            print(f)
            file_list += str(index) + " : " + str(f) + "\n"
            index += 1

        self.list_view.setText(file_list)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    biometric = PhotoUploader(UI_file)
    sys.exit(app.exec_())
