from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
from pytube import YouTube

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.ustAyarlar()
        self.anaMenu()
        self.show()


    def anaMenu(self):
        widget = QWidget()
        hbox = QHBoxLayout()
        yazı = QLabel("<b>Youtube Linki :</b>")
        self.link = QLineEdit()
        button = QPushButton("İndir")
        button.clicked.connect(self.indir)
        hbox.addWidget(yazı)
        hbox.addWidget(self.link)
        hbox.addWidget(button)

        widget.setLayout(hbox)

        self.setCentralWidget(widget)

    def ustAyarlar(self):
        self.setWindowTitle("Youtube Video Downloader by dorukmavis")
        self.setGeometry(250,250,600,80)
        self.setMaximumSize(1000,80)
        self.setMinimumSize(600,80)

    #If you want directly download the link, you can use the code below
    def indir(self):
        acc = self.link.text()
        YouTube(acc).streams.get_highest_resolution().download()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())