from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ClassWidget(QWidget):
    def __init__(self):
        super().__init__()
        button = QPushButton("class")
        f = QGridLayout()
        f.addWidget(button)
        self.setLayout(f)

