from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

UI_file = "ui.ui"


class PhotoUploader(QMainWindow):
    def __init__(self, ui_file):
        super(PhotoUploader, self).__init__()
        uic.loadUi('ui.ui', self)
        self.setFixedSize(self.size())

        self.console_data = ""
        self.select_tab = 0
        self.resize_tab = 1
        self.upload_tab = 2

        self.tabs = self.findChild(QTabWidget, "tabWidget")
        self.browse_btn = self.findChild(QPushButton, "BrowseButton")
        self.select_tab_next_btn = self.findChild(QPushButton, "Select_tab_next_btn")
        self.list_view = self.findChild(QTextEdit, "textEdit_3")
        self.console = self.findChild(QTextEdit, "console")
        self.remove_file = self.findChild(QPushButton, "RemoveFile")
        self.reset_btn = self.findChild(QPushButton, "ResetButton")

        self.show()

    def initialization(self):
        self.reset_btn.setStyleSheet('color: red;')
        self.list_view.setText("")
        self.tab_disable(self.resize_tab, False)
        self.tab_disable(self.upload_tab, False)
        self.list_view.setReadOnly(True)
        self.console.setReadOnly(True)
        self.browse_btn.setEnabled(True)
        self.reset_btn.setEnabled(False)
        self.select_tab_next_btn.setEnabled(False)
        self.remove_file.setEnabled(False)
        self.browse_btn.clicked.connect(self.file_browse_event)
        self.select_tab_next_btn.clicked.connect(lambda: self.tab_next_event(self.resize_tab))
        self.reset_btn.clicked.connect(self.initialization)

        self.add_console_data("Photo Uploader By Python", "white", 'c', True)

    def file_browse_event(self):
        files = QFileDialog.getOpenFileNames()

        #print(files[0])

        file_list = ""
        index = 1
        for file in files[0]:
            f = file.split("/")[-1]
            file_list += str(index) + " : " + str(f) + "\n"
            index += 1

        if index > 1:
            self.list_view.setText(file_list)
            self.add_console_data(str(index - 1) + " files added")
            self.select_tab_next_btn.setEnabled(True)
            self.reset_btn.setEnabled(True)
            self.browse_btn.setEnabled(False)
            self.tab_disable(self.resize_tab, True)
            scroll = self.list_view.verticalScrollBar()
            scroll.setValue(scroll.maximum())

    def tab_next_event(self, tab_num):
        QTabWidget.setCurrentIndex(self.tabs, tab_num)

    def tab_disable(self, tab_num, disable):
        QTabWidget.setTabEnabled(self.tabs, tab_num, disable)

    def add_console_data(self, text, color='white', alignment='l', clear=False):
        if clear:
            self.console_data = ""
        f_alignment = ""
        if alignment == 'c' or alignment == 'C':
            f_alignment = "align = 'center'"
        elif alignment == 'r' or alignment == 'R':
            f_alignment = "align = 'right'"
        elif alignment == 'j' or alignment == 'J':
            f_alignment = "align = 'justify'"
        else:
            f_alignment = "align = 'left'"

        f_color = 'color:' + color

        prefix = "<!DOCTYPE HTML PUBLIC '-//W3C//DTD HTML 4.0//EN' 'http://www.w3.org/TR/REC-html40/strict.dtd'>" \
                 "<html><head><meta name='qrichtext' content='1' /><style type='text/css'>" \
                 "p, li { white-space: pre-wrap; }</style></head>" \
                 "<body style='font-size:11pt;font-weight:400; font-style:normal;'bgcolor='#04242F'>"

        suffix = "</body></html>"
        self.console_data += "<p " + f_alignment + " style='margin-top:12px; margin-bottom:12px; " \
                                                   "margin-left:0px; margin-right:0px; -qt-block-indent:0;" \
                                                   "text-indent:0px;'><span style='font-weight:600; " + f_color + ";'>"
        self.console_data += str(text)
        self.console_data += "</span></p>"
        self.console.setText(prefix + self.console_data + suffix)
        scroll = self.console.verticalScrollBar()
        scroll.setValue(scroll.maximum())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    photo_uploader = PhotoUploader(UI_file)
    photo_uploader.initialization()
    sys.exit(app.exec_())
