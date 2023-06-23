import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
from match_fingerprint import match
from db_search import search
from generate_pdf import generate


class Inspector(QDialog):
    def __init__(self):
        super(Inspector, self).__init__()
        loadUi("GUI/gui.ui", self)
        self.setWindowTitle("Fingerprint Inspector")
        self.info.move(380, 240)
        self.browse.clicked.connect(self.browsefiles)
        self.inspect.clicked.connect(self.matchfingerprint)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', os.getcwd(), 'BMP Files (*.BMP)')
        self.filename.setText(fname[0])

    def adjust_info(self, info):
        self.info.setText(info)
        self.info.adjustSize()

    def matchfingerprint(self):
        path = self.filename.text()
        if not path or "BMP" not in path[-3:]:
            self.adjust_info("Incorrect type of file!")
            self.info.move(320, 240)
            return
        self.adjust_info("Match Found!")
        self.info.move(360, 240)
        fp_img = match(self.filename.text())
        data = search(fp_img)
        if data:
            generate(data)
            self.adjust_info("Generated Criminal Info File!")
            self.info.move(300, 240)
        else:
            self.adjust_info("No Criminal Data Found!")
            self.info.move(240, 240)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = Inspector()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(900)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())
