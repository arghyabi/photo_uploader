from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

UI_file = "ui.ui"


class PhotoUploader(QMainWindow):
    def __init__(self, ui_file):
        super(PhotoUploader, self).__init__()
        uic.loadUi('ui.ui', self)
        self.setFixedSize(self.size())

        self.browse_btn = self.findChild(QPushButton, "BrowseButton")
        self.list_view = self.findChild(QTextEdit, "textEdit_3")

        self.browse_btn.clicked.connect(self.file_browse_event)

        self.show()

    def file_browse_event(self):
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
